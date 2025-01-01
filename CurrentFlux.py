import random
listA_Total = 0
##all_Decks = ["Astronomy", "Cthulhu", "Fantasy", "Jumanji", "Loonacy", "Marvel" , "Star", "Stoner", "Wonderland", "Zombie"]
all_Decks = ["Jumanji", "Loonacy", "Marvel" , "Star", "Stoner", "Wonderland", "Zombie"]

t_Decks = ["Astronomy", "Fantasy", "Jumanji"]
## t_Decks = ["Astronomy", "Fantasy", "Jumanji", "Loonacy","Loonacy", "Marvel" , "Wonderland", "Zombie"]
cur_Deck = []


answer = input("Is Trish playing tonight?\n")

if answer == "Yes":
 print("Nice. There are ",(len(t_Decks)),"in that Deck. Plus Lunacy listed twice") ## or current list = t_deck
 cur_Deck=t_Decks
elif answer == "No":
 print("Ok. In this case we are looking at ", (len(all_Decks)), "With a listing of ",(all_Decks),  "to play tonight") ## or cur_Deck  = all_decks
 cur_Deck=all_Decks
elif answer != ("Yes" or "No"):
 print('Please answer Yes or No')





print("Let's figure out what we are gonna play")
print(random.choice(cur_Deck))
