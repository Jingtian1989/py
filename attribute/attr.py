class Obj(object):
    def __init__(self):
        self.attr1 = 'attr1_value'

def print_attr(msg, obj):
    print(msg)
    for attr in dir(obj):
        if attr.startswith('__'):
            continue
        value = getattr(obj, attr)
        print(attr + ": " + value)


obj = Obj()
print_attr('##before setattr##', obj)

setattr(obj, 'attr2', 'attr2_value')
print_attr('##after setattr##', obj)

delattr(obj, 'attr2')
print_attr('##after delattr##', obj)


#output:     ##before setattr##    
#            attr1: attr1_value
#            ##after setattr##
#            attr1: attr1_value
#            attr2: attr2_value
#            ##after delattr##
#            attr1: attr1_value
