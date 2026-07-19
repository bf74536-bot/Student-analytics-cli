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
    if not st.session_state.students_db:
        st.warning("Please add a student profile first.")
    else:
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
    else:
        st.info("No scores recorded yet to generate analytics.")

elif menu == "4. Search and Generate Individual Report Card":
    st.subheader("INDIVIDUAL REPORT CARD")
    if not st.session_state.students_db:
        st.warning("Please add a student profile first.")
    else:
        name = st.selectbox("Select Student to View Report", list(st.session_state.students_db.keys()))
        scores = st.session_state.students_db.get(name, [])
        if scores:
            st.write(f"### **Student Name:** {name}")
            
            # Formatted text string to hold file contents for downloading
            report_text = f"STUDENT REPORT CARD\n===================\nName: {name}\n\n"
            
            for i, score in enumerate(scores, 1):
                grade = get_letter_grade(score)
                st.write(f"**Assignment {i}:** {score} / 100 ({grade})")
                st.progress(score / 100) # Visual progress tracking bar
                report_text += f"Assignment {i}: {score}/100 ({grade})\n"
            
            avg_score = sum(scores) / len(scores)
            final_grade = get_letter_grade(avg_score)
            
            st.markdown("---")
            st.write(f"📈 **Overall Average Score:** {round(avg_score, 2)}")
            st.write(f"🎓 **Final Grade:** {final_grade}")
            
            report_text += f"\n-------------------\nOverall Average: {round(avg_score, 2)}\nFinal Grade: {final_grade}"
            
            # Download button integration
            st.download_button(
                label="📥 Download Report Card (.txt)",
                data=report_text,
                file_name=f"{name.replace(' ', '_')}_report.txt",
                mime="text/plain"
            )
        else:
            st.info(f"No scores found for {name}.")

elif menu == "5. Shutdown Analytics Engine":
    st.subheader("SHUTDOWN ENGINE")
    st.error("The Analytics Engine session has been paused. Select another protocol or refresh the page to restart operations.")
    st.stop()

elif menu == "5. Shutdown Analytics Engine":
    st.subheader("SHUTDOWN ENGINE")
    st.error("The Analytics Engine session has been paused. Select another protocol or refresh the page to restart operations.")
    st.stop()
    
st.write("---")
st.caption("Built by Batool Fatima | BCA 2026-29 | Akshara Degree College")
