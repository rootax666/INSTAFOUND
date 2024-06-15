import instaloader
from instaloader import Profile
from instaloader.exceptions import LoginRequiredException, ProfileNotExistsException, ConnectionException
import getpass
import json
from datetime import datetime

def print_ascii_banner():
    banner = """
       _ _   _  _  _    _ _  _   _ _   _ ____  
      |_ _| \\ | / _|_   _|/ \\  |  _/ _ \\| | | | \\ | |  _ \\ 
       | ||  \\| \\___ \\ | | / _ \\ | |_ | | | | |  \\| | | | |
       |  |\\  |_)  |/ _ \\|  _|| |_| | |_| | |\\  | |_| |
      |_|_| \\_|/ |_/_/   \\_\\_|   \\_/ \\_/|_| \\_|__/ 
                                                          
                                            made by axpnr         
    """
    print(banner)

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def collect_profile_data(profile):
    data = {
        "username": profile.username,
        "full_name": profile.full_name,
        "biography": profile.biography,
        "followers": profile.followers,
        "followees": profile.followees,
        "posts": profile.mediacount,
        "profile_pic_url": profile.profile_pic_url,
        "external_url": profile.external_url,
    }

    followers = profile.get_followers()
    first_follower = next(followers, None)
    if first_follower:
        data["first_follower"] = {
            "username": first_follower.username,
            "full_name": first_follower.full_name
        }
    else:
        data["first_follower"] = None

    return data

def collect_posts_data(profile):
    posts = []
    for post in profile.get_posts():
        post_data = {
            "date": post.date.isoformat(),
            "caption": post.caption,
            "hashtags": post.caption_hashtags,
            "mentions": [user.username for user in post.tagged_users],
            "likes": post.likes,
            "comments": post.comments,
            "url": post.url,
        }
        posts.append(post_data)
    return posts

def associate_possible_accounts(profile):
    possible_accounts = []

    followees = profile.get_followees()
    for followee in followees:
        if followee.followers >= 1000:  # Example: filter by followers
            possible_accounts.append({
                "username": followee.username,
                "full_name": followee.full_name,
                "followers": followee.followers,
                "profile_pic_url": followee.profile_pic_url
            })

    return possible_accounts

def find_related_accounts(profile):
    related_accounts = []

    mutual_followers = profile.get_mutual_followers()
    for mutual in mutual_followers:
        related_accounts.append({
            "username": mutual.username,
            "full_name": mutual.full_name,
            "followers": mutual.followers,
            "profile_pic_url": mutual.profile_pic_url
        })

    return related_accounts

def get_instagram_data(target_username, my_username, my_password):
    L = instaloader.Instaloader()

    try:
        L.login(my_username, my_password)
        print("Login successful!")
    except Exception as e:
        print(f"Error during login: {e}")
        return

    try:
        profile = Profile.from_username(L.context, target_username)
        print(f"Profile @{target_username} loaded successfully!")
    except ProfileNotExistsException:
        print(f"Error: The profile @{target_username} does not exist.")
        return
    except LoginRequiredException:
        print("Error: Login required to access this profile.")
        return
    except ConnectionException:
        print("Error: Connection failed. Check your internet and try again.")
        return
    except Exception as e:
        print(f"Error loading the profile @{target_username}: {e}")
        return

    # Module choice after login
    try:
        module = int(input("Choose a module (1: Possible Accounts, 2: Related Accounts, 3: Complete Information): "))
    except ValueError:
        print("Invalid input. Choose between 1, 2, and 3.")
        return

    if module == 1:
        possible_accounts = associate_possible_accounts(profile)
        data = {"possible_accounts": possible_accounts}

    elif module == 2:
        related_accounts = find_related_accounts(profile)
        data = {"related_accounts": related_accounts}

    elif module == 3:
        profile_data = collect_profile_data(profile)
        posts_data = collect_posts_data(profile)
        data = {
            "profile_data": profile_data,
            "posts_data": posts_data
        }
    else:
        print("Invalid module. Choose between 1, 2, and 3.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{target_username}_data_{module}_{timestamp}.json"
    save_to_json(data, filename)
    print(f"Data saved in {filename}")

if __name__ == "__main__":
    print_ascii_banner()
    
    target_username = input("Enter the target profile username: ")
    my_username = input("Enter your Instagram username: ")
    my_password = getpass.getpass("Enter your Instagram password: ")

    get_instagram_data(target_username, my_username, my_password)
