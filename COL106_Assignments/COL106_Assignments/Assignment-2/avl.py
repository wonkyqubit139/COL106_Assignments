from node import Node

def comp_1(node_1, node_2):
    # if 1:
    #     1
    pass

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = comp_1
        
    def get_height(self, node) :
        if node is None:
            return 0
        return node.height 
    
    def get_balance(self,node):
        if node is None :
            return 0
        return self.get_height(node.left)-self.get_height(node.right)
    
    def insert (self, node, key, data) :
        if node is None :
            return Node(key,data)
        if key<node.key :
            node.left=self.insert(node.left,key,data)
        else :
            node.right=self.insert(node.right, key , data)
        
        node.height= 1+ max (self.get_height(node.left),self.get_height(node.right))

        balance=self.get_balance(node)
        # LL balancing
        if balance>1 and key< node.left.key :
            return self.right_rotate(node)
        # RR balancing
        if balance <-1 and key>node.right.key:
            return self.left_rotate(node)
        # LR balancing
        if balance > 1 and key >node.left.key:
            node.left=self.left_rotate(node.left)
            return self.right_rotate(node)
        # RL balancing
        if balance < -1 and key < node.right.key :
            node.right=self.right_rotate(node.right)
            return self.left_rotate(node)
        # if remains unchanged
        return node
    
    def right_rotate(self, z):
        c=z.left
        t2=c.right

        c.right=z
        z.left=t2

        z.height=1 + max(self.get_height(z.left),self.get_height(z.right))
        c.height=1 + max(self.get_height(c.left),self.get_height(c.right))
        return c
    def left_rotate(self, z):
        c=z.right
        t2=c.left

        c.left=z
        z.right=t2

        z.height=1 + max(self.get_height(z.left),self.get_height(z.right))
        c.height=1 + max(self.get_height(c.left),self.get_height(c.right))
        return c
    
    def delete(self, node, key):
        if node is None :
            return node
        if key<node.key :
            node.left=self.delete(node.left,key)
        elif key> node.key :
            node.right = self.delete(node.right,key)

        else :
            if node.left is None:
                node1=node.right
                node=None
                return node1
            elif node.right is None:
                node1=node.left
                node=None
                return node1
            
            temp=self.get_min_key_node(node.right)
            node.key=temp.key
            node.data=temp.data
            node.right=self.delete(node.right,temp.key)
        if node is None:
            return node
        
        node.height=1+ max(self.get_height(node.right),self.get_height(node.left))

        balance=self.get_balance(node)

        # LL balance
        if balance>1 and self.get_balance(node.left)>=0 :
            return self.right_rotate(node)
        # RR balancing
        if balance <-1 and self.get_balance(node.right)<=0:
            return self.left_rotate(node)
        # LR balancing
        if balance > 1 and self.get_balance(node.left)<0:
            node.left=self.left_rotate(node.left)
            return self.right_rotate(node)
        # RL balancing
        if balance < -1 and self.get_balance(node.right)>0 :
            node.right=self.right_rotate(node.right)
            return self.left_rotate(node)
        # if remains unchanged
        return node
    
    def get_min_key_node(self, node):
        if node.left is not None:
            return self.get_min_key_node(node.left)
        else :
            return node
        
    def search(self,node,key) :
        if node is None :
            return node
        if key < node.key :
            return self.search(node.left,key)
        elif key > node.key :
            return self.search(node.right,key)
        else :
            return node
    def compact_fit(self,node,size) :
        # self.stack=[]
        # self.min_node
        if node is None :
            return None
        
        if node.key >= size :
            temp=self.compact_fit(node.left,size)
            if temp is None:
                return node
            else :
                return temp
        elif node.key <size:
            return self.compact_fit(node.right,size)
        
        
        # pass

    def largest_fit(self,node,size) :
        # self.stack=[]
        # if 
        # pass
        if node is None :
            return None
        
        if node.key >= size :
            temp=self.largest_fit(node.right,size)
            if temp is None:
                return node
            else :
                return temp
        elif node.key <size:
            return self.largest_fit(node.right,size)
        
    def least_key(self,node):
        if node is None:
            return None
        if node.left is None:
            return node
        else :
            return self.least_key(node.left)
    
    def greatest_key(self, node):
        if node is None:
            return None
        if node.right is None:
            return node
        else :
            return self.greatest_key(node.right)
        
    def get_all_nodes(self,node,node_list) :
        if node is None :
            return 
        
        self.get_all_nodes(node.left,node_list)

        node_list.append(node.key)

        self.get_all_nodes(node.right,node_list)

    