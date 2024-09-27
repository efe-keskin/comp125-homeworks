#Muhammed Efe Keskin 0083781 Comp125-03
# the purpose of this project is to implement a playlist that contains multiple songs.

# This function takes a list of songs together with the title, the release year,
# and the singer’s name of the song to be added. The liked flag should be set to
# False by default. If the song title does not exist in the playlist, the function
# adds a song list, which keeps the information about the song, to the end of
# the playlist. Otherwise, if the song title already exists in the playlist, the
# function does not add any song list to the playlist and displays a warning
# message (for the message format, see the output example of the test program
# given below). You may assume that the function arguments are always valid.
# That is, the title and the singer’s name are always strings, and the release
# year is always a positive integer.
def add_song(playlist, title, year, singer):
    l = [title.title(),year,singer, False]
    for i in range(len(playlist)):
        if playlist[i][0] == l[0]:
            print("This song already exists in the playlist")

    playlist.append(l)


# Write your code here
# ...
# This function takes a list of songs (playlist) together with the title of a
# song to be removed. If the song title exists in the playlist, the function
# removes the corresponding song list from the playlist. Otherwise, if the song
# title does not exist in the playlist, the function does not remove any song
# from the playlist and displays a warning message (for the message format, see
# the output example of the test program given below). You may assume that the
# song title argument is always a string. Remember that all song titles are
# unique and case insensitive.
def remove_song(playlist, title):
    for i in range(len(playlist)):
        if playlist[i][0] == title.title():
            playlist.remove(playlist[i])
            print("Song is removed")

    print("This song doesn't exist in the playlist")
 # Write your code here
 # ...
# This function takes a list of songs (playlist) together with the title of a
# song to be liked. If the song title exists in the playlist, the function
# likes the corresponding song list in the playlist. Otherwise, if the song
# title does not exist in the playlist, the function does not like any song
# in the playlist and displays a warning message (for the message format, see
# the output example of the test program given below). You may assume that the
# song title argument is always a string. Remember that all song titles are
# unique and case insensitive.
def like_song(playlist, title):
    for i in range(len(playlist)):
        if title.title() == playlist[i][0]:
            playlist[i][3] = True
        print("Song couldn't be found")



# Write your code here
# ...

# This function takes a list of songs (playlist) together with the title of a
# song to be unliked. If the song title exists in the playlist, the function
# unlikes the corresponding song list in the playlist. Otherwise, if the song
# title does not exist in the playlist, the function does not unlike any song
# in the playlist and displays a warning message (for the message format, see
# the output example of the test program given below). You may assume that the
# song title argument is always a string. Remember that all song titles are
# unique and case insensitive.
def unlike_song(playlist, title):
    for i in range(len(playlist)):
        if title.title() == playlist[i][0]:
            playlist[i][3] = False
        print("Song couldn't be found")
  # Write your code here
  # ...
  # This function takes a list of songs (playlist) and displays all song lists
  # found in the playlist according to the required output format. If there exist
  # no songs in the playlist, this function displays --EMPTY-- (see the output
  # example of the test program given below).
def display_all_songs(playlist):
    string = """PLAYLIST\n"""
    for i in range(len(playlist)):
        string += f"{playlist[i][0]} by {playlist[i][2]}\n"
    print(string)

# Write your code here
# ...
# This function takes a list of songs (playlist) and displays all liked songs
# in the playlist according to the required output format. If there exist
# no liked songs in the playlist, this function displays --EMPTY-- (see the
# output example of the test program given below).
def display_all_liked_songs(playlist):
    string = """LIKED PLAYLIST\n"""
    for i in range(len(playlist)):
        if playlist[i][3] == True:
            string += f"{playlist[i][0]} by {playlist[i][2]}\n"
    print(string)
 # Write your code here
 # ...
# This function takes a playlist together with the title of a song whose
# information will be showed. If the song title exists in the playlist,
# the function displays the information stored in the corresponding song list
# according to the required output format. If the title does not exist in the
# playlist, it displays a warning message (for the message format, see the output
# example of the test program given below). You may assume that the song title
# argument is always a string
def show_song(playlist, title):
    for i in range(len(playlist)):
        if playlist[i][0]==title.title():
            print(playlist[i])
  # Write your code here
  # ...
def main():
 L = []
 display_all_songs(L)
 print('---------------------------------')

 add_song(L, 'Feeling Good', 1965, 'Nina Simone')
 add_song(L, 'Dance Monkey', 2019, 'Tones and I')
 add_song(L, 'Sinnerman', 1962, 'Nina Simone')
 add_song(L, 'Batsin Bu Dunya Batsin', 1973, 'Orhan Gencebay')
 add_song(L, 'Bella Ciao', 2018, 'Manu Pilas')
 add_song(L, 'Bang Bang', 1966, 'Nancy Sinatra')
 display_all_songs(L)
 print('---------------------------------')

 add_song(L, 'Feeling Good', 2022, 'Somebody else')
 add_song(L, 'BElla CIAo', 2018, 'Manu Pilas')
 print('---------------------------------')
 display_all_songs(L)
 print('---------------------------------')
 display_all_liked_songs(L)
 print('---------------------------------')
 like_song(L, 'Feeling GOOD')
 like_song(L, 'Bella Ciao')
 like_song(L, 'BATSIN BU DUNYA BATSIN')
 display_all_liked_songs(L)
 print('---------------------------------')
 display_all_songs(L)
 print('---------------------------------')
 show_song(L, 'Bella Ciao')
 print('---------------------------------')
 show_song(L, 'SinnERMan')
 print('---------------------------------')
 show_song(L, 'Billie Jean')
 print('---------------------------------')

 show_song(L, 'Feeling Good')
 print('---------------------------------')
 unlike_song(L, 'Feeling Good')
 show_song(L, 'Feeling Good')
 print('---------------------------------')
 unlike_song(L, 'Sinnerman')
 display_all_liked_songs(L)
 print('---------------------------------')

 display_all_songs(L)
 print('---------------------------------')
 remove_song(L, 'BELLA Ciao')
 display_all_songs(L)
 print('---------------------------------')
 display_all_liked_songs(L)
 print('---------------------------------')
 show_song(L, 'Bella Ciao')
 remove_song(L, 'Billie Jean')
 print('---------------------------------')
 remove_song(L, 'Feeling Good')
 remove_song(L, 'Sinnerman')
 display_all_songs(L)
 print('---------------------------------')
 like_song(L, 'Sinnerman')
 print('---------------------------------')
 remove_song(L, 'Dance Monkey')
 remove_song(L, 'Bang BANG')
 remove_song(L, 'Batsin bu DUNYA BATSIN')
 display_all_songs(L)
 print('---------------------------------')

main()
