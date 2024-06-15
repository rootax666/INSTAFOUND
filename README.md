INSTAFOUND
INSTAFOUND is a Python script designed to gather detailed data from Instagram profiles using the Instaloader library. This tool provides insights into a target profile's basic information, posts, and relationships with other accounts.

Features
Profile Information Collection: Retrieve detailed information about a target Instagram profile, including username, full name, biography, followers, followees, number of posts, profile picture URL, and external URL.
Post Data Collection: Gather data from the posts of a target profile, including date, caption, hashtags, mentions, likes, comments, and URL.
Possible Accounts Association: Identify and collect data on accounts that the target profile follows and that have a significant number of followers (e.g., more than 1000 followers).
Related Accounts Identification: Find and collect data on mutual followers of the target profile.
Requirements
Python 3.6 or higher
Instaloader library
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/rootax666/instafound.git
cd instafound
Install the required Python packages:

sh
Copy code
pip install instaloader
Usage
Run the script:

sh
Copy code
python INSTAFOUND.py
Follow the prompts to enter the target profile username, your Instagram username, and your Instagram password.

Choose a module:

1: Possible Accounts
2: Related Accounts
3: Complete Information
The data will be collected and saved in a JSON file with a timestamp.

Example
The script will display an ASCII banner and prompt you for the target profile username, your Instagram username, and your Instagram password.

After successful login, you will be asked to choose one of the following modules:

1: Possible Accounts
2: Related Accounts
3: Complete Information
The script will then collect the data based on the chosen module and save it in a JSON file with a timestamp.

Sample Output
The JSON output will be saved in the format: <target_username>_data_<module>_<timestamp>.json.

Here is an example of the JSON structure for the complete information module:

json
Copy code
{
    "profile_data": {
        "username": "example_user",
        "full_name": "Example User",
        "biography": "This is an example bio",
        "followers": 1500,
        "followees": 300,
        "posts": 50,
        "profile_pic_url": "https://example.com/profile_pic.jpg",
        "external_url": "https://example.com",
        "first_follower": {
            "username": "follower_user",
            "full_name": "Follower User"
        }
    },
    "posts_data": [
        {
            "date": "2023-06-13T12:34:56",
            "caption": "This is an example post",
            "hashtags": ["#example", "#post"],
            "mentions": ["mentioned_user"],
            "likes": 100,
            "comments": 10,
            "url": "https://instagram.com/p/example"
        }
    ]
}
Contributing
Contributions are welcome! If you have any suggestions, bug reports, or improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Instaloader - A powerful tool to download Instagram photos, videos, and metadata.
