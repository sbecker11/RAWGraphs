# RAWgraphs is an online visualization tool

https://app.rawgraphs.io/

Use MSExcel to create your jobs-skills graph.

row 1 shows "Professional Experience" or jobs  
row 2 is the number of "years" at each job  
rows 3 to 5 are visuals  
row 6 shows the year of each job  

col 1 shows "Technical Skills" or "skills"  
each col after 'C' or 3, show skills for a job  
'x' indicates a skill for a given job in a given year  

rawgraph_from_excel.py reads the job-skills.xlsx file  

All 'x' job-skill location are used to create a pandas dataframe.

Open [RAWgraphs 2.0 beta](https://app.rawgraphs.io/)  
Choose get started  
1. Load your data - "Upload your data" - choose the local "dense.csv" file  
2. Choose a chart - choose "Alluvial"  
3. Mapping - drop "job" and "skill" Dimensions into  Steps, and "years" into Size  
4. Customize - make no changes
5. Export - export the result as dense.png

![dense.png](dense.png)

Notice that the resulting graphic is simply too dense and unreadable.

The code reduces the desity of the matrix by normalizing job values and keeping only selected rows before dropping duplicate rows. This is done in the following steps:  
1. normalize job values  
2. keep only skill rows that have more than 1 non-NaN job value  
3. keep only skill rows with years > 1  
4. keep only skill rows that start with '_'  
5. drop duplicate rows  

The uniquified matrix has been saved to "uniques.csv"

Re-open [RAWgraphs 2.0 beta](https://app.rawgraphs.io/)
Choose get started  
1. Load your data - "Upload your data" - choose the local "uniques.csv" file  
2. Choose a chart - choose "Alluvial"  
3. Mapping - drop "job" and "skill" dimensions into Steps, and "years" into Size  
4. Customize - shows the greatly simplified alluvial graphic created for the "uniques.csv" file  
5. Export - exported the result as "uniques.png"  

![uniques.png](uniques.png)

This is less dense, but the colors are a bit harsh. To soften the color palette, open the Colors section, under Customize and change the RGB value of each job to make them more pastel.

Save the graphic as "pastels.png" and 

![pastels.png](pastels.png)

Save the project as "pastels.rawgraphs"

Close the browser window and reopen [RAWgraphs 2.0 beta](https://app.rawgraphs.io/)

In section 1 Load your data, choose "Open your project" 
and select the "pastels.rawgraphs" file to verify that the project was saved and then loaded correctly.






