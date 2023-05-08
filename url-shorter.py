import pyshorteners as pys

# To obtain an API key, you should visit the website 'https://app.bitly.com'

s = pys.Shortener( api_key = "Api-Key")

url = "http://www.example.com"

short_url = s.bitly.short(url)

print(short_url)

# Export : https://bit.ly/Example