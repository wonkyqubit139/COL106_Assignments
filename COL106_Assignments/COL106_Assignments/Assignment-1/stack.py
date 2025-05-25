class Stack:
    def __init__(self) :
        self.stack=[]
    
    def push(self, tup ) :
        self.stack.append(tup)
    def pop(self) :
        return self.stack.pop()
    def isEmpty(self) ->bool:
        if len(self.stack)==0 :
            return True
        else :
            return False
    def top(self) :
        if self.isEmpty()==0 :
            return self.stack[-1]
    def length(self):
        return len(self.stack)
    
    # You can implement this class however you like