# playlist_selection
Create a Python program that will randomly select a song to practice on my bass guitar from a list of songs.
I play bass guitar in a band called Sofa Locusts. We have a wide genre of songs we're in the process of learning - blues, funk, punk, reggae, classic rock, jam band, R&B. When I practice, I tend to keep choosing the same songs to practice and not branching out to explore and practice all the songs in our play list. To that end, I decided to create a program in Python that would randomly choose a song for me to practice from the playlist each time I practice. This will allow me to get a well-rounded exposure to all the songs and genres that we are learning, which will make me a better bass player and in turn will improve the band. 

As of Sept 15, 2017, I have created a dictionary of songs (dict_songs.py) that has a song title and the key to play it in as the key value pairs. When this program is run, it asks if the user would like to play a song. If the answer is yes, the program randomly chooses a song title (along with the key to play it in) for the user. If the answer is no, the program is just supposed to reply, 'ok, maybe tomorrow.' However when I choose No or no or N or n, the program still gives me a song title and the key to play it in and then says 'ok, maybe tomorrow.' I think it is doing it because of my random command that tells the program to choose a song randomly from the list. I need to find a way to combine that with just the yes response and separate it from the no response.

In addition to solving the issue in the previous paragraph, I want several dictionaries of songs sorted by genre (punk, blues, reggae...). Then I want the program to ask what genre the person wants to play, no requesting the same genre twice and then I want it to pull a song randomly from that genre. I'm not sure how to do that yet, I think nesting all of the dictionaries in a list might do it. Time will tell!

Sept 18, 2017 - I have created several dictionaries of songs based on genre today. I fixed the input issue I described earlier. It looks like nesting my dictionaries in a list won't work for my purposes, so I have listed each dictionary separately. I realize that the way I have set up the current file, songs.py, isn't working yet. Once the program goes thru the first layer of prompts and responses, it never moves on to the next layer - so this is my current challenge - I'm getting closer!

Sept 19, 2017 - YEE-HAW!!!! I have improved upon my design even in a sleep deprived state! sept19_songs_copy.py is the latest and greatest thus far. I honestly didn't think today's attempt was going to fly - I fully expected it to involve several days of tweaking - a true miracle. I'm not done and it's not without issues - if my response to the question 'Would you like to play?' is no, the program still gives me a song. This may have something to do with the fact that this program now involves 5 if statements in a row. This is still a work in progress. Stay tuned for more excitement! 

Sept 25, 2017 - Today is the day I fixed my glitch. I'm very happy about finishing strong on a Monday! In sept25_songs_copy.py I put in a break to exit the loop, so if the participant does not wish to play, they can enter quit and the program really ends. Now that I know it is working, I can fully expand all of my song genre dictionaries, save them as a separate module and import them into my program. I've decided not to limit how many times I can choose the same genre. 

I'm going to keep all iterations of this program in this repository to show how I worked through this challenge.

April 30, 2018 - I realized that previous versions of this song generator did not truly randomly choose from the lists of songs for each genre. If you chose the same genre several times in the row, it kept choosing the same song for you. I finally fingured out how to make the program truly choose songs at random in a particular genre. The version that works is called working_genre_song_generator.py 
