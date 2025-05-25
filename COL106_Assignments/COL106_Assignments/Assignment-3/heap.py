'''
Python Code to implement a heap with general comparison function
'''
# def comp1 (a,b):
#     return a<b


class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''

        
        # Write your code here
        self.heap=init_array
        self.comparator=comparison_function
        # self.len=0
        # for i in init_array:
        #     self.insert(i)
            # self.len+=1
        for i in range((len(self.heap)//2)-1,-1,-1):
            self.downheap(i)
        

        

        # pass
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.heap.append(value)
        # self.len+=1
        self.upheap(len(self.heap)-1)
        # pass
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if len(self.heap) !=0:
            value=self.heap[0]
            self.heap[0]=self.heap[len(self.heap)-1]
            self.heap.pop()
            self.downheap(0)
            return value
        else:
            return None
        
        # pass
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if len(self.heap)!=0:
            return self.heap[0]
        else :
            return None
        
    
    # You can add more functions if you want to

    def upheap(self,n):
        if n==0:
            return
        parent =(n-1)//2
        # if self.heap[parent]>self.heap[n]:
        if self.comparator(self.heap[n],self.heap[parent]):
            self.heap[parent], self.heap[n] = self.heap[n], self.heap[parent]
        else :
            return
        self.upheap(parent)

    def downheap(self,n):
        li=2*n+1
        ri=2*n+2
        if (li>=len(self.heap)):
            return
        elif li==len(self.heap) -1:#only left child
            indx=li
        else :
            # if self.heap[li]>self.heap[ri]:
            if self.comparator(self.heap[ri],self.heap[li]):
                indx=ri
            else:
                indx=li
        
        # if self.heap[n]>self.heap[indx]:
        if self.comparator(self.heap[indx],self.heap[n]):
            self.heap[n],self.heap[indx]=self.heap[indx],self.heap[n]
        else:
            return
        
        self.downheap(indx)
    
    def heapify(self,indx):
        self.downheap(indx)
    

    def printHeap(self):
        itr=0
        target_itr=1
        for i in range (len(self.heap)):
            print(self.heap[i],end=" ")
            itr+=1
            if itr==target_itr:
                target_itr=target_itr*2
                itr=0
                print()
            # itr+=1

        

