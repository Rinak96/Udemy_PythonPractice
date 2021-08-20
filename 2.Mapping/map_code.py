import folium
import pandas as pd
import geopy
from geopy.geocoders import ArcGIS
import json

def color_producer(color_in_hebrew):
    if color_in_hebrew == "אדום":
        return 'red'
    elif color_in_hebrew == "ירוק":
        return 'green'
    elif color_in_hebrew == "צהוב":
        return 'yellow'
    elif color_in_hebrew == "כתום":
        return 'orange'
    else:
        return 'gray'

map = folium.Map(location=[32.6778,35.2417])
df = pd.read_csv("ramzor1908.csv")

nom = ArcGIS()
fg = folium.FeatureGroup(name="My Map")

data = json.load(open("world.json",'r',encoding='utf-8-sig'))
city_names = list(df["שם יישוב"])
colors = list(df["צבע לפי חישוב יומי"])

for city in city_names:
    location = nom.geocode(city)
    if location != None :
        latitude = location.latitude
        longitude = location.longitude
        color = df.at[(df[df['שם יישוב'] == city].index)[0],'צבע לפי חישוב יומי']
        fg.add_child(folium.CircleMarker(location=[latitude,longitude],radius = '6', fill_color = color_producer(color), fill_opacity = 0.8))
    
map.add_child(fg)
map.save("Corona_map_Israel.html")