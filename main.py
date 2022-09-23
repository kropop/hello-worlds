# Hello, World!
# My first Python thing I wrote

# global varialbes for use later

name = 'krop'

# plain basic function call; not reusable

print("Hello, worlds!")


# defines the function with the variables it calls for

def just_says_hello():
    print("Hello, worlds!")


# this just calls the function I just wrote; does exactly what I did earlier except I can call it out multiple times

just_says_hello()

# now I'm gonna call it out but using a variable

print("Hello, " + name)


# mixing it up; gonna try a function that takes my variable and then mixes it up; then I'm gonna use it again later

def mixes_up_hello(x):
    # mixed_up_name = name * 3
    # this is a fun one, no idea why python has this functionality but whatever
    # I passed on the variable "name" and created a local variable, which is bad
    # so let's try returning the function's value
    # name = name * 3
    # return mixed_up_name
    # doesn't work either
    return x * 3


mixes_up_hello(name)

# not like this

print(mixes_up_hello(name))


# ah now that works

# the internet says the following stuff is very wrong and I should not ever do that


def mixes_up_hello_terrible():
    global name
    name = "very evil krop"
    return name


print(mixes_up_hello_terrible())

# very bad!
# now let's try user inputs

print("What number am I thinking of?")

number = input()

print("wow, you're good, the number really was " + str(number) + "!")

# I have also created a brand new super exciting development branch of this!