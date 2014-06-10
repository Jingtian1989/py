from contextlib import contextmanager
##
##  The 'with' statement is a control-flow structure whose basic structure is:
##      with expression [as variable]:
##          with-block
##  It is equally to:
##      
##      __enter__()
##      try:
##          with-block
##      finally:
##          __exit__()
##
##        

class File(object):
  
    def __init__(self, path):
        self.file = open(path)

    def __enter__(self):
        """
           Returns a object called context management object,
           it is used in the with-block
        """
        return self.file

    def __exit__(self, exception_type, exception_value, exceptiong_traceback):
        """
           Returns False to indicate re-raise the exception(if
           occured) in with-block
           Returns True to indicate no re-raise the exception(if
           occured) in with-block
        """
        self.file.close()
        return True

#test
    
#demo1
#using open
with open('with.py', 'r') as lines:    
    for line in lines:
        print(line)


#demo2
#using file
with File('with.py') as lines:    
    for line in lines:
        print(line)



        
