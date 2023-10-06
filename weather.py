from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weatcher(city="Kansas City"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    weather_data = requests.get(request_url).json()
    
    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weatcher Conditions ***\n')
    
    city = input("\nPlease enter a City name: ")
    
    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Kansas City"
    
    weatcher_data = get_current_weatcher(city)
    
    print("\n")
    print(weatcher_data)