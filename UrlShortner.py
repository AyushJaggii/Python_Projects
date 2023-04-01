# Importing the PyShorteners library
import pyshorteners

# Taking input of the long URL from the user
url = input("Enter Url: \n")

# Using the PyShorteners library to create a short URL for the long URL provided by the user
short_url = pyshorteners.Shortener().tinyurl.short(url)

print("New Short URL: " ,short_url)

