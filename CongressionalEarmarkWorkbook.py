#!/usr/bin/env python
# coding: utf-8

# In[52]:


# Importing necessary packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Connecting the dataset
earmarks = pd.read_csv('FY2022-Congressionally-Directed-Spending-BPC.csv')
print(len(earmarks))
# Removes unusable "amount" data
for i in earmarks.index[earmarks["amount"]=='?'].tolist():
    earmarks = earmarks.drop(i)

# Quick look at the dataset
print(len(earmarks))
print(earmarks.info)
print(earmarks.head())

# Some unnecessary warnings pop-up on some of the barplots, this line keeps them from showing up and being distracting
pd.options.mode.chained_assignment = None


# In[53]:


# Sectioning off the dataset by party of the first requestor
dem_earmarks = earmarks[earmarks['requestor_one_party']=='Democrat']
print(dem_earmarks.head())
rep_earmarks = earmarks[earmarks['requestor_one_party']=='Republican']
ind_earmarks = earmarks[earmarks['requestor_one_party']=='Independent']


# ### Swing states alone are being studied because they are most likely to show an interesting comparison between the spending by different parties.

# In[54]:


# Creating useful lists for holding values needed for creating the coming for loops and plots
parties = [dem_earmarks, rep_earmarks, ind_earmarks]
swing_states = ["CO", "FL", "IA", "MI", "NC", "NH", "NV", "OH", "PA", "VI", "WI"]


# In[55]:


# Making a function that can be used for each of the states in the swing states list

def state_plt(state_index):
    for i in range(len(parties)):
        # Index was used instead of direct dataframe so that the party can be stated later on above the outputted plots
        party = parties[i]
        str_party = ["Democrat", "Republican", "Independent"][i]

        # Sorting party dataframe by state and category of spending
        party_by_state = party[party.state ==swing_states[state_index]]
        party_by_state['amount'] = party_by_state['amount'].apply(pd.to_numeric)
        grouped = party_by_state.groupby(['category']).sum()

        # Fits the size of the chart to the amount of bars there will be in the chart
        size = 0
        for i in range(len(grouped)):
            size+=3

        # Creates the plot
        if size == 0:
            pass
        else:
            print("State:", swing_states[state_index])
            print("Party Dataframe:", str_party)
            f,ax = plt.subplots(1, 1, figsize=(size, 10))

            # Plots bars on subplot created above
            ax.ticklabel_format(useOffset=False, style = "plain")
            sns.barplot(x= grouped.index, y=grouped.amount, ax=ax)
            ax.set_xticks(list(range(len(grouped.index.unique()))))
            ax.set_xticklabels(list(grouped.index.unique()), rotation=90, fontsize = 15)
            ax.set_ylabel('Amount Spent in Dollars', fontsize = 15)
            ax.set_xlabel('Category')
            plt.show()


# In[56]:


# Creates plots for Colorado

state_plt(0)


# In[57]:


# Creates plots for FLorida

state_plt(1)


# In[58]:


# Creates plots for Iowa
state_plt(2)


# In[59]:


# Creates plots for Michigan
state_plt(3)


# In[60]:


# Creates plots for North Carolina
state_plt(4)


# In[61]:


# Creates plots for New Hampshire
state_plt(5)


# In[62]:


# Creates plots for Nevada
state_plt(6)


# In[63]:


# Creates plots for Ohio
state_plt(7)


# In[64]:


# Creates plots for Pennsylvania
state_plt(8)


# In[65]:


# Creates plots for Virginia
state_plt(9)


# In[66]:


# Creates plots for Michigan
state_plt(10)


# ## Agencies with most Democratic spending by state:
# ##### Colorado: Energy and Water Development
# ##### Florida: Transportation, Housing, and Urban Development
# ##### Iowa: Transportation, Housing, and Urban Development
# ##### Michigan: Transportation, Housing, and Urban Development
# ##### North Carolina: Transportation, Housing, and Urban Development
# ##### New Hampshire: Transportation, Housing, and Urban Development
# ##### Nevada: Transportation, Housing, and Urban Development
# ##### Ohio: Transportation, Housing, and Urban Development
# ##### Pennsylvania: Transportation, Housing, and Urban Development
# ##### Virginia: Interior and Environment
# ##### Wisconsin: Agriculture, Rural Development, and Food and Drug Administration
# 
# As is made clear by both the bar charts and the list above, Transportation, Housing, and Urban Development is the most common kind of agency that Democrat started earmark funding is given to in swing states. 

# # Agencies with most Republican spending by state:
# ##### Colorado: No Data
# ##### Florida: Energy and Water Development
# ##### Iowa: Transportation, Housing, and Urban Development
# ##### Michigan: Transportation, Housing, and Urban Development
# ##### North Carolina: Military Construction and Veterans Affairs
# ##### New Hampshire: No Data
# ##### Nevada: Interior and Environment
# ##### Ohio: Transportation, Housing, and Urban Development
# ##### Pennsylvania: Transportation, Housing, and Urban Development
# ##### Virginia: No Data
# ##### Wisconsin: Interior and Environment (Not by much)
# 
# While Transportation, Housing, and Urban Development is still the most common type of agency that is given funding, there is much more variation in Republican spending. Another intresting thing to note is the lack of Republican Earmark spending in Colorado, New Hampshire, and Virginia. 

# In[67]:


# Grouping all spending from each party
int_amount_list = []
# Converts 'amount' into an integer and adds that column to earmarks -> this makes it possible to sum 'amount' based on party
for index in range(len(earmarks)):
    try:
        num = int(earmarks.iloc[index]['amount'])
        int_amount_list.append(num)
    except: 
        # Some of the rows have different formats that don't convert to integers so those are replaced with zeros
        # This will cause inaccuracies in the new amount column
        int_amount_list.append(0)

# Adds integer values of amount to earmarks
earmarks['int_amount'] = int_amount_list
# Groups earmarks by party, summing 'budget_request' and 'int_amount'
by_party = earmarks.groupby(['requestor_one_party']).sum()
print(by_party)


# In[68]:


# Creates a barplot with the newly condensed data
f,ax = plt.subplots(1, 1, figsize=(15, 10))
ax.ticklabel_format(useOffset=False, style = "plain")
sns.barplot(x= by_party.index, y=by_party.int_amount, ax=ax)
ax.set_xticks(list(range(len(by_party.index.unique()))))
ax.set_xticklabels(list(by_party.index.unique()), rotation=90, fontsize = 15)
ax.set_ylabel('Total Amount Spent', fontsize = 15)
ax.set_xlabel('')
plt.show()


# Both Democrat and Republican Congresspeople divert a substantial amount of US Federal Dolars to their own pet projects. The difference in spending between the two groups isn't massive. Independent Congresspeople spend a lot less, but that can be attributed to the fact that there are almost no independent candidates that have a seat in congress (3 as of 6/7/2023). 

# ### Transportation, Housing, and Urban Development is the agency that is given the most money in congressional earmarks by both parties, agencies that recieve Republican led earmarks in swing states are more varied than Democrat led ones (the most funded agency by Democrats in almost every swing state was Transportation, Housing, and Urban Development), and there is no impactful difference in earmark spending between Republicans and Democrats.
