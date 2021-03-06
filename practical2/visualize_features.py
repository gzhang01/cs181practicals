
# coding: utf-8

# In[88]:

import pandas as pd
import matplotlib.pyplot as plt
try:
    import seaborn as sns
except:
    pass
get_ipython().magic(u'matplotlib inline')


# In[89]:

def plot_feature(csv_path, colname):
    df = pd.DataFrame.from_csv(csv_path)
    return df.boxplot(column=colname, by="classnum")

# In[ ]:



