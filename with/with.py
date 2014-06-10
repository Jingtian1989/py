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

class file(object):
  
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        """
           Returns a object called context management object,
           it is used in the with-block
        """
        return open(self.path)

    def __exit__(self, exception_type, exception_value, exceptiong_traceback):
        """
           Returns False to indicate re-raise the exception(if
           occured) in with-block
           Returns True to indicate no re-raise the exception(if
           occured) in with-block
        """
        return False

#test
with file('with1.py') as lines:    
    for line in lines:
        print(line)


