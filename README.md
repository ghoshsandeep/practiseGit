url- https://www.youtube.com/watch?v=uaeKhfhYE0U

git config --global user.name “[firstname lastname]”
git config --global user.email “[valid-email]”
To check your name and email
           --> git config --global user.email

To Edit the name and email
git config --global --edit --> IT will open an editor

git init
initialize an existing directory as a Git repository
 	
After initialize 
    to check the list --> ls
    to check all the file --> ls -a


git status
	show modified files in working directory, staged for your next commit

git add [file]
	add a file as it looks now to your next commit (stage)

git commit -m “[descriptive message]”
        commit your staged content as a new commit snapshot

git log
	show the commit history for the currently active branch


git checkout
       switch to another branch and check it out into your working directory

If you want to go to any old commit
       git checkout <commit hash code/branch name> --> It will revert all the changes done after this hash code commit

If you again wanted to go to the current original location then use 
git checkout master

To Create another branch 
Suppose you are on master branch and you wanted to create one new branch named "dev" then there is two way for this task
1 create a new branch
	git branch dev
		then checkout (move) to dev branch
	git checkout dev
2 Another way
 git checkout - b NewBranchName


Merging Concept
Suppose you have three branch
1 Main Branch is "Master" 
2 From Master branch I have created on "dev" branch
3 From dev branch I created another branch called "test" branch and also checkout to this branch.
4 Now I am on "test" branch . in this I have added one more file called "helper.py" and also committed
5 Now I wanted to merge all the changes of "test" branch to dev branch
6 for this requirement first checkout dev branch then merge the changes of test branch to dev branch
7 branchName_OnWhichYouWantedToMergeThechanges  > git merge test

Now create a Repository on Github . Suppose I have created a new repository named "practiseGit.git"
So command will be
git remote add origin https://github.com/ghoshsandeep/practiseGit.git

git branch -M main  -->   (I am also not very sure about this command) Seems it rename my local master branch to main branch
After this now run the following commands
git push -u origin master 
   It means that push to code to branch named "origin" and from local master branch

Suppose you have multiple branches on local system and now you wanted to push one of those branch to GitHub 
so first checkout to that branch suppose you wanted to push dev branch to GitHub

git checkout dev
git push -u origin dev
