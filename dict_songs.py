# Create dictionaries instead for the different gentres with each song paired
# with the key it is in. Create user input 'What genre do you want to play?'
# Don't allow person to request same genre 2 times in a row, have a message if
# they try 'I'm sorry, you need to choose a different genre this time.'
# Do I need to write a function and store my function in a module?

import random # imports the random module

reggae = {'No Woman No Cry' : 'C', 'Redemption Song' : 'G',
          'Bankrobber Dub' : 'G'}

current = {'Sweet Jane' : 'D', 'Mighty Quinn' : 'G',
           'Heroes' : 'D', 'Hey Joe' : 'C', 'Gimme Some Lovin\'' : 'E',
           'Basic Blues Jam' : 'Any', 'Walk on the Wildside' : 'D or C',
           'Smokestack Lightning' : 'C', 'Secret Agent Man' : 'G'}

rand_song = random.choice(list(current.items()))

ask = input("Would you like to play a song? ")
if ask == 'yes' or 'Yes' or 'Y' or 'y': 
    print(rand_song)

if ask == 'no' or 'No' or 'N' or 'n':
    print("Ok, maybe tomorrow!") 

