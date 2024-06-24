import json
from pathlib import Path

# read the file with the users I follow.
following_path = Path('following.json')
read_following_file = following_path.read_text()
following_content = json.loads(read_following_file)

# read the file user that follow me. 
follower_path = Path('followers_1.json')
read_follower_file = follower_path.read_text()
follower_content = json.loads(read_follower_file)


# initiate lists for the followers and following users. 
following = []
followers = []

# loop through the users I follow to append them to the following list.
for usernames in following_content['relationships_following']:
    names = usernames['string_list_data'][0]['value']
    #add these users to the 'following' list.
    following.append(names)

# loop through user who follow me to append them to the followers list.
for usernames in follower_content:
    names = usernames['string_list_data'][0]['value']
    #add these users to the 'following' list.
    followers.append(names)

# compare lists for results of who does not follow me back.
for user in following:
    if user not in followers:
        print(user)