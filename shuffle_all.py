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

rand_song_blues = random.shuffle(list(blues.keys()))

songs_active = True
prompt = "\nWould you like to play a song?"
prompt += "\n(Enter 'quit' if you do not.)"

while True:
    ask = input(prompt)    

    if ask == 'quit':
        break
    else: 
        genre = input(
            "\nWhat genre would you like to play? (blues/ current/ punk/ reggae)")

if genre == 'blues':
    print(rand_song_blues)

