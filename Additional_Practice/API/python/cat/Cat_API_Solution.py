# import requests     # Will need to work with API
# import webbrowser   # Will need to open browser window


# def kitty():
#     response = requests.get('https://api.thecatapi.com/v1/images/search?limit=5&breed_ids=aege') # Get the api you are going to work with, and in this case we want 5 cats and the Aegean breed
#     print(response.json()) # See what data you are working with
    
#     prettyKitty = response.json() # Assign a variable to our response.json so that we can read and manipulate the data

#     for i in range(len(prettyKitty)):     # Set up for loop 
#         if i <= 5:                        # As long as our position is less than 6 keep going
#             result = prettyKitty[i]['url']    # Set up variable to hold the url for each image in the index position of i
            
#             webbrowser.open(result)       # Open up a new page for each cat
#             i+=1                          # Increment your variable

# kitty()                                   # Call our function





 