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
        """
           Returns a object called context management object,
           it is used in the with-block
        """
        print("__enter__")
        return self.obj

    def __exit__(self, *arg):
        """
           Returns False to indicate re-raise the exception(if
           occured) in with-block
           Returns True to indicate no re-raise the exception(if
           occured) in with-block
        """
        print("__exit__")
        return True


with WithObj("WithObj") as t:    
    print("With-Block")        
    print(t)                    

#output:    __enter__
#           With-Block
#           WithObj
#           __exit__
