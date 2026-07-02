# Grants ETL Process


** Timeline - early-mid June 2026 **

State and regional transportation agencies manage hundreds of active grants across multiple funding programs at the federal level. Tracking each project's award status, expenditure, and compliance with manual data entry across Excel and SQL Server creates reporting delays and data integrity risks.

This project automates that process, ingesting raw grants data and applying a repeatable cleaning and transformation pipeline. The result is a series of analysis-ready outputs for program reporting and decision-making, reducing manual reporting time and eliminating a class of data integrity errors common in multi-source grant tracking.

Note: Source data has been anonymized for public sharing. Award amounts and total project costs are scaled by a random factor, and project titles are replaced with placeholder labels. Fields containing personally identifiable information or location-specific detail — including local contact names, municipality, congressional/legislative district, and project descriptions/notes — have been removed entirely from the dataset rather than anonymized in place.

## Tools

Google Colab was selected to keep the pipeline off internal infrastructure, avoiding exposure of proprietary tools and ensuring no security risk to agency systems. All personally identifiable information and real award figures are anonymized or removed prior to any external sharing.

Python was chosen for its data manipulation libraries — primarily pandas — enabling a repeatable, portable pipeline without reliance on agency-specific tooling. This reflects a common constraint in public sector work, where data governance policies restrict use of external platforms on native infrastructure.

The following diagram illustrates the manual process that this ETL pipeline replaces: <img width="761" height="906" alt="New ETL flow" src="https://github.com/user-attachments/assets/5f4c1950-3c47-4fc4-ad49-1026333628f9" />

## Pipeline Overview

Three libraries support the pipeline: pandas for data processing and transformation, sqlite3 for structured storage, and string for label substitution across project title fields.

Extract: Ingests the source CSV dataset into a pandas dataframe for inspection and transformation.

Transform: Award Amount and Total Project Cost are cleaned via regular expressions to strip currency symbols and formatting characters, converted to numeric type, then scaled by a fixed multiplier to anonymize real financial figures. Project titles are replaced with sequential placeholder labels using a string substitution function to remove identifying metadata.

Load: The cleaned, anonymized dataframe is written to a SQLite database table, making the output queryable via SQL rather than remaining in a flat file.

A main() function runs extract, transform, and load in sequence, executing the full pipeline with a single call — the standard structure for production ETL workflows.

## Debugging 

Transform functions were run twice during early iterations which resulted in inaccurate multiplication factors. These were rewritten and the code rebuilt in a new notebook to minimize stale function carryover from Colab.

## How to Run

Requires pandas. Place a CSV in the same format in the working directory, update the filename in the extract() call, and run the script. The pipeline outputs a grants.db SQLite file with a table named grants.

## SQL Queries for Reporting

**Timeline — Late May/Early June 2026**

The following queries were executed against the federal grants tracking database at a DOT-state style grants tracking system, supporting grant monitoring and reporting across a multi-county region. Queries preceded the Python automation pipeline and were run in SQL Server Management Studio for report generation. Data has been anonymized as described above.

## Featured query — County grant risk flagging

Identifies awarded grants in a chosen County that remain unprogrammed and unobligated, surfacing at-risk projects before federal spending deadlines. CASE statements convert binary flags into human-readable status fields for distribution to non-technical stakeholders.

```
SELECT 
     [Awarded_FY]
      ,[Agency]
      ,[Grant_Classification]
      ,[Program]
      ,[Project_Title]
      ,[Grant_Type]
      ,[Amount]
      ,[Total_Project_Cost]
      ,CASE
      WHEN [Obligated?_(Y/N)] = 'Y' THEN 'Yes'
      ELSE 'No'
      END AS [Obligated]
      ,[County_ies]
FROM dbo.[Grants Tracker]
WHERE County_ies = 'XYZ'
AND [Obligated?_(Y/N)] = 'N'
ORDER BY [Awarded_FY] ASC
```

Additional queries supported FY 2022-2023 cycle reporting, filtering by obligation status.


## Outputs

During active grant monitoring at a state DOT-style grants tracking system, the manual process supported the following reporting use cases across its subregions:

1. Identification of at-risk grants approaching federal obligation deadlines
2. Cycle-specific reporting for FY 2022-2023 federal grant awards

This ETL pipeline recreates and automates that manual workflow, reducing consolidation time across source systems and eliminating the formatting inconsistencies that previously required manual correction before each reporting cycle.
