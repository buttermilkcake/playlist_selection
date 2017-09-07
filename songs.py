import random # imports the random module

songs = []
songs.append('Hey Joe')
songs.append('Cinnamin Girl')
songs.append('Heroes')
songs.append('Julie\'s Funky Jam')
songs.append('Songs for My Father')
songs.append('Brain Stew')
songs.append('Tubthumping')
songs.append('The Mighty Quinn')
songs.append('Gimme Some Lovin\'')
songs.append('Train Kept A-Rollin\' Yardbirds Version')
songs.append('Should I Stay or Should I Go')
songs.append('Windy')
songs.append('Sloopy')
songs.append('I\'m a Man Spencer Davis Group')
songs.append('Terrible Thing Booker T and the MG\'s')
songs.append('Brain Stew')
songs.append('London Calling')
songs.append('Tied to the Whipping Post')
songs.append('Manic Depression')
songs.append('Hoodoo Stew')
songs.append('Mississippi Queen')
songs.append('Burnin\' Sky')

rand_song = random.choice(songs)
print(rand_song)

