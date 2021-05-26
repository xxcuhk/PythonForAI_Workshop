import python_weather
from imdb import IMDb

def get_intent(prediction):
    return prediction["intent"]["intentName"]

def get_entity_type(prediction):
    if len(prediction["slots"] > 0):
        return prediction["slots"][0]["entity"]
    else:
        return None

def get_entity_value(prediction):
    if len(prediction["slots"] > 0):
        return prediction["slots"][0]["value"]["value"]
    else:
        return None


def get_current_weather(city, raw = False):

    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client()

    # fetch a weather forecast from a city
    weather = await client.find(city)

    # returns the current city temperature (int)
    if raw:
        return {"CurrentTemp": weather.current.temperature, "SkyCondition": weather.current.sky_text}
    else:
        print("The current temperature is" + str(weather.current.temperature) + "degrees Celcius")
        print("The weather condition is" + str(weather.current.sky_text))

    await client.close()
def get_movie_rating(movie_name):
    ia = IMDb()

    # get a movie and print its director(s)
    movie = ia.search_movie(movie_name)
    if (len(movie) == 0):
        print("No movie found with name"+ movie_name)
    else:
        movie = ia.get_movie(movie[0].movieID)
        print(movie_name + " got a rating of "+ str(movie["rating"]) + " out of 10")


def get_movie_directors(movie_name):
    ia = IMDb()

    # get a movie and print its director(s)
    movie = ia.search_movie(movie_name)
    if (len(movie) == 0):
        print("No movie found with name"+ movie_name)
    else:
        movie = ia.get_movie(movie[0].movieID)
        print("The director(s) of "+movie_name + " is/are:")
        for director in movie['directors']:
            print(director['name'])

def get_movie_cast(movie_name):
    ia = IMDb()

    # get a movie and print its director(s)
    movie = ia.search_movie(movie_name)
    if (len(movie) == 0):
        print("No movie found with name" + movie_name)
    else:
        movie = ia.get_movie(movie[0].movieID)
        print("The actors(s) in " + movie_name + " is/are:")
        for actor in movie['cast']:
            print(actor["name"] + " played the role of " + str(actor.currentRole))