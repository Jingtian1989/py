Naming
=========


Naming Style
---------


**CONSTANTS:**

uppercase and underline, centrally store them in a seperate file within a module. 

	from doctest import IGNORE_EXCEPTION_DETAIL


**VARIABLES (PUBLICS & PRIVATES):**

lowercase and one precursor-underline for changable and global variable which needed protecting.<br\>
one precursor-underline makes it a package private variable, and often setter & getter are provided<br\>
by the package.<br\>

	_observers = []
	def add_observer(observer):
		_observers.append(observer)
	def get_observers(observer):
		"""Makes sure _observers cannot be modified."""
		return tuple(_observers)

**PARAMETERS:**

lower case and underline if necessary.


**METHODS & FUNCTIONS:**

lower case and underline.


**NAMING MAILING:**

two precursor-underlined functions & variables in class will be name-mailed for avoiding name collision<br\>
in sub-classes.

	class A(object):
		def __a(self): #name-mailed to _A__a
			pass


**CLASSES:**

CamelCase style for class names.

	class Database(object):
		def open(self):
			pass


**ATTRIBUTES:**

lower case and underline for classes' attribute. usually nouns, adjectives and phrases.

	class Connection(object):

		def __init__(self):
			self._connected = []

		def connect(self, user):
			self._connected.append(user)

		def _connected_people(self):
			return '\n'.join(self._connected)

		connected_people = property(_connected_people)


**MODULES & PACKAGES:**

except the special module `__init__`, module names are usually un-underlined lower case.

	os; sys; shutil


naming for packages is the same as module.




Naming Guide
---------

**bool elements:**

`is` and `has` for bool variable.

	class DB(object):
		is_connected = False
		has_cache = False

**list elements:**

plural form for list variable.

	class DB(object):
		connected_users = ['Tarek']
		tables = {'Customer' : ['id', 'first_name', 'last_name']}


**directory elements:**

obvious names for directory variable.

	person_address = {'Bill':'6565 Monty Road', 
					  'Pamela': '45 Python stree'}

	person_address['Pamela']



Naming Tips
---------

avoid generic names, build-in names(build-in type, module name).

	def compute(data): # too generic
		for element in data:
			yield element * 12

	def display_numbers(numbers): # better
		for number in numbers:
			yield number * 12

create unique names, add a post-underline for keywords.

	def xapian_query(terms, or_True):
		pass

`class` is always renamed to `klass` 
