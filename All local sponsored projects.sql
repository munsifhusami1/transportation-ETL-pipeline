SELECT
     [Awarded_FY]
      ,[Agency]
      ,[Grant_Classification]
      ,[Program]
      ,[Project_Title]
      ,[Description_Summary]
      ,[TIP_DBNUM]
      ,[Grant_Type]
      ,[Amount]
      ,[Obligated_To_Date]
      ,[Obligation_Expenditure_Deadlines]
      ,[Programmed],
      [County_ies]
      ,[Municipality]
      ,[Recipient]
      ,[TIP_Status]
      ,[Notes]
      ,[Local_Contact]

FROM dbo.[Grants Tracker]
WHERE [Recipient] NOT IN ('Agency_A','Agency_B','Agency_C')
ORDER BY [Awarded_FY] ASC
