'''
    Python file to implement the class CrewMate
'''
from heap import *
from treasure import *
def compare_priority(a:Treasure,b:Treasure):
    if a.priority < b.priority :
        return True
    elif a.priority==b.priority:
        # print("Ailah same same priority")
        if a.id<b.id :
            # print("YOU GOT IT RIGHT!!!!!!!")
            return True
        else :
            return False
    else :
        return False
    # return a.priority<b.priority

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.load=0
        self.treasure=[]
        self.treasure_heap=Heap(compare_priority,[])

        # pass

    # Add more methods if required