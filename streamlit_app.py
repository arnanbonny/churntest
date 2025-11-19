import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title('Arnan Bonny')
st.write('Hellow World!')
# Single sheet by position (0-based)
df_demographics = pd.read_excel("churn.xlsx", sheet_name=0)

with st.expander('Patu'): 
  st.scatter_chart(data = df_demographics, x ='IncomeLevel', y ='Age')
  plt.show()
