import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title('Arnan Bonny')
st.write('Hello World!')
# Single sheet by position (0-based)
df_demographics = pd.read_excel("churn.xlsx", sheet_name=1)


# Assuming df_demographics is already loaded

with st.sidebar:
    st.header('Filters')
    Categories = st.multiselect('Category', df_demographics['ProductCategory'].unique(), default=df_demographics['ProductCategory'].unique())

# Filter dataframe for all selected categories
filtered_df = df_demographics[df_demographics['ProductCategory'].isin(Categories)]

with st.expander('Bar Chart'):
    st.bar_chart(data=filtered_df, x='ProductCategory', y='AmountSpent')

with st.expander('DataFrame'):
    st.DataFrame(data=filtered_df)


