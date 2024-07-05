# TaskTracker
 
## Purpose:
- Creates a window that allows one to create task boxes to list tasks.
- Has an option to delete tasks or list all completed tasks.

## **Installation**
### Requirements:
* Visual Studio Code
* Python 3.7
* venv
* Pyside6

### Instructions: 

#### Git Clone
1. In VSCode, press CMD + SHIFT + P to input commands
2. Search and select "Git: Clone" and click "Clone from GitHub"
3. Authorize account if prompted
4. When prompted for repository name, search for "TaskTracker"
5. Create new folder in desired location, and direct the repository to it

#### Virtualenv Setup
1. Ensure your VSCode is configured for Python 3.7
1. In VSCode's terminal, run `$ python -m venv .venv` to create a virtual environment
2. Visit [here](https://www.python.org/downloads/release/python-379/) and download the windows excecutable file or macOS file
3. Bring this file to your cloned directory, and run `$ pip install {File Name}`
4. To install the rest of the packages, run `$ pip install -r requirements.txt`

### To run:
1. If files python files aren't generated, use pyside6-uic to generate py files and use this repo as guideline for structure of workspace
2. Run main.py
