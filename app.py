import datetime
import aiohttp
import asyncio
import os
from dotenv import load_dotenv

    
async def getWeather (key, city):
    
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}"
    
    try:
        
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                
                if response.status != 200:
                    raise Exception(f"Error: {response.status}, {response.reason}") 
                return await response.json()
      
    except aiohttp.ClientError as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Error: {e}")


async def main():
    load_dotenv()

    api_key = os.getenv('api_key')
        
        
    time = int(datetime.datetime.now().strftime("%H"))
    greeting = "good morning!" if time < 12 else "good afternoon!"

    print("Hello, " + greeting)

    city = input("Please, write your City:\n")

    try:
        weather_data = await getWeather(api_key, city)
        
        if weather_data:
            print("The weather condition is: ")
            print(weather_data.get('current', {}).get('condition', {}).get('text', "Not Available"))
    except Exception as e:
        print(f"Main Error: {e}")
    
    
asyncio.run(main())
    
    
    
    