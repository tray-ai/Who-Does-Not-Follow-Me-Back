import json
from pathlib import Path

def read_files(following_file, followers_file):
    '''Read the files and return the Python Object'''

    # read the file with the users I follow.
    following_path = Path(following_file)
    read_following_file = following_path.read_text()
    following_content = json.loads(read_following_file)

    # read the file user that follow me. 
    follower_path = Path(followers_file)
    read_follower_file = follower_path.read_text()
    follower_content = json.loads(read_follower_file)

    return following_content, follower_content