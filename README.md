# Git Install for Windows using CMD
winget install --id Git.Git -e --source winget





## verification
git --version





### git01-pull.sh

git checkout "main"
git fetch origin
git reset --hard origin/main
git branch -D "work_from_school"




### git03-branch+push.sh
if git show-ref --verify refs/heads/work_from_school; then
  git branch -D "work_from_school"
fi
git checkout -b "work_from_school"
git add .
git commit -m "My work from school"
git push -u origin "work_from_school"























# Reset the last commit to a clean state
git reset HEAD^
# Now add the file again, which will be tracked by LFS
git add personal-website/src/videoplayback.mp4
# Commit the changes again
git commit -m "Add videoplayback.mp4 using Git LFS"
# Push to the remote
git push





# Remove the file from the commit but keep it in your local directory
git rm --cached personal-website/src/videoplayback.mp4
# Re-add and commit your changes without the large file
git add .
git commit --amend --no-edit
# Push the fixed commit
git push










### git00-init.sh

git config --global user.name "okggff"
git config --global user.email "imageai317@gmail.com"
git clone "https://github.com/okggff/okggff.github.io.git" "myrepo"
git checkout "main"

