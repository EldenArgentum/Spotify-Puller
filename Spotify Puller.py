import requests
import base64
import requests
import json
import KeyStuff as KS
print()
# user_id = str(input("What is your Spotify ID?"))

# user_id = https://open.spotify.com/user/grmujbo3xangppoykzkko5cn7?si=99200bfd86144eb8
# url = f"https://api.spotify.com/v1/users/{user_id}"

CLIENT_SECRET = KS.CLIENT_SECRET
ACCESS_TOKEN = KS.ACCESS_TOKEN
CLIENT_ID = KS.CLIENT_ID

# response = requests.get(url)
artist_name = ""

def get_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = { 
        "Authorization" : "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    
    token = json_result["access_token"]
    
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    
    query_url = url + query
    result = requests.get(query_url, headers = headers)
    json_result = json.loads(result.content)['artists']['items']
    # json_result_listeners = json.loads(result.content)['artists']['items'][0]['followers']['total']
    # json_result_genres = json.loads(result.content)['artists']['items'][0]['genres']
    
    if len(json_result) == 0:
        print("There are no artists with this name.")
        return None
    return json_result
    # print(f"{artist_name} has {json_result_listeners} followers.")
    # print(f"{artist_name}'s music is under the genres {json_result_genres}.")

def artist_followers(token):
    global artist_name
    
    if artist_name == "":   #So it doesn't have to ask you which artist you are searching for each piece of information
        artist_name = str(input("What artist would you like to lookup?\t"))
    
    artist_search = search_artist(token, artist_name)
    
    if artist_search == None:
        print("There are no artists with that name.")
        return None
    
    return f"{artist_name} has {artist_search[0]['followers']['total']} followers."

def artist_genres(token):
    global artist_name
    
    if artist_name == "":   #So it doesn't have to ask you which artist you are searching for each piece of information
        artist_name = str(input("What artist would you like to lookup?\t"))
    
    artist_search = search_artist(token, artist_name)
    
    if artist_search == None:
        print("There are no artists with that name.")
        return None
    
    return f"{artist_name}'s music is under the genres {artist_search[0]['genres']}."

token = get_token()

userInput = ""

print("If, at any time, you would like to quit the program, type Q or q to quit.")

while userInput.upper() != "Q":
    print()
    userInput = str(input("What feature would you like to use?\n1: View the amount of monthly listeners of an artist\n2: View the genres for the artist\nType in the number of the feature you would like to use, then click enter.\n"))
    if userInput == "1":
        print(artist_followers(token))
    if userInput == "2":
        print(artist_genres(token))
    else:
        print("Sorry, that isn't an option. Please try again.")

exit()
# artistFollowers = artist_followers(token)
# print(artistFollowers)

# artistGenres =  artist_genres(token)
# print(artistGenres)