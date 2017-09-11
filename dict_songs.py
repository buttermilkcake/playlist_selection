# Create dictionaries instead for the different gentres with each song paired
# with the key it is in. Create user input 'What genre do you want to play?'
# Don't allow person to request same genre 2 times in a row, have a message if
# they try 'I'm sorry, you need to choose a different genre this time.'
import random # imports the random module

current = {'Sweet Jane' : 'D', 'Mighty Quinn' : 'G',
           'Heroes' : 'D', 'Hey Joe' : 'C', 'Gimme Some Lovin\'' : 'E',
           'Basic Blues Jam' : 'Any', }


rand_song = random.choice(list(current.items()))
print(rand_song)

