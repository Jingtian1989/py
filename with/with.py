##
##  The 'with' statement is a control-flow structure whose basic structure is:
##      with expression [as variable]:
##          with-block
##  It is equally to:
##      try:
##          __enter__()
##          with-block
##      finally:
##          __exit__()
##
##        

class WithObj(object):
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        print("__enter__")
        return self.obj

    def __exit__(self, *arg):
        print("__exit__")


with WithObj("WithObj") as t:   #the __enter__ returns a object 
    print("With-Block")         #called context management object,
    print(t)                    #it is used in the with-block

#output:    __enter__
#           With-Block
#           WithObj
#           __exit__
