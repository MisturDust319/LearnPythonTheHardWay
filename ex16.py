from sys import argv

script, filename = argv

print("We will erase %r" %filename)
print("If you don't want to, hit CTRL-C (^C)")
print("If you do want to do tha, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, "r+")

target.seek(0)
print("file contents:\n")
target.read()

"""
print("truncating the file. gooodbye!")
target.truncate()

print("now input three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Writing these lines to the file")

target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

print("Finally we close it")
"""
target.close()
