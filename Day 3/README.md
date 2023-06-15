
# **Day 3: Text Analytics and Neural Networks**

-----------------------------------
### **Step 1: Text Analytics:**
-----------------------------------

Today we are going to take a look at text Analytics. More precisely we are going to perform sentiment analysis the Financial News dataset which can be found [here](https://www.kaggle.com/code/khotijahs1/nlp-financial-news-sentiment-analysis).


- a. Please create a new project and name it "NLP: Financial News Dataset" and please selet the project. 
- b. The dataset has the following features: 
    - tweet: the twitter post 
    - sentiment: the sentiment related the post, can be positive, neutral or negative
    Our aim is to predict if the the tweet is positive, negative or neutral.

- c: Please download the dataset that we will be using (the dataset can be downloaded [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/1_financial_news_training_set.csv)). Now please import the dataset, you should be expecting 1791 rows and 2 columns.

- c. To perform this classification, select the dataset "1_financial_news_training_set" and click on the "lab" tab and click on "AutoML prediction". Please select the "sentiment" which corresponds to the target variable. Now please select "Quick Prototypes" and press "CREATE".
- c.This is the space where we will be training the Machine Learning model ! Before clicking on "TRAIN", we will have a look at how the model is initialized. If fact, as we are performing text analytics, we need to vectorize the text in order for it to be handled by the model. To do so, please navigate to DESING and select "Features handling". Now click on the toggle button "on" to activate it. Finally, select in the "Text handling" -> "TF/IDF vectorization", it should look something like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/NLP_features_handling.png)). 
- d. Now we can train our models, please select different models, for example: Logistic Regressio and XGBoost. What is the best accuracy that you get ? (expected: [0.922](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/NLP_results.png))). Now please click on the best model and select "DEPLOY". 

- e. Test the model with new data ! 
    - When machine learning models are trained, you can input new "unseen" data to see how the model would predict a certain value. To do so, you can download the test dataset that we have prepared for you under this [link](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/1_financial_news_testing_set.csv). Now, as we have done before, please import the dataset as "testing_set". Once it is imported please click on "Predict" in the tab on the right side and select the "Predict sentiment (multiclass)" model and create the recipe. 
    - Then please on Run. 
    - Once you get back to the "flow" you should see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/final_pipeline_nlp.png) pipeline, please click on testing_set_scored to see the predicted values. 


-----------------------------------
### **Step 2: Neural Networks:**
-----------------------------------

In this section, we are going to study neural networks ! More precisely, we will perform an image classification using neural networks. Please follow this [link](https://www.dataiku.com/learn/samples/deep-learning/) to have access to the tutorial. You can directly access the flow that is created for the tutorial by clicking on [this](https://gallery.dataiku.com/projects/LIONANDTIGER/) link. 
