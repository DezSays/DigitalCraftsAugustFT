import requests     # Will need to work with API
import webbrowser   # Will need to open browser window

response = requests.get('http://randomfox.ca/floof') # Get the api you are going to work with
# print(response.json()) # See what data you are working with
cuteFox = response.json() # Assign a variable to our response.json so that we can read and manipulate the data
result = cuteFox['image'] # Assign a variable to what we want to pull out of our API, in this case we want the key from 'image'.
webbrowser.open(result)   # Webbrowser.open will allow us to open a browser window, pass in what you would like to see on the browser (in this case, it is result).