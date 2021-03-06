# Pajama Programmer
# Coding Dojo - July 5 Online Flex
# 2-August-2016
# Assignment: Stars

# Part 1
# Create a function called  draw_stars() that takes a list of numbers and prints out*.


def draw_stars(x):
    print ''
    for num in x:
        print num*'*'
        
x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

# Part 2
# Modify the function above. Allow a list containing integers and strings to be passed to the  draw_stars() function.
# When a string is passed, instead of  displaying *, display the first letter of the string according to the example below.
# You may use the .lower() string method for this part.

def draw_stars2(x):
    print ''
    for item in x:
        if isinstance(item, int):
            print item*'*'
        else:
            print item[0].lower()*len(item)


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)
