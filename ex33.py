from sys import argv


def myLoop(n, l):
    """Loops n times incrementing the list l"""
    i = 0
    while i < n:
        print "At the top i is %d" % i
        l.append(i)
        i += 1
        print "Numbers now: ", l
        print "At the bottom i is %d" % i


# i = 0
numbers = []
l = numbers

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)

#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i

myLoop(int(argv[1]), numbers)

print "The numbers:"

for num in numbers:
    print num
