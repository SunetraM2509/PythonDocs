#Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to
#invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

guest = ["Anita", "Sameer","Jimmy", "Sony"]
print(guest)
message = guest[0].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[1].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[2].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[3].title() + " " + "You are cordially invited for dinner at my residence."
print(message)

#Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
 #	• Add a print statement at the end of your program stating the name of the guest who can’t make it.
 #	• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
 #	• Print a second set of invitation messages, one for each person who is still in your list.

guest = ["Anita", "Sameer","Jimmy", "Sony"]
print(guest)
print("Sameer is unable to make it to the dinner, so there is a new guest to be invited")
guest[1] = "Sunny"
print(guest)
message = guest[0].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[1].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[2].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[3].title() + " " + "You are cordially invited for dinner at my residence."
print(message)

#More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
 #	• Add a print statement to the end of your program informing people that you found a bigger dinner table.
 #	• Use insert() to add one new guest to the beginning of your list.
 #	• Use insert() to add one new guest to the middle of your list.
 #	• Use append() to add one new guest to the end of your list.
 #	• Print a new set of invitation messages, one for each person in your list.

guest = ["Anita", "Sunny","Jimmy", "Sony"]
print(guest)
print("I have recently found a new dinner table, so more guests are invited.")
guest.insert(0,"Joy")
guest.insert(3,"Rony")
guest.append("Minu")
print(guest)
message = guest[0].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[1].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[2].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[3].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[4].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[5].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[6].title() + " " + "You are cordially invited for dinner at my residence."
print(message)

#Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
 #	• Start with your program from Exercise 4-3. Add a new line that prints a message saying that you can invite only two people for dinner.
 #	• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print
 #	a message to that person letting them know you’re sorry you can’t invite them to dinner.
 #	• Print a message to each of the two people still on your list, letting them know they’re still invited.
 #	• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end
 #	of your program.

guest = ["Joy","Anita", "Sunny","Rony","Jimmy", "Sony","Minu"]
print(guest)
print("I have just been informed that the new table won't be arriving on time,so only two guests cam be invited")
print(guest.pop() + " " + "Sorry for inconvenience, you are not invited for dinner tonight.")
print(guest.pop() + " " + "Sorry for inconvenience, you are not invited for dinner tonight.")
print(guest.pop() + " " + "Sorry for inconvenience, you are not invited for dinner tonight.")
print(guest.pop() + " " + "Sorry for inconvenience, you are not invited for dinner tonight.")
print(guest.pop() + " " + "Sorry for inconvenience, you are not invited for dinner tonight.")
message = guest[0].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
message = guest[1].title() + " " + "You are cordially invited for dinner at my residence."
print(message)
del guest[1]
del guest[0]
print(guest)

#Seeing the World: Think of at least five places in the world you’d like to visit.
 #	• Store the locations in a list. Make sure the list is not in alphabetical order.
 #	• Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
 #	• Use sorted() to print your list in alphabetical order without modifying the actual list.
 #	• Show that your list is still in its original order by printing it.
 #	• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
 #	• Show that your list is still in its original order by printing it again.
 #	• Use reverse() to change the order of your list. Print the list to show that its order has changed.
 #	• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
 #	• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
 #	• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

 
world = ["Paris","Rome","Dubai","Singapore","Venice","Maldives"]
print(world)
sorted_list = sorted(world)
print("Sorted list : "+ str(sorted_list))
print("Original List : "+str(world))
world.reverse()
print("List in reverse order : "+str(world))
world.reverse()
print("List in original order : "+str(world))
world.sort(reverse = True)
print(world)