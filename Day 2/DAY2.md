
**-------------------BEGIN 5 JUNE----------------------**


### **Day 2: Regression and Classification**

-------
### **Step 0: Initialisation:**
-------
*Disclaimer: Please make sure to have completed the tasks done yesterday*

You should now have 4 projects created, today we will essentially be using two of them: Regression and Classification. 

-----------------------------------
### **Step 1: Regression:**
-----------------------------------

- a. Please select your project: "Regression: Boston Housing Dataset"
- b. To perform regression, select the dataset "1_boston_housing_training_set" and click on the "lab" tab and click on "AutoML prediction". Please select the "target_medv" which corresponds to the target variable. Now please select "Quick Prototypes" and press "CREATE".
- c.This is the space where we will be training the Machine Learning model ! Before clicking on "TRAIN", we will have a look at how the model is initialized. please select the first model that we will use: Logistic Regression. Therefore, click on "DESIGN". We can see a few tabs:
    -  **Target:** We model the problem as a Regression and our target variable is "target_revenue"
    - **Train / Test Set:** This allows us to control how the dataset is split into a training and testing set, we can modify that ratio
    - **Metric:** In our case, we are interested in the R2 Score
    - **Modeling:** Here we can define the different algorithms we want to define for our Regression, we can also define the hyperparameters for our models

Lets have a look at when we train a model, go to "Algorithms" and select the "Ridge Regression" only. Then click "TRAIN". (It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/models.png)). What is the accuracy ? (expected: [0.753](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/accuracy_model.png))
    

- d. Lets train the model using different parameters! Using the same model change the train ratio to 0.6, what is the accuracy ? To do so, you can go on "DESIGN" and change the "Train/Test Set" parameters to 0.6 for the "train ratio"  (expected: [0.696](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/accuracy_model_2.png))

- e. Now have try different algorithms:
    - Use the train ratio 0.8 and the Algorithm: Random Forest: What is the accuracy ? (expected: 0.844)
    - Use the train ratio 0.8 and the Algorithm: Gradient tree boosting: What is the accuracy ? (expected: 0.893)
    - Use the train ratio 0.8 and the Algorithm: Ridge Regression: What is the accuracy ? (expected: 0.696)
    - Use the train ratio 0.8 and the Algorithm: Lasso Regression: What is the accuracy ? (expected: 0.655 )
    - Use the train ratio 0.8 and the Algorithm: KNN: What is the accuracy ? (expected: 0.705)
    It should look [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/model_selection_1.png)
    - What is the best model ? (expected: Gradient Boosted Tree - 0.893 )
    - Your dashboard should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/best_models.png)

    - Now click on the best model and click on "DEPLOY", it should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/best_models_deploy.png). Your flow should now look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/new_flow_deployed.png)

- f. Test the model with new data ! 
    - When machine learning models are trained, you can input new "unseen" data to see how the model would predict a certain value. To do so, you can download the test dataset that we have prepared for you under this [link](https://github.com/michalis0/ML_dataiku/blob/main/Day%202/Datasets/Regression/1_boston_housing_testing_set.csv). Now, as we have done before, please import the dataset as "testing_set". Once it is imported please click on "Predict" in the tab on the right side and select the target_medv (regression) model and create the recipe. 
    - Then select all the input columns, except the "medv" column and click on [run](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/define_prediction.png)
    .
    - Once you get back to the "flow" you should see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/final_pipeline.png) pipeline, please click on testing_set_scored to see the predicted values. 





**-------------------END 5 JUNE----------------------**



-----------------------------------
### **Step 2: Classification:**
-----------------------------------

- a. Please select your project: "Regression: Customer Analytics Dataset"
- b. To perform regression, select the dataset and click on the "lab" tab and click on "AutoML prediction". Please select the "target_revenue" which corresponds to the target variable. Now please select "Quick Prototypes" and press "CREATE".
- c.This is the space where we will be training the Machine Learning model ! Before clicking on "TRAIN", we will have a look at how the model is initialized. please select the first model that we will use: Logistic Regression. Therefore, click on "DESIGN". We can see a few tabs:
    -  **Target:** We model the problem as a Regression and our target variable is "target_revenue"
    - **Train / Test Set:** This allows us to control how the dataset is split into a training and testing set, we can modify that ratio
    - **Metric:** In our case, we are interested in the R2 Score
    - **Modeling:** Here we can define the different algorithms we want to define for our Regression, we can also define the hyperparameters for our models

Lets have a look at when we train a model, go to "Algorithms" and select the "Ridge Regression" only. Then click "TRAIN". What is the accuracy ? (expected: , this should look like this)
    
- d. Lets train the model using different parameters! Using the same model change the train ratio to 0.6, what is the accuracy ? 

- e. Now have try different algorithms:
    - Use the train ratio 0.8 and the Algorithm: Random Forest: What is the accuracy ? (expected: , this should look like this)
    - Use the train ratio 0.8 and the Algorithm: KNN: What is the accuracy ? (expected: , this should look like this)
    - Use the train ratio 0.8 and the Algorithm: Deep Neural Network: What is the accuracy ? (expected: , this should look like this)
- f. Test the model with new data ! 
    - When machine learning models are trained, you can input new "unseen" data to see how the model would predict a certain value. To do so click on "Quick Modeling ..." and click on "DEPLOY SCRIPT". 



---------
### **Step 3: Quick, Draw (image recognition AI ):**
-----------------------------------

**What is Quick draw ?** Quick Draw is an online game where you draw pictures and a computer tries to guess what you're drawing. You have a limited time to sketch, and the computer uses artificial intelligence to recognize and guess the object you're trying to depict. It's a fun way to test your drawing skills and see how well the computer can understand your creations!
Follow this link to test it ! https://quickdraw.withgoogle.com/ 

