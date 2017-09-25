import random # imports the random module

blues = {'Julie\'s r&b Turn Blues' : 'G', 'Julie\'s Funky Jam Blues' : 'G',
         'Little Red Rooster' : 'G', 'Basic 12-bar Blues' : 'Any'}

current = {'Sweet Jane' : 'D', 'Mighty Quinn' : 'G',
           'Heroes' : 'D', 'Hey Joe' : 'C', 'Gimme Some Lovin\'' : 'E',
           'Basic Blues Jam' : 'Any', 'Walk on the Wildside' : 'D or C',
           'Smokestack Lightning' : 'C', 'Secret Agent Man' : 'G'}

punk = {'Guns of Brixton' : 'F#', 'I Wanna be Sedated' : 'E',
        'Should I Stay or Should I Go?' : 'E', 'T.V. Eye' : 'G'}

reggae = {'No Woman No Cry' : 'C', 'Redemption Song' : 'G',
          'Bankrobber Dub' : 'G'}

rand_song_blues = random.choice(list(blues.items()))
rand_song_current = random.choice(list(current.items()))
rand_song_punk = random.choice(list(punk.items()))
rand_song_reggae = random.choice(list(reggae.items()))

songs_active = True
prompt = "\nWould you like to play a song?"
prompt += "\n(Enter 'quit' if you do not.)"

while True:
    ask = input(prompt)    

    if ask == 'quit':
        break
    else: 
        genre = input("\nWhat genre would you like to play? (blues/ current/ punk/ reggae)")
            
    if genre == 'blues':
        print(rand_song_blues)

    if genre == 'current':
        print(rand_song_current)

    if genre == 'punk':
        print(rand_song_punk)
        
    if genre == 'reggae':
        print(rand_song_reggae)

    

    

    

    

               
    
    

    




