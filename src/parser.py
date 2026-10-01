import pdfplumber

position_accounts = None
position_state = None

PDF = "2022 CDS.pdf"

accounts = ["Highway Infrastructure Programs","Transit Infrastructure Grants","Transportation Planning, Re-\nsearch, and Development"]

with pdfplumber.open(PDF) as pdf:
    for page in pdf.pages[0:37]:
        table = page.extract_table()
        if table == None:
          continue
        else:
             if table[0][0] == "Account":
               #print(table[0])
               position_accounts = table[0].index("Account")
               position_state = table[0].index("State")
             else:
               pass 
             for row in table:
               if row[position_accounts] in accounts and row[position_state] == "NJ":
                    print(row)
               else:
                    continue       

# TODO next session:
# 1. Validate: filter CSV to NJ + this PDF's year + HIP/TIG/TPRD, compare
#    project_title + amount against parser output (decide: exact string match
#    or fuzzy, given known title drift under shared DBNUMs)
# 2. Build row -> dict (named fields, not positional)
# 3. Field sourcing per field (NOT a flat list — sort into buckets):
#    - FROM ROW: amount, project_title, account/program, recipient (if present)
#    - DERIVED/LOOKUP: agency_name (from account: HIP->FHWA, TIG/TPRD->FTA)
#    - FROM FILE/RUN CONTEXT: award_year (not on any row -- where does this
#      live? filename? constant set once per run?)
#    - UNRESOLVED / OPEN QUESTION: grant_class is NOT NULL in schema but never
#      appears on the PDF -- is it inferable from "this is a CDS doc", or true
#      missing data like recipient?