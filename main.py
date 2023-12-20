import os
import pathlib

os.system("cd {}".format(pathlib.Path(__file__).parent.resolve()))
os.system("pip3 install PySimpleGUI")

import PySimpleGUI as sg
from Days import Days

days_instances = Days()
days_instances.loadTemp('data_temperature.txt')
days_instances.loadTemp('Paris_data_climate.txt')

# Function to create a new window for Average temperatures

def show_average_temperature():
    layout = [
        [sg.Text('Average temperature window')],
        [sg.Text('Please enter city name')],
        [sg.InputText(key='-USER_INPUT-', size=(30, 1))],
        [sg.Button('OK'), sg.Button('Cancel')],
    ]

    window = sg.Window('Average temperature', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        user_input = values['-USER_INPUT-'].lower()

        if days_instances.getCityWeather(user_input) == []:

            sg.popup(f'Error: {user_input} is not a valid city name.\nPlease select one of this list : \n{[tuple(days_instances.getCityNames())[i].capitalize() for i in range(len(days_instances.getCityNames()))]}')
            continue

        result = days_instances.getAvgTemperature(user_input)
        #Output the result in a new popup window
        sg.popup(f'{user_input.capitalize()} average temperature: {round(result, 2)}°C')
    
    window.close()

def show_total_precipitation():
    layout = [
        [sg.Text('Total Precipitation Window')],
        [sg.Text('Please enter city name')],
        [sg.InputText(key='-USER_INPUT-', size=(30, 1))],
        [sg.Button('OK'), sg.Button('Cancel')],
    ]

    window = sg.Window('Total Precipitation', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        user_input = values['-USER_INPUT-'].lower()

        # Display the message if the user input is invalid
        if days_instances.getCityWeather(user_input) == []:
            sg.popup(f'Error: {user_input} is not a valid city name.\nPlease select one of this list : \n{[tuple(days_instances.getCityNames())[i].capitalize() for i in range(len(days_instances.getCityNames()))]}')
            continue

        result = days_instances.getTotalPrecipitation(user_input)

        # Update the Text element with the result
        sg.popup(f"{user_input.capitalize()}'s total precipitation: {round(result, 2)}mm")
    
    window.close()

def max_and_mind_wind_speed():
    layout = [
        [sg.Text('Max and Min Wind Speed Winds')],
        [sg.Text('Please enter city name')],
        [sg.InputText(key='-USER_INPUT-', size=(30, 1))],
        [sg.Button('OK'), sg.Button('Cancel')],
    ]

    window = sg.Window('Max and Min Wind Speed', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        user_input = values['-USER_INPUT-'].lower()

       # Display the message if the user input is invalid
        if days_instances.getCityWeather(user_input) == []:
            sg.popup(f'Error: {user_input} is not a valid city name.\nPlease select one of this list : \n{[tuple(days_instances.getCityNames())[i].capitalize() for i in range(len(days_instances.getCityNames()))]}')
            continue

        result1 = days_instances.getMaxWindSpeed(user_input)
        result2 = days_instances.getMinWindSpeed(user_input)

        # Update the Text element with the result
        sg.popup(f"{user_input.capitalize()}'s maximum wind speed: {round(result1, 2)}kph\n{user_input.capitalize()}'s minimum wind speed: {round(result2, 2)}kph")
    
    window.close()

def temp_over_time():
    layout = [
        [sg.Text('Temperature over time Window')],
        [sg.Text('Please enter city name')],
        [sg.InputText(key='-USER_INPUT-', size=(30, 1))],
        [sg.Button('OK'), sg.Button('Cancel')],
    ]

    window = sg.Window('Temperature over time', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        user_input = values['-USER_INPUT-'].lower()

        # Display the message if the user input is invalid
        if days_instances.getCityWeather(user_input) == []:
            sg.popup(f'Error: {user_input} is not a valid city name.\nPlease select one of this list : \n{[tuple(days_instances.getCityNames())[i].capitalize() for i in range(len(days_instances.getCityNames()))]}')
            continue

        result = days_instances.plotTemperature(user_input)

        # Update the Text element with the result
        sg.popup(result)
    
    window.close()

def bar_chart_averages():
    layout = [
        [sg.Text('Bar Chart averages Window')],
        [sg.Canvas(days_instances.plotAvgTemperature(*list(days_instances.cities)), key='-GRAPH-')],
    ]

    window = sg.Window('Total Precipitation', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

    window.close()

def hottest_and_coldest_day():
    layout = [
        [sg.Text('Hottest and Coldest day')],
        [sg.Text('Please enter city name')],
        [sg.InputText(key='-USER_INPUT-', size=(30, 1))],
        [sg.Button('OK'), sg.Button('Cancel')],
    ]

    window = sg.Window('Hottest and Coldest day', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        user_input = values['-USER_INPUT-'].lower()

        # Display the message if the user input is invalid
        if days_instances.getCityWeather(user_input) == []:
            sg.popup(f'Error: {user_input} is not a valid city name.\nPlease select one of this list : \n{[tuple(days_instances.getCityNames())[i].capitalize() for i in range(len(days_instances.getCityNames()))]}')
            continue

        result1 = days_instances.hotestDay(user_input)
        result2 = days_instances.coldestDay(user_input)

        # Update the Text element with the result
        sg.popup(f"{user_input.capitalize()}'s hottest day:\n{result1} \n{user_input.capitalize()}'s coldest day:\n{result2}")
    
    window.close()

def all_hottest_and_coldest_days():
    layout = [
        [sg.Text('All Hottest and Coldest days')],
        [sg.Multiline('', size=(200, 50), key='-OUTPUT-', autoscroll=False, disabled=True)],
        [sg.Button('Exit')]
    ]

    window = sg.Window('All Hottest and Coldest day', layout, finalize=True)

    cities_list = list(days_instances.cities)
    output_text = ''

    while len(cities_list)>0:
        city = cities_list[0].capitalize()
        result1 = days_instances.hotestDay(city)
        result2 = days_instances.coldestDay(city)
        output_text += f"{city}'s hottest day: {result1}\n{city}'s coldest day: {result2}\n\n"

        result1 = 0
        result2 = 0

        cities_list.pop(0)

    # Update the Multiline element with the result
    window['-OUTPUT-'].update(value=output_text)

    # Call window.read() to ensure Element updates are processed
    event, values = window.read()

def overall_hottest_day():
    layout = [
        [sg.Text('Overall Hottest Day')],
        [sg.Text('', size=(50, 10), key='-OUTPUT-')],
        [sg.Button('Exit')]
    ]

    window = sg.Window('Overall Hottest Day', layout, finalize=True)

    cities_list = list(days_instances.cities)
    all_hottest_days = []

    while len(cities_list) > 0:
        city = cities_list[0]
        result1 = days_instances.hotestDay(city)
        all_hottest_days.append(result1)

        cities_list.pop(0)

    # Find the overall hottest day
    overall_hottest_day = max(all_hottest_days, key=lambda day: day.getMaxTemp())

    # Update the Text element with the result
    output_text = f"The overall hottest day out of all the cities was:\n{str(overall_hottest_day)}"
    window['-OUTPUT-'].update(output_text)

    # Event loop to keep the window open
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

    window.close()

def overall_coldest_day():
    layout = [
        [sg.Text('Overall Coldest Day')],
        [sg.Text('', size=(50, 10), key='-OUTPUT-')],
        [sg.Button('Exit')]
    ]

    window = sg.Window('Overall Coldest Day', layout, finalize=True)

    cities_list = list(days_instances.cities)
    all_coldest_days = []

    while len(cities_list) > 0:
        city = cities_list[0]
        result1 = days_instances.coldestDay(city)
        all_coldest_days.append(result1)

        cities_list.pop(0)

    # Find the overall coldest day
    overall_coldest_day = min(all_coldest_days, key=lambda day: day.getMinTemp())

    # Update the Text element with the result
    output_text = f"The overall coldest day out of all the cities was:\n{str(overall_coldest_day)}"
    window['-OUTPUT-'].update(output_text)

    # Event loop to keep the window open
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

    window.close()

def specific_day_category():
    # Layout for the input window
    layout_input = [
        [sg.Text('Enter Date (YYYY-MM-DD):'), sg.InputText(key='-DATE-', size=(15, 1))],
        [sg.Text('Enter City:'), sg.InputText(key='-CITY-', size=(15, 1))],
        [sg.Button('OK')]
    ]

    window_input = sg.Window('Enter Date and City', layout_input)

    while True:
        event_input, values_input = window_input.read()

        if event_input == sg.WINDOW_CLOSED or event_input == 'OK':
            break

    window_input.close()

    # Get the values entered by the user
    user_date = values_input['-DATE-']
    user_city = values_input['-CITY-'].lower()


    # Fetch information for the specified date and city
    try:
        day_info = days_instances.getDay(user_date, user_city)
    except KeyError:
        sg.popup(f"             ERROR\nNo data found for {user_city.capitalize()} on {user_date}")
        return

    # Layout for the output window
    layout_output = [[sg.Text(f'On the {user_date} in the city of {user_city.capitalize()} the temperature was')]]
    if day_info:
        category_text = days_instances.categorizeDay(user_city, user_date)
    if category_text is not None:
        layout_output.append([sg.Text(category_text)])
    else:
        layout_output.append([sg.Text("No temperature data available for categorization.")])

    layout_output.append([sg.Button('OK')])
    window_output = sg.Window('Weather Information', layout_output)

    while True:
        event_output, _ = window_output.read()

        if event_output == sg.WINDOW_CLOSED or event_output == 'OK':
            break

    window_output.close()

def correlation_matrix():
    layout = [
        [sg.Text('Correlation Matrix for a city')],
        [sg.Text('Please enter city name')],
        [sg.InputText(key='-USER_INPUT-', size=(30, 1))],
        [sg.Button('OK'), sg.Button('Cancel')],
    ]

    window = sg.Window('Correlation Matrix for a city', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        user_input = values['-USER_INPUT-'].lower()

        # Display the message if the user input is invalid
        if days_instances.getCityWeather(user_input) == []:
            sg.popup(f'Error: {user_input} is not a valid city name.\nPlease select one of this list : \n{[tuple(days_instances.getCityNames())[i].capitalize() for i in range(len(days_instances.getCityNames()))]}')
            continue

        result = days_instances.plotCorrelationMatrix(user_input)
        
        # Update the Text element with the result
        sg.popup(f"{user_input.capitalize()}'s correlation matrix:\n{result}")
    
    window.close()

def potential_factors_for_max_temp():
    layout = [
        [sg.Text('Potential factors leading to max temperature in each city')],
        [sg.Text('Please enter city name')],
        [sg.InputText(key='-USER_INPUT-', size=(30, 1))],
        [sg.Button('OK'), sg.Button('Cancel')],
    ]

    window = sg.Window('Potential factors leading to max temperature in each city', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        user_input = values['-USER_INPUT-'].lower()

        # Display the message if the user input is invalid
        if days_instances.getCityWeather(user_input) == []:
            sg.popup(f'Error: {user_input} is not a valid city name.\nPlease select one of this list : \n{[tuple(days_instances.getCityNames())[i].capitalize() for i in range(len(days_instances.getCityNames()))]}')
            continue

        result_max = days_instances.factors_max_temp(user_input)
        result_min = days_instances.factors_min_temp(user_input)
        
        # Update the Text element with the result
        sg.popup(f"{user_input.capitalize()}'s potential factors for extreme temperatures:\nCold temp: {result_min} - Hot temp: {result_max}")
    
    window.close()

# Define the buttons and their associated functions
buttons = [
    {'text': 'Average temperature', 'function': show_average_temperature},
    {'text': 'Total precipitation', 'function': show_total_precipitation},
    {'text': 'Max and Min Wind Speeds', 'function': max_and_mind_wind_speed},
    {'text': 'Temperature over time plot', 'function': temp_over_time},
    {'text': 'Bar Chart comparison of\n average temperatures', 'function': bar_chart_averages},
    {'text': 'Hottest and Coldest day', 'function': hottest_and_coldest_day},
    {'text': 'All Hottest and\nColdest days', 'function': all_hottest_and_coldest_days},
    {'text': 'Overall Hottest day', 'function': overall_hottest_day},
    {'text': 'Overall Coldest day', 'function': overall_coldest_day},
    {'text': 'Specific day category', 'function': specific_day_category},
    {'text': 'Potential factors leading to \nmax temperature in each city', 'function': potential_factors_for_max_temp},
    {'text': 'Correlation Matrix for a city', 'function': correlation_matrix},



    # Add more buttons with associated functions...
]

column1 = [[sg.B(button['text'], size=(22, 3))] for button in buttons[:4]]
column2 = [[sg.B(button['text'], size=(22, 3))] for button in buttons[4:8]]
column3 = [[sg.B(button['text'], size=(22, 3))] for button in buttons[8:]]

layout = [
    [sg.Column(column1), sg.Column(column2), sg.Column(column3)],
]

window = sg.Window('Final Project', layout, margins=(200, 100), resizable=True)


while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    # Find the button that corresponds to the pressed event
    button_pressed = next(button for button in buttons if button['text'] == event)

    # Call the associated function
    button_pressed['function']()

window.close()