##  distinctdict
##      make sure no two different key has the same value
class DistinctError(Exception):
    pass

class distinctdict(dict):
    def __setitem__(self, key, value):
        try:
            value_index = list(self.values()).index(value)
            existing_key = list(self.keys())[value_index]
            if existing_key != key:
                raise DistinctError("This value already exists for '%s'" % \
                                    str(self[existing_key]))

        except ValueError:
            pass

        super(distinctdict, self).__setitem__(key, value)
#test
mydict = distinctdict()
mydict['key'] = 'value'
mydict['other_key'] = 'value'

