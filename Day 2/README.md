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


- Select the **"target_medv"** (= **median_home_value**) which corresponds to the target variable or what we want the model to predict (the price of the house).
<img width="362" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/46b270dd-a98c-42db-93cf-c1f29aab69a3">

- Select **"Quick Prototypes"** (top left) and press the blue **"CREATE"** (bottom right) .
- **c.** This is the space where we will be training the Machine Learning model ! **DON'T clicking on "TRAIN" yet**, because would like to choose some options for how to do regression. Click on **"DESIGN"** tab (top middle)

<img width="198" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/65a8a2ba-ff45-4651-ac38-7498ad2bae6c">

- In the new view, navigate to **"Algorithms"** from the options on the left.

<img width="166" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/0bdfd414-4a7c-4347-8be9-6e7f40fe35e7">

- Leave on "ON" just the **Ridge Regression**. On the left part of the **DESIGN** section, you can also see different options: 
    -  **BASIC -> Target:** We model the problem as a Regression and our target variable is "target_revenue"
    - **BASIC - Train / Test Set:** This allows us to control how the dataset is split into a training and testing set, we can modify that ratio
    - **BASIC - Metric:** In our case, we are interested in the R2 Score
    - **Modeling - Algorithms:** Here we can define the different algorithms we want to define for our Regression, we can also define the hyperparameters for our models

We won't change any other option (It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/models.png)). Click on the blue **"TRAIN"** (top right). 

<img width="581" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/5a119545-3ea2-4fd5-9404-99a1c5425a67">

In the new popup click "TRAIN" again. The model is training. 




What is the R2 score ? (expected: [0.753](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/accuracy_model.png))

<img width="944" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/4935a2a3-d77f-458d-8220-bf4877734f72">

**Time to pause and THINK!** Which are the parameters that positively or negatively influence the regression? Look at the above figure. 



- **d.** Let's train the model using different parameters! Using the same model change the **train ratio to 0.6** (this can be done by clicking **DESIGN** and **BASIC - Train/Test set** and change the "Train/Test Set" parameters to 0.6 for the "train ratio"), what is the accuracy ? (expected: [0.696](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/accuracy_model_2.png))



- **e.** Now try **other algorithms**. Go again to DESIGN, and from the Algorithms in the left, pick several of them:
    - Use the train ratio **0.8** and the Algorithm: **Random Forest**: What is the accuracy ? (expected: 0.871)
    - Use the train ratio **0.8** and the Algorithm: **Gradient tree boosting**: What is the accuracy ? (expected: 0.901)
    - Use the train ratio **0.8** and the Algorithm: **Ridge Regression**: What is the accuracy ? (expected: 0.753)
    - Use the train ratio **0.8** and the Algorithm: **Lasso Regression**: What is the accuracy ? (expected: 0.700 )
    - Use the train ratio **0.8** and the Algorithm: **KNN**: What is the accuracy ? (expected: 0.683)
    It should look [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/model_selection_.png)
    - What is the best model ? (expected: Gradient Boosted Tree - 0.901 )
    - Your dashboard should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/regression_testing_models.png)

<img width="938" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/c0b4cb79-e412-4bb9-8550-c779c2bc451d">



**Double-click** (important!) on the best model (i.e: Gradient Tree Boosting). 

<img width="267" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/ee0805a8-f2f7-4606-ad48-383cfb66be01">


You will move to another screen. Click on white **"DEPLOY"** button (top right). 

<img width="957" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/6924160e-7f98-4202-a0d6-1922a7b7f100">

 Your flow will look like with the new predictive model in it.

 <img width="386" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/b499a06f-697c-4636-9b69-e485530b0b9b">


Now, we have this predictive model in our flow, and we can apply other data to it.

- **f.** Test the model with new data ! 
    - When machine learning models are trained, you should provide new "unseen" data (also known as "out-of-sample" data) to see how the model would behave in the real-world. To do so, you can download the test dataset that we have prepared for you under this [link](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Regression/1_boston_housing_testing_set.csv), by clicking the "Raw" button and then saving with Ctrl-S (provide a name such as "regression_test.csv").

<img width="154" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/85be2149-005d-4986-b274-3f9eec432357">

    
Import the dataset as **"testing_set"** (you should know how to do that by now! ;). If you forgot, go to "Flow".

<img width="158" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/024116ab-88a0-4d93-ace2-c853e15bd804">

then Dataset -> Upload your files.

<img width="212" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/8404d89c-4acf-4426-944d-c172ef5f2ce6">

<img width="481" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/558b660e-1b08-48e9-89ce-7804c9e2d4d6">

  
    
Once imported, go back to the "Flow" (again!) and click/select the newly imported data. 

<img width="610" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/5a3511b0-2a2b-477d-8d9d-4d6095268914">


Only AFTER you click on the new dataset, on the right tab scroll down to find the green **"Predict**".

<img width="644" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/bd21a517-c712-48ed-8fc2-a23d2504894a">


<br>

Select the Prediction model **target_medv (regression)** model 

<img width="249" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/4648a214-25c8-4441-b381-b7f81db0586e">

Click on "CREATE RECIPE" (bottom right). In the next screen, click on the green [RUN] button (bottom left).

Go back to the "FLOW" (again!). **Double-click** on the "testing_set_scored" to see the actual values and the predictions.

<img width="660" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/c688965c-062a-4094-b16f-9c9c55a22343">

Scroll to the right part of the table and compare the column "prediction" with the values of the test set: **median_values_home** 22.4, 20.6, 23.9, 22.0, 11.9

<img width="232" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/84349b9f-f993-485b-85bd-c0326f9f4b54">

<br>
**REMEMBER**: We should ALWAYS see the accuracy of our model on data it has not seen before, otherwise we are cheating!

#### More information:
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

- **d.** Go back to the **"Flow"** and click on the blue **"Lab"** button on the right and click on **"AutoML prediction"**. Select the **"Clicked ad"** feature from the drop-down menu, which corresponds to the target variable (what we want to predict). Select **"Quick Prototypes"** and press **"CREATE"** (bottom right).
- **c.** This is the space where we will be training the Machine Learning model ! **Before clicking on "TRAIN"**, we will have a look at how the model is initialized. Click on **"DESIGN"**.

It understands that this is a 2-class classification problem.

<img width="359" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/bdef4ced-f309-4bea-8e97-6d3950c132be">


Go to **"Algorithms"** (on the left and select the **"Logistic Regression"** only.

<img width="369" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/489e691c-4ff8-47c6-9dd0-ef4e74b747bb">




Then click blue "TRAIN" button (top right) and again TRAIN in the new screen. What is the score ? (expected: [0.990]
(https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/accuracy_models_day_2.png))

Review again the top coefficients:

<img width="519" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/1feca2d7-b5b1-4f55-b649-c4b1db52c59f">




- **d** Now have try different algorithms:
    - Use the train ratio **0.8** and the Algorithm: **Random Forest**: What is the accuracy ? (expected: 0.992)
    - Use the train ratio **0.8** and the Algorithm: **Gradient tree boosting**: What is the accuracy ? (expected: 0.992)
    - Use the train ratio **0.8** and the Algorithm: **Logistic Regression**: What is the accuracy ? (expected: 0.990)
    - Use the train ratio **0.8** and the Algorithm: **KNN**: What is the accuracy ? (expected: 0.993)
    It should look [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/model_selection_1_day_2.png)

    - What is the best model ? (expected:  KNN - 0.993 )
    - Your dashboard should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/best_models_classification.png)

**QUESTION:** Which are the characteristics that mostly affect if someone will click on an ad or not?

<img width="667" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/5171236e-d9d7-4f48-b75c-62f151a27ab5">


Now click on the Random Forest model (from the list on the left), you move to a new screen and click on "DEPLOY" (top right) and then "Create". Your flow should now look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/HELP/new_flow_deployed_day_2.png)

- **f.** Test the model with new data ! 
    - When machine learning models are trained, you can input new "unseen" data to see how the model would predict a certain value. To do so, you can download the test dataset that we have prepared for you under this [link](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Classification/1_advertising_testing_set.csv) (remember to download as "raw" file, and then save with CTRL-S). Now, as done before, import the dataset naming it "testing_set".

Once imported, go back to the "Flow" (again!), click/select the newly imported test dataset, and then scroll down on the right tab to find the green "Predict". Select the "Predict Clicked on Ad (binary)" as the Prediction model and create the recipe. Then click on the green "RUN" (bottom left). 

After the job is finished, go back to the **"Flow"** you should see this pipeline. 

<img width="545" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/3d8c4321-a0d2-46aa-a4d5-29e4746f44fe">


**Double-click** on scored dataset to see the predicted values. **How many predictions were correct??**

<img width="846" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/f9508c49-4eca-4a0d-988c-7ad9bf090c7a">


<br>

Congratulations!! You have built and deployed your first classification model! Try it on your own dataset. You saw how easy it is!
