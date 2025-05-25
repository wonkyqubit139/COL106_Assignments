from maze import *
from exception import *
from stack import *
def is_valid(x : int, y : int, rows : int, cols : int) -> bool:
    if(x < 0 or x >= rows):
        return False
    elif(y < 0 or y >=cols):
        return False
    return True
def is_neighbour(x1 : int, y1 : int, x2 : int, y2 : int) -> bool:
    return abs(x2-x1) + abs(y2-y1) == 1
class PacMan:
    navigator_maze=[]
    
    def __init__(self, grid : Maze) -> None:
        self.navigator_maze = grid.grid_representation

    def find_path(self, start , end):
        # IMPLEMENT FUNCTION HERE
        self.navigator_maze2 = []
        self.path=Stack()
        self.raasta=[]
        self.raasta2=[]
        for i in range(len(self.navigator_maze)) :
            self.navigator_maze2.append(self.navigator_maze[i][:])
        self.len_x=len(self.navigator_maze2)
        self.len_y=len(self.navigator_maze2[0])
        if self.navigator_maze2[start[0]][start[1]]==0:
            self.path.push(start)
        while (self.path.top()!=end and not self.path.isEmpty()) :
            x=self.path.top()[0]
            y=self.path.top()[1]
            self.navigator_maze2[x][y]=1
            options=[(x-1,y),(x,y+1),(x+1,y),(x,y-1)]
            for i in range(4) :
                # print(options[i][0], options[i][1])
                if (is_valid(options[i][0],options[i][1],self.len_x,self.len_y)) :
                    # print(options[i][0], options[i][1])
                    if (self.navigator_maze2[options[i][0]][options[i][1]]!=1) :
                        self.path.push(options[i])
                        # print (options[i])
                        break
            else :
                self.path.pop()
                # print("POP P")
        # print(self.path.length())
        # a=self.path.pop()
        # print(a)
        leng=self.path.length()
        # yahi kahi gadbad hai
        for i in range(leng) :
            # print("tewst")
            a=self.path.pop()
            self.raasta.append(a)
        for i in range (leng) :
            b=self.raasta.pop()
            self.raasta2.append(b)
        # for i in range (leng) :
        #     print("test")
        #     print (self.raasta2[i])
        if len(self.raasta2)!=0:
            # print("Returning path")
            return self.raasta2
                
                
        else:
            # print("raising path not found exception")
            raise PathNotFoundException

