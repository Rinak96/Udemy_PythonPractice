import folium

map = folium.Map(location=[32.6778,35.2417])

map.add_child(folium.Marker(location=[32.6778,35.2417],popup="Hi this is my home town", icon=folium.Icon(color='red')))

map.save("Map1.html")