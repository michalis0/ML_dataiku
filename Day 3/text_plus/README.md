
# Day 3: Exercises 

-----------------------------------
### **Step 1: Initialization:**
-----------------------------------

- Please download the "Text Preparation" plugin. This can be done by searching in the plugins tab and clicking on "ADD A PLUGING" and adding the plugin like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/text_plus/HELP/text_img_1.png). 
- Create a new project and name it "Text - Playground" and select the project. 
- Please download the three datasets that we will use under this [link](https://github.com/michalis0/ML_dataiku/tree/main/Day%203/text_plus/Datasets) and import them in the project. 
- Your flow shoud look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/text_plus/HELP/text_img_2.png) 


-----------------------------------
### **Step 2: Language Detection:**
-----------------------------------

In this step, we are going to use a library able to detect language from text ! 

- **a** Please select on the "language_detection_dataset" dataset and click on "Text Preparation" on the tab with the new plugin downloaded.<img width="80" alt="text_preparation" src="https://github.com/michalis0/ML_dataiku/assets/43532600/39f96e72-0b52-4363-b7f0-cdc131c6414e"> Please select "Language Detection" and add "language_detected" as the output dataset and click "CREATE DATASET". 

- **b** Now please select the column text and do not add anything anything in the Language scope ! This will allow the model to search all the possible languages that it has access to. It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/text_plus/HELP/text_img_3.png)

- **c** Please click on "RUN" (it should take a few seconds to run). 

- **d** Go back to the flow and check if the languages were correctly identified ! Note that there is a column called "text_language_score" that the probability that the model gives to its prediction. (Try to find the one which is incorrectly classified). 

-----------------------------------
### **Step 3: Spelling detection:**
-----------------------------------

In this step, we are going to use a library able to detect spelling mistakes from a text ! 

- **a** To do so, please click on the "spelling_detection_dataset" and select "Text Preparation" then "Spell Checking". Like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/text_plus/HELP/text_img_5.png). Just add the output dataset name as "spelling_checked", the other sets are optional and click create. 

- **b** Select the "text" column, like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/text_plus/HELP/text_img_6.png) and click "RUN". 

- **c** Go back to the flow and check if it has identified all spelling errors ! 

-----------------------------------
### **Step 4: Cleaning:**
-----------------------------------

In this step, we are going to use a library able to clean a text dataset. This is a crutial step in NLP projects, as it enable to reduce noise that could decrease the accuracy of the machine learning models.  

- **a** To do so, please click on the "cleaning_detection_dataset" and select "Text Preparation" then "Text Cleaning". Like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/text_plus/HELP/text_img_7.png). Just add the output dataset name as "cleaned_text" and click create. 

- **b** Select the "text" column, like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/text_plus/HELP/text_img_8.png) and click "RUN". 

- **c** Go back to the flow, select the new dataset and check how the model handled the cleaning ! 


Your final flow should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/text_plus/HELP/text_img_9.png)



----------
If you are having trouble running the job : Before clicking on RUN you can go to the "Advanced" tab and change the container configuration to "None - Use backend to execute", like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%203/text_plus/HELP/text_img_4.png). Then go back to the "Settings tab". 


