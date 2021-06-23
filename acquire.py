import pandas as pd
import numpy as np
import os
# acquire
from env import host, user, password
from pydataset import data


# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

os.path.isfile('zillow_df.csv')


# Create helper function to get the necessary connection url.
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'



# Use the above helper function and a sql query in a single function.
def new_zillow_data():
    '''
    This function reads data from the Codeup db into a df.
    '''
    zillow_sql = ''' select * from properties_2017 as prop17
    left join (select parcelid, logerror, max(transactiondate) as transactiondate
    FROM predictions_2017
    group by parcelid, logerror) as pred_2017 ON prop17.parcelid= pred_2017.parcelid
    left join propertylandusetype as propland ON prop17.propertylandusetypeid = propland.propertylandusetypeid
    left join airconditioningtype as actype ON prop17.airconditioningtypeid = actype.airconditioningtypeid
    left join architecturalstyletype as arch ON prop17.architecturalstyletypeid = arch.architecturalstyletypeid
    left join buildingclasstype as bc ON prop17.buildingclasstypeid = bc.buildingclasstypeid
    left join heatingorsystemtype as heat ON prop17.heatingorsystemtypeid = heat.heatingorsystemtypeid
    left join buildingclasstype as bct ON prop17.buildingclasstypeid = bct.buildingclasstypeid
    left join storytype as st ON prop17.storytypeid = st.storytypeid
    left join typeconstructiontype as tc ON prop17.typeconstructiontypeid = tc.typeconstructiontypeid
    where (pred_2017.transactiondate Like '%2017%') and (prop17.longitude is not NULL) and (prop17.latitude is not NULL) and prop17.propertylandusetypeid IN (260, 261,262,263,264,265,268,273,274,275,276, 279);
    '''
    return pd.read_sql(zillow_sql, get_connection('zillow'))



def get_zillow_data(cached=False):
    '''
    This function reads in zillow data from Codeup database and writes data to
    a csv file if cached == False or if cached == True reads in telco df from
    a csv file, returns df.
    '''
    if cached == False or os.path.isfile('zillow_df.csv') == False:
        
        # Read fresh data from db into a DataFrame.
        df = new_zillow_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('zillow_df.csv')
        
    else:
        
        # If csv file exists or cached == True, read in data from csv.
        df = pd.read_csv('zillow_df.csv', index_col=0)
        
    return df