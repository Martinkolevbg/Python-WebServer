
# 1. Need function for  myltiplying any element in array and returning array.
# 2. define array
# 3. integers syntax. and "for" loops.

def calc(arr):
	myArray = []
	for element in arr:
		myArray.append(element*69)
	return myArray

userArray = [1,2,3,4,5]

print(calc(userArray))