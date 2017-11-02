import random

songs = {
    "Blues": [
        "Julie\'s r&b Turn Blues, key of G", "Julie\'s Funky Jam Blues, key of G",
         "Little Red Rooster, key of G", "Basic 12-bar Blues, any key"],
    "Punk": [
        "Guns of Brixton, key of F#", "I Wanna be Sedated, key of E",
        "Should I Stay or Should I Go?, key of E", "T.V. Eye, key of G"],
    "Reggae": [
        "No Woman No Cry, key of C", "Redemption Song, key of G",
          "Bankrobber Dub, key of G"]}

for key, value in songs.items():
    print(random.choice(value), key)
        
        
