### **Day 1 Data Cleaning**


Question about the dataset: license https://www.kaggle.com/datasets/utkarshx27/survey-of-labour-and-income-dynamics


In this section we will explore the Project is created with:
Project is created with:

### **Step 1: Launch Dataiku:**
-----------------------------------

Please follow this link: https://www.dataiku.com/. Once the account is created, please create a new project by clicking on the "New Project" button. Enter the name "Day 1: Data Cleaning" and specify the location where you want to save the project.


### **Step 2: Import a dataset:**
-----------------------------------

Within the newly created project, you can import the dataset by following these steps:
- a. Click on the "Import your first dataset" button to open the import options.
- b. Choose the appropriate import method based on the location and format of your dataset. You can find the dataset of this first day under this link. 
- c. Once you have configured the import settings, click on the "Import" or "OK" button to initiate the import process.
- d. Click on the "Create" button.

### **Step 3: Data Cleaning:**
-----------------------------------

Now let's clean the data ! 

- Step 1: Handling Missing Values
- Step 2: Handling Outliers
- Step 3: Renaming columns 
- Step 4: Removing Duplicates 



#### **Step 3.1: Handling Missing Values:Green**
-----------------------------------
- **What:** Identify and handle missing values in your dataset. This can be done by deleting rows or columns with a large number of missing values. 
- **How:**
    -  In the flow, locate the dataset you want to clean. It should be represented as a box or node in the flow canvas.
    - On the menu click on the button "RECIPE" - visual - date preparation
    - This will open a popup, where you can select the dataset 
    - Once the dataset is loaded to delete missing values (NA - represented in red) click on the cell and select "Remove Rows equal to NA". Please do the same for the column "education".
- **Expected:** How many rows are in your dataset (expected 535)

#### **Step 3.2: Handling Outliers: Orage**
-----------------------------------
- **What:** Identify and remove any outliers records from your dataset. 
- **How:**
    - Click on the specific column "wages" and click on "analyze" this will show potential outliers
    - Click on "actions" and "remove rows outside of 1.5 IQR"
    - Please do the same for the "education" and "age" columns 
- **Expected:** How many rows are in your dataset (expected 514)


#### **Step 3.3: Renaming columns:**
-----------------------------------
- **What:** Rename columns for clarity
- **How:**
    -  Click on col_0
    - Rename the columnn to ID


#### **Step 3.4: Removing duplicates:**
-----------------------------------
- **What:** Identify and remove any duplicate records from your dataset. Duplicates can skew your analysis and introduce bias. DataIKU provides tools to identify and remove duplicates based on specific columns or across the entire dataset. 
- **How:**
    -  Click on one of the cell of the column ID and click on "Remove rows equal to 2".
- **Expected:** How many rows are in your dataset (expected -3)


### **Step 4: Data Visualization:**
-----------------------------------


### **Step 5: Export the dataset:**
-----------------------------------