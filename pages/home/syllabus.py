import streamlit as st
import pandas as pd

st.set_page_config(page_title="Syllabus", page_icon="📄")

st.title("Syllabus")
st.subheader("Spring 2025")
st.write("**Department of Computer Science, Kent State University**")
st.write("**Instructor:** Prof. Jonathan I. Maletic")
st.write("[Office Hours](https://www.cs.kent.edu/~jmaletic/office-hours.html)")

st.markdown("---")

st.write("**Course Location:** 110 Smith Hall")
st.write("**Course Time:** MW 2:15pm - 3:30pm")
st.write("**Lab Location:** 162 Math and Science Building")

st.header("Course Description")
st.write("Advanced computer programming design, and development with a primary focus on data structures and "
         "abstraction using an object-oriented programming language.")

st.subheader("Prerequisites")
st.write("CS 13011 Computer Science I-A and CS 13012 Computer Science I-B (both with C or better)")
st.write("Pre/Co-requisite: CS 23022 Discrete Structures for Computer Science")

st.subheader("Text and Reference Books (Optional)")
st.write("- Data Structures and Other Objects Using C++, Main and Savitch, Addison Wesley")
st.write("- The C++ Programming Language, Stroustrup, B., Addison Wesley")
st.write("- [Course Website](https://data-structures.cs.kent.edu/)")

st.header("Course Objectives")
objectives = [
    "Continue developing a disciplined approach to problem solving methods and algorithm development.",
    "Provide a clear understanding of the concepts of abstract data types.",
    "To teach a number of the basic algorithms and data structures used in computer science.",
    "To teach the concepts of object oriented programming.",
    "To provide a foundation for further studies in Computer Science.",
    "On completion of this course, students must have a basic understanding of the concepts of abstract data types "
    "and object oriented programming methods. Data structures such as lists, stacks, queues, strings, and trees must "
    "be understood. The student will have working knowledge of the concepts of classes and objects, "
    "operator overloading, constructors, destructors, and generics. The concepts of dynamic data structures and "
    "recursion must be well understood."
]

for obj in objectives:
    st.write(f"- {obj}")

st.header("Learning Objectives")
st.write("Upon completion of the course students will be able to apply and compare the basic abstract data structures "
         "used in computer science. These include strings, sets, stacks, queues, lists, and binary trees. Students "
         "will understand and demonstrate their ability to construct abstract data types and solve problems using an "
         "object oriented programming language. This includes demonstrated understanding of recursion, dynamic memory "
         "management, generics, and operator overloading.")

st.header("Grading Criteria")
st.write("Grades are available via Canvas. Project feedback is in svn.")
grades = {
    "**Exam 1** (Week of Feb 17, during Lab)": "15%",
    "**Exam 2** (Week of March 24, during Lab)": "15%",
    "**Final Exam** (Thursday May 8, 12:45 - 3:00pm)": "35%",
    "**Projects** (4 projects, a part due each week)": "20%",
    "**Lecture participation** (attendance/in-class & online discussion)": "5%",
    "**Laboratory** (attendance, assignments, quizzes)": "10%"
}
for item, percentage in grades.items():
    st.write(f"- {item}: {percentage}")


st.header("Final Grading Scale")
data = [
    ["0%", "F", "0.00"],
    ["60%", "D", "1.00"],
    ["67%", "D+", "1.30"],
    ["70%", "C-", "1.70"],
    ["73%", "C", "2.00"],
    ["77%", "C+", "2.30"],
    ["80%", "B-", "2.70"],
    ["83%", "B", "3.00"],
    ["87%", "B+", "3.30"],
    ["90%", "A-", "3.70"],
    ["93%", "A", "4.00"]
]

df = pd.DataFrame(data, columns=["Scale", "Grade", "GPA"])
st.dataframe(df, hide_index=True)

st.write("#### Lecture")
st.write("Lecture involves problem solving and the instructor coding solutions. Slides are used to organize lecture "
         "however the bulk is live coding by the instructor. Lecture slides are provided on Canvas. The code done in "
         "lecture by the instructor is NOT provided. Students are expected to take notes on the code. The class "
         "participation grade is determined in part by attendance along with in class quizzes or assignments. "
         "Additionally, credit is given for participating in online discussion. These assignments are completed "
         "during the class period and handed in during class.No makeups for in-class assignments are given.")

st.write("#### Exams")
st.write("There are two exams during the term. The first is in the 6th week, before midterm. The second is in the "
         "10th or 11th week. These two exams are approximately one hour each and be done during part of lab. "
         "Additionally, there is a final exam during finals week as determined by the university. The final exam is 2 "
         "hours and 15 minutes. Exams are mainly short answer and require the student to write and read code. Example "
         "questions are provided.")

st.write("#### Projects")
st.write("There are four substantial projects given over the term. The projects are primarily completed outside of "
         "lab/lecture time. Some small aspects of the projects are addressed in lab.")
st.write("The projects are critical for learning to program in this course and must be attempted/completed to do well "
         "on the exams. Students are to work on these projects on their own. Getting help from the instructors, "
         "tutors, or peers is encouraged. However, copying projects from the web, GitHub, other students, "
         "or using ChatGPT is plagiarism. Students found to be copying on projects will be sanctioned according to "
         "university policies. This includes a zero grade on the project, formal reporting to the university, "
         "and/or plagiarism school.")
st.write("The requirement for these assignments are posted on the course web page. The projects are broken down into "
         "three to four parts each. Each part has its own due date and count as a percentage of the total project "
         "grade. Due dates for each part of the project are posted on the course website. The general topics of the "
         "programs will be:")
st.write("- Abstract Data Types & Classes")
st.write("- Dynamic Memory and Containers")
st.write("- Linked lists and templates")
st.write("- Dynamic Data Structures (Complex Pointers)")

st.write("#### Honors Students")
st.write("For each project there is an associated challenge. Honors students are required to complete this challenge. "
         "This involves a write up to address additional questions about the project and include implementing some "
         "more functionality on top of normal project requirements.")

st.write("#### Other Notes")
other_notes = [
    "Lecture is the student's responsibility, if class is missed; it is in the students best interests to get the "
    "notes from a fellow student. The instructor does not have slides or lecture notes to hand out.",
    "There will be no make up exams.",
    "There will be no make ups for in class assignments or quizzes.",
    "Please mute the sound on phones, lab tops, and other electronic devices.",
    "Any modifications to the syllabus will be made on this page and noted.",
    "This course was previously numbered CS 33001. It was changed to CS 23001 in Fall 2012. There was no change in "
    "content in the course due to this numbering change."
]

for item in other_notes:
    st.write(f"- {item}")

st.write("#### [Requirements and Announcements](https://www.kent.edu/ctl/university-approved-syllabus-statements)")
st.write("- Registration Requirement: The official registration deadline for this course can be found on the "
         "Registrars calendar . University policy requires all students to be officially registered in each class "
         "they are attending. Students who are not officially registered for a course by published deadlines should "
         "not be attending classes and will not receive credit or a grade for the course. Each student must confirm "
         "enrollment by checking his/her class schedule (using Student Tools in FlashFast) prior to the deadline "
         "indicated. Registration errors must be corrected prior to the deadline. Every class has its own schedule of "
         "deadlines and considerations. To view the add/drop schedule and other important dates for this class, "
         "go to the Students Tools and Courses tab in FlashLine and choose either View or Print Student Schedule. To "
         "see the deadlines for this course, click on the CRN or choose the Drop or Add a Course link and click on "
         "the green clock next to the course under Registration Deadlines.")
st.write("- The Student Survey of Instruction (SSI) are administered online via Flash Survey - via Flashline.")
st.write("- Kent State University is committed to inclusive and accessible educational experiences for all students. "
         "University policy 3342-3-01.3 requires that students with disabilities be provided reasonable "
         "accommodations to ensure their equal access to course content. If you have a documented disability and "
         "require accommodations, please contact the instructor at the beginning of the semester to make arrangements "
         "for necessary classroom adjustments. Please note, you must first verify your eligibility for these through "
         "Student Accessibility Services (contact 330-672-3391 or visit [SAS](www.kent.edu/sas) for more information "
         "on registration procedures).")
st.write("- University policy 3342-3-01.8 deals with the problem of academic dishonesty, cheating, and plagiarism. "
         "None of these will be tolerated in this class. The sanctions provided in this policy will be used to deal "
         "with any violations. If you have any questions, please read the policy or contact the instructor. For the "
         "University's complete policy on procedure on cheating and plagiarism go to [Administrative policy]"
         "(https://www.kent.edu/policyreg/administrative-policy-regarding-student-cheating-and-plagiarism).")
st.write("- Diversity statement: Kent State University is committed to the creation and maintenance of equitable and "
         "inclusive learning spaces. This course is a learning environment where all will be treated with respect and "
         "dignity, and where all individuals will have an equitable opportunity to succeed. The diversity that each "
         "student brings to this course is viewed as a strength and a benefit. Dimensions of diversity and their "
         "intersections include but are not limited to: race, ethnicity, national origin, primary language, age, "
         "gender identity and expression, sexual orientation, religious affiliation, mental and physical abilities, "
         "socio-economic status, family/caregiver status, and veteran status.")
st.write("- Land Acknowledgement Statement: We acknowledge that the lands of Kent State University were the previous "
         "homes of people who were removed from this area without their consent by the colonial practices of the "
         "United States government. Before removal, these groups created networks that extended from Wyoming to the "
         "Florida Coast and Appalachia and to the northern reaches of Lake Superior. These societies included people "
         "of the Shawnee, Seneca-Cayuga, Delaware, Wyandots, Ottawa and Miami. We honor their lives – both past and "
         "present – and strive to move beyond remembrance toward reflection and responsibility through honest "
         "accounts of the past and the development of cultural knowledge and community.")
st.write("- The University welcomes individuals from all different faiths, philosophies, religious traditions, "
         "and other systems of belief, and supports their respective practices. In compliance with University policy "
         "and the Ohio Revised Code, the University permits students to request class absences for up to three (3) "
         "days, per term, in order to participate in organized activities conducted under the auspices of a religious "
         "denomination, church, or other religious or spiritual organization. Students will not be penalized as a "
         "result of any of these excused absences. The request for excusal must be made, in writing, during the first "
         "fourteen (14) days of the semester and include the date(s) of each proposed absence or request for "
         "alternative religious accommodation. The request must clearly state that the proposed absence is to "
         "participate in religious activities. The request must also provide the particular accommodation(s) you "
         "desire. The request is then approved, or, approved with modification (a mutually agreeable alternative "
         "arrangement). For more information regarding this Policy contact the Student Ombuds (ombuds@kent.edu).")

st.write("#### Course Content")
st.write("**Abstract Data Types (ADTs) and Object Oriented Concepts:**")
st.write("- Definition of ADTs")
st.write("- Encapsulation and information hiding")
st.write("- Classes, methods, constructors, and destructors")
st.write("- Information hiding: Public, private, (and protected)")
st.write("- Operator overloading and polymorphism")
st.write("- Generics (templates)")

st.write("**Dynamic Memory Structures:**")
st.write("- Allocation and de-allocation of memory (new, delete)")
st.write("- Dynamic Arrays")
st.write("- Pointers, Linked Lists (insertion, deletion, etc.)")

st.write("**Abstract Data Structures & Algorithms:**")
st.write("- Array, multi-dimensional arrays records, files, strings")
st.write("- Lists, stacks, and queues, sets, bags, vectors")
st.write("- Containers and iterators")
st.write("- Infix, prefix, and postfix notations and conversion algorithms")
st.write("- Binary trees, binary search trees")
st.write("- Recursion: Design and implementation of recursive functions")
st.write("- Hashing and priority queues")
st.write("- Brief introduction to graphs & associated algorithms")

st.write("**Additional Topics:**")
st.write("- Multi-file programs, make")
st.write("- Testing and debugging techniques")
st.write("- Exception handling")


