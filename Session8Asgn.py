#Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

name={'first_name': 'Priya','last_name': 'Sahoo','age': '21','city': 'Raipur'}
print(name['first_name'])
print(name['last_name'])
print(name['age'])
print(name['city'])

#Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. 
#Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. 
#For even more fun, poll a few friends and get some actual data for your program.

fav_name={'Priya': '11','Sunetra': '7','Jimmie': '18','Sania': '9','Manas':'4'}
print("Priya: "+fav_name['Priya'])
print("Sunetra: "+fav_name['Sunetra'])
print("Jimmie: " +fav_name['Jimmie'])
print("Sania: "+fav_name['Sania'])
print("Manas: "+fav_name['Manas'])

#Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
 #	• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, 
 #	and store their meanings as values.
 #	• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, 
 #	or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line 
 #	between each word-meaning pair in your output.

glossary={'List': 'A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements',
'Tuple': 'A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.',
'Dictionary': 'A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.',
'for loop': 'Looping statement',
'String': 'A string in Python is a sequence of characters.'}
print("List: "+glossary['List']+"\n")
print("Tuple: "+glossary['Tuple']+"\n")
print("Dictionary: "+glossary['Dictionary']+"\n")
print("for loop: "+glossary['for loop']+"\n")
print("String: "+glossary['String']+"\n")

#Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 8-3  by replacing your series of print
#statements with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your
#glossary. When you run your program again, these new words and meanings should automatically be included in the output.

glossary={'List': 'A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements',
'Tuple': 'A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.',
'Dictionary': 'A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.',
'for loop': 'Looping statement',
'String': 'A string in Python is a sequence of characters.',
'Data types': 'It is a type of data used of a variable',
'python': 'its a programming language',
'Java': 'Its an OOP Language',
'C': 'Its a basic programming language',
'Ruby': 'Its a outdated programmig language'}
for  keyprop,valueprop in glossary.items():
    print("key: "+keyprop.title()+"\ndefinition: "+valueprop+"\n")

#Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
 #	• Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
 #	• Use a loop to print the name of each river included in the dictionary.
 #	• Use a loop to print the name of each country included in the dictionary.
rivers={'Nile': 'Egypt','Mahanadi': 'India','Brahmaputra': 'Nepal'}
for river,countries in rivers.items():
    print(river.title()+" flows through the country "+countries+"\n")
for river in rivers.keys():
    print(river.title())
print("\n")
for countries in rivers.values():
    print(countries)

#Polling: Make a dictionary of favourite languages of people
 #	• Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
 #	• Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding.
 #	If they have not yet taken the poll, print a message inviting them to take the poll.

fav_lang={'Priya': 'Ruby','Sunetra': 'Python','Jimmie': 'Java','Sania': 'CSS','Manas':'HTML'}
for names,lang in fav_lang.items():
    print(names.title()+"'s favourite language is: "+lang)
print("\n")
namepoll=['Harry','Natasha','Reena','Steve','James','Vicky','Priya','Sunetra','Jimmie','Sania','Manas']
for name in namepoll:
    if name in fav_lang.keys():
        print(name+" you are in the poll")
    else:
        print(name.title()+" your fav language is?")


#People: Start with the program you wrote for Exercise 8-1. Make two new dictionaries representing different people, and store all three
#dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

people = []
person={'first_name': 'Priya','last_name': 'Sahoo','age': '21','city': 'Raipur'}
people.append(person)

person={'first_name': 'Sunetra','last_name': 'Mukherjee','age': '20','city': 'Bankura'}
people.append(person)

person={'first_name': 'Vicky','last_name': 'Raj','age': '22','city': 'Bhubaneshwar'}
people.append(person)
 
#for name in people:






#Pets: Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s
#name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.

pets = []
Rocky={'animal': 'dog','owner': 'John'}
pets.append(doggo)
Softy={'animal': 'Cat','owner': 'Nisha'}
pets.append(brain)
Chiku={'animal': 'rabbit','owner': 'Jessy'}
pets.append(fatty)

# for name in pets:
#     print(name.title()+"pet details are as follows")
#     for animal in 