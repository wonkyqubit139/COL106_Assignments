'''
    This file contains the class definition for the StrawHat class.
'''
from crewmate import *
from heap import *
from treasure import *

def comparator(a,b):
        return a.load<b.load

def comparator_treasure_id(a,b):
     return a.id<b.id

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        self.crewmates=[]
        self.assigned_crewmates=[]
        self.treasure=Heap(comparator_treasure_id,[]) #to keep sorted treasure
        
        # Write your code here
        for i in range(m):
            temp_crewmate=CrewMate()
            self.crewmates.append(temp_crewmate)
            # self.heap_crewmates.insert(temp_crewmate)

        self.heap_crewmates=Heap(comparator,self.crewmates)

        # pass
    

    def add_treasure(self, treasure:Treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        treasure.extra_var()
        self.treasure.insert(treasure)

        arrival_time = treasure.arrival_time
        size=treasure.size
        # I have to extract the crewmate, then assign the treasure, find the change in load
        # then reinsert the crewmate
        crewmate=self.heap_crewmates.extract()
        if len(crewmate.treasure)==0:
             self.assigned_crewmates.append(crewmate)
        crewmate.treasure.append(treasure)
        # crewmate.treasure_heap.insert(treasure)

        load=crewmate.load
        if load>arrival_time:
             load=load+size
        else:
             load=arrival_time + size

        crewmate.load=load

        self.heap_crewmates.insert(crewmate)

        # end of function
        # crewmate=self.heap_crewmates.extract()
        # crewmate.load+=treasure.size
        # crewmate.treasure.append(treasure)
        # self.heap_crewmates.insert(crewmate)

        
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''


        # print("Hi")
        # print(len(self.assigned_crewmates))
        # Write your code here
        crew:CrewMate
        for crew in self.assigned_crewmates:
            # print([i.id for i in crew.treasure])
            # print("inside LOOP")
            # Now this crewmate pe i have to do a for loop where i take each tresure one by one 
            #  Basically i have to add the treasure in a heap with priority, as i reach a new timestamp, update the priority of top and then update heap
            # then insert the new treasure
            # in the meantime if any treasure gets processed completely update its completion time and remove from heap as well
            heap=crew.treasure_heap
            first_tre=crew.treasure[0]
            prev_time=first_tre.arrival_time
            # print(prev_time)
            for treasure in crew.treasure:
                # print("Hi There")
                time_gap=treasure.arrival_time-prev_time
                t = heap.top()
                if t is not None :
                    while (time_gap>0):
                        t=heap.extract()
                        if t.size-time_gap > 0:
                             t.size-=time_gap
                             prev_time+=time_gap
                             t.priority-=time_gap
                             heap.insert(t)
                             break
                        
                        prev_time+=t.size
                        t.size=0
                        t.completion_time =prev_time
                        t=heap.top()
                        if t is None :
                             break
                        
                if heap.top() is not None:
                    t=heap.extract()
                    t.size-=treasure.arrival_time - prev_time
                    t.priority=t.size + t.arrival_time 
                    heap.insert(t)

                heap.insert(treasure)
                prev_time= treasure.arrival_time
                # treasure.completion_time=prev_time+treasure.size
            # print(len(heap.heap))
            while (heap.top() is not None):
                t=heap.extract()
                t.completion_time=prev_time+t.size
                prev_time=t.completion_time

        treasure_heap=Heap(comparator_treasure_id,[])
        treasure_heap.heap=self.treasure.heap[:]
        list=[]
        while (treasure_heap.top() is not None):
            tre=treasure_heap.extract()
            list.append(tre)
            tre.re_init()
        return list
    
            
    # You can add more methods if required

    '''
    
    for curr_crewmate in assigned wale crewmates:
        prev_time=arrival time of first treasure
        for tre in crew.treasure:
            time_gap=tre.arrival_time - prev time
                t=heap.top()
            if t none nhi hai:
                while (time_gap>=t.size):
                    t=heap.extract()
                    prev_time+=t.size
                    t.size=0
                    t.completion_time =prev_time
                    t=heap.top()
                    agar t none hai break
            if len(heap)!=0:
                t=heap.extract()
                t.size-=tre.arrivaltime - prev_time
                t.priority=t.size + t.arrival_time 
                heap.insert(t)
            
            heap.insert(tre)



    '''

# jab  bhi get completion time ko call karo toh reinitialize the size and priority

