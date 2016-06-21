ten_things = "apples oranges crows telephone light sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ")

more_stuff = ["day", 'night', 'song', 'frisbee', 'corn', 'banana', 'girl', 'boy']

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("Adding: ", next_one)
	stuff.append(next_one)
	print("There are now %d items" % len(stuff))
	
print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff)) #joins stuff's contents with spaces
print( '#'.join(stuff[3:5])) #joins stuff's 4th-5th item with '#'
