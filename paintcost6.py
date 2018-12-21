# A program that computes the cost of painting a room with four walls
#
# Input: the dimensions of the room 
#        the price of paint per gallon
#        the cost of labour per hour
#        
# Output: the cost to paint the walls of the room broken down in paint and labour costs
#
# The painting company has detetmined that for every 50 square feet of wall 
# they need 1 gallon of paint and 5 hours of labour. 
#
# Functions

# ***** Return 0 if any of the arguments is 0 or negative.
# ***** Add the ceiling area to the room's wall area
# Updated:  J. Jim Sept 2018 for 2018W1

def wall_area(length, width, height):
    ''' 
    (float, float, float) -> float
    
    length, width, height >= 0
        
    Calculates the wall area as well as the ceiling of a room with the given length, width and height.
    
    >>> wall_area(0, 0, 0)
    0.0

    >>> wall_area(10, 10, 10)
    500.0
    >>> wall_area(10, 10, 0)
    0
    >>> wall_area(10, 0, 10)
    0
    >>> wall_area(0, 10, 10)
    0
    '''
    
    if length <= 0:
        return 0
    elif width <=0:
        return 0
    elif height <=0: 
        return 0
    else:
        wall_1 = length * height
        wall_2 = width * height
        ceiling = length * width 
        return (2* wall_1) + (2 * wall_2) + ceiling



# ***** Modify paint_cost to return 0 if any of its arguments is not positive

def paint_cost(area, paint_price):
    ''' 
    (float, float) -> float
    
    area > 0 and paint_price > 0
    
    Calculates the cost for the paint needed to paint the given area. 
    paint_price is the price of one gallon of paint.
    
    >>> paint_cost(0, 0)
    0.0
    >>> paint_cost(50, 10)
    10.0
    >>> paint_cost(200, 10)
    40.0
    >>> paint_cost(200, 0)
    0
    >>> paint_cost(0, 10)
    0
    '''
    
    if paint_price <= 0:
        return 0
    elif area <= 0:
        return 0
    else:
        
        gallons = area / 50
        return gallons * paint_price


# ***** Modify labour_cost to return 0 if any of its arguments is not positive

def labour_cost(area, labour_price):
    ''' 
    (float, float) -> float
    
    area > 0 and labour_price > 0
    
    Calculates the labour cost for painting the given area 
    labour_price is the labour cost per hour.
    
    >>> labour_cost(0, 0)
    0.0
    >>> labour_cost(50, 10)
    50.0
    >>> labour_cost(200, 10)
    200.0
    >>> labour_cost(200, 0)
    0
    >>> labour_cost(0, 10)
    0
    '''
    
    if area <= 0:
        return 0
    elif labour_price <= 0:
        return 0
    else:
        
        hours = (area / 50) * 5
        return  hours * labour_price
    
# ***** Complete the docstring and the code for this function which 
# ***** returns the tax for the given amount and tax_rate
# ***** tax should return 0 if any of its arguments is not positive

def tax(amount, tax_rate) :
     
    return 0     # need to chang this


# MAIN PROGRAM 

# Paint price per gallon
paint_price = float(input("Enter paint price per gallon: "))

# Labour cost per hour
labour_price = float(input("Enter labour price per hour: "))

print()

# ***** Modify the program to culculate a 5% gst tax on labour and 7% pst tax  
# ***** on the paint and add it to the total cost for the room.
# *****
# ***** Modify the program to keep calculating and displaying costs for a 
# ***** number of rooms until the user enters 0 for the rooms length.
# *****
# ***** Modify the program to accumulate the total costs for the rooms we want to paint
# ***** and print at the end the number of room, the total cost for all rooms and 
# ***** the average cost per room (total cost / rooms).


# Get room dimentions and estimate the cost.

room_length = float(input("Enter room's length: "))    
room_width = float(input("Enter room's width: "))
room_height = float(input("Enter room's height: "))

# Total area for painting
total_area = wall_area(room_length, room_width, room_height)
print( "Total area is :", total_area) 

# Calculate the cost of paint needed
cost_for_paint = paint_cost(total_area, paint_price)
print( "Paint cost is:", cost_for_paint)

# Calculate labour cost
cost_for_labour = labour_cost(total_area, labour_price)
print( "Labour cost is:", cost_for_labour)

# Calculate total cost
total_cost = cost_for_paint + cost_for_labour
print( "Total cost is:", total_cost)

print() 

print( "Bye now. Hope to hear from you soon")
    
