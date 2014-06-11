Naming
=========

**CONSTANTS:**

 uppercase and underline, centrally store them in a seperate file within a module. 

	from doctest import IGNORE_EXCEPTION_DETAIL


**PUBLICS & PRIVATES:**

 lowercase and precursor-underline for changable and global variable which needed protecting.
 a precursor-underline makes it a package private variable. 
 and often setter & getter are provide by the package.

	_observers = []
	def add_observer(observer):
		_observers.append(observer)
	def get_observers(observer):
		"""Makes sure _observers cannot be modified."""
		return tuple(_observers)
