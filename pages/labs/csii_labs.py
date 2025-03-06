import streamlit as st

st.set_page_config(page_title="Labs", page_icon="🖥️")

st.title("Computer Science II Labs")
st.subheader("Spring 2025")
st.markdown("---")

st.header("Lab Exams")
st.write("**Exam 1:** The week of February 17th")
st.write("**Exam 2:** The week of March 24th")

st.header("Weekly Labs")
st.write("Lab work is due the day before the next meeting at the end of the day.")

# TO-DO: Optimize
labs = [
    ("Lab 1", "Getting Started"),
    ("Lab 2", "UNIX Development"),
    ("Lab 3", "Testing I"),
    ("Lab 4", "File I/O"),
    ("Lab 5", "Debugging I"),
    ("Lab 6", "Object Creation and Destruction"),
    ("Lab 7", "Testing II (Optional - 5 pts. extra)"),
    ("Lab 8", "Recursion"),
    ("Lab 9", "Linked Lists and Generics"),
    ("Lab 10", "Infix Expressions"),
    ("Lab 11", "Debugging II"),
    ("Lab 12", "Profiling"),
    ("Lab 13", "Binary Trees"),
]

for i, (label, description) in enumerate(labs):
    col1, col2 = st.columns([1, 6])
    with col1:
        st.page_link(f"pages/labs/lab_{i+1}.py", label=label, icon="🖥️️")
    with col2:
        st.write(description)


st.header("Lab Instructors")
st.write("**Eduardo Jirón Alvarado** - [ejironal@kent.edu](mailto:ejironal@kent.edu)")
st.write("Office Hours: Online - Tuesday, Thursday 10:00 - 12:00. In-person on request.")
st.write("**Joshua Behler** - [jbehler1@kent.edu](mailto:jbehler1@kent.edu)")
st.write("Office Hours: In-person - Monday 10:00-12:00, Tuesday 2:00 - 4:00. Online on request.")

st.header("Lab Info")
st.page_link("pages/labs/policy.py", label="Lab Policies", icon="🔗")
st.page_link("pages/assets/requirements.py", label="Program Requirements", icon="🔗")
st.page_link("pages/labs/account_setup.py", label="Account Setup", icon="🔗")

# TO-DO: Implement pages
st.header("Resources")
st.markdown("- [Editing Environment](https://data-structures.cs.kent.edu/labs/Info/editor-guide.html)")
st.markdown("- [Unix Commands](https://data-structures.cs.kent.edu/labs/Info/unix_files.html)")
st.markdown("- [cs23001 Shared Repository](https://svn.cs.kent.edu/courses/cs23001/svn/shared/)")

