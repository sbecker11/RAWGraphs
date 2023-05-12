import pandas as pd

job_skills_data_file = 'job-skills-years.xlsx' # the input MSExcel xlsx spreadsheet
dense_csv_file = "dense.csv" # file to save the dense matrix 
dense_only = False  # if False then a uniqufied matrix will be created
uniques_csv_file = "uniques.csv" # file to save the uniquified matrix 

# load the spreadsheet
df = pd.read_excel(job_skills_data_file,
    sheet_name='job-skills',
    header=0,
    index_col=False,
    keep_default_na=True
    )

# manually entered values
years_row = 0
first_row = 8
last_row = 117
first_col = 2
last_col = 36

# all non NaN cells are stored as tuplets of 
# job,skill,years 
tups = []

jobs = df.columns[2:]
for c in range(first_col, last_col):
    job = df.columns[c]
    for r in range(first_row, last_row):
        skill = df.loc[r-2][0]
        if df.loc[r][c] == 'x':
            years = df.loc[years_row][c]
            tup = (job,skill,years)
            tups.append(tup)

print(f"saving dense ({len(tups)},3) matrix to {dense_csv_file}")
with open(dense_csv_file, 'w') as file:
    columns = "job,skill,years\n"
    file.write(columns)
    for tup in tups:
        job,skill,years = tup
        row = f"{job},{skill},{years}\n"
        file.write(row)

if dense_only:
    print("finished with dense only")

# proceed to create the "uniquified" matrix
# read csv file into a dataframe for post-processing
df = pd.read_csv(dense_csv_file)

# The size of the dataframe will be reduced by:
# dropping all duplicate rows. 

# The following step is taken to foster duplicate
# values, that will be removed at the last step.

# 1. normalize the job titles:
# The first row of the spreadsheet is used to define
# dataframe's columns. To guarantee uniqueness, 
# digit suffixed are added. Remove the trailing suffixes
# from the first row. 
def strip_trailing_digit(string):
    parts = string.split('.')
    if str(parts[-1]).isdigit():
        return '.'.join(parts[0:-1])
    return string
df.loc[:,'job'] = df.loc[:,'job'].apply(strip_trailing_digit)

# 2. keep only skill rows that have more than 1 non-NaN job value
df['nnans'] = df.notna().sum(axis=1)
df = df[df['nnans'] > 1]
df.drop('nnans', axis=1, inplace=True)

# 3. keep only skill rows with years > 1
df = df[df['years'] > 1]

# 4. keep only skill rows that start with '_' 
def keep_skill(string:str) -> bool:
    return str(string).lower().find('_')== 0
df = df[df['skill'].apply(keep_skill)]

# 4.a - remove the prefix for visualization
df.loc[:,'skill'] = df.loc[:,'skill'].str[1:]

# 5. drop duplicate rows
df = df.drop_duplicates()

print(f"saving uniquified {df.shape} matrix to {uniques_csv_file}")
df.to_csv(uniques_csv_file)

print("done")