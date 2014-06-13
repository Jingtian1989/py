
##
##  demonstrate the usage of __import__ | importlib to load module dynamically
##  


#import importlib
class DynamicModule(object):
    def __init__(self, name):
        self.module = __import__(name)
        #self.module = importlib.import_module(name)

    def get_attr(self, name):
        return getattr(self.module, name)



MODULE_NAME = 'testmod'
KLASS_NAME = 'TestModule'
ATTR_NAME = 'get_name'

klass  = DynamicModule(MODULE_NAME).get_attr(KLASS_NAME)
obj = klass()
attr = getattr(obj, ATTR_NAME)
print(attr())

#output:    TestModule
#   
