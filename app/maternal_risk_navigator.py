import streamlit as st
import pandas as pd
import plotly.express as px
from pickle import load as pickle_load

with open('/workspaces/4Geeks_Classes/data/raw/maternal_risk_dftrain.pkl', 'rb') as file:
    df = pickle_load(file)

st.title ('Maternal Risk Navigator')
st.dataframe(df.sample(10,random_state=2025))
st.markdown("## Observations")
st.markdown("We can see that in the 'age' variable, that the range is between **15 and 55** years. This means that we are accounting for teen pregnancies and older people")
st.dataframe(df.describe(include='number').T)
fig = px.scatter_matrix(df,color='risklevel',dimensions=['age','systolicbp','diastolicbp'])
st.plotly_chart(fig)
fig2 = px.parallel_coordinates(df,color_continuous_scale=px.colors.diverging.Tealrose, color=df['risklevel'].map({'high risk':0, 'low risk':1, 'mid risk':2}))
st.plotly_chart(fig2)
fig3 = pd.plotting.parallel_coordinates(df.sample(90, random_state=2025), 'risklevel', color=['teal','gold','crimson'])
st.pyplot(fig3.figure)