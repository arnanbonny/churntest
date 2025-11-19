import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title('Arnan Bonny')
st.write('Hellow World!')
# Single sheet by position (0-based)
df_demographics = pd.read_excel('churntest/Customer_Churn_Data_Large_Lloyds.xlsx', sheet_name=0) 
