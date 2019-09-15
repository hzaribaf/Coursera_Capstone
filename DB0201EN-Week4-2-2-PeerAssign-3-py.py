#!/usr/bin/env python
# coding: utf-8

# <a href="https://cognitiveclass.ai"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# <h1 align=center><font size = 5>Assignment: Notebook for Peer Assignment</font></h1>

# # Introduction
# 
# Using this Python notebook you will:
# 1. Understand 3 Chicago datasets  
# 1. Load the 3 datasets into 3 tables in a Db2 database
# 1. Execute SQL queries to answer assignment questions 

# ## Understand the datasets 
# To complete the assignment problems in this notebook you will be using three datasets that are available on the city of Chicago's Data Portal:
# 1. <a href="https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2">Socioeconomic Indicators in Chicago</a>
# 1. <a href="https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t">Chicago Public Schools</a>
# 1. <a href="https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2">Chicago Crime Data</a>
# 
# ### 1. Socioeconomic Indicators in Chicago
# This dataset contains a selection of six socioeconomic indicators of public health significance and a “hardship index,” for each Chicago community area, for the years 2008 – 2012.
# 
# For this assignment you will use a snapshot of this dataset which can be downloaded from:
# https://ibm.box.com/shared/static/05c3415cbfbtfnr2fx4atenb2sd361ze.csv
# 
# A detailed description of this dataset and the original dataset can be obtained from the Chicago Data Portal at:
# https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2
# 
# 
# 
# ### 2. Chicago Public Schools
# 
# This dataset shows all school level performance data used to create CPS School Report Cards for the 2011-2012 school year. This dataset is provided by the city of Chicago's Data Portal.
# 
# For this assignment you will use a snapshot of this dataset which can be downloaded from:
# https://ibm.box.com/shared/static/0g7kbanvn5l2gt2qu38ukooatnjqyuys.csv
# 
# A detailed description of this dataset and the original dataset can be obtained from the Chicago Data Portal at:
# https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t
# 
# 
# 
# 
# ### 3. Chicago Crime Data 
# 
# This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days. 
# 
# This dataset is quite large - over 1.5GB in size with over 6.5 million rows. For the purposes of this assignment we will use a much smaller sample of this dataset which can be downloaded from:
# https://ibm.box.com/shared/static/svflyugsr9zbqy5bmowgswqemfpm1x7f.csv
# 
# A detailed description of this dataset and the original dataset can be obtained from the Chicago Data Portal at:
# https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
# 

# ### Store the datasets in database tables
# In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. To analyze the data using SQL, it first needs to be stored in the database.
# 
# While it is easier to read the dataset into a Pandas dataframe and then PERSIST it into the database as we saw in Week 3 Lab 3, it results in mapping to default datatypes which may not be optimal for SQL querying. For example a long textual field may map to a CLOB instead of a VARCHAR. 
# 
# Therefore, __it is highly recommended to manually load the table using the database console LOAD tool, as indicated in Week 2 Lab 1 Part II__. The only difference with that lab is that in Step 5 of the instructions you will need to click on create "(+) New Table" and specify the name of the table you want to create and then click "Next". 
# 
# <a href="https://cognitiveclass.ai"><img src = "https://ibm.box.com/shared/static/uc4xjh1uxcc78ks1i18v668simioz4es.jpg"></a>
# 
# ##### Now open the Db2 console, open the LOAD tool, Select / Drag the .CSV file for the first dataset, Next create a New Table, and then follow the steps on-screen instructions to load the data. Name the new tables as folows:
# 1. __CENSUS_DATA__
# 1. __CHICAGO_PUBLIC_SCHOOLS__
# 1. __CHICAGO_CRIME_DATA__

# ### Connect to the database 
# Let us first load the SQL extension and establish a connection with the database

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[2]:


# Remember the connection string is of the format:
# %sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name
# Enter the connection string for your Db2 on Cloud database instance below
get_ipython().run_line_magic('sql', 'ibm_db_sa://qkk01627:8dv7p8g74r1sn%5E9x@dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net:50000/BLUDB')


# ## Problems
# Now write and execute SQL queries to solve assignment problems
# 
# ### Problem 1
# 
# ##### How many rows are in each dataset?

# In[3]:


# Rows in Census Data (Socieconimic Indicators)
get_ipython().run_line_magic('sql', 'select count(*) as "# Rows in Cencus Data" from CENSUS_DATA;')


# In[4]:


# Rows in Public Schools
get_ipython().run_line_magic('sql', 'select count(*) as "# Rows in Public Schools" from CHICAGO_PUBLIC_SCHOOLS;')


# In[5]:


# Rows in Crime Data
get_ipython().run_line_magic('sql', 'select count(*) as "# Rows in Crime Data" from CHICAGO_CRIME_DATA;')


# ### Problem 2
# 
# ##### Find average college enrollments by community area

# In[22]:


get_ipython().run_line_magic('sql', 'select "Community_Area_Number", avg("College_Enrollment__number_of_students_") as "Average College Enrollment" from CHICAGO_PUBLIC_SCHOOLS group by "Community_Area_Number";')


# ### Problem 3
# 
# ##### Find the number of schools that are healthy school certified

# In[26]:


get_ipython().run_line_magic('sql', 'select count("Healthy_Schools_Certified_") as "Number of healthy certified schools"     from CHICAGO_PUBLIC_SCHOOLS where "Healthy_Schools_Certified_"=\'Yes\';')


# ### Problem 4
# 
# ##### How many observations have a Location Description value of GAS STATION
# 

# In[27]:


get_ipython().run_line_magic('sql', 'select count("Location_Description") as "Number of observations in Gas Station"     from CHICAGO_CRIME_DATA where "Location_Description"=\'GAS STATION\';')


# ### Problem 5
# 
# ##### Retrieve a list of the top 10 community areas which have most number of schools and sorted in descending order.

# In[33]:


get_ipython().run_line_magic('sql', 'select "Community_Area_Number", count("Community_Area_Number") as "Number of schools" from CHICAGO_PUBLIC_SCHOOLS     group by "Community_Area_Number" order by "Number of schools" desc limit 10;')


# ### Problem 6
# 
# ##### How many observations have value MOTOR VEHICLE THEFT in the Primary Type variable (this is the number of crimes related to Motor vehicles)

# In[34]:


get_ipython().run_line_magic('sql', 'select count("Primary_Type") as "Number of motor vehicle theft"     from CHICAGO_CRIME_DATA where "Primary_Type"=\'MOTOR VEHICLE THEFT\';')


# ### Problem 7
# 
# ##### Find the minimum “Average Student Attendance” for community are where hardship is 96. Hint: use INNER JOIN

# In[63]:


get_ipython().run_line_magic('sql', 'select S."Community_Area_Number", S."Average_Student_Attendance" as "Minimun average student attendance",     C."HARDSHIP_INDEX" from "CHICAGO_PUBLIC_SCHOOLS" S inner join "CENSUS_DATA" C     on S."Community_Area_Number"=C."Community_Area_Number" where "HARDSHIP_INDEX"=96 order by "Average_Student_Attendance" limit 1;')


# Copyright &copy; 2018 [cognitiveclass.ai](cognitiveclass.ai?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).
# 
