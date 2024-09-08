import instaloader

def get_following(L, username):
    """Get the list of usernames the given user is following."""
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        following_list = [followee.username for followee in profile.get_followees()]
        return set(following_list)
    except instaloader.exceptions.LoginRequiredException as e:
        print("Login required: ", e)
        return set()

def get_followers(L, username):
    """Get the list of followers for the given user."""
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        followers_list = [follower.username for follower in profile.get_followers()]
        return set(followers_list)
    except instaloader.exceptions.LoginRequiredException as e:
        print("Login required: ", e)
        return set()

def find_non_followers(following_list, followers_list):
    """Find users who are in the following list but not in the followers list."""
    non_followers = following_list - followers_list
    return non_followers

def main():
    username = "your_instagram_username"  # Replace with your Instagram username
    password = "your_instagram_password"  # Replace with your Instagram password

    # Initialize Instaloader and log in
    L = instaloader.Instaloader()
    try:
        L.login(username, password)
        print("Logged in successfully.")
    except instaloader.exceptions.BadCredentialsException as e:
        print("Login failed: ", e)
        return

    # Get following and followers
    following_list = get_following(L, username)
    followers_list = get_followers(L, username)

    # Find and display non-followers
    non_followers = find_non_followers(following_list, followers_list)
    print("Users who don't follow you back:")
    for user in non_followers:
        print(user)

if __name__ == "__main__":
    main()
