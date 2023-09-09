import requests
from datetime import datetime
# city,time,temprature,condition
# url="http://api.openweathermap.org/data/2.5/forecast?q=Washington&appid=26631f0f41b95fb9f5ac0df9a8f43c92&units=metric"
# content = requests.get(url).text
# soup= BeautifulSoup(content,'html.parser')
# print(soup[0])
# r=requests.get(url)
# content = r.json()
# weather_content = content['list']
# print(weather_content[0])
# for weather in weather_content:
#     print(weather['main'])
def get_weather(city,api_key='26631f0f41b95fb9f5ac0df9a8f43c92',units='metric'):
        url=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
        r=requests.get(url)
        content = r.json()
        weather_content = content['list']
        with open('weather_data.txt','a') as file:
            file.write("city,time,temprature,condition\n")
            for weather in weather_content:
                time=datetime.fromtimestamp(weather['dt'])
                file.write(f"{city},{time},{weather['main']['temp']},{weather['weather'][0]['description']}\n")
get_weather(city='Washington')