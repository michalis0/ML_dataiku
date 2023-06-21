
# Day 4: Clustering and Graph Analytics

## Table of contents 
* [Clustering](#clustering)


-----------------------------------
### **Clustering:**
-----------------------------------

- Create a new project: "Clustering: Customer Dataset".
- To perform clustering, import the dataset dataset **"4_clustering_dataset_cleaned"**, which can be found [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/4_clustering_dataset_cleaned.csv). 
- Click on the **"LAB"** button and then on **"AutoML Clustering"**. Pick the **K-Means** which corresponds to the clustering algorithm that we will use. Press **"CREATE"**.
- Click on **"TRAIN"**, this will train k-means algorithm to find clusters in the dataset. You should see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_1.png). Now double-click on the model
<img width="284" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/407d271c-64dd-4013-8768-358261970f14">

and have a look at the different informations given by the clusters given under **"CLUSTERS"**. You can have a look at the Heatmap, the Cluster profiles and the scatter plot, it should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_2.png).


- Click on **DEPLOY** and select **DEPLOY A RETRAINABLE MODEL TO THE FLOW"**. It should now look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_3.png).
- Now click on the **"Mall_Customers"** and select **"Cluster"**, like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_5.png). And select the model that just have just created and click on **CREATE**, you can directly click on **RUN**. Your flow should now look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_6.png)
- We will now have a closer look at the clusters that have been created. Therefore click on the new dataset created and select **Charts**. Select **Scatter plot** and add on the X-axis: the cluster_labels and on the Y-axis the spending score (1-100). Finally, add the different features in the sections "Details". It should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_7.png).

Other things you can explore under clustering, is to try the different algorithms:

<img width="400" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/69e6c21e-5b43-435c-8187-64b891476bbb">

and also to try dimensionality reduction, eg PCA. This usually helps the clustering, especially if the data are high-dimensional.

<img width="500" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/c73e9afb-72e1-4e34-a3db-31a8dc51647d">


----
####HOMEWORK (for the motivated ones!)
-----
- Follow the clustering tutorial for [clustering for bikesharing](https://knowledge.dataiku.com/latest/use-cases/clustering/bike-sharing/tutorial-index.html).

-----------------------------------
### **Step 2: Graph Analytics:**
-----------------------------------

(To install the plugin, sign-in to dataiku.com; click Plugins and search for Graph analytics. Install the plugin)

