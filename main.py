import streamlit as st

# Home Page
csii = st.Page("pages/home/home.py", title="Computer Science II")
syllabus = st.Page("pages/home/syllabus.py", title="Syllabus")
topics = st.Page("pages/home/topics.py", title="Topics")
calendar = st.Page("pages/home/calendar.py", title="Calendar")

# Student Assets
requirements = st.Page("pages/assets/requirements.py", title="Requirements")
resources = st.Page("pages/assets/resources.py", title="Resources")
svn = st.Page("pages/assets/svn.py", title="Servers and Submission")
grading = st.Page("pages/assets/grading.py", title="General Program Requirements")

# Projects Page
project_1 = st.Page("pages/projects/project_1.py", title="Project 1")
project_2 = st.Page("pages/projects/project_2.py", title="Project 2")
project_3 = st.Page("pages/projects/project_3.py", title="Project 3")
project_4 = st.Page("pages/projects/project_4.py", title="Project 4")

# Labs Page
labs = st.Page("pages/labs/csii_labs.py", title="Computer Science II Lab")
policy = st.Page("pages/labs/policy.py", title="Labs Policy")
lab_1 = st.Page("pages/labs/lab_1.py", title="Lab 1")
lab_2 = st.Page("pages/labs/lab_2.py", title="Lab 2")
lab_3 = st.Page("pages/labs/lab_3.py", title="Lab 3")
lab_4 = st.Page("pages/labs/lab_4.py", title="Lab 4")
lab_5 = st.Page("pages/labs/lab_5.py", title="Lab 5")
lab_6 = st.Page("pages/labs/lab_6.py", title="Lab 6")
lab_7 = st.Page("pages/labs/lab_7.py", title="Lab 7")
lab_8 = st.Page("pages/labs/lab_8.py", title="Lab 8")
lab_9 = st.Page("pages/labs/lab_9.py", title="Lab 9")
lab_10 = st.Page("pages/labs/lab_10.py", title="Lab 10")
lab_11 = st.Page("pages/labs/lab_11.py", title="Lab 11")
lab_12 = st.Page("pages/labs/lab_12.py", title="Lab 12")
lab_13 = st.Page("pages/labs/lab_13.py", title="Lab 13")

# Navigation
pg = st.navigation(
    {
        "Home": [csii, syllabus, topics, calendar],
        "Assets": [requirements, resources, svn],
        "Projects": [project_1, project_2, project_3, project_4],
        "Labs": [labs, policy, lab_1, lab_2, lab_3, lab_4, lab_5, lab_6, lab_7, lab_8, lab_9, lab_10, lab_11, lab_12, lab_13]
    }
)

pg.run()
