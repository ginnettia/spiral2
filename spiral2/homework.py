def spiralize(size, n=1):
    """ Your code goes somewhere in here"""
    return_value = n
    # theres a pattern in the matrix, once you make a square you need to increase distance between numbers by 2 
    # first I will need a starting variable to keep count
    start_number = n # since n will be counted in the calculation I need to start at n 
    # I need a variable for distance to keep track of the plus 2 each time a new square is made
    distance_between = 2 #start at 2 and we will need to add 2 once a new square is added 
    # I need a counter to count each time there is a set of 4 to increase the distance by 2 
    counter = 0
    # most likely use a While loop to count untill counter is equil to 4
        while starting number < """Had trouble coming up with this, but will need to relate to size""" size * size:
            start_number += distance_between
            #adding the first number to the first distance
            counter += 1 
            # adding 1 to counter untill sets of 4
            return_value = start_number + distance_between
            # updating the return value to reflect 
                if counter == 4 
                # need to increase distance when the counter hits 4
                    distance_between += 2
                    counter = 0 

            return return_value
