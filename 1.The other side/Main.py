from folium import Map
from Geopoint import Geopoint

latitude=float(input("Enter latitude:"))
longitude=float(input("Enter longitude:"))


antipode_latitude=latitude * -1


if longitude < 0.0:
    antipode_longitude=longitude+180
elif longitude==180:
    antipode_longitude=180
elif longitude>180:
    antipode_longitude="Invalid Coordinates"
else:
    antipode_longitude=longitude-180

location=list((antipode_latitude, antipode_longitude))

mymap = Map(location)
mymap.save(str("antipode.html"))

mypoint=Geopoint(antipode_latitude,antipode_longitude)
cp=mypoint.closest_parallel()
print(antipode_latitude)   
print(antipode_longitude)         
print("closest parallel is:",cp)
# print(mymap)                  
 