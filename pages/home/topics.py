import streamlit as st

st.set_page_config(page_title="Topics", page_icon="📄")

st.title("Course Schedule")

st.header("Lecture Topics")
lecture_topics = [
    "Introduction and Overview, Review, Chapter 1",
    "Abstract Data Types (ADTs) and the Class Construct, Chapter 2",
    "Classes, Objects, and ADTs",
    "Compiling, Software Testing, Identifier Naming",
    "Set ADT, Constructors, operator overloading, I/O, Chapter 2",
    "Set ADT, Test Cases",
    "String ADT, operator overloading",
    "String ADT, overloading, Assertions, Pre, Post conditions",
    "Pointers, Chapter 4",
    "Dynamic arrays, copy constructor, destructor",
    "Copy constructor, destructor, assignment, swap",
    "Generics, Templates, Chapter 6.1-2",
    "Stacks, Prefix, Postfix, Infix, Chapter 7",
    "Stacks, Stack algorithms",
    "Recursion, Chapter 9",
    "Queues, Chapter 8",
    "Linked lists, Chapter 5",
    "Linked lists Stack",
    "Linked lists Queue",
    "Double linked lists, Containers/Iterators, Chapter 3, 6.3",
    "Containers/Iterators",
    "Binary Trees, Chapter 10",
    "Binary Trees",
    "Binary Trees - node removal",
    "Discuss Project 4",
    "Backtracking and recursion",
    "Inheritance, exceptions, virtual, Chapter 14",
    "Review",
    "Final Exam",
    "Readings are from Main and Savitch"
]
for topic in lecture_topics:
    st.write(f"- {topic}")

st.header("Lab Topics (Weekly)")
lab_topics = [
    "Introduction to lab, setting up accounts, handing in assignments. Editing and Unix commands.",
    "make, svn, Unix commands",
    "Unit Testing",
    "File I/O",
    "Debugging",
    "Dynamic Memory - object creation and destruction",
    "Command line interface (CLI)",
    "Recursion",
    "Testing",
    "Linked lists",
    "Infix/Postfix/Prefix",
    "Profiling",
    "STL",
    "Project 4"
]

for topic in lab_topics:
    st.write(f"- {topic}")
