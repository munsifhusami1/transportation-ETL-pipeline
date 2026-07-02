SELECT 
     [Awarded_FY]
      ,[Agency]
      ,[Grant_Classification]
      ,[Program]
      ,[Project_Title]
      ,[Grant_Type]
      ,[Amount]
      ,CASE
      WHEN [Obligated?_(Y/N)] = 'Y' THEN 'Yes'
      ELSE 'No'
      END AS [Obligated]
      ,[County_ies]
FROM dbo.[Grants Tracker]
WHERE [Awarded_FY] IN ('2022', '2023')
AND [Obligated?_(Y/N)] = 'N'
ORDER BY [Awarded_FY] ASC
