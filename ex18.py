#uses an arbitrary number of args
def print_two(*args):
	arg1, arg2 = args
	print("arg1: %r, arg2: %r" %(arg1, arg2))

#uses two args, needs two
def print_two_again(arg1, arg2):
	print("arg1: %r, arg2: %r" %(arg1, arg2))
	
print_two("zed", "shaw")
print_two_again("zed", "shaw")