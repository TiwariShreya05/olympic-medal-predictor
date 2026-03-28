
# coding: utf-8

# In[61]:


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
import pickle


# In[62]:


teams=pd.read_csv("teams.csv")


# In[63]:


teams


# In[64]:


teams=teams[["team",'country','year','athletes','age','prev_medals','medals']]


# In[65]:


teams


# In[66]:


teams.corr()['medals']


# In[67]:


import seaborn as sns


# In[68]:


sns.lmplot(x='athletes', y='medals', data=teams, fit_reg=True, ci=None)


# In[69]:


sns.lmplot(x='age',y='medals',data=teams,fit_reg=True,ci=None)


# In[70]:


teams.plot.hist(y='medals')


# In[71]:


teams[teams.isnull().any(axis=1)]


# In[72]:


teams=teams.dropna()


# In[73]:


teams


# In[74]:


train=teams[teams['year']<2012].copy()
test=teams[teams['year']>=2012].copy()
            


# In[75]:


train.shape


# In[76]:


test.shape


# In[77]:


from sklearn.linear_model import LinearRegression

reg=LinearRegression()


# In[78]:


predictors=['athletes','prev_medals']
target='medals'


# In[79]:


reg.fit(train[predictors], train[target])


# In[80]:


predictions=reg.predict(test[predictors])


# In[81]:


predictions


# In[82]:


test['predictions']=predictions


# In[83]:


test


# In[84]:


test.loc[test['predictions']<0,'predictions']=0


# In[85]:


test['predictions']=test['predictions'].round()


# In[86]:


test


# In[87]:


from sklearn.metrics import mean_absolute_error
error=mean_absolute_error(test['medals'],test['predictions'])


# In[88]:


error


# In[89]:


teams.describe()['medals']


# In[90]:


test[test['team']=='USA']


# In[91]:


test[test['team']=='IND']


# In[92]:


error=(test['medals']-test['predictions']).abs()


# In[93]:


error


# In[94]:


error_by_team=error.groupby(test['team']).mean()


# In[95]:


error_by_team


# In[96]:


medals_by_teams=test['medals'].groupby(test['team']).mean()


# In[97]:


error_ratio=error_by_team/medals_by_teams


# In[98]:


error_ratio


# In[99]:


error_ratio[~pd.isnull(error_ratio)]


# In[100]:


import numpy as np
error_ratio=error_ratio[np.isfinite(error_ratio)]


# In[101]:


error_ratio


# In[102]:


error_ratio.plot.hist()


# In[106]:


error_ratio.sort_values()


# In[108]:


import pickle

# Save your trained model
pickle.dump(reg, open('model.pkl', 'wb'))

