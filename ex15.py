from sys import argv
#import the argv (console args) from the
#	sys module

script, filename = argv
#save arg[0] (the script itself)
#	and the 1st arg (a filename)

txt = open(filename)
# open filename

print("Here's your file%r" % filename)
print( txt.read())
#print the filename and its contents

print("type filename again")
file_again = input("> ")
#get user input in script for a new file to open

txt_again = open(file_again)
#open a 2nd file

print( txt_again.read())
#output the 2nd file's contents

txt.close()
txt_again.close()
#close the files
