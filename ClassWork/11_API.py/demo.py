import requests

# data = requests.get("https://www.apicountries.com/countries")

# result = data.json()

# for i in result:
#     print(i['name'], i.get("capital"))

# data = requests.get("https://dummyjson.com/products").json()
# for i in  data.get("products"):
#     print(i.get("title"), i.get("price"))


city_name=input("Enter City Name:")
url=f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
data=requests.get(url).json()

for i in data.get("results"):
    print(i['latitude'],i['longitude'])

lat =i['latitude']
lng =i['longitude']
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid=f7e41ce7e70845cc2b06568cfc7cfb4c&units=metric"

data = requests.get(url).json()

print(data.get("name"))
print("temp : ",data['main']['temp'])
# print("pressure : ",data['main']['pressure'])
# print("Humidity : ",data['main']['humidity'])



# data=requests.get("https://dummyjson.com/products")

# result=data.json()

# for i in result:
#     print(i["title"],i.intget("price"))




