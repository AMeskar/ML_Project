## End-to-End ML Project ##

# Agenda

1. Set up the GitHub repository and link it to your VS Code project so you can push your code directly.

```bash
- git init
  # Initializes a hidden .git folder to track your code version history

- git add README.md
  # Adds the README file to the staging area

- git commit -m "My First Commit"
  # Creates a commit with a message describing the change (-m is for message)

- git config --global user.email "Meskar192@gmail.com"
  git config --global user.name "AMeskar"
  # Identifies yourself to Git for the first time (this is global)

- git status
  # Shows the current state of your working directory (what's staged, what’s not)

- git branch -M main
  # Renames your current branch to 'main' (forcefully with -M)

- git remote add origin "url"
  # Links your local VS Code project to your GitHub repository

- git push -u origin main
  # Pushes your code to GitHub, and -u sets the upstream so future pushes are easier


2- Seting the environments == Python 3.8
{
 - conda create -p venv python==3.8 -y : conda create an enviroment called venv in the path (-p) for python verison 3.8
 - conda activate venv/ : its important to end by /
}

3- create setup.py and requirements files

