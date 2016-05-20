class Prototype:    
    def _clone_func(self):
        # This function will be assigned to the decorated object and can
        # be used to create an exact duplicate of that decorated object
        clone = self.cls()
        # Call _copy_func to ensure the attributes of the objects are identical
        self._copy_func(self.instance, clone)
        return clone
    
    def _copy_func(self, fromObj, toObj):
        # Dual purpose function which is assigned to the decorated object 
        # and used internally in the decorator to copy the original attributes 
        # to the clone to ensure it's identical to the object which made the clone        
        for attr in dir(fromObj):
            setattr(toObj, attr, getattr(fromObj, attr))
    
    def __init__(self, cls):
        # This is only called once per decorated class type so self.cls 
        # should remember the class that called it so it can generate
        # unique objects of that class later on (in __call__)
        self.cls = cls
    
    # NOTE: on a decorator "__call__" MUST be implemented
    # this function will automatically be called each time a decorated
    # object is cloned/created
    def __call__(self):
        # Create an instance of the class here so a unique object can be 
        # sent back to the constructor
        self.instance = self.cls()
        # Assign the private functions back to the unique class 
        # (which is the whole point of this decorator)
        self.instance.Clone = self._clone_func
        self.instance.Copy = self._copy_func
        # Finally, send the unique object back to the object's constructor
        return self.instance        

@Prototype
class Concrete:
    def __init__(self):
        # Test value to see if objects are independently generated as
        # well as if they properly copy from one another
        self.somevar = 0
        
@Prototype
class another:
    def __init__(self):
        self.somevar = 50

if __name__ == '__main__':
    print "Creating A"
    a = Concrete()
    print "Cloning A to B"
    b = a.Clone()
    print "A and B somevars"
    print a.somevar
    print b.somevar
    print "Changing A somevar to 10..."
    a.somevar = 10
    print "A and B somevars"
    print a.somevar
    print b.somevar
    
    print "Creating another kind of class as C"
    c = another()
    print "Cloning C to D"
    d = c.Clone()
    print "Changing C somevar to 100"
    c.somevar = 100
    print "C and D somevars"
    print c.somevar
    print d.somevar
