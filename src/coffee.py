import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df_raw = pd.read_csv('../data/raw/coffee.csv')



#DF Baking

df_baking = df_raw.copy()
df_baking = df_baking[['total_cup_points','species','country_of_origin','aroma','flavor','aftertaste','acidity','body','balance','uniformity','clean_cup','sweetness','cupper_points','cupper_points','moisture']]
df_baking.columns = df_baking.columns.str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.lower()
df_baking['species'] = df_baking['species'].astype("category")
df_baking['country_of_origin'] = df_baking['country_of_origin'].astype("category")
df_baking = df_baking.loc[df_baking['flavor'] != 0].reset_index(drop=True)

df = df_baking.copy()



fig = px.scatter(df,x='total_cup_points',y='flavor',title='Total Cup Points vs Flavor')
st.plotly_chart(fig)




#st.title('Concrete Data Set Navigator')

#st.text('Information that you would like to show to your audience')

#You will make different 'UI's for different 'audience members'
#There are ways to format your information 

#st.markdown('**Streamlit** is a good *tool*!')

#st.dataframe(df)

#plt.figure(figsize=(8,8))
#plt.scatter(x=df['cement'],y=df['compressive_strength'])
#plt.title('Compressive Strength vs Concrete Density')
#st.pyplot(plt)