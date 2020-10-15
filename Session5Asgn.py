#Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
 #	• Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should
 #	have one line of output containing a simple statement like I like pepperoni pizza.
 #	• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines
 #	about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

pizzas = ["Pepperoni", "Cheese","Chicken", "Vegetable"]
for pizza in pizzas:
    print(pizza.upper())
for pizza in pizzas:  
    print("I like " + pizza.title() + " pizza.")
print(" I like cheese pizza the most. I also like pizza with new toppings. I love pizzas! ")

#Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
 #	• Modify your program to print a statement about each animal, such as
 #	A dog would make a great pet.
 #	• Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would
 #	make a great pet!

animals = ["Dog", "Cat", "Hamster"]
for animal in animals:
    print(animal.upper())
for animal in animals:
    print("A " + animal.title() + " would make a great pet.")
print(" All three animals are house pets. Any of these animals would make a great pet.")

#Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for value in range(1,21):
     print(value)

#One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by
#pressing ctrl-C or by closing the output window.)

# numbers = list(range(1,1000001))
# for number in numbers:
#     print(number)

#Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and
#ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

numbers = list(range(1,1000001))
#for number in numbers:
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers = list(range(1,20,2))
print(odd_numbers)

#Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

multiples = list(range(3,31,3))
print(multiples)

#Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
#is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

cubes = []
for value in range(1,11):
	cube = value**3
	cubes.append(cube)
print(cubes)

#Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubes = [value**3 for value in range(1,11)]
print(cubes)

#Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
 #	• Print the message, The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
 #	• Print the message, Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
 #	• Print the message, The last three items in the list are:. Use a slice to print the last three items in the list.

pizza = ["Pepperoni","Cheese","Chicken","Vegetable","BBQ","Sausage","Paneer"]
print("The first three items in the list are:")
print(pizza[0:3])
print("Three items from the middle of the list are:")
print(pizza[3:6])
print("The last three items in the list are:")
print(pizza[-3:])

#My Pizzas, Your Pizzas: Start with your program from Exercise 5-1. Make a copy of the list of pizzas, and call it friend_pizzas.
#Then, do the following:
 #	• Add a new pizza to the original list.
 #	• Add a different pizza to the list friend_pizzas.
 #	• Prove that you have two separate lists. Print the message, My favorite pizzas are:, and then use a for loop to print the first list. Print the message,
 #	My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
 #  Make sure each new pizza is stored in the appropriate list.

my_pizzas = ["Pepperoni", "Cheese","Chicken", "Vegetable"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("Sausage")
friend_pizzas.append("Paneer")
print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza.upper())
print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:  
    print(pizza.upper())