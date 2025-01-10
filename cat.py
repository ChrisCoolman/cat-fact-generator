import json, requests, sys # import useful things

url = "https://meowfacts.herokuapp.com/" # website that gives cat facts

response = requests.get(url) # store website 
response.raise_for_status() # open website

# Uncomment to see the raw JSON text:
#print(response.text)  

catFact = json.loads(response.text) # loads json

fact = catFact['data'][0]  # turns fact into human readable string
print(fact) # print cat fact
f = open("catFacts.txt", "a") # create/use the catFacts.txt file
f.write("\n" + fact) # add a new cat fact
