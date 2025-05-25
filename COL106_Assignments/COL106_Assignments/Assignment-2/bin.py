from avl import AVLTree #extra import
class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id=bin_id
        self.capacity=capacity
        self.objects=AVLTree()
        

    def add_object(self, object):
        # Implement logic to add an object to this bin
        #object=(obj_id,size,color,bin_id)
        self.objects.root=AVLTree.insert(self.objects.root,object.obj_id,object)
        return self.objects.root

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        
        pass
