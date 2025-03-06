import streamlit as st

st.set_page_config(page_title="Account Setup", page_icon="🔒")

st.title("Working Copy Setup")
st.markdown("---")

st.write(
    "The checkout commands done below put the checked-out directories in your home directory. "
    "Put the checked-out directories in another directory if you prefer."
)
st.write(
    "The directories *cs23001* and *shared* should be in the same directory, i.e., in your home directory."
)

st.header("Checkout your Working Copy")
st.write("This only needs to be done once (for your UNIX account).")
st.write("If you already have a directory named *cs23001*, rename it before you do the checkout:")
st.code("mv cs23001 cs23001_old")
st.write("Note that you cannot copy or move entire directories from an old working copy to a new one.")
st.write(
    "In the commands that follow, the `#` and any characters that follow it are comments, like `//` in C++. "
    "You don't need to type the comments."
)
st.write("Checkout your working copy, replace `USERNAME` with your Kent State username.")
st.code("cd                     # Go to your home directory")
st.code("svn co http://svn.cs.kent.edu/courses/cs23001/svn/USERNAME cs23001")
st.write("This will give you a working copy named *cs23001*.")
st.write(
    "If you omit the *cs23001* in the command, the checkout will give you a working copy that is named after your "
    "username."
)
st.write("You can use a web browser to see your repository directory:")
st.markdown(
    "[http://svn.cs.kent.edu/courses/cs23001/svn/USERNAME](http://svn.cs.kent.edu/courses/cs23001/svn/USERNAME)"
)

st.header("Instructor Provided Material")
st.write("Material will be provided in a *shared* repository for the labs.")
st.write("You can check out a working copy of the provided material.")
st.write("This only needs to be done once (for your UNIX account).")
st.write("If you already have a directory named *shared*, either rename or delete it before you do the checkout:")
st.code("mv shared shared_old   # Rename")
st.code("rm -rf shared          # Delete")
st.write("Do the checkout:")
st.code("cd                     # Go to your home directory")
st.code("svn co http://svn.cs.kent.edu/courses/cs23001/svn/shared")
st.write("When additional material is provided or changes are made, you will need to do an update in your working copy:")
st.code("cd                     # Go to your home directory")
st.code("cd shared")
st.code("svn update             # Make the working copy match the repository")
st.write("The material may be seen at:")
st.markdown(
    "[http://svn.cs.kent.edu/courses/cs23001/svn/shared](http://svn.cs.kent.edu/courses/cs23001/svn/shared)"
)
