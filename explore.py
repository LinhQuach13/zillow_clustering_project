import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns



def create_cluster(df, X, k, col_name = None):
    
    """ Takes in df, X (dataframe with variables you want to cluster on) and k
    # It scales the X, calcuates the clusters and return train (with clusters), the Scaled dataframe,
    #the scaler and kmeans object and scaled centroids as a dataframe"""
    
    scaler = StandardScaler(copy=True).fit(X)
    
    X_scaled = pd.DataFrame(scaler.transform(X), columns=X.columns.values).set_index([X.index.values])
    
    kmeans = KMeans(n_clusters = k, random_state = 42)
    
    kmeans.fit(X_scaled)
    
    centroids_scaled = pd.DataFrame(kmeans.cluster_centers_, columns = list(X))
    
    if col_name == None:
        #clusters on dataframe 
        df[f'clusters_{k}'] = kmeans.predict(X_scaled)
    else:
        df[col_name] = kmeans.predict(X_scaled)
    
    
    return df, X_scaled, scaler, kmeans, centroids_scaled




# def creating_clusters(X_df, k, col_name = None):
#     '''
#     Function takes in scaled dataframe, k number of clusters you want to make
#     Optional arguemenet col_name, If none is entered column returned is {k}_k_clusters
#     Returns dataframe with column attched and dataframe with centroids (scaled) in it
#     Returns: X_df, centroids_scaled, kmeans
#     '''
#     #make thing
#     kmeans = KMeans(n_clusters=k, random_state=713)
#     #Fit Thing
#     kmeans.fit(X_df)
#     centroids_scaled = pd.DataFrame(kmeans.cluster_centers_, columns = list(X_df))
#     if col_name == None:
#         #clusters on dataframe 
#         X_df['clusters'] = kmeans.predict(X_df)
#     else:
#         X_df[col_name] = kmeans.predict(X_df)
#     return X_df, centroids_scaled, kmeans




def create_scatter_plot(x, y, df, kmeans, X_scaled, scaler):
    
    """ Takes in x and y (variable names as strings, along with returned objects from previous
    function create_cluster and creates a plot"""
    
    plt.figure(figsize=(14, 9))
    sns.scatterplot(x = x, y = y, data = df)
    centroids = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=X_scaled.columns)
    centroids.plot.scatter(y=y, x= x, ax=plt.gca(), alpha=.30, s=500, c='black')
    
    
    


# def create_scatter_plot(x, y, df, kmeans, X_scaled, scaler, hue_column= None):
    
#     """ Takes in x and y (variable names as strings, along with returned objects from previous
#     function create_cluster and creates a plot"""
    
#     plt.figure(figsize=(14, 9))
#     sns.scatterplot(x = x, y = y, data = df, hue = hue_column)
#     centroids = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=X_scaled.columns)
#     centroids.plot.scatter(y=y, x= x, ax=plt.gca(), alpha=.30, s=500, c='black')
    
    
    
    
    
    
    

    
def create_scatter_plot_hue(x, y, df, kmeans, X_scaled, scaler, hue_column= None):
    
    """ Takes in x and y (variable names as strings, along with returned objects from previous
    function create_cluster and creates a plot"""
    
    plt.figure(figsize=(14, 9))
    sns.scatterplot(x = x, y = y, data = df, hue = hue_column)
    centroids = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=X_scaled.columns)
    centroids.plot.scatter(y=y, x= x, ax=plt.gca(), alpha=.30, s=500, c='black')
    
    

    
def four_scatter_plots(X_scaled, col_name= 'column_one', col_name_two= 'column_two'):
    fig, axs = plt.subplots(2, 2, figsize=(10, 10), sharex=True, sharey=True)
    for ax, k in zip(axs.ravel(), range(2, 6)):
        clusters = KMeans(k).fit(X_scaled).predict(X_scaled)
        ax.scatter(X_scaled[col_name], X_scaled[col_name_two], c=clusters)
        ax.set(title='k = {}'.format(k), xlabel=col_name, ylabel=col_name_two)


    
    
# def create_scatter_plot_lat_csqft(x,y,df,kmeans, X_scaled, scaler, col_name = None):
    
#     """ Takes in x and y (variable names as s
#     trings, along with returned objects from previous
#     function create_cluster and creates a plot"""
    
    
#     plt.figure(figsize=(14, 9))
#     sns.scatterplot(x = x, y = y, data = df, hue = 'cluster_latitude_calculatedsqft')
#     centroids = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=X_scaled.columns)
#     centroids.plot.scatter(y=y, x= x, ax=plt.gca(), alpha=.30, s=500, c='black')

    
    
    
    
# def create_scatter_plot_lat_long(x, y, df, kmeans, X_scaled, scaler):
    
#     """ Takes in x and y (variable names as strings, along with returned objects from previous
#     function create_cluster and creates a plot"""
    
    
#     plt.figure(figsize=(14, 9))
#     sns.scatterplot(x = x, y = y, data = df, hue = 'cluster_latitude_longitude')
#     centroids = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=X_scaled.columns)
#     centroids.plot.scatter(y=y, x= x, ax=plt.gca(), alpha=.30, s=500, c='black')
    
    
    

    
# def create_scatter_plot_lat_yb(x, y, df, kmeans, X_scaled, scaler):
    
#     """ Takes in x and y (variable names as strings, along with returned objects from previous
#     function create_cluster and creates a plot"""
    
    
#     plt.figure(figsize=(14, 9))
#     sns.scatterplot(x = x, y = y, data = df, hue = 'cluster_latitude_yearbuilt')
#     centroids = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=X_scaled.columns)
#     centroids.plot.scatter(y=y, x= x, ax=plt.gca(), alpha=.30, s=500, c='black')
    
    
    
    
def drop_logerror_bins(X_train, X_validate, X_test, col= None):
    X_train = X_train.drop(columns=[col])
    X_validate = X_validate.drop(columns=[col])
    X_test = X_test.drop(columns=[col])
    return X_train, X_validate, X_test