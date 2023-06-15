# Day 1 Data Cleaning and Visualization


## Table of contents 
* [Step 1 Launch DataIku](#step-1-launch-dataiku)
* [Step 2 Import the dataset](#step-2-import-the-dataset)
* [Step 3 Data Cleaning](#step-3-data-cleaning)
* [Step 4 Data Visualization](#step-4-data-visualization)
* [Step 5 Export the dataset](#step-5-export-the-dataset)

-----------------------------------
### **Step 1: Launch Dataiku:**
-----------------------------------

Please follow this link: https://www.dataiku.com/company/academic-program/ and create an account.

Once the account is created, please create a new project, this is done by:
- Clicking on the **"New Project"** button - **"Blank Project"**
- Entering the name **"Regression: Boston Housing Dataset"**
- Click on **"CREATE"**

You just created your first project ! It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_1_init.png).

-----------------------------------
### **Step 2: Import the dataset:**
-----------------------------------

Within the newly created project, you can import the dataset by following these steps:
- **a.** Download the dataset we will be using. You can find the dataset of this first day under this [link](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Dataset/NotCleaned/1_boston_housing_dataset.csv) and click on the download button "Download raw file". <img width="232" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/a194b207-37d0-4fe7-b401-53df771e54db">

- **b.** Click on the **"IMPORT YOUR FIRST DATASET"** - **"upload your files"** and drag the dataset you just downloaded *(1_boston_housing_dataset)*. Once the dataset is imported click on "CREATE". You just imported your dataset! 
- **c.** Have a look at the dataset and the different features, we have:
    - **crim:** per capita crime rate by town.
    - **zn:** proportion of residential land zoned for lots over 25,000 sq.ft.
    - **chas:** charles River dummy variable (1 if tract bounds river; 0 otherwise)
    - **nox:** nitric oxides concentration (parts per 10 million)
    - **rm:** average number of rooms per dwelling
    - **age:** proportion of owner-occupied units built prior to 1940
    - **dis:** weighted distances to five Boston employment centres
    - **rad:** index of accessibility to radial highways
    - **tax:** full-value property-tax rate per $10,000 
    - **ptratio:** pupil-teacher ratio by town
    - **lstat:** % lower status of the population
    - **medv:** Median value of owner-occupied homes in $1000's -> **Target variable**

- **d.** The Boston Housing dataset is a collection of data regarding housing prices and various attributes in different suburbs of Boston. **The variable we aim to predict using machine learning models is the median value of owner-occupied homes in thousands of dollars**.


**Check**: You dataset should have **502 rows** and **12 columns**. 

-----------------------------------
### **Step 3: Data Cleaning:**
-----------------------------------

You may ask yourselves why we need to clean this dataset, as it may seem complete. 

We clean data for several reasons:
- **Accuracy:** cleaning data ensures that it is accurate, free from errors, and inconsistencies, enabling reliable analysis.
- **Consistency:** data cleaning helps ensure consistency by standardizing formats, resolving discrepancies, and handling missing values
- **Quality:** cleaning the data improves the overall quality of analysis and models, minimizing biases, outliers, and irrelevant information. 

**Now let's clean the data !** We will perform the steps below in order to have a perfectly cleaned dataset, which we could use to build our machine learning models, to make predictions ! 

The cleaning steps we will go though: 
- **Step 1:** Handling Missing Values
- **Step 2:** Handling Outliers
- **Step 3:** Renaming columns 
- **Step 4:** Removing Duplicates 


You should currently see the table containing the dataset (it should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_3_init.png)). Now click on the tab menu "Regression: Boston Housing Dataset", this will show your [project](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_1_init_project_overview.png), you can now click on **"GO TO FLOW"**. <img width="471" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/52699461-fb78-4942-a632-cb71c857ce9b">


The **"flow"** allows you to create and manage data pipelines, workflows, and transformations for data preparation, analysis, and machine learning tasks. 

You can now select the tab **"RECIPE"** and select **"Visual"** and click on **"Data preparation"**. Now on the popup, select the "1_boston_housing_dataset" and click on **"CREATE RECIPE"**. This creates a space where you can perform data cleaning techniques. (it should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_3_cleaning.png)) Lets start cleaning ! 


-------------------------------------------
#### **Step 3.1: Handling Missing Values:**
-----------------------------------
- **What:** Identify and handle missing values in your dataset. 

- **How:** You should see some cells that do not have data, in order to identify them, please click on a cell that has no data (from the column "crim") and select "Remove rows where cell is empty"

- **Expected:** How many rows are in your dataset now (Expected: -2 -> 500 rows left) 

#### **Step 3.2: Handling Outliers:**
-----------------------------------
- **What:** Identify and remove any outliers records from your dataset. 

- **How:** Click on "zn" and click on **"Analyze"**, this opens a popup which shows potential outliers. Click on **"ACTIONS"** and **"remove rows outside of 5 IQR"**

- **Expected:** How many rows are in your dataset (Expected: -30 -> 570 rows left) 


#### **Step 3.3: Renaming columns:**
-----------------------------------
- **What:** Rename columns for clarity

- **How:** Click on "medv" and click **"Rename"**, and insert "target_medv". This columns is the target column, which corresponds to the value we would like to predict with our model. It is a good approach to give it the name of the target variable, in order to add some clarity in the dataset. 


Once this is done, click on **"RUN"** (bottom left). This will clean the table by executing the operations that we have created. (It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_3_4_clean.png)) Then go back to the "flow board", by clicking on "Regression: Boston Housing Dataset" -> "GO TO FLOW".  (It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_flow_board.png))



#### **Step 3.4: Removing duplicates:**
---------------------------------------
- **What:** In this setp we will identify and remove any duplicate records from the dataset, as duplicates can skew your analysis and introduce bias.

- **How:** There are duplicate rows in the dataset that we need to remove. Now please select **"RECIPE"** and select **"visual"** and click on **"group"**. In the popup select the **"1_boston_housing_dataset_prepared"** and group by **"crim"**. Now rename the output dataset as **"1_regression_cleaned_dataset"**. Now add all the keys **"Select key to add"**. Then click on **"RUN"** (It should look something like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/remove_duplicates.png)). Go back to the **"flow"** screen and click on the last dataset **"1_regression_cleaned_dataset"**
- **Expected:** How many rows are in your dataset (Expected: 468)


#### **Step 3.5: Creating the training set:**

Now, please go back to the flow, click on the last dataset created (1_regression_cleaned_dataset), and as done before, click on **"RECIPE"** - **"Visual"** - **"Data Preparation"**. Please name the output dataset **"1_boston_housing_training_set"**. Please delete the column **"count"** and click **"RUN"**.  (Your data flow should look something like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_3_4_clean_flow.png))



-----------------------------------
### **Step 4: Data Visualization:**
-----------------------------------

We will now focus on **Data Visualization**, which is used to visually represent data patterns, relationships, and insights in a more accessible and intuitive way, aiding understanding and decision-making. To do so we will perform **4 different visualizations:**

- **Plot 1:** Scatter Plot of Average Number of Rooms vs. Housing Prices (scatter plot)
- **Plot 2:** Average Housing Prices by nitric oxides concentration (bar plot)
- **Plot 3:** Average Housing Prices by per capita crime rate (pie chart)
- **Plot 4:** Box Plot of Housing Prices by nitric oxides concentration (box plot)

--------------
#### **Step 4.1:** Plot Income Distribution by Education Level

- **What:** Visualize a scatter plot to explore the relationship between age and revenue.
- **How:** Click on "1_boston_housing_training_set" then click on the tab **"Charts"** - this is how we are going to create our plots. I will walk you through the first plot - *Scatter Plot of Average Number of Rooms vs. Housing Prices*, where we will plot the average number of rooms per dwelling (rm) on the x-axis and the Housing prices on the y-axis (target_medv). Select **"Scatter plot"** and drag and drop rm (x_axis) and target_medv (y_axis). Click on **"PUBLISH"** then **"CREATE"**, this creates a Dashboard (which is also accessible from the project root)

    
Do the same for the other plots ! (you can try scatter plots, pie charts, feel free to explore different graphs) (Your dashboard should look something like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_4_dashboard.png))
<img width="550" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/c4481a55-2458-413b-b90b-13317948e4d6">



-----------------------------------
### **Step 5: Export the dataset:**
-----------------------------------
To export the dataset, go back to the **"flow"** and click on **"1_boston_housing_training_set"** then open the panel and click on **"Export"**. If you did not manage to do all the tasks, the cleaned dataset can be found [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Regression/1_boston_housing_training_set.csv). Please have it downloaded for tomorrow, as we will use it for the machine learning models ! 
