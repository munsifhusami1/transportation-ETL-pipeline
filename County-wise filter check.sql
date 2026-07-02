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
FROM dbo.[Grants Tracker]
WHERE County_ies = 'XYZ'
AND [Obligated?_(Y/N)] = 'N'
ORDER BY [Awarded_FY] ASC
