# Git tips and tricks for Git noobs and boobs

### 1. Pushing new changes
So, you've done some excellent changes that you want to share with the world (well, everyone who has access to that repo). Firstly, well done! Secondly, open your terminal window and do the following:

	cd [directory that you are writing to e.g. Documents/Github/IOP-events]
	git status 
	git add .
	git commit -m ”I made x change”
	git pull (brings all other people’s changes down)
	git push (pushes your changes and other people’s changes to main repository)

You may get some `error message` about conflicts...

To solve this:<br>

	1. press "i"<br>
	2. write your merge message<br>
	3. press "esc"<br>
	4. write ":wq"<br>
	5. then press enter<br>

To avoid these error messages, try and remember to `git pull` before making any changes.

<hr>

### 2. Making your own branch

Typically, there will be different branches within your repo e.g. Develop, Staging and Live. 

It is good practice to create your own temporary branch for each new code changing mission you are on. This keeps any maverick changes you do out of the main branches, so dodgy alterations don’t get accidentally merged. It basically means you are free to relax and go wild without fear of repercussions (the dream). 

To see what branch you are in, head to terminal and type:

	git branch
	
To switch to (or **checkout**) another branch:

	git checkout [name of branch you want to checkout]
	
￼To create your very own branch:

	git checkout -b [name of branch you want to create]
	git push (gives you command to activate your new branch)
	copy given command and execute 

If you are happy with the changes you've made in your new branch, you'd probably like to merge these into one of the main branches and show everyone how great you are. Let's say, for this example, you have made a branch called `NewFeature` and you want to merge it to the `Develop` branch.

To merge NewFeature (your new branch) with Develop:

	add, commit and push any changes in NewFeature (see part 1)
	git checkout Develop (switches you to Develop branch)
	git status (check you haven’t got any uncommitted changes)
	git pull (make sure you have latest changes)
	git merge NewFeature
	git push

Then, you'll want to delete your new branch locally and remotely:

**Note: you must NOT be in the branch you want to delete**

Locally:
	
	git branch -d [branch_name]

Remotely:
	
	git push origin --delete [branch_name]

[Further reading on deleting branches](https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-both-locally-and-remotely)


### 3. Running localhost

If you want to build the app on your computer and try out any changes before pushing them, this is for you.
 
Get the full low-down [here](https://github.com/amphio/IOP-events)

1. Build your virtual environment:

		cd ./IOP-events/web_app 
		boot build-dev-n

2. Run the server on localhost:

		cd ./IOP-events/web_app/target
		node server

3. Comment out develop routing on build.boot

4. Uncomment out localhost routing

5. CHANGE BACK 3 & 4 BEFORE PUSHING ANY CHANGES


### Release notes

You've just pushed some fantastic new features and bug fixes through to Live, but before you sit back and bask in the glory of a job well done, you need to craft some release notes so that any interested soul can see what fantastic new things they have in store for them with this release. 

	1. Go to your repo on the Git site —> releases —> Draft a new release

Then add something that may look like this:

![screen shot 2017-11-06 at 17 16 42](https://user-images.githubusercontent.com/26869008/32454159-4f0bf8a8-c316-11e7-875e-ae341b5e61b2.png)

You want to do this **straight after pushing live**, this is to ensure that it links the commit number with the release notes.

Finally, send an email to the respective humans that need to know about the release.

### 5. Fun extras

If you are unsure what a terminal command means:

	man [command] 
	
This tells you all you need to know (hopefully).
