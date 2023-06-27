
# **Day 3: Text Analytics and Neural Networks**

-----------------------------------
### **Step 1: Text Analytics:**
-----------------------------------

<img width="400" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/ff1c5b3b-82e8-4e09-b50a-95e7979b37db">


Today we are going to take a look at text Analytics. We are going to perform sentiment analysis using a [Financial News dataset](https://www.kaggle.com/code/khotijahs1/nlp-financial-news-sentiment-analysis). Download the dataset [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/1_financial_news_training_set.csv).


- Create a new project and name it "NLP: Financial News Dataset"; select the project. 
- The dataset has the following features: 
    - **tweet**: the twitter post 
    - **sentiment**: the sentiment related the post, can be positive, neutral or negative
    Our aim is to predict if the the tweet is positive, negative or neutral.

- Import the dataset; you should expect 1791 rows and 2 columns.

- To perform this classification, go to the "flow", select the dataset "1_financial_news_training_set" and click on the blue "LAB" button, then on "AutoML prediction". Select the "sentiment" which corresponds to the target variable. Select "Quick Prototypes" and press "CREATE".

**Question 1:** What is the baserate accuracy? How do you find it? (Should be 33%, Go to Design -> "Target" and see the class distribution).

- This is the space where we will be training the Machine Learning model ! Before clicking on "TRAIN", we will have a look at how the model is initialized. In fact, as we are performing text analytics, we need to vectorize the text in order for it to be handled by the model. To do so, navigate to DESIGN and select "Features handling". Now click on the toggle button of the tweet feature to "on" to activate it. Finally, select in the "Text handling" -> "TF/IDF vectorization".

<img width="1000" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/61dcb640-ff6e-449a-ba1c-e1ec094dbb6c">


- Now we can train our models; select different models, for example: Logistic Regression and XGBoost. What is the best accuracy that you get ? (expected: [0.922](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/NLP_results.png))). Now, double-click on the best model on the left and then in the new screen select "DEPLOY". 

- Test the model with new data ! 
    - When machine learning models are trained, you can input new "unseen" data to see how the model would predict a certain value. To do so, you can download the test dataset that we have prepared for you under this [link](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/1_financial_news_testing_set.csv). Now, as we have done before, please import the dataset as "testing_set". Once it is imported please click on "Predict" in the tab on the right side and select the "Predict sentiment (multiclass)" model and create the recipe. 
    - Then click on Run. 
    - Once you get back to the "flow" you should see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%201/Help/final_pipeline_nlp.png) pipeline, please click on testing_set_scored to see the predicted values.


<BR><BR>
#### More info

See also here for more information on the various text and [column preprocessings](https://knowledge.dataiku.com/latest/ml-analytics/model-design/concept-feature-handling.html):

<img width="726" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/247d7b45-1b24-4c76-a04a-3dfbb50e81d9">

 
-------
#### EXERCISE/HOMEWORK
-------
1. Try the [sentiment analysis plugin](https://knowledge.dataiku.com/latest/ml-analytics/nlp/tutorial-sentiment-analysis-plugin.html) which is already provided by dataiku. For this you need first to sign in to [dataiku](https://www.dataiku.com) and then install the plugin.

<img width="1040" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/0f644593-5c7c-4c24-b3bd-8b71a1b9b77b">


Then, you should be able to access it in a Flow under "Recipe" -> "Natural Language Processing"-> "Sentiment Analysis".

<img width="340" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/fea90acf-704d-4cdc-892b-8dcc6d7a8885">


2. There are many other text plugins that you can install. Eg with the **"Text Visualization" you can do word clouds. You can apply it on the text dataset that we used above to get the following word cloud.

<img width="624" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/d80165a0-f145-4be0-b566-ca3f9af7b8a3">


<img width="1345" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/9a1f11de-3923-4e1b-bbc7-2e9e682f80c2">




-----------------------------------
### **Step 2: Neural Networks:**
-----------------------------------

<img width="363" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/487fb7ac-218f-4ed8-a292-719ff13e1ca4">


In this section, we are going to study neural networks ! Neural Networks (NNs) and Deep Learning represent some the most exciting areas in the field of AI. More precisely, we will perform an sentiment analysis using a Neural Network. To do so, we will use the IMDB movie review dataset and predict if movie reviews are positive or negative.

- **a.** To do so please start by downloading the dataset that we will use. It can be found under [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/imdb_dataset_Neural_Network.csv) link. Create a new project on DataIKU called **"Neural Network: IMDB Dataset"** and import the dataset.

- **b.** Training a Neural Network model is costly, so we will use a pre-built one. We use the API from HuggingFace that allows use to access the pre-trained model. The actual model and its documentation can be found [here](https://huggingface.co/siebert/sentiment-roberta-large-english). To connect the dataset and use the model through the API, we will need to use some python code. Therefore click on **RECIPE** - **Code** and select **PYTHON** like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/HELP/PICTURE_1_3.png). Add the training set that you just imported and create a new dataset called **Prediction** (make sure it's <ins>capital "P"</ins>) and click on **CREATE RECIPE**. 

- **c.** In order for the model to connect please copy and paste this code and adapt the code to the one you have in the codebox. 

**IMPORTANT COMMENT**: Copy paste the code below. You may have to adapt mildly. (1) adjust the names of the datasets if you changed them , 2) Replace the word API_KEY with a string that I will provide you, I will paste it in our Teams chat.)

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
It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/HELP/PICTURE_4_3.png).
This code reads a dataset called "imdb_dataset_Neural_Network" from Dataiku, sends the "review" column of the dataset to a Hugging Face API for sentiment analysis using the model "siebert/sentiment-roberta-large-english". The API response is stored in the "result" variable, and then the code adds a new column called "Predictions" to the dataset with the sentiment analysis results. Finally, it writes the modified dataset, renamed as "Predictions", back to Dataiku with the output schema.

- **d.** Now click on **RUN** and go back to the flow, which should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/HELP/PICTURE_2_3.png). Finally, have a look of how the model predicted the movie reviews ! It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/HELP/PICTURE_3_3.png).

**Congratulations! You called your first Deep Learning API from the Internet. That's a BIG accomplishment!**




