from folium import Map



latitude=str("40.09") #latitiude
longitude=str("300.47") #longitude

antipode_latitude=latitude.__mul__(int(("-1")))


if longitude.__lt__(float("0")):
    antipode_longitude=longitude.__add__(float("180"))
elif longitude.__eq__(float("180")):
    antipode_longitude=float("180")
elif longitude.__gt__(float("180")):
    antipode_longitude=str("Invalid Coordinates")    
else:
    antipode_longitude=longitude.__sub__(float("180"))

location=list((antipode_latitude, antipode_longitude)) 

mymap = Map(location)    

print(antipode_latitude)   
print(antipode_longitude)                                   
                                   
 