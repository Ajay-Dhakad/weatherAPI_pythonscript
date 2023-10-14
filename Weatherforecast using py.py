import requests

print("\n--------------------------------------WEATHER MAP---------------------------------------------")
city_name=input("\nEnter city name : ")
api=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=30d4741c779ba94c470ca1f63045390a")
data=api.json()

if data['cod']=="404":
    print("\nInvalid City Name ")
else:
    print("\nPOSITION")
    print(f"position of {city_name} is (longitude)",data['coord']['lon'])
    print(f"position of {city_name} is (latitude)",data['coord']['lat'])

    print("\nTEMPERATURE")

    tmp=data["main"]['temp']
    x=float(tmp-273.15)

    tmpmax=data["main"]['temp_max']
    y=float(tmpmax-273.15)

    tmpmin=data["main"]['temp_min']
    z=float(tmpmin-273.15)


    print(f"the current temperature of {city_name} is:",float(x),"Degree celcius")
    print(f"the current humidity of {city_name} is:",data['main']['humidity'])
    print(f"the current maximum temperature of {city_name} is:",float(y),"Degree celcius")
    print(f"the current minimum temperature of {city_name} is:",float(z),"Degree celcius")
print("\n------------------------------------------------------------------------------------------------------")
