
def typechecker(in_=(), out_=(type(None),)):
    def _typechecker(function):
        def _check_types(elements, types):
            """Subfunction that checks the types"""
            if len(elements) != len(types):
                raise TypeError('argument count is wrong')
            typed = enumerate(zip(elements, types))
            for index, couple in typed:
                arg, of_the_right_type = couple
                if isinstance(arg, of_the_right_type):
                    continue
                raise TypeError('arg #%d should be %s' % \
                                (index, of_the_right_type))

        def __typechecker(*args):   #don't allow keywords
            #check inputs
            #checkable_args = args[1:]   #if in class should remove self
            checkable_args = args
            _check_types(checkable_args, in_)
            
            #invoke the function
            res = function(*args)
            
            #check outputs
            if not type(res) in (tuple, list):
                checkable_res = (res,)
            else:
                checkable_res = res
            _check_types(checkable_res, out_)
            return res
        return __typechecker
    return _typechecker

#test
#demo1
@typechecker((str,),(int,))
def string_int(instr):
    print(instr)
    return 1
string_int("string_int")



#demo2
@typechecker()
def null_null():
    print("null_null")
null_null()

