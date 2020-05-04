import json
import requests

weather_url = "http://api.openweathermap.org/data/2.5/forecast?zip=72761,us&APPID=8fc532fa1fa981e1237c5ce9ed510080&units=imperial"

def find_temps(data):
    # print(weather['list'][0]['main'])
    for x in data['list']:
        for key,value in x.items():
            if key == 'dt_txt':
                print(value.split(' ')[0])
            if key == 'weather':
                print( value[0]['description'].title() )


try:
  response = requests.get(weather_url)
  weather = json.loads(response.text)

  print(f" Hello there, the Weather in {weather['city']['name']} , {weather['city']['country']} is:" )
  # find_temps(weather)

  print(f"Temperature {weather['list'][0]['main']['temp']}" )
  print(f"However, it feels like {weather['list'][0]['main']['feels_like']}" )
  print(f"The weather has a {weather['list'][0]['weather'][0]['description']}" )

  listado = weather['list']
  diccionario = {}
 

  for datos in listado: 
    date = datos['dt_txt'].split()[0]
    if date in diccionario:
      if diccionario[date]["mintemp"] > datos ['main']['temp_min']:
         diccionario[date]["mintemp"] = datos ['main']['temp_min']
      if diccionario[date]["maxtemp"] < datos ['main']['temp_max']: 
         diccionario[date]["maxtemp"] = datos ['main']['temp_max']  
    else: 
      diccionario[date] = {"mintemp" : datos ['main']['temp_min'], "maxtemp" : datos ['main']['temp_max'] , "weather" : datos ['weather'][0]['description']}
 
 
  for smthdiccionario, valuev  in diccionario.items():
    print (smthdiccionario, "-", "Min Temp", valuev["mintemp"], ",Max Temp", valuev["maxtemp"], ",Weather", valuev["weather"].title())
 
  
except Exception as e:
  print(e)
