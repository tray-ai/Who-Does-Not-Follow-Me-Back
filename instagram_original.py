import json
from pathlib import Path

# Read the files with users I follow, and user who do not follow back.
following_path = Path('following.json')
follower_path = Path('followers_1.json')

try:
    read_following_file = following_path.read_text()
    read_follower_file = follower_path.read_text()
except FileNotFoundError:
    print('The file does not exist in current directory.')
else:
    following_content = json.loads(read_following_file)
    follower_content = json.loads(read_follower_file)

# Initiate lists for the followers and following users. 
following = []
followers = []

# Loop through the users I follow to append them to the following list.
for usernames in following_content['relationships_following']:
    names = usernames['string_list_data'][0]['value']
    #add these users to the 'following' list.
    following.append(names)

# Loop through user who follow me to append them to the followers list.
for usernames in follower_content:
    names = usernames['string_list_data'][0]['value']
    #add these users to the 'followers' list.
    followers.append(names)

# Compare lists for results of who does not follow me back.
for user in following:
    if user not in followers:
        print(user)