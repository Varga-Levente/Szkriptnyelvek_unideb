import json

class Movies(object):
    def __init__(self, id, title, rate, genres):
        self.id = id
        self.title = title
        self.rate = rate
        self.genres = genres

def MoviesDecoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Movies':
        return Movies(obj['id'], obj['title'], obj['rate'], obj['genres'])
    return obj

with open('filmek.json') as json_file:
    movieObj = json.load(json_file, object_hook=MoviesDecoder)

#Print all movies witch movie['genres'] contains "Animation" and get the highest rate
highestRate = 0
hishestRateMovie = None
print("Animation movies:")
for movie in movieObj:
    if "Animation" in movie['genres']:
        print("\t"+movie['title'])
        if(highestRate < movie['rate']):
            highestRate = movie['rate']
            hishestRateMovie = movie
print("\nThe highest rated animation movie is: "+hishestRateMovie['title']+" with rate: "+str(highestRate))