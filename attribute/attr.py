class Obj(object):
    def __init__(self):
        self.attr1 = 'attr1_value'

def print_attr(obj):
    for attr in dir(obj):
        if attr.startswith('__'):
            continue
        value = getattr(obj, attr)
        print(attr + ": " + value)


obj = Obj()
print('##before setattr##')
print_attr(obj)
setattr(obj, 'attr2', 'attr2_value')

print('##after setattr##')
print_attr(obj)


print('##after delattr##')
delattr(obj, 'attr2')
print_attr(obj)


#output:     ##before setattr##    
##           attr1: attr1_value
##           ##after setattr##
##           attr1: attr1_value
##           attr2: attr2_value
##           ##after delattr##
##           attr1: attr1_value
