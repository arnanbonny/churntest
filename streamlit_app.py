import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title('Arnan Bonny')
st.write('Hello World!')
# Single sheet by position (0-based)
df_demographics = pd.read_excel("churn.xlsx", sheet_name=1)
df_transaction = pd.read_excel("churn.xlsx", sheet_name=2)


# Assuming df_demographics is already loaded

with st.sidebar:
    st.header('Filters')
    Categories = st.multiselect('Category', df_demographics['ProductCategory'].unique(), default=df_demographics['ProductCategory'].unique())

with st.sidebar:
    st.header('Filters')
    Categories = st.select('Category', df_demographics['ProductCategory'].unique(), default=df_demographics['ProductCategory'].unique())

# Filter dataframe for all selected categories
filtered_df = df_demographics[df_demographics['ProductCategory'].isin(Categories)]

with st.expander('Bar Chart'):
    st.bar_chart(data=filtered_df, x='ProductCategory', y='AmountSpent')

with st.expander('DataFrame'):
    st.dataframe(data=filtered_df)
# --- Sidebar Selection ---
st.sidebar.header("Select a DataFrame")

# Create a dictionary for easy mapping of names to DataFrame objects
dataframes = {
    "Demographics Data": df_demographics,
    "Transaction Data": df_transaction
}

selected_df_name = st.sidebar.selectbox( # Corrected from st.sidebar.select
    "Choose a dataset:",
    list(dataframes.keys() 

# Get the actual DataFrame object based on the user's selection
selected_df = dataframes[selected_df_name]

# --- Main Page Display ---

# Use an expander as requested
with st.expander(f"View {selected_df_name}"):
    # Display the selected DataFrame using the recommended st.dataframe()
    st.dataframe(data=selected_df, use_container_width=True)

st.write(f"Displaying {selected_df_name} above.")


