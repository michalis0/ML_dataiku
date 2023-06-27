
# **Day 3: Text Analytics and Neural Networks**

-----------------------------------
### **Step 1: Initialization:**
-----------------------------------

- Please download the "Text Preparation plugin". This can be done by searching in the plugins tab and clicking on "ADD A PLUGING" and adding the plugin like [this]. 
- Create a new project and name it "Text - Playground" and select the project. 
- Please download the three datasets that we will use under this [link]() text image 3 and import them in the project. 
- Your flow shoud look like [this]() 


-----------------------------------
### **Step 2: Language Detection:**
-----------------------------------

In this step, we are going to use a library able to detect language from text ! 

- **a** Please select on the "language_detection_dataset" dataset and click on "Text Preparation" on the tab with the new plugings downloaded. Please select "Language Detection" and add "language_detected" as the output dataset and click "CREATE DATASET". 

- **b** Now please select the column text and do not add anything anything in the Language scope ! This will allow the model to search all the possible languages that it has access to. It should look like [this]()

- **c** Please click on "RUN" (it should take a few seconds to run). text image 4

- **d** Go back to the flow and check if the languages were correctly identified ! Note that there is a column called "text_language_score" that the probability that the model gives to its prediction. (Try to find the one which is incorrectly classified). 

-----------------------------------
### **Step 3: Spelling detection:**
-----------------------------------

In this step, we are going to use a library able to detect spelling mistakes from a text ! 

- **a** To do so, please click on the "spelling_detection_dataset" and select "Text Preparation" then "Spell Checking". Like [this](). Just add the output dataset name as "spelling_checked", the other sets are optional. And click create. 

- **b** Select the "text" column, like [this]() and click "RUN". 


-----------------------------------
### **Step 4: Cleaning detection:**
-----------------------------------

In this step, we are going to use a library able to clean a dataset containing mistakes. 

- **a** To do so, please click on the "cleaning_detection_dataset" and select "Text Preparation" then "Text Cleaning". Like [this](). Just add the output dataset name as "cleaned_text" and click create. 

- **b** Select the "text" column, like [this]() and click "RUN". 

- **c** Go back to the flow, select the new dataset and check how the model handled the cleaning ! 


Your final flow should look like [this]()

If you are having trouble running the job :
Before clicking on RUN please go to the "Advanced" tab and change the container configuration to "None - Use backend to execute", like [this](). Then go back to the "Settings tab" and c



