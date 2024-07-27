import json
from pathlib import Path

def read_files(file):
    """Read the files and return the Python Object"""

    # Read the file with the users I follow.
    path = Path(file)
    try:
        read_file = path.read_text()
    except FileNotFoundError:
        print(f'The file {path} is not available.')
    else:
        content = json.loads(read_file)
        
    return content