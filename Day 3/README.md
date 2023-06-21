
# **Day 3: Text Analytics and Neural Networks**

-----------------------------------
### **Step 1: Text Analytics:**
-----------------------------------

Today we are going to take a look at text Analytics. We are going to perform sentiment analysis using a [Financial News dataset](https://www.kaggle.com/code/khotijahs1/nlp-financial-news-sentiment-analysis) (you will download below -- don't download from the above link...).


- Create a new project and name it "NLP: Financial News Dataset"; select the project. 
- The dataset has the following features: 
    - **tweet**: the twitter post 
    - **sentiment**: the sentiment related the post, can be positive, neutral or negative
    Our aim is to predict if the the tweet is positive, negative or neutral.

- Download the dataset [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/1_financial_news_training_set.csv)). Now import the dataset; you should be expecting 1791 rows and 2 columns.

- To perform this classification, select the dataset "1_financial_news_training_set" and click on the "lab" tab and click on "AutoML prediction". Select the "sentiment" which corresponds to the target variable. Select "Quick Prototypes" and press "CREATE".

- This is the space where we will be training the Machine Learning model ! Before clicking on "TRAIN", we will have a look at how the model is initialized. In fact, as we are performing text analytics, we need to vectorize the text in order for it to be handled by the model. To do so, navigate to DESIGN and select "Features handling". Now click on the toggle button "on" to activate it. Finally, select in the "Text handling" -> "TF/IDF vectorization", it should look something like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/NLP_features_handling.png)). 
- Now we can train our models; select different models, for example: Logistic Regressio and XGBoost. What is the best accuracy that you get ? (expected: [0.922](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/NLP_results.png))). Now, double-click on the best model on the left and then in the new screen select "DEPLOY". 

- Test the model with new data ! 
    - When machine learning models are trained, you can input new "unseen" data to see how the model would predict a certain value. To do so, you can download the test dataset that we have prepared for you under this [link](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/1_financial_news_testing_set.csv). Now, as we have done before, please import the dataset as "testing_set". Once it is imported please click on "Predict" in the tab on the right side and select the "Predict sentiment (multiclass)" model and create the recipe. 
    - Then click on Run. 
    - Once you get back to the "flow" you should see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/final_pipeline_nlp.png) pipeline, please click on testing_set_scored to see the predicted values.
 
-------
#### HOMEWORK
-------
- Try the [sentiment analysis plugin](https://knowledge.dataiku.com/latest/ml-analytics/nlp/tutorial-sentiment-analysis-plugin.html) which is already provided by dataiku. For this you need first to login to dataiku and install the plugin.


-----------------------------------
### **Step 2: Neural Networks:**
-----------------------------------

In this section, we are going to study neural networks ! More precisely, we will perform an sentiment analysis using a Neural Network. To do so, we will use IMDB movie dataset and predict if movie reviews are positive or negative.

- **a.** To do so please start by downloading the dataset that we will use. It can be found under [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/imdb_dataset_Neural_Network.csv) link. Now please create a new project on DataIKU called **"Neural Network: IMDB Dataset"** and import the dataset.

- **b.** Because training Machine Learning model using pre-trained models such as BERT we will be using an API from HuggingFace that allows use to use the pre-trained model. The actual model and its documentation can be found [here](https://huggingface.co/siebert/sentiment-roberta-large-english). In order to connect the dataset and use the model through the API, we will need to use some python code. Therefore please click on **RECIPE** - **Code** and select **PYTHON** like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/HELP/PICTURE_1_3.png). Add the training set that you just imported and create a new dataset called **Prediction** and click on **CREATE RECIPE**. 

- **c.** In order for the model to connect please copy and paste this code and adapt the code to the one you have in the codebox. 

**COMMENT**: Is it easy enough to adapt the code ? 

```
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import requests
# Read recipe inputs
# Dataset imdb_dataset_Neural_Network_prepared_1 renamed to imdb_dataset_Neural_Network by alexis.erne@etu.unige.ch on 2023-06-15 14:54:18
imdb_dataset_Neural_Network_prepared_1 = dataiku.Dataset("imdb_dataset_Neural_Network")
imdb_dataset_Neural_Network_prepared_1_df = imdb_dataset_Neural_Network_prepared_1.get_dataframe()


api_url = "https://api-inference.huggingface.co/models/siebert/sentiment-roberta-large-english"
headers = {
    "Authorization": "Bearer API_KEY",
    "Content-Type": "application/json"
}
data = {"inputs": imdb_dataset_Neural_Network_prepared_1_df["review"].tolist()}
response = requests.post(api_url, headers=headers, json=data)
result = response.json()


imdb_dataset_Neural_Network_prepared_1_df['predictions'] = result
Prediction_df = imdb_dataset_Neural_Network_prepared_1_df

# Write recipe outputs
Prediction = dataiku.Dataset("Prediction")
Prediction.write_with_schema(Prediction_df)


```
It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/HELP/PICTURE_4_3.png)
This code reads a dataset called "imdb_dataset_Neural_Network" from Dataiku, sends the "review" column of the dataset to a Hugging Face API for sentiment analysis using the model "siebert/sentiment-roberta-large-english". The API response is stored in the "result" variable, and then the code adds a new column called "Predictions" to the dataset with the sentiment analysis results. Finally, it writes the modified dataset, renamed as "Predictions", back to Dataiku with the output schema.

- **d.** Now please click on **RUN** and go back to the flow, which should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/HELP/PICTURE_2_3.png). Finally, have a look of how the model predicted the movie reviews ! It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/HELP/PICTURE_3_3.png).




