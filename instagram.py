from instagram_function import read_files

# initiate lists for the followers and following users. 
following = []
followers = []

# call function for python object (dictionary)
following_content, follower_content = read_files('following.json', 'followers_1.json')

# loop through users in dictionary to add them to the following list.
for usernames in following_content['relationships_following']:
    names = usernames['string_list_data'][0]['value']
    following.append(names)

# loop through user in follower dictionary to add them to the followers list.
for usernames in follower_content:
    names = usernames['string_list_data'][0]['value']
    #add these users to the 'followers' list.
    followers.append(names)

# compare lists to find users who are not following back.
for user in following:
    if user not in followers:
        print(user)