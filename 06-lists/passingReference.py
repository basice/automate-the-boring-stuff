# Passing Reference

# When function is called, the value of arguments are copied to the parameter variables.
# For the lists, a copy of the reference is used for the parameter
# The append(), extend(), remove(), sort(), reverse(), and other list methods
# modifiy their lists in place, directly.


def eggs(someParameter):
    someParameter.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)
