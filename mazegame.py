import random
import sys
import re
import params
import codecs
from Maze import Maze


def main():
    global text_params

    if len(sys.argv) > 1:
        if '--rus' in sys.argv:
            text_params = params.language['rus']
        else:
            text_params = params.language['eng']

        if '-l' in sys.argv or '--line' in sys.argv:
            line=True
        else:
            line=False
    else:
        text_params = params.language['eng']
        line = False

    global navs
    navs = text_params['movements']

    dimension = set_difficulty()
    maze = Maze(dimension, line, text_params)

    print(text_params['greeting'])

    print(maze)

    print(get_instructions(text_params['instructions']))

    while maze.player != maze.finish:
        move = input(text_params['where_next']).strip().lower()
        
        if move == text_params["map"]:
            print()
            print(maze)
            print()
            continue
        elif move == text_params["help"]:
            print(get_instructions(text_params['instructions']))
            continue
        elif move == text_params["exit"]:
            exit()
        
        pattern = "^(" + f"{navs['up']}|{navs['down']}|{navs['left']}|{navs['right']}" + r")( [0-9]+)?$"

        matches = re.search(pattern, move)
        if matches and matches.group(1):
            if matches.group(2):
                steps = int(matches.group(2).strip())
            else:
                steps = 1
            
            walk(maze, matches.group(1), steps)
        
        # if player == finish:
        #     break
    
    victory()



def set_difficulty():
    diffs = list(text_params['dimensions'].keys())

    while True:       
        lvl = input(f"{text_params['difficulty']} ({', '.join(diffs)}): ").strip().lower()
        if lvl in diffs:
            return text_params['dimensions'][lvl]
            
    


def walk(maze, direction, steps):
    directions = {"up": (-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)}
    dir_key = list(navs.keys())[list(navs.values()).index(direction)]
    xx, yy = directions[dir_key]

    counter = 0

    if maze.player == maze.entrance and dir_key == "up":
        exit()
        return


    for i in range(steps):
        x,y = maze.player
        if maze.maze[x+xx][y+yy] != maze.w:
            maze.player = (x+xx,y+yy)
            maze.maze[x][y] = maze.p
            maze.maze[x+xx][y+yy] = maze.c

            if maze.player == maze.finish:
                return
        else:
            break
        
        counter = i+1

    if counter == 0:
        print(text_params['wall'])
        return
    elif counter != steps:
        print(text_params['too_far'])

    print(f"{text_params['too_far_walked']} {counter} {direction}")



def get_instructions(file):
    txt = ""

    try:
        with codecs.open(file, "r", "utf-8") as instructions:
            for line in instructions:
                txt += line
    except FileNotFoundError:
        txt = text_params['FileNotFoundError']

    return txt


def exit():
    response = input(text_params['go_back'])
    if response.lower() in ["yes", "y", "1", "true", "да", "д"]:
        print(text_params['bye'])
        sys.exit()
    else:
        print(text_params['changed_mind'])
        return


def victory():
    print(text_params['congrats'])

    repeat = input(text_params['replay'])
    if repeat.lower() in ["yes", "y", "1", "true", "да", "д"]:
        main()




if __name__=="__main__":
    main()