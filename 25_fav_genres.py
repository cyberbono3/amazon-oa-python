"""


Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.

Example 1:

Input:
userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output: {  
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}

Explanation:
David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.


"""

from collections import defaultdict

class Solution:
    def fav_genres(self, userSongs, songGenres):
        
        
        song_to_name = {}
        for name, song_list in userSongs.items():
            for song in song_list:
                song_to_name[song] = name
        
        dic = defaultdict(int)
        for genre, song_list in songGenres.items():
            for song in song_list:
                if song in song_to_name:
                    name = song_to_name[song]
                    dic[(name, genre)] += 1
        print(dic.items())
        # {David,Rock: 2, David,Techno:2, david, Jazz:1]
        sorted_dic = sorted(dic.items(), key = lambda x: x[1])
        
        most_popular = sorted_dic[-1][1]
        
        result = defaultdict(list)
        
        while sorted_dic and sorted_dic[-1][1] == most_popular:
            (name, genre), _ = sorted_dic.pop()
            result[name].append(genre)
        
        return result
        
sol = Solution()
userSongs = {"David": ["song1", "song2", "song3", "song4", "song8"],"Emma":  ["song5", "song6", "song7"]}
songGenres = { "Rock":["song1", "song3"],"Dubstep": ["song7"],"Techno":  ["song2", "song4"],"Pop": ["song5", "song6"],"Jazz":["song8", "song9"]} 
print(sol.fav_genres(userSongs,songGenres))        
                    
                    
                    
                
                
            
                
            
            