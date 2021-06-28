# Zillow Cluster Project


#### Project Objectives
> - For this project you will continue working with the zillow dataset. Continue to use the 2017 properties and predictions data for single unit / single family homes.

> - In addition to continuing work on your previous project, you should incorporate clustering methodologies on this project.

> - Your audience for this project is a data science team. The presentation will consist of a notebook demo of the discoveries you made and work you have done related to uncovering what the drivers of the error in the zestimate is.


### Project Planning 

The following link contains my project planning process on my Trello Board: https://trello.com/b/s5Tb32WM/zillow-cluster-project

Here is a snapshot of my project planning from my Trello Board

![image](https://user-images.githubusercontent.com/80718476/123652251-be04ae00-d7f1-11eb-8a2c-08bb1e9d2e0e.png)

### Project Summary
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>


#### Audience
> - Zillow Data Science team

#### Project Deliverables
> - A clearly named final notebook. This notebook will be what you present and should contain plenty of markdown documentation and cleaned up code.
> - A README that explains what the project is, how to reproduce you work, and your notes from project planning.
> - A Python module or modules that automate the data acquisistion and preparation process. These modules should be imported and used in your final notebook.


#### Data Dictionary
    
- This is a data dictionary as a reference for the variables used within in the data set.


 |   Target    |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
| logerror| | 𝑙𝑜𝑔𝑒𝑟𝑟𝑜𝑟=𝑙𝑜𝑔(𝑍𝑒𝑠𝑡𝑖𝑚𝑎𝑡𝑒)−𝑙𝑜𝑔(𝑆𝑎𝑙𝑒𝑃𝑟𝑖𝑐𝑒)



|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
|  bathroomcnt | float64   | number of bathrooms  |
| bedroomcnt   | float64 | number of bedrooms|
| calculatedfinishedsquarefeet   | float64 | Calculated total finished living area of the home |
| propertylandusetypeid  | float64   | Type of land use the property is zoned for|
| taxamount  | float64 |The total property tax assessed for that assessment year|
| yearbuilt  | float64 |  The Year the principal residence was built |
| fips  | float64 | Federal Information Processing Standard code -  see https://en.wikipedia.org/wiki/FIPS_county_code for more details|
| parcelid | float64 | Unique identifier for parcels (lots) |



#### Initial Hypotheses

### Hypothesis 1:
> - **Hypothesis 1 -** I rejected the Null Hypothesis; there is a relationship.
> - alpha = .05
> - $H_0$: calculatedfinishedsquarefeet has no relationship with logerror. 
> - $H_a$: calculatedfinishedsquarefeet has a relationship with logerror. 

### Hypothesis 2:
> - **Hypothesis 2 -** I rejected the Null Hypothesis; there is a difference in the means.
> - alpha = .05
> - $H_0$: There is no difference in means between bedroom count and logerror. 
> - $H_a$: There is a difference in means between bedroom count and logerror. 

### Hypothesis 3:
> - **Hypothesis 3 -** I rejected the Null Hypothesis; there is a relationship.
> - alpha = .05
> - $H_0$: There is no relationship between latitude and logerror. 
> - $H_a$: There is a relationship between latitude and logerror.

### Hypothesis 4:
> - **Hypothesis 4 -** I rejected the Null Hypothesis; there is a difference in means between logerror and cluster_latitude_calulatedsqft.
> - alpha = .05
> - $H_0$: There is no difference in means between logerror and cluster_latitude_calulatedsqft. 
> - $H_a$: There is a difference in means between logerror and cluster_latitude_calulatedsqft. 

### Hypothesis 5:
> - **Hypothesis 5 -** I rejected the Null Hypothesis; there is a difference in means between logerror and cluster_latitude_yearbuilt.
> - alpha = .05
> - $H_0$: There is no difference in means between logerror and cluster_latitude_yearbuilt. 
> - $H_a$: There is a difference in means between logerror and cluster_latitude_yearbuilt.


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>
<b>The following are key takeways:</b>

  -Log_error does not correlate well with any one feature
 
  - All models performed relatively the same but the Polynomial Regression Model with the clusters performed the best
    - RMSE: 0.045734
  
  - The models I created were a  Linear Regression, Lasso Lars, and Polynomial Regression Model. All of the models outperformed the baseline. I chose was the Polynomial Regression Model as my best model with a 0.007 % improvement for predicting features of Logerror.
  
  -  The Polynomial Regression Model outperformed my baseline score by 0.007 % thus it has value.
  

- With more time:
    - would like to find if there are better predictors of log error by creating more clusters
    - would like to fill out the missing data so that there are even more data points to work with
    - would have like to perform ANOVA statistical testing.


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - Data Acquisition: Data is collected from the codeup cloud database with an appropriate SQL query
> -  Data Prep: Column data types are appropriate for the data they contain
> - Data Prep: Missing values are investigated and handled
> - Data Prep: Outliers are investigated and handled
> - Exploration: the interaction between independent variables and the target variable is explored using visualization and statistical testing
> - Exploration: Clustering is used to explore the data. A conclusion, supported by statistical testing and visualization, is drawn on whether or not the clusters are helpful/useful. At least 3 combinations of features for clustering should be tried.
> - Modeling: At least 4 different models are created and their performance is compared. One model is the distinct combination of algorithm, hyperparameters, and features.
> - Best practices on data splitting are followed


___

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>



### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, and zillow_final.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the zillow_final.ipynb notebook
