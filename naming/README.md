Naming
=========


Style
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




Guide
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



Tips
---------

avoid generic names, build-in names(build-in type, module name).

	def compute(data): # too generic
		for element in data:
			yield element * 12

	def display_numbers(numbers): # better
		for number in numbers:
			yield number * 12

create unique names, add a post-underline for keywords.

	def xapian_query(terms, or_ = True):
		pass

`class` is always renamed to `klass` 



Practice
---------


**PARAMETER DESIGN:**
	
iterative design, parameter should reflect use scene, provide defaults as far as possible.


	class DB(object): 	#version 1
		def _query(self, query, type):
			print 'done'

		def execute(self, query):
			self._query(query, 'EXECUTE')


	import logging #version 2

	class DB(object):
		def _query(self, query, type, logger):
			logger('done')

		def execute(self, query, logger=logging.info):
			self._query(query, 'EXECUTE', logger)

	DB().execute('my query') #old style call
	DB().execute('my query', logging.warning)


**CLASSES DESIGN:**

represent it's type or character's suffix.

	SQLEngine
	MimeTypes
	StringWidgets
	TestCase

for base class, use `Base` or `Abstract` prefix.

	BaseCookie
	AbstractFormatter

avoid redundancy.

	SMTP.smtp_send() 	# redundancy with it's namespace
	SMTP.send()  		# better


**PACKAGES & MODULES DESIGN:**

lower case and no underline.

	sqlite
	postgres
	sha1

if it implemented a protocol, add `lib` suffix.

	import smtplib
	import urllib
	import telnetlib

keep uniformity in namespace.

	from widgets.stringwidgets import TextWidget # not good
	from widgets.strings import TextWidget # better