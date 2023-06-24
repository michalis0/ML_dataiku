


### **Day 5: Chatbots - AI for social Good - Generative AI - Risks of AI**

<img width="349" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/9e938ecb-38c2-4d79-8a5f-c9d8311acd75">

-----------------------------------
### ChatGPT for Summarizing Text
-----------------------------------

Today we will use the OPENAI ChatGPT API ! We will use it in order to summarize newspapers articles. 

**a.** Begin by downloading the two newspaper articles we will summarize using ChatGPT. The articles can be found [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/text_articles_dataset.csv). Those two articles were taken from the BBC Finance, the first one talks about Interest Rates and the second one about Crypto in the USA. 

**b.** Download the OPEN AI ChatGpt plugin. To install the plugin, navigate to the launchpad of dataIKU (this can be done by clicking on the top left icon), you should see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_1_5.png). Navigate to the  **"Plugins"** tab and click on the **+ ADD A PLUGIN** then type "OpenAI GPT". This should look something like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_2_5.png). Once you have clicked on the **INSTALL** button please go back to the **Plugins** tab and you should be able to see your plugin (like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_3_5.png))

**c.** To be able to use the API, we have to add an API key. To do so click on the Plugin name and click on "ADD A PRESET", you should now see this [screen](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_4_5.png). Now add the following text for the name insert "ChatGPT" for the description "Key" and for the key, please copy and paste your API_KEY credentials if you already have an account (if you don't, we will provide one), and click on **CONFIRM**. 

**d.** Go back to your main screen and create a new project called **"Chatbots: CHATGPT Text summarization"** and import the "text_articles_dataset.csv" dataset. As you have downloaded the plugin, you should now see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_5_5.png) icon on the right hand side of the screen. Select the dataset and click on the icon "OPENAI GPT". Now  select the button **Summarize text with OpenAI GPT**, like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_6_5.png) and create an output dataset called "summarized_dataset". And select the column "Text" and the key that we have created before. Finally click on **RUN** !

**e.**: The text has been summarized ! Your flow should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_8_5.png) and the output dataset should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%205/HELP/PICTURE_9_5.png)


Congrats! You have used cutting-edge advances of AI and Machine Learning!

For [more](https://content.dataiku.com/email-llm-demo?utm_campaign=GLO+CONTENT+ChatGPT+%26+LLMs+March+2023&utm_medium=email&_hsmi=260388734&_hsenc=p2ANqtz-9Pr_dfkoaZufRgm3jgYC9oYxUUz66dNBYkpZl810Obz32bu7hY7ihY726mj6TdRF-OgyIYvDkEUtTe9OKn_RcxnrnhTQ&utm_content=260390385&utm_source=hs_email) info.

