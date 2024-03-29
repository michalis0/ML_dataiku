


### **Day 5: Chatbots - AI for social Good - Generative AI - Risks of AI**

<img width="349" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/9e938ecb-38c2-4d79-8a5f-c9d8311acd75">

Today is our last day of this course. The description below is _intentionally_ not as descriptive as for the previous days. You have been working 4 days with the dataiku tool. So, by now you should be able to accomplish this task with minimal supervision ;). 

-----------------------------------
### ChatGPT for Summarizing Text
-----------------------------------

<img width="646" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/26c94cb6-0add-4b1f-aa5d-bd78d7f05a81">


Today we will use the OPENAI ChatGPT API ! We will use it in order to summarize newspapers articles. 

**a.** Begin by downloading the two newspaper articles we will summarize using ChatGPT. The articles can be found [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/text_articles_dataset.csv). Those two articles were taken from the BBC Finance, the first one talks about Interest Rates and the second one about Crypto in the USA. 

**b.** Install the OPEN AI ChatGpt plugin for Dataiku. a) Login to Dataiku.com, b) once logged in, navigate to the  **"Plugins"** tab on the left and click on the **+ ADD A PLUGIN** then type "OpenAI GPT". This should look something like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_2_5.png). Once you have clicked on the **INSTALL** button go back to the **Plugins** tab and you should be able to see your plugin (like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_3_5.png))

**c.** To be able to use the API, we have to add an API key. To do so click on the Plugin name and click on "ADD A PRESET", you should now see this [screen](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_4_5.png). Now add the following text for the name insert "ChatGPT" for the description "Key" and for the key, copy and paste your API_KEY credentials if you already have an account (if you don't, we will provide one), and click on **CONFIRM**. 

<img width="417" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/95987471-64eb-45ec-abd1-0ca25f3c5771">


**d.** Go back to your main screen and create a new project called **"Chatbots: CHATGPT Text summarization"** and import the "text_articles_dataset.csv" dataset. As you have downloaded the plugin, you should now see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_5_5.png) icon on the right hand side of the screen. Select the dataset and click on the icon "OPENAI GPT". Now  select the button **Summarize text with OpenAI GPT**, like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_6_5.png) and create an output dataset called "summarized_dataset". And select the column "Text" and the key that we have created before. Finally click on **RUN** !

**e.**: The text has been summarized ! Your flow should look like this

<img width="300" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/d9d20349-1715-4e62-99f7-ad5c31e70780">


and the output dataset should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_9_5.png)


**CONGRATS! You have used cutting-edge advances of AI and Machine Learning!**

### More information

For your research the classification recipe should also be relevant. There, you give some examples and let chatGPT classify the remaining text (eg sentiment analysis, topic detection, anything that you really want to detect in your text). Remember, that you only need to give it a few examples, and then everything should be super accurate! So, why not try it on your own data?

Watch [this video](https://content.dataiku.com/email-llm-demo?utm_campaign=GLO+CONTENT+ChatGPT+%26+LLMs+March+2023&utm_medium=email&_hsmi=260388734&_hsenc=p2ANqtz-9Pr_dfkoaZufRgm3jgYC9oYxUUz66dNBYkpZl810Obz32bu7hY7ihY726mj6TdRF-OgyIYvDkEUtTe9OKn_RcxnrnhTQ&utm_content=260390385&utm_source=hs_email)
to see what what more you can do with the chatgpt plugin in dataiku.

Now, try on your own some of the other recipes that we haven't used.
