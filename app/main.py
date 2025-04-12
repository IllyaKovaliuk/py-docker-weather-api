import requests
from dotenv import load_dotenv
import os


load_dotenv()
base_url = "http://api.weatherapi.com/v1"


def get_weather(city) -> None:
    api_key = os.getenv("api_key")
    url = f"{base_url}/current.json?key={api_key}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_info = response.json()
        city_name = weather_info['location']['name']
        country = weather_info['location']['country']
        localtime = weather_info['location']['localtime']
        temp_c = weather_info['current']['temp_c']
        print(f"City: {city_name}, Country: {country}, Local Time: {localtime}, Temperature: {temp_c}°C")
    else:
        return print("Failed to find data")



if __name__ == "__main__":
    get_weather("Paris")