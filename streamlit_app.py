import streamlit as st
st.title('Arnan Bonny')
st.write('Hellow World!')
# Single sheet by position (0-based)
df_demographics = pd.read_excel(r"E:\Data Science and Analytics\PROJECT 1 - CUSTOMER CHURN\Customer_Churn_Data_Large  Lloyds.xlsx", sheet_name=0) 
