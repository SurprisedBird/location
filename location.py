import requests

class Location():

    API_KEY = "AIzaSyBO4vjZjodHXbmIGjf4B2ZuXGZcYudiips"
    URL = "https://maps.googleapis.com/maps/api/geocode/json"

    def get_coordinats(self):
        address = str(input("Print address "))

        fool_url = f"{self.URL}?address={address}&amp&key={self.API_KEY}"
        request = requests.get(fool_url)
        response = request.json()

        lat = response["results"][0]["geometry"]["location"]["lat"]
        lng = response["results"][0]["geometry"]["location"]["lng"]
        print(lat, lng)

    
    def get_location(self):
        lat = float(input("Print latitude "))
        lng = float(input("Print longitude "))

        fool_url = f"{self.URL}?latlng={lat},{lng}&amp&key={self.API_KEY}"
        request = requests.get(fool_url)
        response = request.json()
        address = response["results"][0]["formatted_address"]
        print(address)



location = Location()
location.get_coordinats()
location.get_location()





