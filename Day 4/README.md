
# Day 4: Clustering and Graph Analytics

## Table of contents 
* [Clustering](#clustering)
* [Graph Analytics](#graph-analytics)

-----------------------------------
### **Clustering:**
-----------------------------------
In clustering we try to create groups of "similar" objects. We use clustering when we don't have labelled data. Question: is the following clustering a proper one? 

<img height="200" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/ca4b163e-5d2f-485b-be29-4eae7c7891e8">

<img height="200" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/3e0be064-1749-42ea-a19f-22839964b33e">

<img height="200" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/21251564-c0cc-4fe1-be6a-9ef111172fe1">


Let's do clustering with Dataiku!

- Create a new project: "Clustering: Customer Dataset".
- To perform clustering, import the dataset **"4_clustering_dataset_cleaned"**, from [here](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/4_clustering_dataset_cleaned.csv). 
- Click on the **"LAB"** button and then on **"AutoML Clustering"**. Go to "DESIGN" <img width="107" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/ed98b3e9-7075-4cc3-822a-b97f451d594f"> and under the "Algorithms" tab on the left
pick the **K-Means** which corresponds to the clustering algorithm that we will use. Press **"CREATE"**.
- Click on **"TRAIN"**, this will train k-means algorithm to find clusters in the dataset. You should see [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_1.png). Now double-click on the model name on the left
  
<img width="341" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/03b5edcc-defe-4ba7-b774-bbdc4879258a">


and have a look at the different information given by the clusters given under **"CLUSTERS"**. You can have a look at the Heatmap, the Cluster profiles and the scatter plot, it should look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_2.png).

<img width="670" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/3f684fd3-71e5-49ed-8c5e-96c28f72c065">


- Click on **DEPLOY** and select **DEPLOY A RETRAINABLE MODEL TO THE FLOW"**. It should now look like [this](https://github.com/michalis0/ML_dataiku/blob/main/Day%204/HELP/picture_3.png).

What we did above created a model using unlabelled data by considering the similarities of the objects. Essentially it computed the cluster centers. But we cannot see the cluster assignment. For this we apply the model on the same data.

- In the Flow, click on the **"4_clustering_dataset_cleaned"**, then scroll down on the tab on the right and select the green **"Cluster"** button.
  

<img width="952" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/2ca5f9ca-3269-4d1b-aee7-7a4ac260a462">



-    In the popup window, select the model that just have just created and click on **CREATE**, you can directly click on **RUN**. Your flow should now look like

<img width="644" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/4dd580a1-fdab-48d9-87f7-285555251909">


- We will now have a closer look at the clusters that have been created. **Double-click** on the newly created scored dataset (4_clustering_dataset_cleaned_scored, possibly!) and select **Charts**.

<img width="566" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/ddcf3d22-1b08-4ced-873a-0bda8b864b30">


- Select **Boxplot** : Show Y-axis "Spending score" by X-axis "cluster_label". It should look like this:

<img width="1027" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/ba40d91f-1615-4a4a-ae02-54591962cfd5">


Other things you can explore under clustering, is to try the different algorithms:

<img width="473" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/70f37e46-0f12-4ff5-b6e7-6f95b33b8169">


and also to try dimensionality reduction, eg PCA. This usually helps the clustering, especially if the data are high-dimensional.

<img width="772" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/4ce620ac-49a0-464d-8d8d-b59492dec32d">



----
#### HOMEWORK (for the motivated ones!)
-----
- Follow the clustering tutorial for [clustering for bikesharing](https://knowledge.dataiku.com/latest/use-cases/clustering/bike-sharing/tutorial-index.html).

<img width="600" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/2c6fc19c-3e54-4eb1-a481-e09a5e6ec403">


-----------------------------------
### **Graph Analytics**
-----------------------------------

<img width="500" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/2325b518-87cb-47e3-86c7-372c62e99ae7">

Graphs are a prevalent way of modeling connections between entities. 

(To install the plugin, sign-in to dataiku.com; click Plugins and search for Graph analytics. Install the plugin)

- Download the dataset from [here](./actorfilms.csv). You can delete most of the columns, leave only the columns "Actor" and "Film".
- Follow this [tutorial](https://www.dataiku.com/product/plugins/graph-analytics/)

You can visualize the graph of actors and movies. It should look like this:

<img width="1318" alt="image" src="https://github.com/michalis0/ML_dataiku/assets/28807066/feffc622-f20a-4e1c-a4f5-6756bc70de27">


