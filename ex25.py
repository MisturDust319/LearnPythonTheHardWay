def break_words(stuff):
	"""This function will break words for us"""
	return stuff.split(' ')

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""prints the 1st word after popping it off"""
	return words.pop(0)
	
def print_last_word(words):
	"""Prints the last word after poppping it off"""
	return words.pop(-1)
	
def sort_sentence(sentence):
	"""takes in a full sentence & returns the sorted words"""
	return sort_words(break_words(words))
	
def print_first_and_last(sentence):
	"""prints the first and last words of the sentence"""
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)