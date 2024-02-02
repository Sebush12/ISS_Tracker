# Dependencies
import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("There are currently" +
           str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]
for p in people:
    file.write(p["name"] + " - on board" + "\n")
    #print long and lad
g = geocoder.ip('me')
file.write("\n your current lat / long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

# set up the world map in turtle module
screen = turtle.Screen()
screen.setup(1280,720)
screen.setworldcoordinates(-180,-90,180,90)

#load world map image
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")

iss.setheading(45)
iss.penup()

input("Stop")

while True:
    #load the current status of the ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract ISS loaction

    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]

    #Output lat / lon to terminal
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # update ISS location on the map
    iss.goto(lon, lat)

    #Refresh every 5 secons
    time.sleep(5)
