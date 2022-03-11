import requests
from datetime import datetime
from math import sqrt
from time import sleep
import smtplib

def check_time():
    time = str(datetime.now()).split(" ")[1].split(".")[0]
    print(time)
    return time

def get_my_location():
    ip = requests.get('https://ipapi.co/ip/').text
    response = requests.get(url=f"http://ip-api.com/json/{ip}")
    ip_json = response.json()
    my_location = (float(ip_json["lat"]), float(ip_json["lon"]))
    print(ip_json["city"])
    print(my_location)
    return my_location

def sunrise_sunset(my_location):
    parameters = {
        "lat": my_location[0],
        "lng": my_location[1],
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
    sunset = data["results"]["sunset"].split("T")[1].split("+")[0]
    print(sunrise.split(":")[0])
    daylight_hours = {
        "sunrise": sunrise,
        "sunset": sunset
    }
    return daylight_hours

def iss_within_range(my_location):
    iss_position = get_iss_position()
    distance_to_iss = sqrt((my_location[0] - iss_position[0])**2 + (my_location[1] - iss_position[1])**2)
    print(f"My location = {my_location}, Iss = {iss_position}")
    print(f"Distance to iss = {distance_to_iss}")
    print("Due ", end="")
    if my_location[0] - iss_position[0] > 1:
        print("south ", end="")
    elif my_location[0] - iss_position[0] < -1:
        print("north ", end="")
    if my_location[1] - iss_position[1] > 1:
        print("west")
    elif my_location[1] - iss_position[1] < -1:
        print("east")
    if distance_to_iss < 5:
        bearing = ""
        print("Within sight")
        if distance_to_iss < 1:
            print("Overhead")
            bearing += "overhead"
        else:
            print("Due ", end = "")
            if my_location[0] - iss_position[0] > 1:
                bearing += "south"
                print("south ", end="")
            elif my_location[0] - iss_position[0] < -1:
                bearing += "north"
                print("north ", end="")
            if my_location[1] - iss_position[1] > 1:
                bearing += " west"
                print("west")
            elif my_location[1] - iss_position[1] < -1:
                bearing += " east"
                print("east")
            else:
                bearing += ""
            return bearing
    else:
        pass
    return

def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_json = response.json()
    iss_position = (float(iss_json["iss_position"]["latitude"]), float(iss_json["iss_position"]["longitude"]))
    print(iss_position)
    return iss_position

def Generate_Email(bearing):
    message = Generate_Message(bearing)
    subject = f"ISS is nearby!"
    recipient = "automationtester22@yahoo.com"
    send_email(recipient, subject, message)
    return

def Generate_Message(bearing):
    bearing = bearing.rstrip().lstrip()
    message = "The ISS is nearby, it should be roughly due " + bearing
    print(f"Message generated:\n" + message)
    return message

def send_email(recipient, subject, message):
    send_email = "4utomationtest@gmail.com"
    password = "V3Png7h#By7#f9QcD5z"

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=send_email, password=password)
            connection.sendmail(from_addr=send_email, to_addrs=recipient, msg=f"Subject:{subject}\n\n{message}")
            print(f"\nSending Email\nFrom: {send_email}\nTo: {recipient}\nSubject: {subject}\nMessage: {message}\n"
                  f"___________________________________\n")
    except Exception as e:
        print("Sending failed.")
    return

if __name__ == '__main__':

    while True:
        time = check_time()
        my_location = get_my_location()
        daylight_hours = sunrise_sunset(my_location)
        if time > daylight_hours["sunrise"] and time < daylight_hours["sunset"]:
            bearing = iss_within_range(my_location)
            print(bearing)
            if not bearing == None:
                try:
                    Generate_Email(bearing)
                except:
                    print("Sending failed")

        sleep(10)