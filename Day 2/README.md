# Day 2 Regression and Classification

With regression, we predict numerical values (e.g., someone's age, given his/her picture). With classification, categorical values (e.g., someone's eye color from his face picture).
<img width="324" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/71ac0c68-1ff1-4ecd-afcd-1d7d312adc84">


## Table of contents 
* [Step 1 Regression](#step-1-regression)
* [Step 2 Classification](#step-2-classification)

-----------------------------------
### **Step 1: Regression:**
-----------------------------------

- **a.** Please select your project: "Regression: Boston Housing Dataset". (If you did not manage to do the steps yesterday, please import the dataset [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Regression/1_boston_housing_training_set.csv)).
- **b.** To perform regression, select the dataset **"1_boston_housing_training_set"** and click on the **"Lab"** button (top right).
<img width="340" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/6b1c944f-2ac4-4426-9875-30b90d781f51">

-   click on **"AutoML prediction"**. Select the **"target_medv"** which corresponds to the target variable. Pick **"Quick Prototypes"** and press **"CREATE"**.
- **c.**This is the space where we will be training the Machine Learning model ! **Before clicking on "TRAIN"**, we will have a look at how the model is initialized. Please click on **"DESIGN"** and navigate to **"Algorithms"**. Please select the first model that we will use: **Ridge Regression**. In the **DESIGN** section, you can see differnent tabs: 
    -  **BASIC - Target:** We model the problem as a Regression and our target variable is "target_revenue"
    - **BASIC - Train / Test Set:** This allows us to control how the dataset is split into a training and testing set, we can modify that ratio
    - **BASIC - Metric:** In our case, we are interested in the R2 Score
    - **Modeling - Algorithms:** Here we can define the different algorithms we want to define for our Regression, we can also define the hyperparameters for our models

Now please click **"TRAIN"**. (It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/models.png)). What is the accuracy ? (expected: [0.753](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/accuracy_model.png))
    

- **d.** Lets train the model using different parameters! Using the same model change the **train ratio to 0.6** (this can be done by clicking **DESIGN** and **BASIC - Train/Test set** and change the "Train/Test Set" parameters to 0.6 for the "train ratio"), what is the accuracy ? (expected: [0.696](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/accuracy_model_2.png))

- **e.** Now try **other algorithms**:
    - Use the train ratio **0.8** and the Algorithm: **Random Forest**: What is the accuracy ? (expected: 0.871)
    - Use the train ratio **0.8** and the Algorithm: **Gradient tree boosting**: What is the accuracy ? (expected: 0.901)
    - Use the train ratio **0.8** and the Algorithm: **Ridge Regression**: What is the accuracy ? (expected: 0.753)
    - Use the train ratio **0.8** and the Algorithm: **Lasso Regression**: What is the accuracy ? (expected: 0.700 )
    - Use the train ratio 0.8 and the Algorithm: **KNN**: What is the accuracy ? (expected: 0.683)
    It should look [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/model_selection_.png)
    - What is the best model ? (expected: Gradient Boosted Tree - 0.901 )
    - Your dashboard should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/regression_testing_models.png)

    - Now click on the best model (i.e: Gradient Tree Boosting) and click on **"DEPLOY"**, it should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/best_models_deploy.png). Your flow should now look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/new_flow_deployed.png)

- **f.** Test the model with new data ! 
    - When machine learning models are trained, you can input new "unseen" data (also known as "out-of-sample" data) to see how the model would behave in the real-world. To do so, you can download the test dataset that we have prepared for you under this [link](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Regression/1_boston_housing_testing_set.csv). Now, as we have done before, please import the dataset as **"testing_set"**. Once it is imported please click on **"Predict**" in the tab on the right side and select the **target_medv (regression)** model and create the recipe. 
    - Then select all the input columns, except the **"medv"** column and click on [run](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/define_prediction.png). 
    - Compare the column "prediction" with the values of the test swet: **medv** 22.4, 20.6, 23.9, 22.0, 11.9
    - Once you get back to the "flow" you should see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/final_pipeline.png) pipeline, please click on testing_set_scored to see the predicted values. 

-----------------------------------
### **Step 2: Classification:**
-----------------------------------

- **a.** Please create a new project by clicking on **"NEW PROJECT"** and call it **"Classification: Advertising dataset"**. Now, please select the project.
- **b.** To perform classification, please download the dataset that we are going to use, that is accessible [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Classification/1_advertising_training_set.csv) and import it in the project.  

- **c.** This dataset has **916 rows** and **10 features**:
    - **Daily Time Spent on Site:** consumer time on site in minutes
    - **Age:** customer age in years
    - **Area Income:** average income of geographical area in which customer resides
    - **Daily Internet Usage:** average minutes a day a customer is online
    - **Ad Topic Line:** headline of the advertisement
    - **City:** city of the customer
    - **Male:** takes 1 if customer is male
    - **Country:** country of the customer
    - **Timestamp:** time at which customer clicked on ad
    - **Clicked ad:** 1 if clicked on ad and 0 otherwise.

Using this dataset, we will predict if a user has clicked or not the ad. 

- **d.** Please go back to the **"Flow"** and click on the **"lab"** tab and click on **"AutoML prediction"**. Please select the **"Clicked ad"** which corresponds to the target variable. Now please select **"Quick Prototypes"** and press **"CREATE"**.
- **c.** This is the space where we will be training the Machine Learning model ! **Before clicking on "TRAIN"**, we will have a look at how the model is initialized. Click on **"DESIGN"** and go to **"Algorithms"** and select the **"Logistic Regression"** only. Then click "TRAIN". What is the accuracy ? (expected: [0.990](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/accuracy_models_day_2.png))
- **d** Now have try different algorithms:
    - Use the train ratio **0.8** and the Algorithm: **Random Forest**: What is the accuracy ? (expected: 0.992)
    - Use the train ratio **0.8** and the Algorithm: **Gradient tree boosting**: What is the accuracy ? (expected: 0.992)
    - Use the train ratio **0.8** and the Algorithm: **Logistic Regression**: What is the accuracy ? (expected: 0.990)
    - Use the train ratio **0.8** and the Algorithm: **KNN**: What is the accuracy ? (expected: 0.993)
    It should look [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/model_selection_1_day_2.png)

    - What is the best model ? (expected:  KNN - 0.993 )
    - Your dashboard should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/best_models_classification.png)

    - Now click on the best model and click on "DEPLOY". Your flow should now look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/new_flow_deployed_day_2.png)

- **f.** Test the model with new data ! 
    - When machine learning models are trained, you can input new "unseen" data to see how the model would predict a certain value. To do so, you can download the test dataset that we have prepared for you under this [link](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Classification/1_advertising_testing_set.csv). Now, as we have done before, please import the dataset as "testing_set". Once it is imported please click on "Predict" in the tab on the right side and select the "Predict Clicked on Ad (binary)" as the Prediction model and create the recipe. Then click on run. 
    - Once you get back to the **"flow"** you should see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/final_pipeline_day_2.png) pipeline, please click on testing_set_scored to see the predicted values. 
