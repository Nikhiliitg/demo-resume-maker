import instaloader

# Create an Instaloader object
bot = instaloader.Instaloader()

# Login to Instagram
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
bot.login(username, password)

# Download posts from a specific profile
profile_username = input("Enter the username of the profile you want to download posts from: ")

# Download the profile posts
try:
    bot.download_profile(profile_username, profile_pic_only=False)
    print(f"Downloaded posts from {profile_username}")
except Exception as e:
    print(f"Error: {e}")

