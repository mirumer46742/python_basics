# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "My name is '%s %s'" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "First Name: %r, Last Name: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "This function with one agrument as: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got no arguments"


print_two("Mir","Umer")
print_two_again("Mir Umer","Shafi")
print_one("First")
print_none()
