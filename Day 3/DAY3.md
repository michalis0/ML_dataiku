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