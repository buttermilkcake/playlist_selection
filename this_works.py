import random 

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

songs_blues = random.choice(list(blues.items()))

songs_current = random.choice(list(current.items()))

songs_punk = random.choice(list(punk.items()))

songs_reggae = random.choice(list(reggae.items()))

songs_active = True
prompt = "\nWould you like to play a song? Enter no if you do not."

while True:
    ask = input(prompt)    

    if ask == 'no':
        break
    else: 
        genre = input(
            "\nWhat genre would you like to play? (blues/ current/ punk/ reggae)")

    if genre == 'blues':
        print(songs_blues)

    if genre == 'current':
        print(songs_current)

    if genre == 'punk':
        print(songs_punk)

    if genre == 'reggae':
        print(songs_reggae)

