
# The Dictionary class is the same as dict with additional methods


class Dictionary(dict):

	def copy(self):
		return Dictionary(super().copy())

	# the map method allows you to run a function on all values of the dictionary
	def map(self, func, inplace = False):
		if inplace:
			copy = self
		else:
			copy = self.copy()

		try:
			for key in copy:
				copy[key] = func(copy[key])
		except TypeError:
			return False

		if inplace==False:
			return copy

	# based on a solution on stackoverflow:
	# https://stackoverflow.com/questions/12229064/mapping-over-values-in-a-python-dictionary

	@staticmethod
	def from_lists(keys, values = None):
		if values is None:
			values = keys

		return Dictionary(zip(keys, values))

	@staticmethod
	def from_dict(x):
		return Dictionary.from_lists(keys = x.keys(), values = x.values())

