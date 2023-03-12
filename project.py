import random
import sys
import re
import params


def main():
    reset_skin()
    dimension = set_difficulty()
    
    print("\nIn your wanderings around this magical world you came across a maze.")
    print("Find the way through it to continue your journey!")
    print()

    # create the maze
    maze, entrance, finish = generate_maze(dimension)

    # add the player
    player = entrance
    maze[player[0]][player[1]] = c

    # show maze
    print(draw_map(maze))

    print(get_instructions("instructions.txt"))

    while player != finish:
        move = input("Where will you go next? ").strip().lower()
        
        if move == "map":
            print()
            print(draw_map(maze))
            print()
            continue
        elif move == "help":
            print(get_instructions("instructions.txt"))
            continue
        elif move == "exit":
            exit()
        
        matches = re.search(r"^(up|down|left|right)( [0-9]+)?$", move)
        if matches and matches.group(1):
            if matches.group(2):
                steps = int(matches.group(2).strip())
            else:
                steps = 1
            
            player = walk(maze, player, matches.group(1), steps, entrance, finish)
        
        # if player == finish:
        #     break
    
    victory()



def set_difficulty():
    diffs = list(params.dimensions.keys())

    while True:       
        lvl = input(f"Choose difficulty ({', '.join(diffs)}): ").strip().lower()
        if lvl in diffs:
            return params.dimensions[lvl]
            
    


def generate_maze(dimension):
    maze = []

    # add top
    maze.append([w for _ in range(dimension)])

    # add body
    for i in range(dimension-2):
        row = [w]
        for _ in range(dimension-2):
            row.append(u)
        row.append(w)
        maze.append(row)

    # add footer
    maze.append([w for _ in range(dimension)])

    # list of tiles which will be processed next
    tiles = []

    # choose starting tile
    x = random.choice(range(1, dimension-1))
    if x % 2 == 0:
        x = x+1 if x != dimension-2 else x-1

    y = random.choice(range(1,dimension-1))
    if y % 2 == 0:
        y = y+1 if y != dimension-2 else y-1

    # make it a "passage" tile and add walls around
    maze[x][y] = p
    add_walls(maze, x,y)

    # add tiles around starting tile to the queue
    add_undefind_tiles(maze, dimension, tiles, x, y)

    # choose next tile and repeat the procedure above until there are no undefined tiles left
    while any(u in row for row in maze):
        random.shuffle(tiles)
        x,xx,y,yy = tiles.pop(0)

        if maze[x][y] == u:
            maze[x][y] = p
            maze[x-xx][y-yy] = p

            add_walls(maze, x,y)
            add_undefind_tiles(maze, dimension, tiles, x, y)

    E = create_entrance(maze, dimension)
    F = create_finish(maze, dimension)

    return maze, E, F



def add_walls(maze, x,y):
    for i in range(-1,2):
        for j in range(-1,2):
            if maze[x+i][y+j] == u:
                maze[x+i][y+j] = w



def add_undefind_tiles(maze, dimension, lst, x, y):
    if x != 1 and maze[x-2][y] == u:
        lst.append((x-2, -1, y, 0))
    
    if x != dimension-2 and maze[x+2][y] == u:
        lst.append((x+2, 1, y, 0))
        
    if y != 1 and maze[x][y-2] == u:
        lst.append((x, 0, y-2, -1))

    if y != dimension-2 and maze[x][y+2] == u:
        lst.append((x, 0, y+2, 1))



def create_entrance(maze, dimension):
    y = random.choice(range(1,dimension-1))
    
    if maze[1][y] != p:
        _,y = create_entrance(maze, dimension)
    
    return (0,y)



def create_finish(maze, dimension):
    y = random.choice(range(1,dimension-1))
    
    if maze[dimension-2][y] != p:
        _,y = create_finish(maze, dimension)
    
    maze[dimension-1][y] = f

    return (dimension-1,y)



def walk(maze, player, direction, steps, entrance, finish):
    directions = {"up": (-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)}
    xx, yy = directions[direction]

    counter = 0

    if player == entrance and direction == "up":
        exit()
        return player


    for i in range(steps):
        x,y = player
        if maze[x+xx][y+yy] != w:
            player = (x+xx,y+yy)
            maze[x][y] = p
            maze[x+xx][y+yy] = c

            if player == finish:
                return player
        else:
            break
        
        counter = i+1

    if counter == 0:
        print("You can't go there!")
        return player
    elif counter != steps:
        print("You can't go that far!")

    print(f"You've walked {counter} {direction}")

    return player



def draw_map(maze):
    maze_str = "\n".join(["".join(row) for row in maze])
    return maze_str


def get_instructions(file):
    txt = ""

    try:
        with open(file) as instructions:
            for line in instructions:
                txt += line
    except FileNotFoundError:
        txt = "\nInstructions are not found\n"

    return txt


def exit():
    response = input("Are you sure you want to go back? (y/n) ")
    if response.lower() in ["yes", "y", "1", "true"]:
        print("Umm... okay... bye...")
        sys.exit()
    else:
        print("I'm glad you've changed your mind!")
        return



def reset_skin():
    skin = params.skin
    global u
    u = "⬛️" # undefined
    global w
    w = skin["w"] # wall
    global p
    p = skin["p"] # passage
    global c
    c = random.choice(skin["sprites"]) # cursor
    global f
    f = skin["f"] # finish
    global e 
    e = skin["p"] # entrance



def victory():
    print("\n🎊🎉🎊 Congratulations! 🎊🎉🎊")
    print("Your courage and intelligence have guided you through this maze to new adventures!")
    print()

    repeat = input("Do you want to play again? (y/n) ")
    if repeat.lower() in ["yes", "y", "1", "true"]:
        reset_skin()
        main()




if __name__=="__main__":
    main()