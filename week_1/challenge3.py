# code to get the names of all scrappy squirrels in an astronaut suit in the first 200 squirrels
import requests

astronaut_suit=[]
error=[]

for i in range(2000):
    try:
        r = requests.get(f'https://scrappyart.s3.ap-south-1.amazonaws.com/json/{i}')
        for person in r.json()['attributes']:
            if person['trait_type'] == "Clothes" and "Astronaut"in person['value'] :
                astronaut_suit.append(r.json()["name"])
    except:
        error.append(r.json()["name"])
        continue

# save the list to a txt file.    
with open(r'c:\Users\olude\OneDrive\Documents\academics\stuff\The scrappy project\tsp_repository\week_1\astronaut_suit.txt', "w") as f:
    for s in astronaut_suit:
        f.write(str(s) +"\n")