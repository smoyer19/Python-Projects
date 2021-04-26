

#Missing trailing comma ('one') will be returned as a string data type.
oneTuple = ('one',)
multiTuple = ('two', 'three', 'four')

#this will produce an error
result = oneTuple + multiTuple
print(result)
