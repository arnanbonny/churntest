import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title('Arnan Bonny')
st.write('Hellow World!')
# Single sheet by position (0-based)
df_demographics = pd.read_excel("churn.xlsx", sheet_name=1)

with st.sidebar:
    st.header('Filters')
    Category = st.multiselect('Category', df_demographics['ProductCategory'].unique())

# Filter the dataframe based on the selected category
filtered_df = df_demographics[df_demographics['ProductCategory'] == Category]

with st.expander('Patu'):
    st.bar_chart(data=filtered_df, x='ProductCategory', y='AmountSpent')

