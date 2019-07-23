"""http://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot"""

import pandas as pd

df = pd.DataFrame({
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['california','dc','california','dc','california','texas','texas'],
    'num_children':[2,0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
})


import matplotlib.pyplot as plt
import pandas as pd

# a scatter plot comparing num_children and num_pets
df.plot(kind='scatter',x='num_children',y='num_pets',color='red')
plt.show()

# a simple line plot
df.plot(kind='bar',x='name',y='age')

# gca stands for 'get current axis'
ax = plt.gca()
df.plot(kind='line',x='name',y='num_children',ax=ax)
df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)
plt.show()


df.groupby('state')['name'].nunique().plot(kind='bar')
plt.show()

df.groupby(['state','gender']).size().unstack().plot(kind='bar',stacked=True)
plt.show()

df.groupby(['gender','state']).size().unstack().plot(kind='bar',stacked=True)
plt.show()

df[['age']].plot(kind='hist',bins=[0,20,40,60,80,100],rwidth=0.8)
plt.show()