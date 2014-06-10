##
##  decorator without parameters
##

def aopdecorator1(function):
    #using (*args, **kw) to adapt uncertain parameters 
    def _aopdecorator(*args, **kw):
        print("before invoke")
        #invoke the wrapped method
        res = function(*args, **kw)
        print("after invoke")
        return res
    #return the wrapper method
    return _aopdecorator


#demo1
#using function wrapper
def hellowrapper1():
    print("hello wrapper1")
    
hellowrapper1 = aopdecorator1(hellowrapper1)
hellowrapper1()
#output:    before invoke
#           hello wrapper
#           after invoke


#demo2
#using syntactic sugar
@aopdecorator1
def hellosugar1():
    print("hello sugar1")

hellosugar1()
#output:    before invoke
#           hello wrapper
#           after invoke






##
##decorator with parameters
##

def aopdecorator2(arg1, arg2):
    def _aopdecorator2(function):
        def __aopdecorator2(*args, **kw):
            print("arg1: %s, arg2: %s" % (arg1, arg2))
            res = function(*args, **kw)
            return res
        return __aopdecorator2
    return _aopdecorator2


#demo2
#using syntactic sugar
@aopdecorator2("arg1", "arg2")
def hellosugar2():
    print("hello sugar2")


hellosugar2()
#output:    arg1: arg1, arg2: arg2
#           hello sugar2












            
            
