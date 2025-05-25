'''
    Python file to implement the Treasure class
'''

class Treasure:
    '''
    Class to implement a treasure
    '''
    
    def __init__(self, id, size, arrival_time):
        '''
        Arguments:
            id : int : The id of the treasure (unique positive integer for each treasure)
            size : int : The size of the treasure (positive integer)
            arrival_time : int : The arrival time of the treasure (non-negative integer)
        Returns:
            None
        Description:
            Initializes the treasure
        '''
        
        # DO NOT EDIT THE __init__ method
        self.id = id
        self.size = size
        self.arrival_time = arrival_time
        self.completion_time = None
    
    # You can add more methods if required
    def extra_var(self):
        list=[self.size]
        list2=list[:]

        # self.id_copy = self.id
        self.size_copy = list2[0]
        # self.arrival_time_copy = self.arrival_time
        # self.completion_time_copy = None
        self.estimated_time=None
        # self.remaining_size=self.size_copy
        # self.time_elapsed=None
        self.priority=self.size+self.arrival_time

    def re_init(self):
        self.size=self.size_copy
        self.priority=self.size+self.arrival_time
