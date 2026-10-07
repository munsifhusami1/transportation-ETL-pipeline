import pdfplumber
import decimal 

position_accounts = None
position_state = None
grant_class = None 
position_project = None
position_amount = None
position_recipient = None

agency_lookup ={"Highway Infrastructure Programs":"FHWA",
                "Transit Infrastructure Grants":"FTA",
                "Transportation Planning, Re-\nsearch, and Development":"FTA"}

award_year = 2022

#for replacing the print(row) with a dict of named fields, positional

PDF = "/Users/munsifhusami/Desktop/PRACTICE DATABASES/SQL Project Rebuild/2022 CDS.pdf"

accounts = ["Highway Infrastructure Programs","Transit Infrastructure Grants","Transportation Planning, Re-\nsearch, and Development"]

with pdfplumber.open(PDF) as pdf:
    for page in pdf.pages[0:37]:
        table = page.extract_table()
        if table == None:
          continue
        else:
             if table[0][0] == "Account":
               if "Community Project Funding/Congressionally Directed Spending" in page.extract_text():
                    grant_class = "Community Project Funding/Congressionally Directed Spending"
                    print(grant_class)
               #print(table[0]) (only to check if first table header is a real header row)
               position_accounts = table[0].index("Account")
               position_state = table[0].index("State")
               position_project = table[0].index("Project")
               position_amount = table[0].index("Amount")
               if "Recipient" in table[0]:
                   position_recipient = table[0].index("Recipient")
               else:
                   position_recipient = None
             else:
               pass 
             for row in table:
               if row[position_accounts] in accounts and row[position_state] == "NJ":
                    row_dict = {"project title": row[position_project], "program" : row[position_accounts], "award_amount": decimal.Decimal(row[position_amount].strip().replace('$', '').replace(',', '')), "recipient_name" : row[position_recipient] if position_recipient is not None else None, "agency_name": agency_lookup.get(row[position_accounts]), "award_year" : award_year, "grant_class" : grant_class}
                    print(row_dict)
                    #break (enter only when the check for dict against records is needed)
               else:
                    continue       

# TODO next session:
# 1. Validate: filter CSV to NJ + this PDF's year + HIP/TIG/TPRD, compare
#    project_title + amount against parser output -- DONE, all 7 rows match
# 2. Build row -> dict (named fields, not positional) -- DONE
# 3. Field sourcing -- DONE:
#    - FROM ROW: amount, project_title, account/program, recipient (NULL when
#      table shape has no Recipient column)
#    - DERIVED/LOOKUP: agency_name via agency_lookup dict (HIP->FHWA, TIG/TPRD->FTA)
#    - FROM FILE/RUN CONTEXT: award_year set manually at top of script
#    - grant_class: sourced from bracketed section text via page.extract_text(),
#      persists across pages same as position_accounts/position_state
#.   - award_amount cleaned to Decimal in row_dict -- DONE.
# 3b. Clean project_title before the projects insert: the PDF puts a hidden \n
#    (line break) inside titles, so they won't match the clean titles in the
#    projects table. Decide what \n should become (nothing vs. a space) and
#    test on a scratch string first. Check hyphenated breaks like "Re-\nplacement"   
# 4. NEXT: connect to Postgres (psycopg2/SQLAlchemy) and actually INSERT
#    row_dict values into the 4-table schema -- not started yet. Need to
#    figure out: agencies/recipients/projects lookups first (get-or-create
#    pattern?) before funding insert, same shape as last night's SQL
#    INSERT...SELECT JOIN pattern. Connection proven. Insert logic is left. 