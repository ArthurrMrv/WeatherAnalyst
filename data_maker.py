import csv
import random
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

def generate_weather_data(filename, start_date, num_days, *city_names, delta_days = 1):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Location", "Max Temperature (C)", "Min Temperature (C)", "Precipitation (mm)", "Wind Speed (km/h)", "Humidity (%)", "Cloud Cover (%)"])
        
        for city_name in city_names:
            date = start_date
            for _ in range(num_days):
                max_temp = random.randint(-10, 30)
                min_temp = random.randint(-15, max_temp)
                precipitation = random.randint(0, 20)
                wind_speed = random.randint(0, 30)
                humidity = random.randint(50, 100)
                cloud_cover = random.randint(0, 100)

                writer.writerow([date.strftime('%Y-%m-%d'), city_name, max_temp, min_temp, precipitation, wind_speed, humidity, cloud_cover])
                date += timedelta(days=delta_days)


# Usage
#start_date = datetime(2023, 1, 1)
#generate_weather_data('data_temperature(homemade).txt', start_date, 365, *cities, delta_days=1)


def generate_correlated_data(filename, num_samples, correlation_matrix, titles):
    # Convert the correlation matrix to a numpy array
    correlation_matrix = np.array(correlation_matrix)
    
    # Generate samples from a multivariate normal distribution
    samples = np.random.multivariate_normal(np.zeros(len(titles)), correlation_matrix, num_samples)
    
    #round the data to 2dp
    samples = np.round(samples, 2)

    # Create a DataFrame from the samples
    df = pd.DataFrame(samples, columns=titles)

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)

cities = ['beijing',
 'berlin',
 'cairo',
 'london',
 'los angeles']
 
# Usage
correlation_matrix = [[ 1.        ,  0.98754809, -0.68241852, -0.64267025, -0.16173548, -0.55057438],
                      [ 0.98754809,  1.        , -0.67108632, -0.66524463, -0.15621472, -0.51438853],
                      [-0.68241852, -0.67108632,  1.        ,  0.11762976, -0.34936123,  0.79052773],
                      [-0.64267025, -0.66524463,  0.11762976,  1.        ,  0.58420548,  0.02322061],
                      [-0.16173548, -0.15621472, -0.34936123,  0.58420548,  1.        , -0.41276115],
                      [-0.55057438, -0.51438853,  0.79052773,  0.02322061, -0.41276115,  1.        ]]
titles = ['Max Temp', 'Min Temp', 'Wind Speed', 'Humidity', 'Cloud Cover', 'Precipitation']

generate_correlated_data('correlated_weather_data.txt', 1000, correlation_matrix, titles)