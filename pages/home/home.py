import streamlit as st
import pandas as pd

st.set_page_config(page_title="Computer Science II", page_icon="🖥️")

st.title("CS 23001 Computer Science II")
st.write("## Data Structures & Abstraction | Spring 2025")
st.markdown("---")

st.markdown("#### Instructor: [Prof. Jonathan Maletic](https://www.cs.kent.edu/~jmaletic/)")
st.write("#### [Office Hours](https://www.cs.kent.edu/~jmaletic/office-hours.html)")
st.write("**Lecture & Location:**")
st.write("- **MW 2:15 - 3:30pm** - SMH 110")

st.write("**Lab Location:**")
st.write("- **162 MSB**")

st.header("Exams")
st.write("- **Exam 1:** Week of **February 17th** during Lab")
st.write("- **Exam 2:** Week of **March 24th** during Lab")
st.write("- **Final Exam:** Thursday **May 8th, 12:45 - 3:00pm** in labs (**MSB 162, 139, 274**) ")

st.header("Course Materials")
st.page_link("pages/home/syllabus.py", label="Syllabus")
st.page_link("pages/home/topics.py", label="Topics for each Lecture")
st.page_link("pages/home/calendar.py", label="Schedule and Calendar")

st.header("Announcements")
st.write("- All course communication will be done via a **CSII Discord server**. See the announcement in **Canvas** for an invite link.")
st.write("- **Change your nickname** on this server to your real name. We will not answer anyone using an alias.")

st.header("Course Information")
st.write("- **ALL COURSE COMMUNICATION** will be done using the course **Discord server**.")
st.write("- **Office hours** will be conducted on **Discord and in person**.")
st.write("- You can **ask and answer questions** about the lecture, labs, and assignments on Discord.")
st.write("- Please **change your nickname** on this server to your real name. We will not answer anyone using an alias.")
st.write("##### Lecture Format")
st.write("  - Instructor typing code (in an IDE)")
st.write("  - Explaining code (via slides, board, etc.)")
st.write("  - Answering questions")
st.write("  - **Lecture slides** are available on **Canvas**.")

st.header("Resources")
st.write("- Computer Science tutoring [schedule](https://www.kent.edu/cs/tutoring-undergraduate-cs-courses)")
st.write("- **Lab Instructors (contact via Discord):** Eduardo Jirón Alvarado, Joshua Behler, Xinyu (Bruce) Li")
st.page_link("pages/assets/resources.py", label="Additional Resources")

st.header("Lab Sections | 162 MSB ")
data = [
    ["001", "Tue", "12:05pm - 01:45pm", "Eduardo"],
    ["002", "Thu", "12:05pm - 01:45pm", "Eduardo"],
    ["003", "Tue", "04:25pm - 06:05pm", "Josh"],
    ["004", "Fri", "12:05pm - 01:45pm", "Josh"],
    ["005", "Wed", "04:10pm - 05:50pm", "Josh"]
]

df = pd.DataFrame(data, columns=["Section", "Day", "Time", "Instructor"])
st.dataframe(df, hide_index=True)

st.header("Project Due Dates")

st.subheader("Project 1")
st.write("- **Milestone 1 Due:** Monday **Feb 3** - 9:00am")
st.write("- **Milestone 2 Due:** Monday **Feb 10** - 9:00am")
st.write("- **Milestone 3 Due:** Monday **Feb 17** - 9:00am")

st.subheader("Project 2")
st.write("- **Milestone 1 Due:** Monday **Feb 24** - 9:00am")
st.write("- **Milestone 2 Due:** Monday **Mar 3** - 9:00am")
st.write("- **Milestone 3 Due:** Monday **Mar 17** - 9:00am")
st.write("- **Milestone 4 Due:** Monday **Mar 24** - 9:00am")

st.subheader("Project 3")
st.write("- **Milestone 1 Due:** Monday **Mar 31** - 9:00am")
st.write("- **Milestone 2 Due:** Monday **Apr 7** - 9:00am")
st.write("- **Milestone 3 Due:** Monday **Apr 14** - 9:00am")

st.subheader("Project 4")
st.write("- **Milestone 1 Due:** Monday **Apr 21** - 9:00am")
st.write("- **Milestone 2 Due:** Monday **Apr 28** - 9:00am")
st.write("- **Milestone 3 Due:** Wednesday **May 7** - 3:00pm (**No regrades**) ")