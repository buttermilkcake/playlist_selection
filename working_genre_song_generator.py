import random 

blues = ['Julie\'s r&b Turn Blues, Key of G',
         'Julie\'s Funky Jam Blues, Key of G',
         'Little Red Rooster, Key of G', 'Basic 12-bar Blues, Any Key']

current = ['Sweet Jane, Key of D', 'Mighty Quinn, Key of G', 'Heroes, Key of D',
           'Hey Joe, Key of C', 'Gimme Some Lovin\', Key of E',
           'Walk on the Wildside, Key of D or C',
           'Smokestack Lightning, Key of C', 'Secret Agent Man, Key of G']

punk = ['Guns of Brixton, Key of F#', 'I Wanna be Sedated, Key of E',
        'Should I Stay or Should I Go?, Key of E', 'T.V. Eye, Key of G']

reggae = ['No Woman No Cry, Key of C', 'Redemption Song, Key of G',
          'Bankrobber Dub, Key of G']

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
        print(random.choice(blues))

    if genre == 'current':
        print(random.choice(current))

    if genre == 'punk':
        print(random.choice(punk))
        
    if genre == 'reggae':
        print(random.choice(reggae))
