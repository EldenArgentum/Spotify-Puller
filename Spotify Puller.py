import requests
import base64
import requests
import json

# user_id = str(input("What is your Spotify ID?"))

# user_id = https://open.spotify.com/user/grmujbo3xangppoykzkko5cn7?si=99200bfd86144eb8
# url = f"https://api.spotify.com/v1/users/{user_id}"
# redirect_uri = "http://127.0.0.1:5500/GitKraken%20Stuff/Spotify%20Puller/"

CLIENT_SECRET = "fcdb0dc9da2f41e8ad3c2c506fccf12f"
ACCESS_TOKEN = "BQCLbkmCodTHWScPXYb3JoQLz6UPTd1WOjZOxlOiIUTXmRY2m-FV53F-NPpGQz2Dp2hYZ3mUIvIvvzj-38fR-WaAVZNFIIgkbFzQ8Dy2VrsSpCCEiw5uTpBuKYx8GuQuwox83zybbP62mOzhXStVTwMbXir-fxhwhskQ0vxeoE8EAYrQVr2ijMv6dzQCndHkMS7IAUlONBb3cfb3ig"
CLIENT_ID = "9f9d70512af64b7c9f3775b8de528ffc"

# response = requests.get(url)

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
    json_result_listeners = json.loads(result.content)['artists']['items'][0]['followers']['total']
    json_result_genres = json.loads(result.content)['artists']['items'][0]['genres']
    print(json_result)
    print(f"{artist_name} has {json_result_listeners} followers.")
    print(f"{artist_name}'s music is under the genres {json_result_genres}")
    

token = get_token()

search_artist(token, "BTS")