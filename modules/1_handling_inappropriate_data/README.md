# Data Preprocessing Pipeline Summary

**1. Initial Assessment & Deduplication (Steps 1–3)**
* **Identify:** Classify every column's data type (Numerical, Categorical, Ordinal, or Pure String).
* **Deduplicate:** Remove any duplicate rows (records) and duplicate columns from the dataframe.

**2. Numerical Validation (Step 4)**
* Evaluate continuous (CND) and discrete (DND) numerical data against domain-specific rules. 
* Ensure values meet constraints regarding signs (positive/negative), formatting (decimals vs. integers), and expected ranges. Delete entries that violate these rules.

**3. Categorical & Ordinal Cleaning (Steps 5–6)**
* Standardize the text by unifying the case and fixing spelling errors.
* Validate the unique values (and their expected ranks, in the case of ordinal data) against domain specifications. Drop entire records if they contain unrecognized categories or ranks.

**4. String & Date Handling (Steps 7–8)**
* **Strings:** Leave pure string columns completely unaltered.
* **Dates:** If you are performing Time Series analysis, convert date columns into a `datetime` format and set that column as the dataframe's index. Otherwise, skip this step.
