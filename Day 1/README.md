# Day 1 Data Cleaning and Visualization

A machine learning scientist will spend 80% of his/her time on data wranging: finding/creating/labelling a dataset, "cleaning" it and getting insights with the aid of visualization. We will deal with this part today.

<img width="450" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/37fe2aa6-0e27-44cd-8054-c37e36a95014">



## Table of contents 
* [Step 1 Launch Dataiku](#step-1-dataiku)
* [Step 2 Import the dataset](#step-2-import-the-dataset)
* [Step 3 Data Cleaning](#step-3-data-cleaning)
* [Step 4 Data Visualization](#hour-2-data-visualization)
* [Step 5 Export the dataset](#step-5-export-the-dataset)

-----------------------------------
### **Step 1: Dataiku**
-----------------------------------

We will be using Dataiku to do no-code machine learning.
Please follow this link: https://www.dataiku.com/company/academic-program/. Go to the bottom right of this page, and create an "Individual Academic Licence" (click on the "Get Started") It may take 10mins or so for the environment to be setup, because it will be created on the cloud.

<img width="1276" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/c068da44-ba84-4b13-96c3-384b58d37cb3">


**Note for later:** Because this is on the cloud, it may "turn-off" later. If this happens, when you sign-in to [dataiku.com](dataiku.com) you may have to turn ON your instance again from the main dashboard. Once powered-up, click on blue "Open Instance" to load the main view of DataIku.


<img width="400" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/64d0e84d-877d-4bed-84bf-35addd09c6e1">

<br><br>
**Until your instance is created, you can watch this nice video that [showcases various features of Dataiku.](https://youtu.be/-amc9iVauuE).**
<br><br>



With the account is created, create a new project. This is done by:
- Clicking on the **"New Project"** button - **"Blank Project"**
- Entering the name **"Regression: Boston Housing Dataset"**
- Click on **"CREATE"**

You just created your first project ! It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_1_init.png).

-----------------------------------
### **Step 2: Import the dataset:**
-----------------------------------
However, your new project has no dataset yet. Let us add one.
Within the newly created project, you can import the dataset by following these steps:
- **a.** Download the dataset we will be using. You can find the dataset of this first day under this [link](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Dataset/NotCleaned/1_boston_housing_dataset.csv) and click on the download button "Download raw file".

<img width="207" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/db4be753-bd43-4b0e-a923-fdff74d1ce49">


- **b.**
<img width="257" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/0b76d4c9-c7ab-4b19-8256-bf7ef3e3847b">


- Click on the **"IMPORT YOUR FIRST DATASET"** - **"upload your files"** and drag the dataset you just downloaded *(1_boston_housing_dataset.csv)*. Once the dataset is imported click on "CREATE". You just imported your dataset! 
- **c.** Have a look at the dataset and the different features (or columns), we have:
    - **crime_rate:** per capita crime rate by town.
    - **residential_land_zone:** proportion of residential land zoned for lots over 25,000 sq.ft.
    - **bounds_river:** charles River dummy variable (1 if tract bounds river; 0 otherwise)
    - **nitric_oxides_concentration:** nitric oxides concentration (parts per 10 million)
    - **average_rooms:** average number of rooms per dwelling
    - **pre_1940_units:** proportion of owner-occupied units built prior to 1940
    - **employment_distance:** weighted distances to five Boston employment centres
    - **accessibility_highways:** index of accessibility to radial highways
    - **property_tax_rate:** full-value property-tax rate per $10,000 
    - **pupil_teacher_ratio:** pupil-teacher ratio by town
    - **lower_status_population:** % lower status of the population
    - **median_home_value:** Median value of owner-occupied homes in $1000's -> **Target variable**

- **d.** The Boston Housing dataset is a collection of data regarding housing prices and various attributes in different suburbs of Boston. **The variable we aim to predict using machine learning models is the median value of owner-occupied homes in thousands of dollars or median_home_value**.


**Check**: Your dataset should have **502 rows** and **12 columns**. 

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


You should currently see the table containing the dataset (it should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_3_init.png)). 

Now click on the top left part of the window "Regression: Boston Housing Dataset".
<img width="260" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/c2e12556-7610-47e0-a446-ecc9a7057368">


This will show your [project](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_1_init_project_overview.png), you can now click on **"GO TO FLOW"**. 

<img width="409" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/668b356a-10b9-410c-9ef6-6dcbf9923915">


The **flow** allows you to do various operations on your datasets, perform analyses and machine learning tasks. 

You can now select on the top the button **"RECIPE"** and select **"Visual"** and click on **"Data preparation"**. 
<img width="529" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/da4b4f31-60fc-464f-ab50-55735b66fccb">

Now on the popup, select the "1_boston_housing_dataset" and click on **"CREATE RECIPE"**. This creates a space where you can perform data cleaning techniques. (it should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_3_cleaning.png)) Let's start cleaning ! 


-------------------------------------------
#### **Step 3.1: Handling Missing Values:**
-----------------------------------
- **What:** Identify and handle missing values in your dataset. 

- **How:** You will see that the first column (crime_rate) has some rows with no values. Click on a cell that has no data (in the column "crime_rate") and select "Remove rows where cell is empty"

<img width="348" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/2926a84d-ee09-4d23-9ae6-159b8e6366aa">

- **Expected:** How many rows are in your dataset now? (Expected: -2 -> 500 rows left) 


**Note:** In the so-called recipe, we will be adding several operations that we wish to do. We will apply them all at the end.


-----------------------------------
#### **Step 3.2: Handling Outliers:**
-----------------------------------
- **What:** Identify and remove any outliers records from your dataset. 

- **How:** Click on the right part of column "residential_land_zone" and click on **"Analyze"**, this opens a popup which shows potential outliers. 

<img width="153" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/9640dd23-f3f7-427d-a10d-e7224939af49">


Click on **"ACTIONS"** and **"remove rows outside of 5 IQR"**

<img width="277" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/9f7574e1-62cc-4b87-8017-b01f6bcfb05b">

- **Expected:** How many rows are in your dataset (Expected: -30 -> 470 rows left)
  
<img width="221" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/bd75e2c1-7ae5-4de6-96bc-f3deb189c7ee">


-----------------------------------
#### **Step 3.3: Renaming columns:**
-----------------------------------
- **What:** Rename columns for clarity

- **How:** Click on right part of the column "median_home_value" and click **"Rename"**, and insert "target_medv". This columns is the target column, which corresponds to the value we would like to predict with our model. It is a good approach to give it the name of the target variable, in order to add some clarity in the dataset.

Once this is done, click on **"RUN"** (bottom left part of the screen). 

<img width="178" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/06140760-c182-44e7-9245-ef7facee91a2">


This will apply all the operations, one-by-one, on the table. (It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_3_4_clean.png)) Then go back to the "flow board", by clicking on "Regression: Boston Housing Dataset" -> "GO TO FLOW".  (It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_flow_board.png))

<img width="395" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/3b6de848-b044-4675-a175-ed870d750870">



-----------------------------------
#### **Step 3.4: Removing duplicates:**
---------------------------------------
- **What:** In this step we will identify and remove any duplicate records from the dataset. Duplicates are rows that are exactly identical. Duplicates can skew your analysis and introduce bias.

- **How:** There are duplicate rows in the dataset that we need to remove. We are in the flow view. select **"RECIPE"** and select **"visual"** and click on **"distinct"**.

<img width="317" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/45da5a96-556f-44bf-85a2-ab0705b57962">


- In the popup select the **"1_boston_housing_dataset_prepared"**. Accept the output dataset as **"1_regression_cleaned_dataset"**.  Then click on **"RUN"** (bottom left).

<img width="506" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/c159b1f9-8944-4403-b19f-15af4281afeb">

In the new screen that pops up, click on the green **RUN** button on the bottom left.

- Go back to the **"Flow"** screen (you should know by now how! ;) and **double-click** on the last dataset **"1_regression_cleaned_dataset"**
- **Expected:** How many rows are in your dataset (Expected: 468)

<img width="279" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/c83dde5d-775a-4829-a03d-ca66b46ce8b6">


-----------------------------------
#### **Step 3.5: The final training dataset:**
-----------------------------------
Now we will create our final dataset which we will use tomorrow to perform regression.

Now, go back to the flow. **Right-click** on the last dataset created (1_regression_cleaned_dataset), and click rename and rename it to **"1_boston_housing_training_set"**. 



We have only scratched the surface, on what you need to do as a data and machine learning scientist when dealing with data. Remember, that the role of the data scientists deals to a large extent with data wrangling! If you can do this part very fast and efficiently, it will save you a lot of time! (so you can spend your time on the beach, on your sailing boat, doing BBQs,...)

-----------------------------------
### **Hour 2: Data Visualization:**
-----------------------------------

<img width="250" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/1540718b-4af9-4a91-b8e1-47b6663390a1">



We will now focus on **Data Visualization**, with which we can comprehend data patterns and relationships. Visualization also provides insights in a more intuitive way, aids understanding and decision-making. We will perform **4 different visualizations:**

- **Plot 1:** Scatter Plot of Average Number of Rooms vs. Housing Prices (scatter plot)
- **Plot 2:** Average Housing Prices by nitric oxides concentration (bar plot)
- **Plot 3:** Average Housing Prices by per capita crime rate (pie chart)
- **Plot 4:** Box Plot of Housing Prices by nitric oxides concentration (box plot)

--------------
#### **Step 4.1:** Plot Income Distribution by Education Level
-----------------------------------

- **What:** Visualize a scatter plot to explore the relationship between age and revenue.
- **How:** Click on "1_boston_housing_training_set" then click on the tab **"Charts"** (it is on the right, 2nd tab)

<img width="369" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/8625d7bd-6079-476d-ba94-a60dcc4563cf">


I will walk you through the first plot 

- *Scatter Plot of Average Number of Rooms vs. Housing Prices*. On the left side we see the columns of the dataset.  In the combo-box in the middle select **"Scatter plot"**. Drag and drop the column **average_rooms** on the "Show X" position and the **target_medv** on the "Show Y".
<img width="798" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/d5e5095a-26f9-4a99-b2b7-be327f848eca">


Click on **"PUBLISH"** then **"CREATE"**, this creates a Dashboard.

    
Do the same for the other plots ! (you can try scatter plots, boxplots, etc. Feel free to explore different graphs) (Your dashboard should look something like this:

<img width="751" alt="image" src="https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/step_4_dashboard.png">



-----------------------------------
### **Step 5: Export the dataset:**
-----------------------------------
To export the dataset, go back to the **"Flow"** and click on **"1_boston_housing_training_set"** then open the panel and click on **"Export"**. If you did not manage to do all the tasks, the cleaned dataset can be found [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Regression/1_boston_housing_training_set.csv). Please have it downloaded for tomorrow, as we will use it for the machine learning models ! 


-----------------------------------
### ** HOMEWORK **
-----------------------------------
Yes, there is a bit of homework as well!

- Pick a dataset you have been working on for your research, and do 1 or 2 visualizations of it. Share with the rest of the class by posting them in our Teams channel! Consider the visualization principles and your storytelling...

- For those that prefer to follow tutorials, do [this one](https://content.dataiku.com/dataiku-mystery-gang-data-project) at home.
  
- For more information consult the dataiku tutorials on [data visualization](https://knowledge.dataiku.com/latest/data-viz/index.html#) and for the more ambitious ones how to code an [interactive webapp](https://knowledge.dataiku.com/latest/data-viz/webapps/tutorial-python-bokeh.html) with Bokeh inside dataiku.

  


