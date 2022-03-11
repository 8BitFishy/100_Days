import requests
from tkinter import *

def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_json = response.json()
    iss_position = (float(iss_json["iss_position"]["latitude"]), float(iss_json["iss_position"]["longitude"]))
    print(iss_position)
    return iss_position


ip = requests.get('https://ipapi.co/ip/').text
response = requests.get(url=f"http://ip-api.com/json/{ip}")
ip_json = response.json()
my_position = (float(ip_json["lat"]), float(ip_json["lon"]))
print(ip_json["city"])
print(my_position)

imagesize = [1439, 720]

window = Tk()
window.title("Find Position")
window.config(width=imagesize[0]+50, height=imagesize[1]+50, padx=50, pady=50)


canvas = Canvas(width=imagesize[0], height=imagesize[1])
backgroundimage = PhotoImage(file="rect1389_resized.png")
#backgroundimage = backgroundimage.subsample(2, 2)
canvas.create_image(imagesize[0]/2, imagesize[1]/2, image=backgroundimage)
canvas.grid(row=0, column=0)

def refresh():
    global update
    new_iss_position = get_iss_position()
    new_iss_coords = degreestocoords([new_iss_position[0], new_iss_position[1]])
    if abs(new_iss_coords[0] - iss_coords[0]) < 10 and abs(new_iss_coords[1] - iss_coords[1] < 10):
        canvas.create_line(iss_coords[0], iss_coords[1], new_iss_coords[0], new_iss_coords[1], fill="black", width=3)
    else:
        print("Jumping across map")
    move_coords = [new_iss_coords[0] - iss_coords[0], new_iss_coords[1] - iss_coords[1]]
    print(f"Moving by ({move_coords[0]}, {move_coords[1]})")
    canvas.move(item, move_coords[0], move_coords[1])
    iss_coords[0] = new_iss_coords[0]
    iss_coords[1] = new_iss_coords[1]
    update = window.after(10000, refresh)
    return

def manual_refresh():
    window.after_cancel(update)
    refresh()

def invertvalues(values):
    newvalues = values.copy()
    newvalues.reverse()
    return newvalues

def degreestocoords(degrees):
    print(f"\nImage size = {imagesize}\nImage centre = ({imagesize[0]/2}, {imagesize[1]/2})")
    print(f"Converting - {degrees}")
    coords = [0, 0]
    imagecoords = invertvalues(imagesize)
    print(f"Image coordinates = {imagecoords}")
    for i in range(len(degrees)):
        if i == 0:
            print("\n\nLatitude:")
        else:
            print("\n\nLongitude:")
        degreerange = 360
        multiplier = 1
        offset = 0

        if i == 0:
            degreerange = 180
            multiplier = -1

        pxperdeg = imagecoords[i] / degreerange
        print(f"Pixels per degree:\n{imagecoords[i]} / {degreerange} = {pxperdeg}")

        if degrees[i] != 0:
            offset = degrees[i] * pxperdeg * multiplier
            print(f"Offset:\n{degrees[i]} * {pxperdeg} * {multiplier} = {offset}")

        else:
            pass


        coords[i] = ((imagecoords[i] / 2) + (offset))
        print(f"Coordinate:\n{imagecoords[i]/2} + {offset} = {coords[0]}")
    coords = invertvalues(coords)
    return coords

'''
for i in range(1):
    coord = degreestocoords([25.373, 127.2629])
    coord1 = degreestocoords([my_position[0], my_position[1]])
    print(f"Plotting line from {coord[0]}, {coord[1]} to {coord1[0]}, {coord1[1]}")
    canvas.create_line(coord[0], coord[1], coord1[0], coord1[1], fill="black", width=3)
'''

iss_position = get_iss_position()
iss_coords = degreestocoords([iss_position[0], iss_position[1]])
issimage = PhotoImage(file="iss.png")
issimage = issimage.subsample(30, 30)
item = canvas.create_image(iss_coords[0], iss_coords[1], image=issimage)
refresh_button = Button(text="Refresh", command=manual_refresh)
refresh_button.grid(row=1, column=0)


refresh()


window.mainloop()



