# Who Does Not Follow Me Back
 This script helps identify Instagram users you follow who do not follow you back. It reads data from JSON files containing your Instagram followers and following lists, then compares the two lists to highlight non-reciprocal follow relationships.

Data Files:

followers_1.json: This file contains the list of accounts that follow you on Instagram. It is in JSON format and is part of the data package you receive when you download your information from Instagram.

following.json: This file contains the list of accounts that you follow on Instagram. Similar to followers_1.json, this is in JSON format and can be obtained from your Instagram data download.

Python Files:

instagram_original.py: This is the original version of the code used for processing the JSON files. It includes all the operations in a single script without modularization. It’s useful for understanding the basic workflow before functions were introduced.

instagram_function.py: This module defines functions that are utilized to read the JSON files into Python objects. It helps in modularizing the code and making it reusable and cleaner.

instagram.py: This script contains the main logic for analyzing your Instagram followers and following lists. It uses the functions defined in ig_function.py to:

Load the JSON data into Python objects (dictionaries and lists).
Loop through these dictionaries to add the users to respective lists.
Determine which users you follow but who do not follow you back.