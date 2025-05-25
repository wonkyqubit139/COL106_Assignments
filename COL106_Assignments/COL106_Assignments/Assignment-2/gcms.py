from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bin=AVLTree()#(bin_id,bin_class)  bin_class=(bin_id,capacity,objects=AVLTree())
        self.obj_tree=AVLTree()#(object_id,object(id,size,color,bin_id))
        self.bin_capacity=AVLTree()
        # pass 

    def add_bin(self, bin_id, capacity):
        # self.bin.append([bin_id,capacity])
        bin_class=Bin(bin_id,capacity)
        self.bin.root=self.bin.insert(self.bin.root,bin_id,bin_class)
        node=self.bin_capacity.search(self.bin_capacity.root,capacity)
        if node is None :
            # print("Test\n")
            sub_tree=AVLTree()
            sub_tree.root=sub_tree.insert(sub_tree.root,bin_id,bin_class)
            self.bin_capacity.root=self.bin_capacity.insert(self.bin_capacity.root,capacity,sub_tree)
        else :
            #add tree inside this tree
            node.data.root=node.data.insert(node.data.root,bin_id,bin_class)
        
            
        # pass

    def add_object(self, object_id, size, color):
        #choose algo using color
        #using algo find suitable bin_id
        #now add this object in the bin
        #also update the bin_capacity tree=delete+insert
        #also add this obj in obj tree along with its binId
        
        # object initialized
        self.obj=Object(object_id,size,color)

        if (color.value == 1) :
            #  Blue Cargo (Compact Fit, Least ID):
            self.min_capa_node=self.bin_capacity.compact_fit(self.bin_capacity.root,size)
            if (self.min_capa_node is None):
                raise NoBinFoundException
            min_id_node=self.min_capa_node.data.least_key(self.min_capa_node.data.root)
            node_of_concern=min_id_node
            capa_node=self.min_capa_node
            
        elif (color.value == 2) :
            # Yellow Cargo (Compact Fit, Greatest ID):
            self.min_capa_node=self.bin_capacity.compact_fit(self.bin_capacity.root,size)
            if (self.min_capa_node is None):
                raise NoBinFoundException
            max_id_node=self.min_capa_node.data.greatest_key(self.min_capa_node.data.root)
            node_of_concern=max_id_node
            capa_node=self.min_capa_node
        elif (color.value == 3) :
            # Red Cargo (Largest Fit, Least ID):
            self.max_capa_node=self.bin_capacity.largest_fit(self.bin_capacity.root,size)
            if (self.max_capa_node is None):
                raise NoBinFoundException
            min_id_node=self.max_capa_node.data.least_key(self.max_capa_node.data.root)
            node_of_concern=min_id_node
            capa_node=self.max_capa_node
        else :
            # Green Cargo (Largest Fit, Greatest ID):
            self.max_capa_node=self.bin_capacity.largest_fit(self.bin_capacity.root,size)
            if (self.max_capa_node is None):
                raise NoBinFoundException
            max_id_node=self.max_capa_node.data.greatest_key(self.max_capa_node.data.root)
            node_of_concern=max_id_node
            capa_node=self.max_capa_node
        
        if capa_node is not None:
            # print(capa_node.key)
            self.obj.bin_id=node_of_concern.key
            node_of_concern.data.objects.root=node_of_concern.data.objects.insert(node_of_concern.data.objects.root,object_id,self.obj)
            capacity=capa_node.key
            # now i have to update the capacity of this bin
            # for this i will first create a new bin with updated capacity and the delete prev bin and insert new bin
            bin_id=node_of_concern.key
            new_bin=Bin(node_of_concern.key,capacity-size)
            new_bin.objects.root=node_of_concern.data.objects.root
            #delete
            capa_node.data.root=capa_node.data.delete(capa_node.data.root,bin_id)
            if capa_node.data.root is None:
                self.bin_capacity.root=self.bin_capacity.delete(self.bin_capacity.root,capacity)
            #search karna if new capacity wala node hai otherwise add a new node, then uss node me ye bin add karna hai
            #insert
            search_node=self.bin_capacity.search(self.bin_capacity.root,capacity-size)
            # print("TEST")
            if search_node is not None :
                # print("True")
                search_node.data.root=search_node.data.insert(search_node.data.root,bin_id,new_bin)
            else:
                # print("ELSE")
                new_tree=AVLTree()
                new_tree.root=new_tree.insert(new_tree.root,bin_id,new_bin)
                self.bin_capacity.root=self.bin_capacity.insert(self.bin_capacity.root,capacity-size,new_tree)
            # self.bin.root=self.bin.delete(self.bin.root, bin_id)
            # self.bin.root=self.bin.insert(self.bin.root, bin_id,new_bin)
            search_bin=self.bin.search(self.bin.root,bin_id)
            search_bin.data=new_bin
        
        else:
            # print("ERROR")
            raise NoBinFoundException
        #objects k tree me object add karna hai
        self.obj_tree.root=self.obj_tree.insert(self.obj_tree.root, object_id,self.obj)

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        #bin_class se delete ho jaega through bin wala tree and obj wala tree se bhi d
        
        #object delete from obj_tree
        search_node=self.obj_tree.search(self.obj_tree.root,object_id)
        if search_node is not None:
            obj_size=search_node.data.size
            bin_id=search_node.data.bin_id
            self.obj_tree.root=self.obj_tree.delete(self.obj_tree.root,object_id)

            #object delete from bin wala tree
            search_node_in_bin=self.bin.search(self.bin.root,bin_id)
            search_node_in_bin.data.objects.root=search_node_in_bin.data.objects.delete(search_node_in_bin.data.objects.root,object_id)
            old_capacity=search_node_in_bin.data.capacity
            search_node_in_bin.data.capacity+=obj_size
            new_capacity=search_node_in_bin.data.capacity

            # bin_capacity me bhi changes honge
            search_node_in_bin_capacity=self.bin_capacity.search(self.bin_capacity.root,old_capacity)
            search_node_in_bin_capacity.data.root=search_node_in_bin_capacity.data.delete(search_node_in_bin_capacity.data.root,bin_id)
            if search_node_in_bin_capacity.data.root is None :
                self.bin_capacity.root=self.bin_capacity.delete(self.bin_capacity.root,old_capacity)
            search_node_in_bin_capacity_new=self.bin_capacity.search(self.bin_capacity.root,new_capacity)

            if search_node_in_bin_capacity_new is not None :
                    # print("True")
                    search_node_in_bin_capacity_new.data.root=search_node_in_bin_capacity_new.data.insert(search_node_in_bin_capacity_new.data.root,bin_id,search_node_in_bin.data)
            else:
                # print("ELSE")
                new_tree=AVLTree()
                new_tree.root=new_tree.insert(new_tree.root,bin_id,search_node_in_bin.data)
                self.bin_capacity.root=self.bin_capacity.insert(self.bin_capacity.root,new_capacity,new_tree)
        else :
            return

        

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        search_bin=self.bin.search(self.bin.root,bin_id)
        capacity=search_bin.data.capacity
        list=[]
        search_bin.data.objects.get_all_nodes(search_bin.data.objects.root,list)
        return (capacity,list)
    
    
    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        search_obj=self.obj_tree.search(self.obj_tree.root,object_id)
        if search_obj is not None:
            bin_id=search_obj.data.bin_id
            return bin_id
        else :
            return None
        
    
    
