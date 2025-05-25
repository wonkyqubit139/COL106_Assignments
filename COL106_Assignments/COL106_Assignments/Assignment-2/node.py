class Node:
    # __slots__='_data','_rChild','_lChild','_parent'
    def __init__(self,key,data):
        self.data=data
        self.key=key
        self.right=None
        self.left=None
        # self._parent=parent
        self.height=1