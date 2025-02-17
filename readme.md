[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18235804&assignment_repo_type=AssignmentRepo)
# 404B Lesson 4 Class Project - Activity Suggestions

## Instructions

### Split VS Code Window

You can drag `main.py` tab to the right side of the window to split the window into two panes. This will allow you to see the instructions and the code at the same time.

### Answering

You can answer the questions by writing your answers in the `main.py` file.

You can run the code by clicking the `Run` button on the top right corner of the editor.

The output will be shown in the `Terminal` tab at the bottom of the editor.

## Before We Start

### Bored API

We will be using a free web service (API) that provides random activity suggestion for bored people.

For example, visiting this link: <https://bored.api.lewagon.com/api/activity>,
you should see similar response like:

```json
{
    "activity":"Invite some friends over for a game night",
    "type":"social",
    "participants":4,
    "price":0,
    "link":"",
    "key":"6613428",
    "accessibility":0.2
}
```

We can also specify the type of activity in the link: <https://bored.api.lewagon.com/api/activity?type=recreational>.

Should give you response of type 
`recreational` only:

```json
{
    "activity":"Do a jigsaw puzzle",
    "type":"recreational",
    "participants":1,
    "price":0.1,
    "link":"https://en.wikipedia.org/wiki/Jigsaw_puzzle",
    "key":"8550768",
    "accessibility":1
}
```

You may explore more in the documentation: <https://bored.api.lewagon.com/documentation>.

As you explored this API, you should have noticed the response format is a lot like the dictionary format in Python. This is a very common format used in data transfer between web/app and server.

## To Get Started

Run the following command in the terminal to install required libraries:

for Mac:

```bash
pip3 install requests
pip3 install pprint
```

for Windows/Linux:

```bash
pip install requests
pip install pprint
```

## Your Task

Write a program that accepts user input and provide random activity suggestion base on that input. The response should be printed in a readable format.

### Sample Input

```diff
Don't know what to do?
Pick a number below and I will suggest something for you:

    0: education
    1: recreational
    2: social
    3: diy
    4: charity
    5: cooking
    6: relaxation
    7: music
    8: busywork
    9: no preference
    
4 ↩
```

### Sample Output

```diff
You may donate blood at a local blood center?
This could be helpful: <https://www.redcross.org/give-blood>
```

## Submitting Your Work

1. Make sure the assignment repository is opened in VS Code.

2. Make sure you have completed all the tasks.

3. (First time only)
Use Command + J to open the Terminal tab and config your git username and email:

    ```bash
    git config user.name "Your Name"
    git config user.email "Your GitHub Email"
    ```

4. Click on the "Source Control" icon on the left. Source Control

    ![1](https://github.com/BlueinnoClassroom/404B-L2.1-Template/assets/155412668/2c31026e-c14d-484f-bb9e-dc87189a0216)

5. Enter a commit message and click on the "Commit" button.

6. Click on the "Sync Changes" button.
