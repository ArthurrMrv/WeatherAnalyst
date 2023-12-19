from typing import Any
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

class Days:
    def __init__(self) -> None:
        self.data = dict()
        self.cities = set()
    
    def getDayArttibutes(self):
        return ['date', 'location', 'maxTemp', 'minTemp', 'precipitation', 'windSpeed', 'humidity', 'cloudCover', 'co2Levels', 'seaLevelRise']
    
    def getCityNames(self):
        return self.cities
    
    def addDay(self, day):
        self.cities.add(day.location)
        self.data[f"{day.getDate()}|{day.getLocation()}"] = day
        
    def getDay(self, date, location):
        return self.data[f"{date}|{location}"]
    
    def getDays(self):
        return self.data.values()
    
    def getCityWeather(self, city_name):
        return [day for day in self.getDays() if day.getLocation() == city_name.lower()]
    
    def getAvgTemperature(self, city_name):
        city_weather = self.getCityWeather(city_name)
        return sum([day.getMaxTemp() for day in city_weather]) / len(city_weather) if len(city_weather) > 0 else None
    
    def getPrecipitation(self, city_name):
        city_weather = self.getCityWeather(city_name)
        return sum([day.getPrecipitation() for day in city_weather]) if len(city_weather) > 0 else None
    
    def getMaxWindSpeed(self, city_name):
        city_weather = self.getCityWeather(city_name)
        return max([day.getWindSpeed() for day in city_weather]) if len(city_weather) > 0 else None
    
    def getMinWindSpeed(self, city_name):
        city_weather = self.getCityWeather(city_name)
        return min([day.getWindSpeed() for day in city_weather]) if len(city_weather) > 0 else None
    
    def getMedianTemperature(self, city_name):
        city_weather = self.getCityWeather(city_name)
        return sorted([day.getMaxTemp() for day in city_weather])[len(city_weather) // 2] if len(city_weather) > 0 else None
    
    def getTotalPrecipitation(self, city_name):
        city_weather = self.getCityWeather(city_name)
        return sum([day.getPrecipitation() for day in city_weather]) if len(city_weather) > 0 else None
    
    def categorizeDay(self, city_name, date, t = 0.2):
        
        if city_name.lower() not in self.cities:
            return None
        
        avgTemp = self.getAvgTemperature(city_name.lower())
        day_temp = self.getDay(date, city_name.lower()).getAverageTemp()
        tolerance = t*avgTemp
        
        if avgTemp - tolerance < day_temp < avgTemp + tolerance:
            return "Moderate"
        elif avgTemp > avgTemp + tolerance:
            return "Warm"
        else:
            return "Cold"
    
    def hotestDay(self, city_name):
        city_weather = self.getCityWeather(city_name)
        return max(city_weather, key=lambda day: day.getMaxTemp()) if len(city_weather) > 0 else None
    
    def coldestDay(self, city_name):
        city_weather = self.getCityWeather(city_name)
        return min(city_weather, key=lambda day: day.getMinTemp()) if len(city_weather) > 0 else None

    def correlationMatrix(self, city_name):
        city_weather = self.getCityWeather(city_name)
        if city_weather == []:
            return None
        
        elif np.mean([city_weather[i].getPrecipitation() for i in range(len(city_weather))]) == 0:
            matrix = np.array([[day.getMaxTemp(), day.getMinTemp(), day.getWindSpeed(), day.getHumidity(), day.getCloudCover()] for day in city_weather])
            titles = ['Max Temp', 'Min Temp', 'Wind Speed', 'Humidity', 'Cloud Cover']
        elif city_weather[0].getCo2Levels() is None:
            matrix = np.array([[day.getMaxTemp(), day.getMinTemp(), day.getWindSpeed(), day.getHumidity(), day.getCloudCover(), day.getPrecipitation()] for day in city_weather])
            titles = ['Max Temp', 'Min Temp', 'Wind Speed', 'Humidity', 'Cloud Cover', 'Precipitation']
        else:
            matrix = np.array([[day.getMaxTemp(), day.getMinTemp(), day.getWindSpeed(), day.getHumidity(), day.getCloudCover(), day.getPrecipitation(), day.getCo2Levels(), day.getSeaLevelRise()] for day in city_weather])
            titles = ['Max Temp', 'Min Temp', 'Wind Speed', 'Humidity', 'Cloud Cover', 'Precipitation', 'CO2 Levels', 'Sea Level Rise']

        correlation_matrix = np.corrcoef(matrix, rowvar=False)
        return correlation_matrix, titles
    
    def plotCorrelationMatrix(self, *city_names):
        for city_name in city_names:
            matrix, titles = self.correlationMatrix(city_name)
            plt.matshow(matrix)
            plt.xticks(range(len(titles)), titles, rotation=45)
            plt.yticks(range(len(titles)), titles)
            plt.title(f'Correlation Matrix for {city_name.capitalize()}')
            plt.colorbar()
            plt.show()

    def saveCorrelationMatrix(self, filename, *city_names):
        num_cities = len(city_names)
        fig, axs = plt.subplots(num_cities, 1, figsize=(10, 10*num_cities))

        for idx, city_name in enumerate(city_names):
            matrix, titles = self.correlationMatrix(city_name)
            cax = axs[idx].matshow(matrix)
            axs[idx].set_xticks(range(len(titles)))
            axs[idx].set_xticklabels(titles, rotation=45)
            axs[idx].set_yticks(range(len(titles)))
            axs[idx].set_yticklabels(titles)
            axs[idx].set_title(f'Correlation Matrix for {city_name.capitalize()}')
            fig.colorbar(cax, ax=axs[idx])

        plt.tight_layout()
        plt.savefig(filename)
    
    def plotTemperature(self, *city_names):
        for city_name in city_names:
            city_weather = self.getCityWeather(city_name)
            plt.plot([day.getDate() for day in city_weather], [day.getMaxTemp() for day in city_weather], label = city_name)
        #affiche labels
        plt.legend()
        
        #put legent box outside of graph
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

        plt.xticks(rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature over time')
        plt.show()
        
    def saveTemperature(self, filename, *city_names):
        for city_name in city_names:
            city_weather = self.getCityWeather(city_name)
            plt.plot([day.getDate() for day in city_weather], [day.getMaxTemp() for day in city_weather], label = city_name)
        #affiche labels
        plt.legend()
        
        #put legent box outside of graph
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

        plt.xticks(rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature over time')
        plt.savefig(filename)
    
    def plotAvgTemperature(self, *city_names):
        for city_name in city_names:
            city_weather = self.getCityWeather(city_name)
            plt.bar(city_name.capitalize(), self.getAvgTemperature(city_name), label = city_name)
        
        plt.xticks(rotation=45)
        plt.xlabel(f'City')
        plt.ylabel('Temperature (°C)')
        plt.title('Average Temperature')
        plt.show()
        
    def saveAvgTemperature(self, filename, *city_names):
        for city_name in city_names:
            city_weather = self.getCityWeather(city_name)
            plt.plot([day.getDate() for day in city_weather], [day.getMaxTemp() for day in city_weather], label = city_name)
        #affiche labels
        plt.legend()
        
        #put legent box outside of graph
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

        plt.xticks(rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature over time')
        plt.savefig(filename)
        
    #add data by loading a file
    def loadTemp(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()[1:]
            for line in lines:
                line = line.strip().split(',')
                #date = datetime.datetime.strptime(line[0], '%Y-%m-%d')
                date = line[0]

                location = line[1]
                maxTemp = float(line[2])
                minTemp = float(line[3])
                precipitation = float(line[4])
                windSpeed = float(line[5])
                humidity = float(line[6])
                cloudCover = float(line[7])
                co2Levels = float(line[8]) if len(line) > 8 else None
                seaLevelRise = float(line[9]) if len(line) > 9 else None
                self.cities.add(location.lower())
                self.addDay(Day(date, location, maxTemp, minTemp, precipitation, windSpeed, humidity, cloudCover, co2Levels, seaLevelRise))
    
    def factors_max_temp(self, city_name):
        """find the most correlated factor to max_temp (exept min_temp)
        """
        corr_matrix = self.correlationMatrix(city_name)
        return corr_matrix[1][np.max(np.where(np.abs(corr_matrix[0]) == np.max(np.abs(corr_matrix[0][0][2:]))))]
    
    def factors_min_temp(self, city_name):
        """find the most correlated factor to min_temp (exept max_temp)
        """
        corr_matrix = self.correlationMatrix(city_name)
        return corr_matrix[1][np.max(np.where(np.abs(corr_matrix[0]) == np.max(np.abs(corr_matrix[0][1][2:]))))]
    
    def compare_variables(self, variable1, variable2, *city_names, color_list = tuple(mcolors.CSS4_COLORS.values())[20:]):
        """compare two variables by plotting them on a scatter plot
        """
        for i, city_name in enumerate(city_names):
            city_weather = self.getCityWeather(city_name)
            if len(city_weather) == 0:
                print(f"Error: {city_name} is not a valid city name")
                continue
            try:
                plt.scatter([getattr(day, variable1) for day in city_weather], 
                            [getattr(day, variable2) for day in city_weather], 
                            label = city_name,
                            c = color_list[(i+20)%len(color_list)] )
            except:
                raise Exception(f"Error: {variable1} or {variable2} is not a valid variable")
        plt.legend()
        plt.xlabel(variable1)
        plt.ylabel(variable2)
        plt.title(f'{variable1} vs {variable2}')
        plt.show()

class Day:
    
    def __init__(self, date, location, maxTemp, minTemp, precipitation, windSpeed, humidity, cloudCover, co2Levels = None, seaLevelRise = None):
        self.date = date
        self.location = location.lower()
        self.maxTemp = maxTemp
        self.minTemp = minTemp
        self.precipitation = precipitation
        self.windSpeed = windSpeed
        self.humidity = humidity
        self.cloudCover = cloudCover
        self.co2Levels = co2Levels
        self.seaLevelRise = seaLevelRise
    
    def getDate(self):
        return self.date
    
    def getLocation(self):
        return self.location
    
    def getMaxTemp(self):
        return self.maxTemp
    
    def getMinTemp(self):
        return self.minTemp
    
    def getPrecipitation(self):
        return self.precipitation
    
    def getWindSpeed(self):
        return self.windSpeed
    
    def getHumidity(self):
        return self.humidity
    
    def getCloudCover(self):
        return self.cloudCover
    
    def getCo2Levels(self):
        return self.co2Levels
    
    def getSeaLevelRise(self):
        return self.seaLevelRise
    
    def getAverageTemp(self):
        return (self.maxTemp + self.minTemp) / 2
    
    def __str__(self):
        ans = "Date: " + str(self.date) + "\nLocation: " + str(self.location) + "\nMax Temp: " + str(self.maxTemp) + "\nMin Temp: " + str(self.minTemp) + "\nPrecipitation: " + str(self.precipitation) + "\nWind Speed: " + str(self.windSpeed) + "\nHumidity: " + str(self.humidity) + "\nCloud Cover: " + str(self.cloudCover)
        if self.co2Levels is not None:
            ans += "\nCO2 Levels: " + str(self.co2Levels)
        if self.seaLevelRise is not None:
            ans += "\nSea Level Rise: " + str(self.seaLevelRise)
        return ans + '\n'
