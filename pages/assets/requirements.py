import streamlit as st

st.set_page_config(page_title="Requirements", page_icon="✏️")

st.title("General Program Requirements")
st.markdown("---")

st.write("The following are requirements that apply to all programs.")
st.write("Additional requirements will be given with a programming assignment.")
st.write(
    "Points may be deducted for requirements not fulfilled and for failure to follow good programming practices.")

# TO-DO: Change URL after Policy page implementation
st.header("Due Dates and Late Policy")
st.write("See [lab policy](https://data-structures.cs.kent.edu/labs/Info/lab_policy.html).")

st.header("Submission")
st.markdown("""
- Programs must run and compile with `clang++` on the department's computers (e.g., WASP).
- You must use the `clang++` option `-Wall`.
- **DO NOT** commit any object or executable files. These can be generated.
- Output must be readable and easy to understand.
- The contents of these folders will be copied over, by the grader, to the EVAL directory on the due date and used as your submission.
- You have read-only access to the EVAL folder.
- If you wish to submit your assignment late, you must contact the instructor/grader so they can copy your submission into EVAL.
- See the lab page for more details about folder and file names.
""")

st.header("Basic Requirements")
st.markdown("""
- A comment must be at the very top of each file with the following format:
  ```cpp
  /**
  * Firstname  Lastname
  * program_name
  * CS course_number
  */
  ```
- There must be a comment at the top of each program, after the initial comment, describing what the program does.
- The program body must include comments.
- The program must have the functionality described in the programming assignment.
- There is no debugging output from your programs.
- Your program does not have an infinite loop for any valid input.
- The program must produce correct results with any valid input.
  - Just because a program compiles does not mean it is correct.
  - Just because a program produces a correct result with 1 or 2 different inputs does not mean it is correct.
  - Test your program thoroughly to ensure that it performs correctly.
  - Even thorough testing does not guarantee a correct program.
- **All programs must compile and run on the CS Department's Computers.**
- All programs should follow good programming practices.
""")

st.header("Fundamental Good Programming Practices")
st.markdown("""
- *Use good indentation.*
  - Indentation is used so that blocks may be easily recognized. Two or four spaces per level is widely regarded as good.
- *Be consistent with indentation and indentation style.*
- *Separate subtasks by empty lines.*
  - To accomplish its task, a program or function often must perform a number of subtasks. Separate these with empty lines.
- *Include helpful comments.*
  - Precede each subtask with a comment that describes what the subtask does.
- *Define a variable right before its first use.*
- *Initialize a variable when it is defined.*
- *Use good variable names.*
- *Use constants.*
  - If a variable's value will not change, make it `const`.
- *Do not use line wrapping.*
  - Keep lines under 80 characters to maintain readability.
""")

st.header("Also")
st.markdown("""
- It is a good habit to not change the value of input variables.
- Separate the input of values, calculations, and the output of values.
- Pretend you are a user of your program and observe its output.
- Start with a minimal program, get it to compile and run, and add to it in small, incremental steps.
""")
