import streamlit as st

st.set_page_config(page_title="Lab Policies", page_icon="🖥️")

st.title("CSII Lab Policies")
st.subheader("Spring 2025")
st.markdown("---")

st.header("Lab Attendance")
st.write("Students are required to attend lab meetings.")
st.write("Assignments will not be accepted from those who don't participate in the lab. This includes attendance.")
st.write("Attendance is *mandatory*.")

st.header("Turning in Assignments")
st.write("A version control system will be used to turn in assignments (programs and any other required files).")
st.write("All assignments must be put in the version control system's repository.")
st.write("Students are responsible for making sure that their work is in the repository.")
st.write("Work not in the repository will not be accepted.")
st.write(
    "Code that is not committed cannot be counted. There is no way for the instructor to see code that is not "
    "committed.")

st.header("Grading")
st.write("Grading for the lab will come in two components:")

st.subheader("1. Lab Participation")
st.write("A score of 0 - 10 will be given for each lab.")
st.write("Lab scores are based on lab attendance, the assignment, and an occasional quiz.")
st.write(
    "**Before you leave the lab you must show the lab instructor you have completed or made significant progress on "
    "the assignment.**")
st.write("If you do not finish the assignment, show your lab instructor what you have done before you leave.")
st.write("The lab quiz grades will be graded separately, but are worth ~20% of the overall lab grade.")

st.subheader("2. Project Scores")
st.write("Projects are broken into sub-parts.")
st.write("Each sub-part is worth a specified number of points, as specified in the project assignment document.")
st.write("Each sub-part is graded and scored.")

st.subheader("Grading System")
st.write("1. Grades for your project parts will be submitted to the EVAL folder in your version control.")
st.write("2. Check your EVAL folders regularly.")
st.write(
    "3. We will leave comments after we've graded your assignments, giving you an idea of why you received the score "
    "we gave you.")

st.header("Project Due Dates")
st.write("Project parts are due by the time specified on the project assignment pages.")

st.header("Regrade Policy")
st.write("**Regrades must be requested via Discord post ONLY in the #regrade-requests channel.**")
st.write(
    "To be eligible for a regrade, a reasonable attempt on the milestone must have been made and committed to "
    "subversion by the due date.")
st.write("There is only one regrade request per milestone.")
st.write("After initial milestone grade, there is a one-week period to request a regrade.")
st.write("Regrades incur a flat 10% off. This means the highest possible score from a regrade is 90%.")
st.write("If a request was made and the code is not noticeably better, you will lose 5% off your current grade.")
st.write(
    "Regrades **MUST** follow the format specified in the Discord Server. Any deviation will result in the regrade "
    "not being processed.")

st.header("Compiling")
st.write("All programs must compile on the CS Department's machines `WASP` or `HORNET`.")
st.write(
    "When a lab instructor is grading the labs, the instructor will not spend time fixing programs that do not compile.")
st.write(
    "There will be a large point deduction for programs that do not compile, and they will not otherwise be graded.")
st.write("Depending on deadlines you may get some points back if you fix your program (see regrade section).")

st.header("Additional Notes")
st.write("- If you have compiling problems, talk to your lab instructor.")
st.write("- It is your responsibility to make sure your code in the repository compiles. When in doubt - recompile.")
st.write("- It is easy to make a mistake in a small change and cause your program to not compile.")
st.write("- Don't hesitate to contact your lab instructor if you have any problems or questions.")

st.header("Plagiarism")
st.write(
    "Plagiarism of any type will not be tolerated and will be dealt with in accordance with Kent State University's "
    "policy on cheating and plagiarism described in the student handbook.")
st.write("See your lecture instructor's syllabus for plagiarism details.")
st.write(
    "Students may discuss programming assignments with each other - however, each student must write their own program.")
st.write(
    "It is not permitted to copy, in any manner, assignment-related material (except material provided by the "
    "instructor).")
st.write("You should understand and be able to explain any and every part of any assignment you turn in.")
