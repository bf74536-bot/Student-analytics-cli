import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Student Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Analytics Web Interface")
st.markdown("Upload your student dataset to view performance metrics, grades distributions, and report summaries.")

# 2. Sidebar File Upload
st.sidebar.header("Data Source")
uploaded_file = st.sidebar.file_uploader("Upload a Student CSV File", type=["csv"])

# 3. Main Dashboard Logic
if uploaded_file is not None:
    try:
        # Read the uploaded dataset
        df = pd.read_csv(uploaded_file)
        
        # Display raw data preview inside an expander
        with st.expander("👀 View Raw Data Preview", expanded=False):
            st.dataframe(df)

        # Standardizing column names for convenience (optional)
        # Expected baseline columns: 'name', 'grade' / 'score'
        grade_col = next((col for col in df.columns if 'grade' in col.lower() or 'score' in col.lower()), None)
        
        if grade_col:
            # 4. Metric Calculations
            total_students = len(df)
            avg_grade = df[grade_col].mean()
            max_grade = df[grade_col].max()
            min_grade = df[grade_col].min()

            # Display Key Metrics Side-by-Side
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Students", total_students)
            col2.metric("Average Grade", f"{avg_grade:.2f}")
            col3.metric("Highest Grade", f"{max_grade}")
            col4.metric("Lowest Grade", f"{min_grade}")

            # 5. Data Visualizations
            st.subheader("📈 Grade Performance Distributions")
            
            # Interactive Bar Chart of individual scores
            if 'name' in [c.lower() for c in df.columns]:
                name_col = next(col for col in df.columns if 'name' in col.lower())
                st.bar_chart(data=df, x=name_col, y=grade_col)
            else:
                # Fallback to a histogram/distribution if names aren't present
                st.bar_chart(df[grade_col])
                
        else:
            st.warning("⚠️ Could not automatically detect a 'grade' or 'score' column in your CSV. Please ensure your file contains numeric performance data.")

    except Exception as e:
        st.error(f"Error parsing file: {e}")

else:
    # Landing state when no file is uploaded yet
    st.info("💡 Please upload a student CSV dataset using the sidebar file picker to view the live analytics charts.")
