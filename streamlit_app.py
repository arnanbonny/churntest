import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title('Arnan Bonny')
st.write('Hellow World!')
# Single sheet by position (0-based)
df_demographics = pd.read_excel("https://raw.githubusercontent.com/arnanbonny/churntest/main/Customer_Churn_Data_Large%20%20Lloyds.xlsx", sheet_name=0)

