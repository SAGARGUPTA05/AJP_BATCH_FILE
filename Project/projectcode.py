import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

# Set page layout to wide
st.set_page_config(layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    try:
        file_path = r"C:\Users\sggup\OneDrive\Desktop\MyLearning\Pythonlearning\Project\india_job_sector.xlsx"
        df = pd.read_excel(file_path)
        
        # Add missing columns if necessary
        if "Gender" not in df.columns:
            df["Gender"] = np.random.choice(["Male", "Female"], size=len(df))
        
        if "GDP_Contribution" not in df.columns:
            df["GDP_Contribution"] = np.random.uniform(1, 10, size=len(df))
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load data
df = load_data()
if df is None:
    st.stop()

# Title
st.title("📊 India's Job Sector Analysis")
st.sidebar.header("Filter Options")

# Initialize session state variables if not present
if "filtered_df" not in st.session_state:
    st.session_state.filtered_df = df  # Store initially unfiltered data

# Sidebar Filters
sector_filter = st.sidebar.multiselect("Select Sector(s)", options=df["Sector"].unique(), default=df["Sector"].unique())
gender_filter = st.sidebar.multiselect("Select Gender", options=["Male", "Female"], default=["Male", "Female"])
experience_filter = st.sidebar.slider("Select Experience (Years)", min_value=int(df["Experience_Years"].min()), 
                                      max_value=int(df["Experience_Years"].max()), 
                                      value=(int(df["Experience_Years"].min()), int(df["Experience_Years"].max())))

# Filter button
if st.sidebar.button("Apply Filters"):
    st.session_state.filtered_df = df[(df["Sector"].isin(sector_filter)) & 
                                      (df["Gender"].isin(gender_filter)) & 
                                      (df["Experience_Years"].between(experience_filter[0], experience_filter[1]))]

# Use session_state filtered data
filtered_df = st.session_state.filtered_df

# ---- CHARTS ----
st.subheader("📌 Job Sector Insights at a Glance")

# Layout with three rows, each containing two columns
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Sector-wise GDP Contribution
fig1 = px.pie(filtered_df.groupby("Sector")["GDP_Contribution"].sum().reset_index(), values="GDP_Contribution", 
              names="Sector", title="Sector Contribution to GDP")
fig1.update_layout(height=300)
col1.plotly_chart(fig1, use_container_width=True)

# Salary Distribution
fig2 = px.box(filtered_df, x="Sector", y="Salary", color="Sector", title="Salary Distribution by Sector")
fig2.update_layout(height=300)
col2.plotly_chart(fig2, use_container_width=True)

# Gender Distribution
fig3 = px.bar(filtered_df.groupby(["Sector", "Gender"]).size().reset_index(name="Count"), x="Sector", y="Count", 
              color="Gender", title="Gender Distribution by Sector", barmode="group")
fig3.update_layout(height=300)
col3.plotly_chart(fig3, use_container_width=True)

# Experience vs Salary
fig4 = px.scatter(filtered_df, x="Experience_Years", y="Salary", color="Sector", title="Experience vs Salary Trend")
fig4.update_traces(marker=dict(size=5))
fig4.update_layout(height=300)
col4.plotly_chart(fig4, use_container_width=True)
