import pyshorteners

long_url = input("Enter the URL to shorten: ")

# Create an instance of Shortener
type_tiny = pyshorteners.Shortener()

# Shorten the URL using TinyURL
short_url = type_tiny.tinyurl.short(long_url)

# Display the shortened URL
print('The shortened URL is:', short_url)
