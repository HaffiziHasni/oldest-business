#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_cell_magic('sql', '', 'postgresql:///oldestbusinesses\n \n\nSELECT MIN(year_founded), MAX(year_founded) \nFROM businesses')


# In[ ]:


get_ipython().run_cell_magic('sql', '', '\nSelect count(*)\nFROM businesses\nWHERE year_founded < 1000;')


# In[ ]:


get_ipython().run_cell_magic('sql', '', '\n\nSELECT * \nFROM businesses \nWHERE year_founded<1000 \nORDER BY year_founded ')


# In[ ]:


get_ipython().run_cell_magic('sql', '', '\n\nSELECT businesses.business, businesses.year_founded, businesses.country_code, categories.category\nFROM businesses\nINNER JOIN categories\nON businesses.category_code=categories.category_code\nWHERE year_founded <1000\nORDER BY year_founded')


# In[ ]:


get_ipython().run_cell_magic('sql', '', '\n\nSELECT category, count(category) as n\nFROM categories\nINNER JOIN businesses\nON businesses.category_code=categories.category_code\nGROUP BY category\nORDER BY n DESC\nLIMIT 10')


# In[ ]:


get_ipython().run_cell_magic('sql', '', '\nSELECT MIN(year_founded) as oldest, countries.continent\nFROM businesses\nINNER JOIN countries\nON businesses.country_code=countries.country_code\nGROUP BY continent\nORDER BY oldest ')


# In[ ]:


get_ipython().run_cell_magic('sql', '', '\nSELECT business,year_founded, categories.category, countries.country, countries.continent\nFROM businesses\nINNER JOIN countries\nON businesses.country_code=countries.country_code\nINNER JOIN categories\nON businesses.category_code=categories.category_code')


# In[ ]:


get_ipython().run_cell_magic('sql', '', '\nSELECT  countries.continent, categories.category, COUNT(business) as n\nFROM businesses\nINNER JOIN countries\nON businesses.country_code=countries.country_code\nINNER jOIN categories\nON businesses.category_code=categories.category_code\nGROUP BY continent,category')


# In[ ]:


get_ipython().run_cell_magic('sql', '', '\nSELECT  countries.continent, categories.category, COUNT(business) as n\nFROM businesses\nINNER JOIN countries\nON businesses.country_code=countries.country_code\nINNER jOIN categories\nON businesses.category_code=categories.category_code\nGROUP BY continent,category\nHAVING COUNT(business)>5\nORDER BY n DESC')

