#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd
from uszipcode import SearchEngine


# In[73]:


search = SearchEngine(simple_zipcode=True)


# In[78]:


df = pd.read_csv(r"C:\Users\pcali\Desktop\combined_csv_with_country.csv", dtype = {'zipcode': str})
df['zipcode'] = df['zipcode'].astype(str)


# In[79]:


#get list of zip codes (unique)

zips = df['zipcode'].unique().tolist()

#look up information for each of those zipcodes and create master dataframe

dfZipCode = pd.DataFrame()


#query us zip code for data on each zip code
for item in zips: 
    zipcode = search.by_zipcode(item) #queries zipcode database
    
    dict1 = zipcode.to_dict() #convert result to dictionary
    
    zipcode = dict1.get("zipcode")
    city = dict1.get("major_city")
    post_office_city = dict1.get("post_office_city")
    state = dict1.get("state")
    pop_density = dict1.get("population_density")


    data = {'Zip Code': [zipcode], 'City': [city], 'State Code': [state], 'City State': [post_office_city], 'Population Density': [pop_density]}
    dfTemp = pd.DataFrame(data)
    
    dfZipCode = pd.concat([dfZipCode, dfTemp], axis =0) #add zip code results to master dataframe

dfZipCode

#Get region information by state from US census (not included in uszipcode library)
dfRegion =pd.read_csv('https://raw.githubusercontent.com/cphalpert/census-regions/master/us%20census%20bureau%20regions%20and%20divisions.csv')

dfZipCode = pd.merge(dfZipCode, dfRegion, how = 'left',  on = "State Code")  #merge on State Code to get region



#Merge state/zipcode information with raw results dataframe
df['zipcode'] = df['zipcode'].astype(str)
dfZipCode['Zip Code'] = dfZipCode['Zip Code'].astype(str)
dfFinal = pd.merge(df, dfZipCode, how = 'left', left_on = 'zipcode', right_on = 'Zip Code')

dfFinal

#write results to csv
dfFinal.to_csv(r"C:\Users\pcali\Desktop\combined_csv_zipandcountry.csv")




# In[84]:


regionCounts = dfFinal.groupby("Region").count().reset_index()
print (regionCounts)


# In[66]:





# In[62]:





# In[25]:





# In[26]:


search


# In[10]:


profile = df.profile_report()


# In[13]:


profile.to_html()


# In[ ]:




