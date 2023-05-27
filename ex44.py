class parent(object):
    def override(self):
        print("parent override()")

    def implicit(self):
        print("parent implicit()") 

    def altered(self):
        print("parent altered()")

class child(parent): 
    def override(self):
        print("child override()")

    def altered(self):
        print("child,before parent altered()")
        super(child,self).altered()
        print("child, alfer parent altered()")

dad = parent()
son = child() 
dad.implicit()
son.implicit()
dad.override()
son.override()    
dad.altered()
son.altered()
