import streamlit as st

st.set_page_config(page_title="Servers and Submission", page_icon="💾")

st.title("Linux Servers and Project Submission")
st.subheader("CS 23001")
st.markdown("---")

st.write("All assignments must compile and run on the departmental servers (Wasp/Hornet):")
st.code("wasp.cs.kent.edu")
st.code("hornet.cs.kent.edu")

st.write("Log into these machines using your Flashline ID and password. There are a number of clients you can use to "
         "log into these machines: ")
st.write("- `ssh` - installed on Mac and Windows")
st.write("- [PuTTY](https://www.putty.org/)")
st.write("- Secure Shell App in Chrome Extension")
st.write("- [MobaXterm](https://data-structures.cs.kent.edu/(https://mobaxterm.mobatek.net/))")

st.markdown("---")

st.write("#### Project Submission")
st.write("All assignments must be committed to the course subversion (svn) repository for submission and grading. "
         "Subversion is a version control system (git is another version control tool) that is used for storing and "
         "working on software. All grading and assignment submission will be done using svn and your repository. Your "
         "subversion repository (folder) for the course is located at the following URL (replace USERNAME with your "
         "account name):")
st.code("https://svn.cs.kent.edu/courses/cs23001/svn/USERNAME/")

st.write("To checkout this repository into your home directly in a folder called cs23001 as follows:")
st.code("svn --username USERNAME checkout https://svn.cs.kent.edu/courses/cs23001/svn/USERNAME/ cs23001")

st.write("All the files in the repo folder USERNAME will be in a local folder called cs23001/ in your home directory.")
st.write("A shared folder (`shared/`) is also in the repository. Check this out in your home directory. Data files, "
         "example code, and other course related information will be posted there.")

st.code("svn --username USERNAME checkout https://svn.cs.kent.edu/courses/cs23001/svn/shared/")
st.write("Clicking the link above for shared will pull up the folder contents in the web browser.")

st.markdown("---")

st.write("#### Installing Subversion")
st.write("If you want to use svn on your personal machine you will most likely need to install subversion.")

st.write("**MS Windows:**")
st.write("- [TortoiseSVN](http://tortoisesvn.net/) is a nice interface for subversion.  This is a client for MS "
         "Windows and integrates into the file systems.")
st.write("- You can also install [WSL 2](https://docs.microsoft.com/en-us/windows/wsl/install-win10) on your Windows "
         "machine. This is a Linux (typically Ubuntu) subsystem for Windows. You will also need to install the "
         "software you need (e.g., compiler, subversion, etc.). This will give you a development environment much the "
         "same as Wasp/Hornet.")

st.write("**MacOS**")
st.write("- Recent versions of MacOS do not have svn installed. First, you need Xcode installed (this is Mac's IDE). "
         "If it is not already installed go to the app store for Xcode. The best way to install subversion is using "
         "[Homebrew](https://brew.sh/).")
st.write("- Follow the instructions and install brew. Then after Homebrew is installed you can install subversion "
         "with the following command (in Terminal):")
st.code("brew install subversion")

st.markdown("---")

st.write("#### Using Subversion")
st.write("Complete information about Subversion can be found in the book [Version Control with Subversion]("
         "http://svnbook.red-bean.com/).")
st.write("- A [tutorial](http://www.youtube.com/watch?v=KUXGKxFSxHQ&feature=related) at YouTube on using subversion")
st.write("- There is a set of slides explaining svn in the shared folder in svn.")

st.markdown("")

st.write("Your source code repository can be accessed via the check out command svn checkout. Use your user name for "
         "USERNAME below. It will create a cs23001 folder and you will need to go into that folder and do an update. "
         "You can also check out the shared folder in the same place. Below are the commands to check out your "
         "repository into your home directory on Wasp/Hornet or personal machine.")
st.code("""
#svn --username USERNAME checkout https://svn.cs.kent.edu/courses/cs23001/svn/USERNAME/ cs23001
#cd cs23001
#svn update

#svn --username USERNAME checkout https://svn.cs.kent.edu/courses/cs23001/svn/shared/
#svn update
""")
st.write("Normally, you only check out your repository once (per machine). For example, you check it out on your "
         "laptop and on your department account. Doing this will give you two working copies of your repository. "
         "Before you start working on your files (for the day or a session) do svn update. This makes sure that your "
         "local working copy is up to date with any changes you may have made (from another working copy). After you "
         "make changes to your files you commit them to the repository with svn commit. It's preferable to commit "
         "after you made any major change or addition. This way nothing is ever lost and you can roll back to a "
         "previous version if necessary. If you did this work from you laptop (using MS visual studio for example) "
         "you can sign into your department account and do svn update. Now your working copy there will reflect the "
         "changes you committed previously.")
st.write("Remember to:")
st.write("1. **ALWAYS** update before you start working.")
st.write("2. **ALWAYS** commit after changes.")

st.markdown("---")

st.write("#### Essential Subversion Commands")

import streamlit as st

st.markdown("""##### **Checking Out a Working Copy**
```sh
svn checkout http://www.foo.edu/svn/oop/username
svn co http://www.foo.edu/svn/oop/username
```
Checks out a working copy from the repository. Normally, do this only once or 
when something is messed up and you need a fresh copy from the server.

##### **Updating Your Working Copy**
```sh
svn update
```
Brings your working copy up-to-date with the server repository. Any changes made in the 
repository are put into your working copy. Always do this before you start working on a file (or repo).

##### **Adding Files to Version Control**
```sh
svn add filename
```
Puts the file `filename` under control of the versioning system. Do this once when you create a new file or folder.

##### **Committing Changes**
```sh
svn commit -m "Added new method."
svn ci -m "Added new method."
```
Commits the changes that you have made to the working copy to the server repository with a comment. Do this every time you stop working on a file.

##### **Checking Status**
```sh
svn status
```
Gives the status of all files in the current versioned directory/folder. Indicates if files are under version control or modified.
- `?` - File is not under version control. You may have forgotten to do an `svn add`.
- `M` - File is modified. You will need to do a commit.

##### **Deleting Files**
```sh
svn delete filename
```
Deletes the file `filename`. Only occurs in the working copy, i.e., must be committed to show up in the repository.

##### **Moving or Renaming Files**
```sh
svn mv oldfilename newfilename
```
Changes the name of a file from `oldfilename` to `newfilename`. Only occurs in the working copy, i.e., must be committed to show up in the repository.

##### **Creating a New Directory**
```sh
svn mkdir directory_filename
```
Creates a new directory with the name `directory_filename`. Only occurs in the working copy, i.e., must be committed to show up in the repository.

##### **Renaming a Directory**
```sh
svn mv old_directory new_directory
```
Changes the name of the directory from `old_directory` to `new_directory`. Make sure to commit any work and perform an update first to avoid problems. Only occurs in the working copy, i.e., must be committed to show up in the repository.

##### **Viewing Log History**
```sh
svn log filename
```
Presents information about the various versions of `filename`. Can be used to find the version number that corresponds to a version that you may want.

##### **Reverting to a Previous Version**
```sh
svn update filename -r####
```
If you want to move back to a previous version, use `update` with the `-r` option. Get the version number from `svn log filename` and replace `####` with it.
""")
