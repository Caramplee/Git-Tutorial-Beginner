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

db.sql # << specific file
password.txt # << specific file
*.log # << entire . log files
node_modules/ # entire working directory
!important.log # ignore specific file in *.log

# moving file or rename file

git rm # << remove file, but it will be staged so it is not permentely lost until commit
git rm --cached "filename" # << remove from git tracking, alternatively add filename to git ignored

#Command Description
git status #Show working tree status

git diff #Show unstaged changes

git diff --staged #Show staged changes

git restore [file] #Discard working directory changes

git restore --staged [file] #Unstage files

git reset --soft HEAD~1 #Undo last commit, keep changes staged

git reset HEAD~1 #Undo last commit, keep changes unstaged

git reset --hard #HEAD~1 Undo last commit, discard changes

git rm [file] # Remove file from repository

git rm --cached [file] #Stop tracking file

git mv [old] [new] #Rename/move file


# Branch

git branch #<<< check list of branch exists (main or master is a defult branch)
git switch -c "Filename" #<< create new branch and switch to that branch
git switch "File name" #<< move to named branch

git branch -d "Branch name" #<< remove branch (USE CAREFULLY!)

#merging branch

git merge "Name of the branch"

#merging conflict
# when 2 file develops differently it need to verified which version is used
git checkout --ours "filename" # <<< use our filename final version
git checkout --theirs "filename" #<<< use theirs filename as finalversion

# or resloved by yourself , open the conflict file to see the marker and reslove it
#finally git add "filename" and git commit 

#pushing (update file to github)

git remote add origin https://github.com/Caramplee/Git-Tutorial-Beginner.git #<<< this is the url of github repository
git branch -M main # change the name of the branch from master to main
git push -u origin main # push your code and file to github