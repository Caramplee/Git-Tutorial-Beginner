#Command for git

git -v # checking the version or checking whether environment variable reaches git.exe or not

#name your git

git config --global user.name "Caramlplee"
git config --global user.email "megabiskit"
git config --global user.country "Thailand"

git config --list #<<< check all information in this directory

# can be anything after global to specify coder detail

# git commit staging 

git log #<< check the commit history

    bonus : gitlog --oneline #<<< will show all commit history in one line

git status #<< check what file has been modified or staged for commit

git add .   #<< stage all modified files

    bonus : # <<. mean add all the file if want to specify the file type the name

git commit -m "Message for commit title"

# move through commit file.

git restore . # << restore all file in the previous commit (discard all changes)
git restore "file name or press tab" #<< restore specify file

git reset --soft HEAD~1 # << soft reset keep changing in stage
git reset HEAD~1 # << keep chanes in working directory
git reset --hard HEAD~ #<<< hard reset deletes uncommited work

# gitignore

create file .gitignore 