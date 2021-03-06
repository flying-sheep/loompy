import logging
from typing import *
from inspect import currentframe, getouterframes


def deprecated(message: str) -> None:
	frameinfo = getouterframes(currentframe())
	logging.warn(f"╭── " + message)
	logging.warn(f"╰──> at {frameinfo[2].filename}, line {frameinfo[2].lineno}")


# def normalize_attr_strings(a: np.ndarray) -> np.ndarray:
# 	"""
# 	Take an np.ndarray of all kinds of string-like elements, and return an array of ascii (np.string_) objects
# 	"""
# 	if np.issubdtype(a.dtype, np.object_):
# 		if np.all([type(x) is str for x in a]) or np.all([type(x) is np.str_ for x in a]) or np.all([type(x) is np.unicode_ for x in a]):
# 			return np.array([x.encode('ascii', 'xmlcharrefreplace') for x in a])
# 		elif np.all([type(x) is np.string_ for x in a]) or np.all([type(x) is np.bytes_ for x in a]):
# 			return a.astype("string_")
# 		else:
# 			print(type(a[0]))
# 			raise ValueError("Arbitrary numpy object arrays not supported (all elements must be string objects).")
# 	elif np.issubdtype(a.dtype, np.string_) or np.issubdtype(a.dtype, np.object_):
# 		return a
# 	elif np.issubdtype(a.dtype, np.str_) or np.issubdtype(a.dtype, np.unicode_):
# 		return np.array([x.encode('ascii', 'xmlcharrefreplace') for x in a])
# 	else:
# 		raise ValueError("String values must be object, ascii or unicode.")


# def normalize_attr_array(a: Any) -> np.ndarray:
# 	"""
# 	Take all kinds of array-like inputs and normalize to a one-dimensional np.ndarray
# 	"""
# 	if type(a) is np.ndarray:
# 		return a
# 	elif type(a) is np.matrix:
# 		if a.shape[0] == 1:
# 			return np.array(a)[0, :]
# 		elif a.shape[1] == 1:
# 			return np.array(a)[:, 0]
# 		else:
# 			raise ValueError("Attribute values must be 1-dimensional.")
# 	elif type(a) is list or type(a) is tuple:
# 		return np.array(a)
# 	elif sparse.issparse(a):
# 		return normalize_attr_array(a.todense())
# 	else:
# 		raise ValueError("Argument must be a list, tuple, numpy matrix, numpy ndarray or sparse matrix.")


# def normalize_attr_values(a: Any) -> np.ndarray:
# 	"""
# 	Take all kinds of input values and validate/normalize them.
	
# 	Args:
# 		a	List, tuple, np.matrix, np.ndarray or sparse matrix
# 			Elements can be strings, numbers or bools
	
# 	Returns
# 		a_normalized    An np.ndarray with elements either float64 or unicode string objects
	
# 	Remarks:
# 		This method should be used to prepare the values to be stored in the HDF5 file. You should not
# 		return the values to the caller; for that, use materialize_attr_values()
# 	"""
# 	arr = normalize_attr_array(a)
# 	if np.issubdtype(arr.dtype, np.integer) or np.issubdtype(arr.dtype, np.floating):
# 		pass  # We allow all these types
# 	elif np.issubdtype(arr.dtype, np.character) or np.issubdtype(arr.dtype, np.object_):
# 		arr = normalize_attr_strings(arr)
# 	elif np.issubdtype(arr.dtype, np.bool_):
# 		arr = arr.astype('ubyte')
# 	return arr


# def materialize_attr_values(a: np.ndarray) -> np.ndarray:
# 	if np.issubdtype(a.dtype, np.string_):
# 		return np.array([html.unescape(x) for x in a.astype(str)], dtype=np.str_)
# 	elif np.issubdtype(a.dtype, np.str_) or np.issubdtype(a.dtype, np.unicode_):
# 		return np.array(a.astype(str), dtype=np.str_)
# 	else:
# 		return a

