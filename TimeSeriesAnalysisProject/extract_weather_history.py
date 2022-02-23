from datetime import datetime
import matplotlib.pyplot as plt
import meteostat

from enum import Enum

class MeteostatInterval(Enum):
    HOURLY = 1
    DAILY = 2
    MONTHLY = 3
    YEARLY = 4


# get the weather data from map coordinates using the meteostat weather python api
# https://dev.meteostat.net/python/#installation
def get_weather_data(longitude, latitude, elevation, start_time, end_time, value_names=['tavg', 'tmin', 'tmax'], intervals = MeteostatInterval.DAILY):
    # Set time period


    # Create Point for Vancouver, BC
    location_coords = meteostat.Point(longitude, latitude, elevation)

    # Get daily data for 2018
    if intervals == MeteostatInterval.DAILY :
        data = meteostat.Daily(location_coords, start_time, end_time)
    elif intervals == MeteostatInterval.HOURLY :
        data = meteostat.Hourly(location_coords, start_time, end_time)
    elif intervals == MeteostatInterval.MONTHLY :
        data = meteostat.Monthly(location_coords, start_time, end_time)
    elif intervals == MeteostatInterval.YEARLY :
        data = meteostat.Yearly(location_coords, start_time, end_time)
    
    data = data.fetch()

    

    

    return data.loc[value_names]

    # Plot line chart including average, minimum and maximum temperature
    # data.plot(y=['tavg', 'tmin', 'tmax'])
    # plt.show()