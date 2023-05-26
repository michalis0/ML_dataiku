### **Day 2: Regression and Classification**

----
### **Step 0: Initialization:**
-----------------------------------

Today we are going to train machine learning models ! To do so we need to go back on DataIku and create the necessary projects. 

Go back to the root of the project and create two new projects: 

1. First project named: regression
- a. Click on "NEW PROJECT" - "Blank project" and name it "regression"
- b. Import the dataset from this link:  (this is the cleaned version of the dataset we used yesterday)


----
### **Step 1: Regression:**
-----------------------------------

Please follow this link: https://www.dataiku.com/. Once the account is created, please create a new project by clicking on the "New Project" button - "Blank Project". Enter the name "Day 1: Data Cleaning: Survey of Labour and Income Dynamics" and specify the location where you want to save the project.

### **Step 2: Classification:**
-----------------------------------

### **Step 2: Classification:**
-----------------------------------

### **Step 2: Classification:**
-----------------------------------

### **Step 2: Classification:**
-----------------------------------

-----
### **Step 2: Classification:**
-----------------------------------

### **Step 2: Classification:**
-----------------------------------

### **Step 2: Classification:**
-----------------------------------

### **Step 2: Classification:**
-----------------------------------

----
### **Step 3: Quick, Draw (image recognition AI ):**
-----------------------------------

**What is Quick draw ?** Quick Draw is an online game where you draw pictures and a computer tries to guess what you're drawing. You have a limited time to sketch, and the computer uses artificial intelligence to recognize and guess the object you're trying to depict. It's a fun way to test your drawing skills and see how well the computer can understand your creations!
Follow this link to test it ! https://quickdraw.withgoogle.com/ 



Within the newly created project, you can import the dataset by following these steps:
- a. First download the dataset we will be using for this project. You can find the dataset of this first day under this link: https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Dataset/NotCleaned/Income_dataset.csv and click on the download button "Download raw file".
- b. Click on the "Import your first dataset" - "select files" and drag the dataset you just downloaded. Once the dataset is imported click on "CREATE". You just imported your dataset! 
- c. Let's take a look at the dataset, as we can see, it has the following columns:
    - col_0: the ID
    - wages: composite hourly wage rate from all jobs
    - education: number of years of schooling
    - age: in years
    - sex: a factor with levels: Female, Male.
    - language: a factor with levels: English, French, Other
- d. This dataset shows information on various aspects of labor market activities, income, and related factors for individuals and households in Canada over time. Using this dataset, we will try to predict the salary based on those informations (features). In fact, predict salary based on wages, education, age, sex, and language, allowing for better compensation decision-making and understanding potential pay disparities. The salary is what we call the "target variable". But before creating the machine learning model, we need to clean the model. 

**Check**: You dataset should have 1'000 rows and 6 columns. 

-----
### **Step 3: Data Cleaning:**
-----------------------------------

You may ask yourselves why we need to clean this dataset, as it may seem complete. We clean data for several reasons:
- **Accuray:** Cleaning data ensures that it is accurate, free from errors, and inconsistencies, enabling reliable analysis.
- **Consistency:** data cleaning helps ensure consistency by standardizing formats, resolving discrepancies, and handling missing values
- **Quality:** clean data improves the overall quality of analysis and models, minimizing biases, outliers, and irrelevant information. 

Now let's clean the data ! We will perform the steps below in order to have a perfectly cleaned dataset, which we could use to build our machine learning models, to make predictions ! 

- **Step 1:** Handling Missing Values
- **Step 2:** Handling Outliers
- **Step 3:** Renaming columns 
- **Step 4:** Removing Duplicates 


After importing the dataset, click on teh tab menu "Day 1: Data Cleaning: Survey...", this will show a dashboard, you can now click on "Go to Flow". The "flow" refers to a visual interface that allows users to create and manage data pipelines, workflows, and transformations for data preparation, analysis, and machine learning tasks. You can now select the tab "RECIPE" and select "Visual" and click on "Data Preparation". Now on the popup, select the "income dataset" and click on "CREATE RECIPE". This creates a space where you can perform data cleaning techniques. Lets start cleaning ! 
    

#### **Step 3.1: Handling Missing Values:Green**
-----------------------------------
- **What:** Identify and handle missing values in your dataset. This can be done by deleting rows or columns with a large number of missing values. 
- **How:**
    - To delete missing values (NA - represented in red) click on the cell and select "Remove Rows equal to NA". Please do this for two specific columns: "wages" and "education". 
- **Expected:** How many rows are in your dataset (Expected: -447 and -18 => 535 rows left) 

#### **Step 3.2: Handling Outliers: Orage**
-----------------------------------
- **What:** Identify and remove any outliers records from your dataset. (An outlier data point is a value that significantly deviates from the expected or typical range of values in a dataset)
- **How:**
    - Click on the specific column "wages" and click on "analyze", this opens a popup which shows potential outliers. 
    - Click on "actions" and "remove rows outside of 1.5 IQR"
    - Please do the same for the "education"
- **Expected:** How many rows are in your dataset (Expected: -11 and -10  => 514 rows left) 


#### **Step 3.3: Renaming columns:**
-----------------------------------
- **What:** Rename columns for clarity
- **How:**
    -  Click on col_0 and click "Rename", and insert "ID". This columns is the ID column which is used to uniquely identify each row or instance in a dataset, allowing for easy referencing and identification of specific records. 
    - Rename the columnn to ID. Renaming "col_0" to "ID" provides a more descriptive and meaningful name, enhancing the readability and interpretability of the dataset.

- Once this is done, click on "RUN", this will clean the table by executing the operations that we have created. Then go back to the "flow board", by clicking on "Day 1: Data Cleaning: Survey..."

#### **Step 3.4: Removing duplicates:**
-----------------------------------
- **What:** Identify and remove any duplicate records from your dataset. Duplicates can skew your analysis and introduce bias. 
- **How:**
    - There are duplicate rows in the dataset that we need to remove, i.e: row 988 and 998
    - Now please select "RECIPE" and select "visual" and click on "group". In the popup select the "Income_dataset_prepared" and group by "wages". Now rename the dataset as "cleaned_dataset" and select the format "CSV". 
    - Now add all the keys "Select key to add" except the "ID" column. Then click on "RUN" (it is okay to have warnings)
    - Go back to the "flow" screen and click on the last dataset "cleaned_dataset"
- **Expected:** How many rows are in your dataset (Expected: 527)

---
### **Step 4: Data Visualization:**
-----------------------------------

We will now focus on Data Visualization, which is used to visually represent data patterns, relationships, and insights in a more accessible and intuitive way, aiding understanding and decision-making. To do so we will perform 3 different visualizations:

- Plot 1: Plot Income Distribution by Education Level
- Plot 3: Plot Income by Age Group
- Plot 4: Plot Income by Gender

---
#### **Step 4.1:** Plot Income Distribution by Education Level

- **What:** Visualize a histogram or box plot showing the distribution of income across different education levels, highlighting any disparities or trends.

- **How:**
    - Click on "cleaned dataset" then click on the tab "Charts" - this is how we are going to create our plots. I will walk you through the first plot - Income Distribution by Education level, where we will plot a histogram showing the distribution of income across different education levels. To do so, drag the "education" column in the X axis and the "wages" column in the Y axis. 

    - There are duplicate rows in the dataset that we need to remove, i.e: row 988 and 998
    - Now please select "RECIPE" and select "visual" and click on "group". In the popup select the "Income_dataset_prepared" and group by "wages". Now rename the dataset as "cleaned_dataset" and select the format "CSV". 
    - Now add all the keys "Select key to add" except the "ID" column. Then click on "RUN" (it is okay to have warnings)
    - Go back to the "flow" screen and click on the last dataset "cleaned_dataset". Then click on "PUBLISH" and create. This will create a Dashboard with all the plots. 
    
Do the same for the other plots ! (you can try scatter plots, pie charts, feel free to test different graphs)

### **Step 5: Export the dataset:**
-----------------------------------
To export the dataset, go back to the "flow" and click on "cleaned_dataset" then click on "ACTION" and select "Export". 