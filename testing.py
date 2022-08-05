print('hello world!!!')

x = 1
y = 7.0

# indentation seems a little odd without curcly braces
if x == 1:
    print("x is 1")

# concatting things together, very similar to javascript
print("x is simply " + str(x) + " and why is simply " + str(y))

# conacting - mixing types
hello = "greeting young traveller!"
print(hello + " " + str(x) + str(y))

# -- Excerise
simpleString = "hello"
simpleFloat = 11.01
simpleInt = 8
if simpleString == "hello":
    print("string: %s" % simpleFloat)
if isinstance(simpleFloat, float) and simpleFloat == 11.01:
    print("Float: %f" % simpleFloat)
if isinstance(simpleInt, int) and simpleInt == 8:
    print("Int: %d" % simpleInt)

# -- Exercise 02
simpleArray = []
simpleArrayTwo = []
simpleArray.append('testing');
simpleArray.append('testing 02');
simpleArray.append('testing 03');

simpleArrayTwo.append('testing 04');
simpleArrayTwo.append('testing 05');

for x in simpleArray:
    print(x)
    if x == "testing 02":
        print('hooorah we have a miracle... NAWT!')

# -- Exercise 03
squaredNumber = 7 ** 2
cubed = 2 ** 22
print(squaredNumber)
print(cubed)

duplicateStrings = "testing " * 10
print(duplicateStrings)

mergedLists = simpleArray + simpleArrayTwo
print(mergedLists)

print([1, 2, 3] * 3)

x = object()
y = object()
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Fantastic!")

# -- Exercise 03
stageThreeName = "Julian"
stageThreeAge = 31
print("%s is %d years old." % (stageThreeName, stageThreeAge))

stageThreeList = [1, 2, 3]
print("A list: %s" % stageThreeList)

stageThreeData = ("Julian", "test", 41.99)
print("Hello %s %s. Your current balance is £%s." % stageThreeData)

# -- Exercise 04
stageFourString01 = "Hello World!"
stageFourString02 = "Hello World 'testing!!!!'"
print(len(stageFourString02))
print(stageFourString02.index("e"))