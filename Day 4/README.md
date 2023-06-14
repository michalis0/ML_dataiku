
# Day 4: Clustering and Graph Analytics

## Table of contents 
* [Step 1 Clustering](#step-1-clustering)
* [Step 2 Time series prediction](#step-2-time-series-prediction)

-----------------------------------
### **Step 1 Clustering:**
-----------------------------------

- **a.** Create a new project: "Clustering: Customer Dataset".
- **b.** To perform clustering, please first import the dataset dataset **"4_clustering_dataset_cleaned"**, which can be found [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/4_clustering_dataset_cleaned.csv). 
- **c.** Now please click on the **"lab"** tab and click on **"AutoML Clustering"**. Please select the **K-Means** which corresponds to the model that we will use. Now please press **"CREATE"**.
- **d.**Please click on **"TRAIN"**, this will train k-means algorithm to find clusters in the dataset. You should see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_1.png). Now please click on the model and have a look at the different informations given by the clusters given under **"CLUSTERS"**. You can have a look at the Heatmap, the Cluster profiles and the scatter plot, it should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_2.png).
- **e.** Now please click on **DEPLOY** and select **DEPLOY A RETRAINABLE MODEL TO THE FLOW"**. It should now look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_3.png).
- **f.** Now please click on the **"Mall_Customers"** and select **"Cluster"**, like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_5.png). And select the model that just have just created and click on **CREATE**, you can directly click on **RUN**. Your flow should now look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_6.png)
- **g.** We will now have a closer look at the clusters that have been created. Therefore click on the new dataset created and select **Charts**. Please select **Scatter plot** and add on the X-axis: the cluster_labels and on the Y-axis the spending score (1-100). Finally, please add the different features in the sections "Details". It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_7.png).

-----------------------------------
### **Step 2: Time Series Prediction:**
-----------------------------------

Go to the  

**Issues with the plugin**
(To install the plugin, open the  Apps menu, click Plugins and search for Graph analytics. Should look something like this. Install the plugin)

