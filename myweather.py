from myweather import Weather
class CurrentWeather():
    temperature = ''
    weather_conditions = ''
    wind_speed = ''
    city = ''
def __init__ (self,city):
    self.city = city
    weather = Weather (unit =Unit.CELSIUS)
    lookup = weather.lookup_by_location (self.city)
    self.temperature = lookup.condition.temp
    self.weather_conditions = lookup.condition.text
    self.wind_speed = lookup.wind.speed
def getTemperature(self):
    return self.temperature
def getCity(self):
    return self.city
if __name__ == "__main__":
    current_weather = CurrentWeather('Montreal')
    print("%s %sC "%(current_weather.getCity(),current_weather.getTemperature()))