from tkinter import *
import requests
import datetime


class App():
    def __init__(self):

        #setup window
        self.window = Tk()
        self.window.title("Find Position")
        monitor_height = self.window.winfo_screenheight()
        monitor_width = self.window.winfo_screenwidth()
        print(monitor_width)
        self.window.config(width=1000, height=monitor_height, padx=50, pady=50, bg="light grey")
        #self.window.attributes('-fullscreen', True)
        self.weather_canvas_height = 200
        self.weather_canvas_width = 600
        self.weather_canvas = Canvas(width=self.weather_canvas_width, height=self.weather_canvas_height, bg = "dark grey", highlightthickness = 0)
        self.weather_canvas.grid(row=1, column=1, sticky="NESW")
        self.weather_canvas.bind('<Button-1>', self.update_weather_display)

        self.sun_icon = PhotoImage(file="Icons/Sun.png")
        self.rain_icon = PhotoImage(file="Icons/Rain.png")
        self.clouds_icon = PhotoImage(file="Icons/Clouds.png")
        self.shower_icon = PhotoImage(file="Icons/Showers.png")
        self.missing_icon = PhotoImage(file="Icons/Unknown.png")
        self.weather_button = Button(text = "Loading data...", image=self.sun_icon, compound= TOP, bg="light grey", highlightthickness=0, relief="flat", command=self.update_weather_display)
        self.weather_button.grid(row=2, column=1, sticky="NESW")

        self.generate_weather_display()
        print("Hereeeeee")

        self.window.mainloop()


    def generate_weather_display(self):
        #Initialise weather display
        self.weather_view = 1
        self.multi_view_start = 0

        try:
            print("Trying to get weather data")
            self.get_weather_forecast()
            print(f"Weather data")

        except Exception as e:
            print(e)
            weather_data = []
            for i in range(5):
                weather_data.append(["?", "?", self.missing_icon])
                self.weather_forecast = list(weather_data)
        print("Updating display")
        self.update_weather_display(None)
        self.window.after(1000, self.update_weather())



    def update_weather_display(self, event):
        #Alternate between multi-view and single view weather forecast
        #If weather view = 1 (i.e. multi-view) change to single view
        if self.weather_view == 1:
            self.weather_view = 0
            self.display_single_view()

        #If weather view = 0 (i.e. single view) change to multi view
        else:
            self.weather_view = 1
            self.multi_view_start = 0
            self.display_multi_view()


    def display_single_view(self):
        self.weather_canvas.delete("all")
        self.weather_canvas_width = 100
        self.weather_canvas.config(width=self.weather_canvas_width)
        self.label_blank = Label(text="    ", bg="light grey")
        self.label_blank2 = Label(text="    ", bg="light grey")
        print("Initialising")
        self.label_blank.grid(row=1, column=2, sticky="NESW")
        self.label_blank2.grid(row=1, column=0, sticky="NESW")
        self.weather_time_text = self.weather_canvas.create_text(self.weather_canvas_width / 2,
                                                                 self.weather_canvas_height / 2 - 80,
                                                                 font=("Arial", 10, "bold"), justify="center",
                                                                 fill="white",
                                                                 text=f"{self.weather_forecast[0][3]}")
        self.weather_icon = self.weather_canvas.create_image(self.weather_canvas_width / 2,
                                                             self.weather_canvas_height / 2 - 25,
                                                             image=self.weather_forecast[0][2])
        self.weather_text = self.weather_canvas.create_text(self.weather_canvas_width / 2,
                                                            self.weather_canvas_height / 2 + 40,
                                                            font=("Arial", 14, "bold"), justify="center",
                                                            fill="white",
                                                            text=f"{self.weather_forecast[0][0]}")
        self.temperature_text = self.weather_canvas.create_text(self.weather_canvas_width / 2,
                                                                self.weather_canvas_height / 2 + 80,
                                                                font=("Arial", 10, "bold"), justify="center",
                                                                fill="white",
                                                                text=f"{self.weather_forecast[0][1]}")
        print("Initialisation complete")


    def display_multi_view(self):
        self.weather_canvas.delete("all")
        self.weather_canvas_width = 600
        self.weather_canvas.config(width=self.weather_canvas_width)
        self.weather_slide_button_right = Button(text=">", width=10, bg="light grey", highlightthickness=0, relief="flat",
                                                 command=self.scroll_weather_right)
        self.weather_slide_button_left = Button(text="<", width=10, bg="light grey", highlightthickness=0, relief="flat",
                                                command=self.scroll_weather_left)
        self.weather_slide_button_right.grid(row=1, column=2, sticky="NESW")
        self.weather_slide_button_left.grid(row=1, column=0, sticky="NESW")
        for i in range(0, 5):
            self.weather_time_text = self.weather_canvas.create_text((self.weather_canvas_width/6) * (i+1),
                                                                     self.weather_canvas_height / 2 - 80,
                                                                     font=("Arial", 10, "bold"),
                                                                     justify="center",
                                                                     fill="white",
                                                                     text=f"{self.weather_forecast[self.multi_view_start + i][3]}")
            self.weather_canvas.create_image((self.weather_canvas_width/6) * (i+1), self.weather_canvas_height / 2 - 25,
                                             image=self.weather_forecast[self.multi_view_start + i][2])
            self.weather_canvas.create_text((self.weather_canvas_width/6) * (i+1), self.weather_canvas_height / 2 + 40,
                                            font=("Arial", 14, "bold"), justify="center",
                                            fill="white",
                                            text=f"{self.weather_forecast[self.multi_view_start + i][0]}")
            self.temperature_text = self.weather_canvas.create_text((self.weather_canvas_width/6) * (i+1),
                                                                self.weather_canvas_height / 2 + 80,
                                                                font=("Arial", 10, "bold"), justify="center",
                                                                fill="white",
                                                                text=f"{self.weather_forecast[self.multi_view_start + i][1]}")

    def scroll_weather_right(self):
        if self.multi_view_start + 5 < len(self.weather_forecast):
            self.multi_view_start += 1
        self.display_multi_view()

    def scroll_weather_left(self):
        if self.multi_view_start > 0:
            self.multi_view_start -= 1
        self.display_multi_view()

    def update_weather(self):
        #Update single view forecast
        print("Getting weather forecast in update_weather")
        self.get_weather_forecast()
        print("Weather forecast returned")
        self.weather_view = 1
        self.update_weather_display(None)
        print("Weather updated")
        self.window.after(1000*60, self.update_weather)
        print("Looping")

    def generate_weather_list(self, weather_data):
        #Convert weather data into GUI format
        print("Generating weather list")
        for i in range(len(weather_data)):
            if " " in weather_data[i][0]:
                weather_data[i][0] = weather_data[i][0].replace(" ", "\n")
            else:
                weather_data[i][0] = weather_data[i][0] + "\n"
            if "01" in weather_data[i][2]:
                weather_data[i][2] = self.sun_icon
            elif "10" in weather_data[i][2]:
                weather_data[i][2] =  self.rain_icon
            elif "09" in weather_data[i][2]:
                weather_data[i][2] =  self.shower_icon
            elif "02" or "03" or "04" in weather_data[i][2]:
                weather_data[i][2] =  self.clouds_icon
            else:
                weather_data[i][2] =  self.sun_icon
        print(weather_data)
        self.weather_forecast = list(weather_data)
        print("Weather list updated \n")

    def get_weather_forecast(self):
        print("Getting weather forecast")
        #Update weather forecast
        end_point = "https://api.openweathermap.org/data/2.5/onecall"
        params = {
            "lat": 51.454768,
            "lon": -2.596210,
            "appid": "",
            "exclude": "current,minutely,daily,alerts",
            "units": "metric"
        }

        response = requests.get(end_point, params=params)
        code = response.raise_for_status()
        if code is not None:
            print("Issue found")
            print(code)
        data = response.json()

        data = data["hourly"]
        print(data)
        date_time = datetime.datetime.now()
        today = date_time.date()
        time = date_time.time()
        weather_data = []
        for entry in data:
            weather_data.append([str(entry["weather"][0]["description"]).title(), f"{entry['temp']}°C",
                                 entry["weather"][0]["icon"], str(self.convert_time(entry['dt']).strftime("%H:%M"))])
        #weather_data = weather_data[:5]
        print(weather_data)
        self.generate_weather_list(weather_data)
        print("Here")

    def convert_time(self, time_to_convert):
        import datetime
        import time
        #today = datetime.datetime.now()
        #tomorrow = today.day + 1
        #date_to_check = today.replace(day=tomorrow)
        time_string = str(time_to_convert)
        if " " in time_string:
            converted_time = time.mktime(time_to_convert.timetuple())

        else:
            converted_time = datetime.datetime.fromtimestamp(time_to_convert)

        #print(f"Complete, converted {time_to_convert} to {converted_time}")
        return converted_time

Interface = App()