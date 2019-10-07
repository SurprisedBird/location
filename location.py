import requests

class Location():

    API_KEY = "AIzaSyBO4vjZjodHXbmIGjf4B2ZuXGZcYudiips"
    URL = "https://maps.googleapis.com/maps/api/geocode/json"

    def get_coordinats(URL=URL, API_KEY=API_KEY):
        lat = None
        lng = None
        address = str(input("Print address "))

        fool_url = f"{URL}?address={address}&amp&key={API_KEY}"
        request = requests.get(fool_url)
        results = request.json()

        lat = results["results"][0]["geometry"]["location"]["lat"]
        lng = results["results"][0]["geometry"]["location"]["lng"]
        print(lat, lng)

    
    def get_location(URL=URL, API_KEY=API_KEY):
        address = None
        lat = float(input("Print latitude "))
        lng = float(input("Print longitude "))

        fool_url = f"{URL}?latlng={lat},{lng}&amp&key={API_KEY}"
        request = requests.get(fool_url)
        results = request.json()
        address = results["results"][0]["formatted_address"]
        print(address)



    get_coordinats()
    get_location()





