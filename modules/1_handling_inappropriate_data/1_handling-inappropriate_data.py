# Handling inappropriate data
# 1. Initial Assessment & Deduplication (Steps 1–3)
# Identify: Classify every column's data type (Numerical, Categorical, Ordinal, or Pure String).
# Deduplicate: Remove any duplicate rows (records) and duplicate columns from the dataframe.

# 2. Numerical Validation (Step 4)
# Evaluate continuous (CND) and discrete (DND) numerical data against domain-specific rules.
# Ensure values meet constraints regarding signs (positive/negative), formatting (decimals vs. integers), and expected ranges. Delete entries that violate these rules.

# 3. Categorical & Ordinal Cleaning (Steps 5–6)
# Standardize the text by unifying the case and fixing spelling errors.
# Validate the unique values (and their expected ranks, in the case of ordinal data) against domain specifications. Drop entire records if they contain unrecognized categories or ranks.

# 4. String & Date Handling (Steps 7–8)
# Strings: Leave pure string columns completely unaltered.

# Dates: If you are performing Time Series analysis, convert date columns into a datetime format and set that column as the dataframe's index. Otherwise, skip this step.

import pandas as pd
import numpy as np

print("Loading the data...")
data = pd.read_csv('../../data/datasetExample.csv')
print(" \u2714Data loading completed.")

print(f"--------- Information about the data --------- ")
print(data.info())

print ("=" * 100)
print("1. Identify the type of the data for each column (Numerical, Categorical, Ordinal , Pure String")
print("=" * 100)

column_data = """
   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   CustomerID       11 non-null     int64  -------------------> Numerical (Cont)
 1   Age_Group        11 non-null     object -------------------> Categorical
 2   Rating(1-5)      11 non-null     int64  -------------------> Numerical  (Discrete)
 3   Hotel            11 non-null     object -------------------> Categorical
 4   FoodPreference   11 non-null     object -------------------> Categorical
 5   Bill             11 non-null     int64  -------------------> Numerical  (Cont)
 6   NoOfPax          11 non-null     int64  -------------------> Numerical  (Discrete)(1-20)
 7   EstimatedSalary  11 non-null     int64  -------------------> Numerical  (Cont)
 8   Age_Group.1      11 non-null     object -------------------> Categorical
"""

print(f"{column_data}")

print ("=" * 100)
print("2. Check and remove all Duplicate RECORDS from the dataframe")
print("=" * 100)

duplicate_rows = data[data.duplicated()]
if duplicate_rows.size > 0:
    print(f" Duplicate rows found: {duplicate_rows.size}")
    print(" Deleting duplicate rows...")
    print(f" Before deleting, no of rows: {data.size}")
    data.drop_duplicates(inplace=True)
    data.reset_index(inplace=True)
    print(" \u2714 Deleted duplicate rows.")
    print(f" After deleting duplocate {duplicate_rows.size} rows, data size is {data.size}")


print ("=" * 100)
print("3. Check and remove all Duplicate COLUMNS from the dataframe")
print("=" * 100)

print(f"Columns: {[column for column in data.columns]}")
print("Deleting the column 'Age_Group.1'")
data.drop( ['Age_Group.1'] , axis=1 ,inplace=True)
print(" \u2714 Deleted duplicate column.")


print ("=" * 100)
print("4. Handle numerical columns")
print("=" * 100)

print("For Continuous Numerical data check if the values fit within the domain allowed limits")
print("In our case the columns 'Bill', 'CustomerID' and 'EsstimatedSalary' dont allow negative values.")

print(f"\n\nRows with Bill negative: \n{data.loc[ data['Bill'] < 0 ]}")
print(f"\n\nRows with CustomerID negative: \n{data.loc[ data['CustomerID'] < 0 ]}")
print(f"\n\nRows with EstimatedSalary negative: \n{data.loc[ data['EstimatedSalary'] < 0 ]}")

print("\n\nSet the negative column entry to NAN")
data.loc[ data['Bill'] < 0 ] = np.nan
data.loc[ data['CustomerID'] < 0 ] = np.nan
data.loc[ data['EstimatedSalary'] < 0 ] = np.nan

print("\u2714 Done")


print("\n\nFor Discrete Numerical data in addition to allowed value, range of value is also checked.")
print("In our case the 'Rating(1-5)'  range is 1-5 and , 'NoOfPax' is 1-20")

ratings_out_of_range = data.loc[(data['Rating(1-5)'] < 1) | (data['Rating(1-5)'] > 5)]
print(f"Out of range values for 'Rating(1-5)' are \n {ratings_out_of_range[['Rating(1-5)']]} ")

noofpax_out_of_range = data.loc[(data['NoOfPax'] < 1) | (data['NoOfPax'] > 20)]
print(f"Out of range values for 'NoOfPax' are \n {noofpax_out_of_range[['NoOfPax']]} ")

print("Set out of range data entries to NAN")
ratings_out_of_range = np.nan
noofpax_out_of_range = np.nan
print("\u2714 Done")


print ("=" * 100)
print("5. Handle categorical columns")
print("=" * 100)

categorical_data_handling = """
         a. Get the unique values of the column
         b. Handle the data that has SPELLING ERRORS, CASE ERRORS. Ensure case is UNIFIED !
         c. Check whether the groups/categorices shown in unique values match the domain spec.

         If any unusual category found, delete that SPECIFIC RECORD

 1   Age_Group        11 non-null     object -------------------> Categorical (Nothing to change)
 3   Hotel            11 non-null     object -------------------> Categorical (Handle Spelling error of Ibis (Ibys))
 4   FoodPreference   11 non-null     object -------------------> Categorical

"""

print(categorical_data_handling)

print(f"Unique 'FoodPreference': {[fp for fp in data['FoodPreference'].unique()]}")
print(f"Unique 'Hotel': {[hotel for hotel in data['Hotel'].unique()]}")

data['FoodPreference'] = data['FoodPreference'].replace(['veg','Vegetarian'] , 'Veg')
data['FoodPreference'] = data['FoodPreference'].replace(['non-Veg'] , 'Non-Veg' )

data['Hotel'] = data['Hotel'].replace(['Ibis'], 'Ibys')



data.drop( ['index'] , axis=1 ,inplace=True)



print ("=" * 100)
print("Completed handling of in appropriate data")
print("=" * 100)