# MAZE TEXT GAME
### Video Demo:  <https://youtu.be/TgwzuXTsVyc>
## Table of contents
* [General info](#general-info)
* [Usage](#usage)
* [FIles](#Files)
    * [mazegame.py](#mazegame.py)
    * [Maze.py](#Maze.py)
    * [params.py](#params.py)
    * [instructions.txt](#instructions.txt)
    * [instructions_rus.txt](#instructions_rus.txt)

## General info
This project is a game in which you need to find your way out of a procedurally generated maze with the help of text commands.

By default, the player can choose from 3 levels of difficulty, but this can be manually modified in the file [params.py](#params.py).

Additional challenge is introduced by not redrawing the map after every move, though the player can request to see the map with their current position at any moment.

## Usage

#### **Prerequisites**
*You will need to have Python installed to run the game*

For a full picture mode you will need to run the following command from the IDE ternimal:

```
$ python mazegame.py
```
Defaulf system terminal may not support the characters used to create the picture of the maze. If you decide to run the game from the system terminal, run one of the following commands:
```
$ python mazegame.py -l
```
or
```
$ python mazegame.py --line
```
In this case, walls will be shown as '#', paths as '_', player as 'u' and exit as 'e'

#


## Files
### **mazegame.py**
Main file of the project that does all the work, i.e. determines difficulty for the level, creates a maze object, displays the instructions and handles commands typed by the player.

When the player reaches the exit, congratulation massage is printed and the player is asked if they want to play again.

### **Maze.py**
Handles generation and storing of the maze itself.

### **params.py**
Contains maze sizes for each available difficulty, skin sets and other parameters in a form of dictionaries. Additionally, current maze skin is randomly chosen here (if the argument -l was not provided).

### **instructions.txt**
Contains a set of instructions for the user on which commands are eligible for navigation in the maze.

### **instructions_rus.txt**
Instructions for russian version of the game. Instructions of how to run this version are in the file *README_RUS.md*