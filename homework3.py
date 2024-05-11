# Your name here: Cedar Liu
# Your CNET ID here (this is the part of your uchicago email id before the @): cedarliu
# Your github user id here: cedarliu0906

"""
INSTRUCTIONS

Available: May 2nd

Due: May 12th at 11:59PM

Gentle reminder that, among other things, you

(a) Must answer your questions in the homework3.py file
(b) Must homework3.py commit to your clone of the GitHub homework repo
(c) Must link your GitHub repo to GradeScope
(d) Must NOT repeatedly use a hard-coded path for the working directory
(e) Must NOT modify the original data in any way

Failure to do any of these will result in the loss of points
"""

"""
QUESTION 1

In this question, you'll be replicating the graph from Lecture 14, slide 5
which shows the population of Europe from 0 AD to the present day in both
the linear and the log scale. You can find the data in population.csv, and the
variable names are self-explanatory.

Open this data and replicate the graph. 

Clarification: You are not required to replicate the y-axis of the right hand
side graph; leaving it as log values is fine!

Clarification: You are not required to save the figure

Hints: Note that...

- The numpy function .log() can be used to convert a column into logs
- It is a single figure with two subplots, one on the left and the other on
the right
- The graph only covers the period after 0 AD
- The graph only covers Europe
- The figure in the slides is 11 inches by 6 inches
"""
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Specify an absolute path using the Python os library to join filenames
popfile_path="E:/Working Files/UChicago MPP/24spring/PPHA 30537 2 Data and Programming for Public Policy I - Python Programming/hwk/hwk3"
pop_path=os.path.join(popfile_path, "population.csv")
pop_data=pd.read_csv(pop_path)

# Filter the data for entries related to Europe and from the year 0 AD onwards
eu_pop = pop_data[(pop_data['Entity'] == 'Europe') & (pop_data['Year'] >= 0)]

# Setting up the figure and subplots
fig, (ax1, ax2)=plt.subplots(1, 2, figsize=(11, 6))

# Plotting the linear scale population
ax1.plot(eu_pop['Year'], eu_pop['Population (historical estimates)'])
ax1.set_title('Population of Europe')
ax1.set_xlabel('Year')
ax1.set_ylabel('Population')

# Plotting the log scale population
ax2.plot(eu_pop['Year'], np.log(eu_pop['Population (historical estimates)']))
ax2.set_title('Population of Europe (Log)')
ax2.set_xlabel('Year')
ax2.set_ylabel('Population (Log)')

# Enhancing layout
plt.tight_layout()
plt.show()

"""
QUESTION 2

A country's "capital stock" is the value of its' physical capital, which includes the 
stock of equipment, buildings, and other durable goods used in the production 
of goods and services. Macroeconomists seem to conisder it important to have 
public policies that encourage the growth of capital stock. Why is that?

In this exercise we will look at the relationship between capital stock and 
GDP. You can find data from the IMF in "capitalstock.csv" and documentation in
"capitalstock documentation.txt".

In this exercise we will only be using the variables that are demarcated in
thousands of 2017 international dollars to adjust for variation in the value 
of nominal national currency. Hint: These are the the variables that 
end in _rppp.

1. Open the dataset capitalstock.csv and limit the dataframe to only 
observations from 2018

2. Construct a variable called "capital_stock" that is the sum of the general
government capital stock and private capital stock. Drop 
observations where the value of capital stock is 0 or missing. (We will be 
ignoring public-private partnership capital stock for the purpose of t
his exercise.)

3. Create a scatterplot showing the relationship between log GDP and log
capital stock. Put capital stock on the y-axis. Add the line of best 
fit. Add labels where appropriate and make any cosmetic adjustments you want.

(Note: Does this graph suggest that macroeconomists are correct to consider 
 capital stock important? You don't have to answer this question - it's 
 merely for your own edification.)

4. Estimate a model of the relationship between the log of GDP 
and the log of capital stock using OLS. GDP is the dependent 
variable. Print a table showing the details of your model and, using comments, 
interpret the coefficient on capital stock. 

Hint: when using the scatter() method that belongs to axes objects, the alpha
option can be used to make the markers transparent. s is the option that
controls size
"""
# Open the dataset and limit the df to only obs from 2018
csfile_path="E:/Working Files/UChicago MPP/24spring/PPHA 30537 2 Data and Programming for Public Policy I - Python Programming/hwk/hwk3"
cs_path=os.path.join(csfile_path, "capitalstock.csv")
cs_data=pd.read_csv(cs_path)
cs_data_2018=cs_data[cs_data['year']==2018]

# Construct "capital_stock" and drop missing values
cs_data_2018['capital_stock']=cs_data_2018['kgov_n']+cs_data_2018['kpriv_n']
cs_data_2018=cs_data_2018[(cs_data_2018['capital_stock']>0) & (cs_data_2018['capital_stock'].notnull())]

# Create a scatterplot showing the relationship between log GDP and log capital stock
cs_data_2018['log_GDP']=np.log(cs_data_2018['GDP_n'])
cs_data_2018['log_capital_stock']=np.log(cs_data_2018['capital_stock'])
plt.figure(figsize=(10,7))
sns.scatterplot(data=cs_data_2018, x='log_capital_stock', y='log_GDP', alpha=0.6, s=80)
sns.regplot(data=cs_data_2018, x='log_capital_stock', y='log_GDP', scatter=False, color='blue')

plt.title('Relationship between Log GDP and Log Capital Stock in 2018')
plt.xlabel('Log Capital Stock')
plt.ylabel('Log GDP')
plt.grid(False)
plt.show()

# Estimate a model of the relationship between the log GDP and the log capital stock
x=sm.add_constant(cs_data_2018['log_capital_stock'])
y=cs_data_2018['log_GDP']

log_GDP_capital_stock_model=sm.OLS(y,x).fit()
print(log_GDP_capital_stock_model.summary())


