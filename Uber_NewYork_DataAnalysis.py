#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##################################
#Name-Mallinath Elekar
#Dataset - Uber New York Data
##################################


# In[1]:


#Q1)----->Analysis of which month has max rides


# In[2]:


#Analysis of journey of each day


# In[3]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


import os 


# In[5]:


files=os.listdir(r'C:\Users\user\Desktop\Udemy\Uber')[-7:]
files


# In[6]:


files.remove( 'uber-raw-data-janjune-15.csv')


# In[7]:


files


# In[ ]:





# In[8]:


path=r'C:\Users\user\Desktop\Udemy\Uber'

final=pd.DataFrame()

for file in files:
    df=pd.read_csv(path+"/"+file,encoding='utf-8')
    final=pd.concat([df,final])


# In[9]:


final.shape


# In[10]:


#PREPARE DATA FOR ANALYSIS


# In[ ]:





# In[11]:


df=final.copy()


# In[12]:


df.head()


# In[13]:


df.dtypes


# In[14]:


df['Date/Time']=pd.to_datetime(df['Date/Time'],format='%m/%d/%Y %H:%M:%S')


# In[15]:


df.dtypes


# In[16]:


df.head()


# In[17]:


df['weekday']=df['Date/Time'].dt.day_name()


# In[18]:


df['day']=df['Date/Time'].dt.day


# In[19]:


df['minute']=df['Date/Time'].dt.minute
df['month']=df['Date/Time'].dt.month
df['hour']=df['Date/Time'].dt.hour


# In[20]:


df.head()


# In[21]:


df.dtypes


# In[22]:


#Analysing Trips Of Uber


# In[23]:


pip install plotly


# In[24]:


#Analysis Of Journey By Weekdays
#Rush in every weekday


# In[25]:


import plotly.express as px


# In[26]:


px.bar(x=df['weekday'].value_counts().index,
      y=df['weekday'].value_counts())


# In[ ]:





# In[27]:


df['weekday'].value_counts()


# In[28]:


#Analysis of journey by hour
#Rush in each and every hour


# In[29]:


plt.hist(df['hour'])


# In[30]:


df['month'].unique()


# In[31]:


for i,month in enumerate(df['month'].unique()):
    print(i)
    print(month)


# In[32]:


#Rush in each and every hour of month


# In[33]:


plt.figure(figsize=(40,20))
for i,month in enumerate(df['month'].unique()):
    plt.subplot(3,2,i+1)
    df[df['month']==month]['hour'].hist()
    


# In[ ]:





# In[34]:


df.head()


# In[35]:


#Analysis of which month has max rides


# In[36]:


pip install chart_studio


# In[37]:


import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot


# In[ ]:





# In[38]:


df.groupby('month')['hour'].count()


# In[39]:


plot=go.Bar(x=df.groupby('month')['hour'].count().index,
      y=df.groupby('month')['hour'].count(),
      name='Priority')


# In[40]:


iplot([plot])


# In[41]:


#Analysis of journey of each day


# In[42]:


sns.distplot(df['day'])


# In[43]:


plt.figure(figsize=(10,8))
plt.hist(df['day'],bins=30,rwidth=0.7,range=(0.5,30.5))
plt.xlabel('date of the month')
plt.ylabel('total journey')
plt.title('Journey by month day')


# In[44]:


plt.figure(figsize=(20,8))

for i,month in enumerate(df['month'].unique(),1):
    plt.subplot(3,2,i)
    df_out=df[df['month']==month]
    plt.hist(df_out['day'])
    plt.xlabel('days in month()'.format(month))
    plt.ylabel('total_rides')


# In[45]:


ax=sns.pointplot(x='hour',y='Lat',data=df,hue='weekday')
ax.set_title('hoursoffday vs latitude of passenger')


# In[46]:


#Analyse which base number gets popular by month name


# In[47]:


#perform cross analysis
#1--->heatmap by hour and weekday
#2---->heatmap by hour and day
#3---->heatmap by month and day
#4---->heatmap by month and weekday


# In[48]:


df.head()


# In[49]:


base=df.groupby(['Base','month'])['Date/Time'].count().reset_index()
base


# In[50]:


sns.lineplot(x='month',y='Date/Time',hue='Base',data=base)


# In[51]:


#Heatmap- Advance level of visualization
#perform cross analysis
#1--->heatmap by hour and weekday
#2---->heatmap by hour and day
#3---->heatmap by month and day
#4---->heatmap by month and weekday


# In[52]:


#HeatMap---->heatmap by hour and weekday


# In[53]:


def count_rows(rows):
    return len(rows)


# In[54]:


by_cross=df.groupby(['weekday','hour']).apply(count_rows)
by_cross


# In[55]:


pivot=by_cross.unstack()
pivot


# In[ ]:





# In[56]:


plt.figure(figsize=(10,6))
sns.heatmap(pivot)


# In[57]:


def heatmap(col1,col2):
    by_cross=df.groupby([col1,col2]).apply(count_rows)
    pivot=by_cross.unstack()
    plt.figure(figsize=(10,6))
    return sns.heatmap(pivot)
    


# In[58]:


heatmap('day','hour')


# In[59]:


#Analysis of location data points


# In[60]:


#perform spatial analysis using heatmap to get a clear cut of rush


# In[61]:


#automate your analysis


# In[62]:


df.head()


# In[ ]:





# In[63]:


plt.figure(figsize=(12,6))
plt.plot(df['Lon'],df['Lat'],'b+',ms=0.5)
plt.xlim(-74.2,-73.7)
plt.ylim(40.6,41)


# In[64]:


#perform spatial analys
# Meaning of spatial analysis--> Spatial analysis is a type of geographical analysis which seeks to explain patterns of
# human behavior  and its spatial expression in terms of mathematics and geometry, that is, locational analysis


# In[65]:


df_out=df[df['weekday']=='Sunday']


# In[66]:


df_out.shape


# In[67]:


df_out.head()


# In[68]:


rush=df_out.groupby(['Lat','Lon'])['weekday'].count().reset_index()
rush.columns=['Lat','Lon','no of trips']
rush


# In[69]:


pip install folium


# In[70]:


from folium.plugins import HeatMap


# In[71]:


import folium


# In[72]:


basemap=folium.Map()


# In[73]:


HeatMap(rush,zoom=20,radius=15).add_to(basemap)
basemap


# 

# In[74]:


#Automate your analysis 


# In[75]:


def plot(df,day):
    basemap=folium.Map()
    df_out=df[df['weekday']==day]
    HeatMap(df_out.groupby(['Lat','Lon'])['weekday'].count().reset_index(),zoom=20,radius=15).add_to(basemap)
    return basemap


# In[76]:


plot(df,'Saturday')


# In[ ]:





# In[77]:


# Data Preparation


# In[78]:


#uber pickups by the month in NYC


# In[79]:


uber_15=pd.read_csv(r'C:/Users/user/Desktop/Udemy/Uber/uber-raw-data-janjune-15.csv')


# In[80]:


uber_15.head()


# In[81]:


uber_15.dtypes


# In[82]:


uber_15['Pickup_date']=pd.to_datetime(uber_15['Pickup_date'],format="%Y-%m-%d %H:%M:%S")


# In[83]:


uber_15.dtypes


# In[84]:


uber_15['weekday']=uber_15['Pickup_date'].dt.day_name()
uber_15['day']=uber_15['Pickup_date'].dt.day
uber_15['minute']=uber_15['Pickup_date'].dt.minute
uber_15['month']=uber_15['Pickup_date'].dt.month
uber_15['hour']=uber_15['Pickup_date'].dt.hour


# In[86]:


uber_15.head()


# In[ ]:


#Uber pickups in NYC


# In[89]:


px.bar(x=uber_15['month'].value_counts().index,
       y=uber_15['month'].value_counts())


# In[ ]:


#Anlysing Rush In New York City


# In[ ]:





# In[90]:


plt.figure(figsize=(12,6))
sns.countplot(uber_15['hour'])


# In[91]:


#Analysing In depth Analysis of rush in new york city day and hour wise


# In[93]:


summary=uber_15.groupby(['weekday','hour'])['Pickup_date'].count().reset_index()
summary.head()


# In[94]:


summary.columns=['weekday','hour','counts']


# In[95]:


summary.head()


# In[98]:


plt.figure(figsize=(12,8))
sns.pointplot(x='hour',y='counts',hue='weekday',data=summary)


# In[ ]:





# In[99]:


uber_foil=pd.read_csv(r'C:/Users/user/Desktop/Udemy/Uber/Uber-Jan-Feb-FOIL.csv')


# In[100]:


uber_foil.head()


# In[101]:


uber_foil.shape


# In[ ]:


#Analyse which base number has most active vehicles


# In[102]:


uber_foil['dispatching_base_number'].unique()


# In[ ]:





# In[103]:


sns.boxplot(x='dispatching_base_number',y='active_vehicles',data=uber_foil)


# In[ ]:





# In[ ]:


#Analysing which base number has most trips


# In[104]:


sns.boxplot(x='dispatching_base_number',y='trips',data=uber_foil)


# In[ ]:


#How average trips/vehicle decreases with dates with each of base number


# In[106]:


uber_foil['trips/vehicle']=uber_foil['trips']/uber_foil['active_vehicles']


# In[107]:


uber_foil.head()


# In[109]:


plt.figure(figsize=(12,6))
uber_foil.set_index('date').groupby(['dispatching_base_number'])['trips/vehicle'].plot()
plt.ylabel('Avg trips/vehicles')
plt.title('Demand vs Supply Chart')
plt.legend()


# In[ ]:





# In[ ]:





# In[ ]:




