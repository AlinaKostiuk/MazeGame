import random
import params




class Maze:
    def __init__(self,dim="regular", line=False, text_params=None) -> None:
        self.dimension = dim
        self.maze = []
        self.entrance = (0,0)
        self.finish = (0,0)
        self.player = (0,0)

        self.choose_skin(line)

        self.generate_maze()
        

    def __str__(self) -> str:
        return self.draw_maze()


    def generate_maze(self):
        # add top
        self.maze.append([self.w for _ in range(self.dimension)])

        # add body
        for i in range(self.dimension-2):
            row = [self.w]
            for _ in range(self.dimension-2):
                row.append(self.u)
            row.append(self.w)
            self.maze.append(row)

        # add footer
        self.maze.append([self.w for _ in range(self.dimension)])

        self.tiles = []

        # choose starting tile
        x = random.choice(range(1, self.dimension-1))
        if x % 2 == 0:
            x = x+1 if x != self.dimension-2 else x-1

        y = random.choice(range(1,self.dimension-1))
        if y % 2 == 0:
            y = y+1 if y != self.dimension-2 else y-1

        # make it a "passage" tile and add walls around
        self.maze[x][y] = self.p
        
        self.add_walls(x,y)

        # add tiles around starting tile to the queue
        self.add_undefind_tiles(x, y)


        while any(self.u in row for row in self.maze):
            random.shuffle(self.tiles)
            x,xx,y,yy = self.tiles.pop(0)

            if self.maze[x][y] == self.u:
                self.maze[x][y] = self.p
                self.maze[x-xx][y-yy] = self.p

                self.add_walls(x,y)
                self.add_undefind_tiles(x, y)

        self.entrance = self.create_entrance()
        self.finish = self.create_finish()
        self.player = self.entrance
        self.maze[self.player[0]][self.player[1]] = self.c



    def add_walls(self, x, y):
        for i in range(-1,2):
            for j in range(-1,2):
                if self.maze[x+i][y+j] == self.u:
                    self.maze[x+i][y+j] = self.w



    def add_undefind_tiles(self, x, y):
        if x != 1 and self.maze[x-2][y] == self.u:
            self.tiles.append((x-2, -1, y, 0))
        
        if x != self.dimension-2 and self.maze[x+2][y] == self.u:
            self.tiles.append((x+2, 1, y, 0))
            
        if y != 1 and self.maze[x][y-2] == self.u:
            self.tiles.append((x, 0, y-2, -1))

        if y != self.dimension-2 and self.maze[x][y+2] == self.u:
            self.tiles.append((x, 0, y+2, 1))


    def create_entrance(self):
        y = random.choice(range(1,self.dimension-1))
        
        if self.maze[1][y] != self.p:
            _,y = self.create_entrance()
        
        return (0,y)


    def create_finish(self):
        y = random.choice(range(1,self.dimension-1))
        
        if self.maze[self.dimension-2][y] != self.p:
            _,y = self.create_finish()
        
        self.maze[self.dimension-1][y] = self.f

        return (self.dimension-1,y)


    def draw_maze(self):
        maze_str = "\n".join(["".join(row) for row in self.maze])
        return maze_str


    def choose_skin(self, line=False):
        if line:
            skin = params.line_skin
        else:
            skin = params.skin

        self.u = "⬛️" # undefined
        self.w = skin["w"] # wall
        self.p = skin["p"] # passage
        self.c = random.choice(skin["sprites"]) # cursor
        self.f = skin["f"] # finish
        self.e = skin["p"] # entrance