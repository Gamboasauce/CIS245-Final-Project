import requests
from pprint import pprint #module providing pretty print capabilities

def zipcode_check(zip_code): #function checks length of zipcode
    if len(zip_code) != 5:
        return False 
    return True
    
def weatherapp():
    zip_code = input('Enter your Zip Code : ') #variable for zipcode

    if not zipcode_check(zip_code):
        print('zipcode invalid, Enter five digit zip code')
        return

    url = 'http://api.openweathermap.org/data/2.5/weather?zip={},us&appid=d2a06405be9a1197999ebfa4dd8406d8&units=imperial'.format(zip_code) #url for API link with API code and {} Zipcode and added units in imoerial for US

    res = requests.get(url) #requests using URL link

    data = res.json()

    temp = data['main']['temp'] #variable for temp
    wind_speed = data['wind']['speed'] #variable for Wind speed

    description = data['weather'][0]['description'] #forecast data

    print('Temperature : {} degrees'.format(temp)) #print temperature wind speed and forecast 
    print('Wind Speed : {} mph'.format(wind_speed)) 
    print('Forecast : {}'.format(description))

while True: #loop to run weather app function
    try:
        weatherapp()
        print('Connection Successful')
    except:
        print('Connection Unsuccessful, Zip code invalid')
    
    run_again = input('Would you like to run this program again? Type yes or no : ')

    if run_again == "no":
        break
    


