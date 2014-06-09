##
##    Container & Iterators
##
##    Basic Functions:
##        next(), returns the next element
##        __iter__(), returns the iterator itself
##
##    Excetpions:
##        raise StopIteration
##
##


class IntegerIterator(object):
    def __init__(self, step):
        self.step = step

    def next(self):
        """ Returns the next elements."""
    
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        """Returns the iterator itself"""
        return self


    
for el in IntegerIterator(5):
    print el
    
#output:    4
#           3
#           2
#           1
#           0

