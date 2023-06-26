# Day 2 Regression and Classification

With regression, we predict numerical values (e.g., someone's age, given his/her picture). With classification, categorical values (e.g., someone's eye color from his face picture).

<img width="250" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/9c90430a-81f4-43c0-8768-91dc3d93260d">


## Table of contents 
* [Step 1 Regression](#step-1-regression)
* [Step 2 Classification](#step-2-classification)

-----------------------------------
### **Step 1: Regression:**
-----------------------------------
We will try to predict the selling price of a house, given its characteristics (number of rooms, area, etc).


- **a.** Please select your project: "Regression: Boston Housing Dataset". (If you did not manage to do the steps yesterday, please import the dataset [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Regression/1_boston_housing_training_set.csv)).
- **b.** To perform regression, select the dataset **"1_boston_housing_training_set"** (the final dataset after the data cleaning) and click on the blue **"Lab"** button (top right).
  
<img width="864" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/f73229bb-6a71-468c-b587-b037dc568a48">


- Next, click on green icon of **"AutoML prediction"**.

<img width="310" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/1a765f76-d34f-472e-8766-f0c9d30b4fea">


- Select the **"target_medv"** which corresponds to the target variable or what we want the model to predict (the price of the house). Pick **"Quick Prototypes"** and press **"CREATE"**.
- **c.** This is the space where we will be training the Machine Learning model ! **Before clicking on "TRAIN"**, we will have a look at how the model is initialized. Please click on **"DESIGN"** and navigate to **"Algorithms"**. Please select the first model that we will use: **Ridge Regression**. In the **DESIGN** section, you can see differnent tabs: 
    -  **BASIC - Target:** We model the problem as a Regression and our target variable is "target_revenue"
    - **BASIC - Train / Test Set:** This allows us to control how the dataset is split into a training and testing set, we can modify that ratio
    - **BASIC - Metric:** In our case, we are interested in the R2 Score
    - **Modeling - Algorithms:** Here we can define the different algorithms we want to define for our Regression, we can also define the hyperparameters for our models

Now please click **"TRAIN"**. (It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/models.png)). What is the accuracy ? (expected: [0.753](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/accuracy_model.png))

<img width="431" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/5c9e6412-a0e5-4c02-8a09-cc997b4f45ed">


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


  <img width="344" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/40f79e95-16f2-4a43-b871-b22765df5b02">


**Double-click** on the best model (i.e: Gradient Tree Boosting). You will move to another screen. Click on **"DEPLOY"** (top right). It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/best_models_deploy.png). Your flow will look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/new_flow_deployed.png).

Now, we have this predictive model in our flow, and we can apply other data to it.

- **f.** Test the model with new data ! 
    - When machine learning models are trained, you can input new "unseen" data (also known as "out-of-sample" data) to see how the model would behave in the real-world. To do so, you can download the test dataset that we have prepared for you under this [link](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Regression/1_boston_housing_testing_set.csv), by clicking the "Download Raw File". <img width="189" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/d22cc855-9e1b-4ac1-a65c-360b9cf3c998">
    
 Import the dataset as **"testing_set"** (as we did previously). 

<img width="249" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/45128c91-c454-4189-b262-19baa8b1ee8c">

  
    
Once imported, click/select the newly imported data and on the right tab scroll down to find the green **"Predict**".

<img width="267" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/8f2fd26e-971e-40eb-8026-ab67b1ff18a0">

Select the Prediction model **target_medv (regression)** model and click on "CREATE RECIPE". 
In the next screen, click on the green [RUN](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/define_prediction.png).  (bottom left).

Compare the column "prediction" with the values of the test set: **medv** 22.4, 20.6, 23.9, 22.0, 11.9

Once you get back to the "flow" you should see [this](HELP/final%20pipeline.png) pipeline, click on testing_set_scored to see the predicted values. 


## More information:
- See also the [model scoring tutorials at Dataiku](https://knowledge.dataiku.com/latest/ml-analytics/model-scoring/tutorial-scoring-data.html)
  

-----------------------------------
### **Step 2: Classification:**
-----------------------------------
<img width="192" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/73c5eb31-d31d-40d5-956e-59018e97d692">




Now, we will build a classification model. 
We will try to predict if an online user will click on an advertisement or not, based on various features. Such a predictive model is very important for websites. We should only show those advertisements for which have high-propensity to click on. We will build a predictive model just for one advertisement, but in reality you can imagine that we have models for many advertisements.

First, click on the bird on the top left, to go to the screen with our projects:

<img width="116" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/aae68b29-3ee6-4c43-a405-e2fafb61e1a4">



- **a.** Create a new project by clicking on **"NEW PROJECT"** and call it **"Classification: Advertising dataset"**. Select the project.
- **b.** To perform classification, download the dataset that we are going to use, that is accessible [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Classification/1_advertising_training_set.csv) and import it in the project.  

- **c.** This dataset has **916 rows** and **10 features**:
    - **Daily Time Spent on Site:** consumer time on site in minutes
    - **Age:** customer age in years
    - **Area Income:** average income of geographical area in which customer resides
    - **Daily Internet Usage:** average minutes a day a customer is online
    - **Ad Topic Line:** headline of the advertisement
    - **City:** city of the customer
    - **Male:** 1 if customer is male
    - **Country:** country of the customer
    - **Timestamp:** time at which customer clicked on ad
    - **Clicked ad:** 1 if clicked on ad and 0 otherwise.

Using this dataset, we will predict if a user will click or not on the ad. 

- **d.** Go back to the **"Flow"** and click on the **"lab"** tab and click on **"AutoML prediction"**. Select the **"Clicked ad"** which corresponds to the target variable. Select **"Quick Prototypes"** and press **"CREATE"**.
- **c.** This is the space where we will be training the Machine Learning model ! **Before clicking on "TRAIN"**, we will have a look at how the model is initialized. Click on **"DESIGN"** and go to **"Algorithms"** and select the **"Logistic Regression"** only.

<img width="450" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/39071020-58cd-43a7-810f-e14182284959">



Then click "TRAIN". What is the accuracy ? (expected: [0.990](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/accuracy_models_day_2.png))
- **d** Now have try different algorithms:
    - Use the train ratio **0.8** and the Algorithm: **Random Forest**: What is the accuracy ? (expected: 0.992)
    - Use the train ratio **0.8** and the Algorithm: **Gradient tree boosting**: What is the accuracy ? (expected: 0.992)
    - Use the train ratio **0.8** and the Algorithm: **Logistic Regression**: What is the accuracy ? (expected: 0.990)
    - Use the train ratio **0.8** and the Algorithm: **KNN**: What is the accuracy ? (expected: 0.993)
    It should look [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/model_selection_1_day_2.png)

    - What is the best model ? (expected:  KNN - 0.993 )
    - Your dashboard should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/best_models_classification.png)

**QUESTION:** Which are the characteristics that mostly affect if someone will click on an ad or not?

<img width="691" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/83b12b88-fbf0-4344-89a0-5fac00dc9e09">


Now click on the best model and click on "DEPLOY". Your flow should now look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/new_flow_deployed_day_2.png)

- **f.** Test the model with new data ! 
    - When machine learning models are trained, you can input new "unseen" data to see how the model would predict a certain value. To do so, you can download the test dataset that we have prepared for you under this [link](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Classification/1_advertising_testing_set.csv) (remember to download as "raw" file, clicking on the top right icon). Now, as done before, import the dataset naming it "testing_set".

Once imported, click/select the newly imported test dataset, and then scroll down on the right tab to find the green "Predict". Select the "Predict Clicked on Ad (binary)" as the Prediction model and create the recipe. Then click on run. 

Once you get back to the **"flow"** you should see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/final_pipeline_day_2.png) pipeline, click on testing_set_scored to see the predicted values. 
