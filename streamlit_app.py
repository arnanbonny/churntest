import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title('Arnan Bonny')
st.write('Hellow World!')
# Single sheet by position (0-based)
df_demographics = pd.read_excel("churn.xlsx", sheet_name=1)

with st.expander('Patu'): 
  st.bar_chart(data=df_demographics, x='ProductCategory', y='AmountSpent')
  plt.show()

with st.sidebar:
  st.header('Filters')
  Category = st.selectbox('Category', ('Books','Clothing','Electronics','Furniture','Groceries'))
