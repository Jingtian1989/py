Naming
=========

**CONSTANTS:**

uppercase and underline, centrally store them in a seperate file within a module. 

	from doctest import IGNORE_EXCEPTION_DETAIL


**PUBLICS & PRIVATES:**

lowercase and one precursor-underline for changable and global variable which needed protecting.<br\>
one precursor-underline makes it a package private variable, and often setter & getter are provided<br\>
by the package.<br\>

	_observers = []
	def add_observer(observer):
		_observers.append(observer)
	def get_observers(observer):
		"""Makes sure _observers cannot be modified."""
		return tuple(_observers)

**NAMING MAILING:**

two precursor-underlined functions & variables in class will be name-mailed for avoiding name collision<br\>
in sub-classes.

	class A(object):
		def __a(self): #name-mailed to _A__a
			pass
