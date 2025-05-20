## ENd To END ML Project ##

# Agenda

1- We set up the github {repository} ==> How to link it with your VS code project and then u can push ur code to the github directly

{

 - git init : intialize .git which is a hidden folder that track the version of you code eah time u commit
 - git add README.md 
 - git commit -m "My First Commit" : it create a message in your log file to track what change (.e.g. add), -m to make the message with need of text editor
 - git config --global user.email "Meskar192@gmail.com" & git config --global user.name "AMeskar" : Identifying urself for the firt time
 - git status : give u the status everything u changed
 -git brach -M main: rename ur branch to main and -M force this operation
 - git remote add origin "url": linking ur vs code codes project with git hub
 - git push -u origin main: every change u did in Vs code u can push it to the repository in github remotely, -u is upstream, further understanding in the futur

}

2- Seting the environments == Python 3.8
{
 - conda create -p venv python==3.8 -y : conda create an enviroment called venv in the path (-p) for python verison 3.8
 - conda activate venv/ : its important to end by /
}

3- create setup.py and requirements files

