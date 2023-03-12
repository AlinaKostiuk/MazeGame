# MAZE TEXT GAME
### Video Demo:  <https://youtu.be/TgwzuXTsVyc>
## Table of contents
* [General info](#general-info)
* [Usage](#usage)
* [FIles](#technologies)
    * [project.py](#project.py)
    * [test_project.py](#test_project.py)
    * [params.py](#params.py)
    * [instructions.txt](#instructions.txt)

## General info
This project is a game in which you need to find your way out of a procedurally generated maze with the help of text commands.

By default, the player can choose from 3 levels of difficulty, but this can be manually modified in the file [params.py](#params.py).

Additional challenge is introduced by not redrawing the map after every move, though the player can request to see the map with their current position at any moment.

## Usage
```
$ python project.py
```
#


## Files
### **project.py**
Main file of the project that does all the work, i.e. determines difficulty for the level, generates a maze, displays the maze and instructions and handles commands typed by the player.

When the player reaches the exit, congratulation massage is printed and the player is asked if they want to play again.

Originally, maze was supposed to be a separate class, but this way requirements for the project would not have been met as there would have been less three functions at the same indentation level as ```main``` for which test are reasonably easy to implement. Therefore, functional programming was chosen.



### **test_project.py**
Contains three sets of tests for [project.py](#project.py).

First checks maze generation: whether the maze is the right size, whether the function returns correct values and whether the entrance and the exit from the maze are in suitable places.

Second and third ensure that when printing the maze and the instruction respectively, they are displayed correctly.


### **params.py**
Contains maze sizes for each available difficulty and skin sets in a form of dictionaries. Additionally, current maze skin is randomly chosen here.

### **instructions.txt**
Contains a set of instructions for the user on which commands are eligible for navigation in the maze.
