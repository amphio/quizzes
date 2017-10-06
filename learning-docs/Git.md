# Git
<hr>
## Concepts

### Version Control System (VCS):
* Allows developers to work simultaneously.
* Does not allow overwriting each other’s changes.
* Maintains a history of every version

<br>
Following are the types of `VCS`:

* **Centralized version control system (CVCS)** – everything stored in one place
 
* **Distributed/Decentralized version control system (DVCS)** – distributed 
    * Every checkout is a backup 
    * Stored locally so you can work offline

###Git = DVCS

<img width="354" alt="screen shot 2017-10-05 at 11 42 51" src="https://user-images.githubusercontent.com/26869008/31223599-c0fd91a0-a9c2-11e7-9557-47c091401bb3.png">

**Workflow** – working directory (holds the actual files) –> Index (staging area) –> HEAD (points to last commit you made)

<img width="838" alt="gitworkflow" src="https://user-images.githubusercontent.com/26869008/31222316-9867a0f4-a9be-11e7-9297-0b51c15e3282.png">

###Branches
Branches are used to develop features isolated from each other. 
The `Master branch` is the ‘default’ branch when you create a repo.
You can use other branches for development and merge them back to the master branch when finished.



## Commands

###Gettings started

**git init** creates a new Git repository

**git clone /path/to/repository** copies remote repository to local directory 

**git add <filename>** or **git add .** adds to the Index

**git commit -m “Commit message”** Commits file to the HEAD (but not remote repository yet)

**git push origin [branch name]** sends changes to remote repo

**git checkout -b feature_x** create new branch
git checkout master
git branch -d feature_x
git push origin [branch] – pushes to remote repo

**git pull** updated local repo to the newest commit

**pwd** path to working directory 

**touch <filename>** creates file in current directory

**ls -a** shows all hidden files

**git branch -r** shows remote branches 

**git log** show's history of pushed commits

**git bisect**  use binary search to find the commit that introduced a bug

**git merge** merges pushed changes to selected branch, always forward moving change record

**git rebase** similar to merging, but re-writing history. Rebasing is the process of moving or combining a sequence of commits to a new base commit. The primary reason for rebasing is to maintain a linear project history. *The golden rule of git rebase is to never use it on public branches*.

<img width="478" alt="gitrebase" src="https://user-images.githubusercontent.com/26869008/31228110-3225cada-a9d4-11e7-973a-35a190261966.png">

###Merging vs rebasing
Merging shows actual history of commits

Rebasing shows a cleaner, but not acurate representation of history

###Undo undo!

**git reset** a simple way to undo changes that haven't been shared with anyone else i.e. deleting commits from the HEAD *“Oh crap, everything I've done is terrible, I just want to start afresh”*

	--soft    The staged snapshot and working directory are not altered in any way

	--mixed   Default option, staged snapshot updated to match specified commit, working directory not affected.

	--hard    The staged snapshot and working directory are both updated to match the specified commit
	
	git reset --hard HEAD  Throws away all uncommited changes

<img width="517" alt="gitreset" src="https://user-images.githubusercontent.com/26869008/31273647-76c8b7e8-aa87-11e7-8a69-8fbb832f55b1.png">

**git checkout**  
	
	git checkout HEAD~2   Checkout the grandparent of current commit – good for checking an old version of project

**git revert** Reverting undoes a commit by creating a new commit.

**git stash** stashes away all your changes

###Fork a repo 
A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

