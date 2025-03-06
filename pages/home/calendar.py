import streamlit as st

st.set_page_config(page_title="Calendar", page_icon="📅️")

st.title("CS 23001 Calendar | Spring 2025")
st.markdown("---")

calendar_url = "https://calendar.google.com/calendar/embed?showPrint=0&mode=AGENDA&height=600&wkst=1&bgcolor=%23FFFFFF&src=kent.edu_msqtrf4krrubs9rtd4d8pgh8jo@group.calendar.google.com&color=%236B3304&ctz=America/New_York"
st.markdown(
    f'<iframe src="{calendar_url}" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>',
    unsafe_allow_html=True
)

st.markdown("You can subscribe to this calendar from [Google Calendars](http://www.google.com/calendar/) or via the [iCal address](https://www.google.com/calendar/embed?src=kent.edu_msqtrf4krrubs9rtd4d8pgh8jo%40group.calendar.google.com&ctz=America/New_York).")

st.header("Important Dates")
st.markdown("**Lab Start:** First week of courses, January 13th")

st.subheader("Exams")
st.markdown("- **Exam 1:** Week of February 17th")
st.markdown("- **Exam 2:** Week of March 24th")
st.markdown("- **Final Exam:** Thursday, May 8th, 12:45 - 3:00 PM")

st.subheader("No Lectures")
st.markdown("- **January 20th:** Martin Luther King Jr. Day")
st.markdown("- **Week of March 10th:** Spring Break")

st.subheader("No Lab")
st.markdown("- **Week of March 10th:** Spring Break")
