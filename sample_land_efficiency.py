"""
Created on Mon Dec 4, 2017, 
Updated Jan 17, 2018, Sept 15, 2018, Sept 29 2018

 A simple program that calculates the predicted number of people that can be sustained
 with agriculture and livestock land (a hypothetical theory)
 
 Input: 
        Name of the plot of land to analyze (ie: West Plot A)
        Size of the plot of land (ie: square kms)
        Percentage of land that can be used for agriculture
        Percentage of land that can be used for livestock
        Percentage of fertilizer to use on agricultural land
        
 Output: Calculates the number of people that land can support in agriculture and livestock.
 A total of the two is also generated.
 
 The calculations are completed using the following 
     P = (A * S * 1.2) + (A * S * F * M)  + (L * S * 0.5)
     Where
     S = Square km available on the plot
     A = The portion (%) of land available for agriculture
     L = The portion (%) of the land is available to support livestock
     F= How much of the land which is available for agriculture is fertilized
     P = number of people supported by the land
     M = impact of fertilizer to food growth

@author: Jerry Jim
"""

#Get the name of the plot of land 
plot_name = input("Enter the name of your area being mapped: ")

#get the land size
land_size = float(input("What is the size of the mapped area (in square km):"))

#Get the percentage of agriculture land
agriculture = float(input("Enter percentage of the land that can be agriculture land:"))

#Get the percentage of land that is being fertilized
fertilizer = float(input("What percentage of the agriculture land can be fertilized:"))
multiplier = float(input("What is the impact of fertilizer (multiplier between 1.1 to 3.0):"))

#Get the percentage of land that is available for livestock
livestock = float(input("What percentage of the land can support livestock:"))

# Get the impact
impact = fertilizer * multiplier


#print the data that has been gathered
print("Data Entry Summary:")
print("Size of the Mapped area:", land_size)
print("Agriculture land percentage:", agriculture)
print("Percentage of agriculture land fertilized:", fertilizer)
print("Multiplier of fertilizer:", multiplier)
print("Livestock land percentage:", livestock)
print()

# Add the rest of the code for your program below

#Create a variable to store size of land for agriculture
agriculture_land = land_size * (agriculture / 100)
 

#create a variable to store the total impact of agriculture land with fertilizer
fertilizer_multiplier = impact/100

#Create a variable to store the livestock portion of the land
livestock_land = (livestock /100 * land_size)


#Create a variable to store total number of people the plot of land will support
ppl_agriculture = round(agriculture_land * 1.2 + (agriculture_land * fertilizer_multiplier), 3)
ppl_livestock = round(livestock_land * 0.5, 3)
ppl_total = round(ppl_agriculture + ppl_livestock, 3)


# Print the results


print("The name of the area being mapped:", plot_name)
print("The land can produce agriculture output to sustain", round(ppl_agriculture, 2), "people")
print("The land scan produce livestock output to support", round(ppl_livestock, 2), "people")
print("Overall, the land can produce enough food to support", round(ppl_total, 2), "people")

