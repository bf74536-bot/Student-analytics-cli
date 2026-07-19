import streamlit as st

# storage dictionary
if 'students_db' not in st.session_state:
    st.session_state.students_db = {}

def get_letter_grade(score):
    if score >= 90: return "A+"
    elif score >= 75: return "A"
    elif score >= 60: return "B"
    else: return "C"

st.title("📊 STUDENT GRADING & ANALYTICS CLI")

menu = st.selectbox(
    "Select analytical protocol",
    ["1. Add New Student Profile",
     "2. Enter/Record Assignment Score", 
     "3. View Classroom Statistical Summary",
     "4. Search and Generate Individual Report Card",
     "5. Shutdown Analytics Engine"]
)

if menu == "1. Add New Student Profile":
    st.subheader("REGISTER NEW STUDENT")
    name = st.text_input("Enter unique student full name")
    if st.button("Add Student"):
        if name:
            if name in st.session_state.students_db:
                st.error("Student registry collision. Name exists.")
            else:
                st.session_state.students_db[name] = []
                st.success(f"Profile instantiated for {name}")

elif menu == "2. Enter/Record Assignment Score":
    st.subheader("RECORD SCORE")
    name = st.selectbox("Select Student", list(st.session_state.students_db.keys()))
    score = st.number_input("Enter Score out of 100", 0, 100)
    if st.button("Save Score"):
        st.session_state.students_db[name].append(score)
        st.success(f"Score {score} added for {name}")

elif menu == "3. View Classroom Statistical Summary":
    st.subheader("CLASSROOM SUMMARY")
    all_scores = [s for scores in st.session_state.students_db.values() for s in scores]
    if all_scores:
        st.metric("Highest", max(all_scores))
        st.metric("Lowest", min(all_scores))
        st.metric("Average", round(sum(all_scores)/len(all_scores), 2))
        st.metric("Total Students", len(st.session_state.students_db))

st.write("---")
st.caption("Built by Batool Fatima | BCA 2026-29 | Akshara Degree College")
