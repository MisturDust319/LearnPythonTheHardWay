from sys import argv

if( len(argv) < 2 ):
	print("No args")
	print(input("tell me what to repeat once\n"))
elif( int(argv[1]) > 2 ):
	print("data overflow")
else:
	for i in range(0, int(argv[1])):
		print(input("arg: " + str(i + 1) + " input: "))