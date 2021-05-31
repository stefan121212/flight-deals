import requests

# my table of cheap flights
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/6e6a5f6df4aa7ab3d686fa50f49dc969/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/6e6a5f6df4aa7ab3d686fa50f49dc969/flightDeals/users"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data