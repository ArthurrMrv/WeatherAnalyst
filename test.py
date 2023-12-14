import PySimpleGUI as sg
from Days import Days

#C:\Users\ulyss\Documents\Visual Studio\Python\Algorithms and Software Concepts\Final_Project\Algorithms-main

days_instances = Days()
days_instances.loadTemp('data_temperature.txt')

# Function to create a new window for Average temperatures

def show_average_temperature():
    layout = [
        [sg.Text('Average temperature window')],
        [sg.Text('Please enter all city names in lowercase')],
        [sg.InputText(key='-USER_INPUT-', size=(30, 1))],
        [sg.Button('OK'), sg.Button('Cancel')],
    ]

    window = sg.Window('Average temperature', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        user_input = values['-USER_INPUT-']

        # Display the message if the user input contains uppercase characters
        if any(char.isupper() for char in user_input):
            sg.popup('ERROR: Please enter all city names in lowercase')
            continue

        if days_instances.getCityWeather(user_input) == []:
            sg.popup(f'Error: {user_input} is not a valid city name')
            continue

        result = days_instances.getAvgTemperature(user_input)
        #Output the result in a new popup window
        sg.popup(f'{user_input.capitalize()} average temperature: {round(result, 2)}°C')
    
    window.close()

def show_total_precipitation():
    layout = [
        [sg.Text('Total Precipitation Window')],
        [sg.Text('Please enter all city names in lowercase')],
        [sg.InputText(key='-USER_INPUT-', size=(30, 1))],
        [sg.Button('OK'), sg.Button('Cancel')],
    ]

    window = sg.Window('Total Precipitation', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        user_input = values['-USER_INPUT-']

        # Display the message if the user input contains uppercase characters
        if any(char.isupper() for char in user_input):
            sg.popup('ERROR: Please enter all city names in lowercase')
            continue
        # Display the message if the user input is invalid
        if days_instances.getCityWeather(user_input) == []:
            sg.popup(f'Error: {user_input} is not a valid city name')
            continue

        result = days_instances.getTotalPrecipitation(user_input)

        # Update the Text element with the result
        sg.popup(f"{user_input.capitalize()}'s total precipitation: {round(result, 2)}mm")
    
    window.close()

def max_and_mind_wind_speed():
    layout = [
        [sg.Text('Max and Min Wind Speed Winds')],
        [sg.Text('Please enter all city names in lowercase')],
        [sg.InputText(key='-USER_INPUT-', size=(30, 1))],
        [sg.Button('OK'), sg.Button('Cancel')],
    ]

    window = sg.Window('Max and Min Wind Speed', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        user_input = values['-USER_INPUT-']

        # Display the message if the user input contains uppercase characters
        if any(char.isupper() for char in user_input):
            sg.popup('ERROR: Please enter all city names in lowercase')
            continue
        # Display the message if the user input is invalid
        if days_instances.getCityWeather(user_input) == []:
            sg.popup(f'Error: {user_input} is not a valid city name')
            continue

        result1 = days_instances.getMaxWindSpeed(user_input)
        result2 = days_instances.getMinWindSpeed(user_input)

        # Update the Text element with the result
        sg.popup(f"{user_input.capitalize()}'s maximum wind speed: {round(result1, 2)}kph\n{user_input.capitalize()}'s minimum wind speed: {round(result2, 2)}kph")
    
    window.close()

def temp_over_time():
    layout = [
        [sg.Text('Temperature over time Window')],
        [sg.Text('Please enter all city names in lowercase')],
        [sg.InputText(key='-USER_INPUT-', size=(30, 1))],
        [sg.Button('OK'), sg.Button('Cancel')],
    ]

    window = sg.Window('Temperature over time', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        user_input = values['-USER_INPUT-']

        # Display the message if the user input contains uppercase characters
        if any(char.isupper() for char in user_input):
            sg.popup('ERROR: Please enter all city names in lowercase')
            continue
        # Display the message if the user input is invalid
        if days_instances.getCityWeather(user_input) == []:
            sg.popup(f'Error: {user_input} is not a valid city name')
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
        [sg.Text('Please enter all city names in lowercase')],
        [sg.InputText(key='-USER_INPUT-', size=(30, 1))],
        [sg.Button('OK'), sg.Button('Cancel')],
    ]

    window = sg.Window('Hottest and Coldest day', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        user_input = values['-USER_INPUT-']

        # Display the message if the user input contains uppercase characters
        if any(char.isupper() for char in user_input):
            sg.popup('ERROR: Please enter all city names in lowercase')
            continue
        # Display the message if the user input is invalid
        if days_instances.getCityWeather(user_input) == []:
            sg.popup(f'Error: {user_input} is not a valid city name')
            continue

        result1 = days_instances.hotestDay(user_input)
        result2 = days_instances.coldestDay(user_input)

        # Update the Text element with the result
        sg.popup(f"{user_input.capitalize()}'s hottest day:\n{result1} \n{user_input.capitalize()}'s coldest day:\n{result2}")
    
    window.close()

"""def all_hottest_and_coldest_days():
    layout = [
        [sg.Text('All Hottest and Coldest day')],
    ]

    window = sg.Window('All Hottest and Coldest day', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        names = []

        user_input = names.append(days_instances)


        result1 = days_instances.hotestDay()
        result2 = days_instances.coldestDay()

        for c in days_instances.cities:
            names.append(f"{user_input.capitalize()}'s hottest day:\n{result1} \n{user_input.capitalize()}'s coldest day:\n{result2}")


        # Update the Text element with the result
        sg.popup(print(names))
    
    window.close()

"""

def all_hottest_and_coldest_days():
    layout = [
        [sg.Text('All Hottest and Coldest day')],
        [sg.Text('', size=(100, 50), key='-OUTPUT-')],
        [sg.Button('Exit')]
    ]

    window = sg.Window('All Hottest and Coldest day', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        cities_list = list(days_instances.cities)

        output_text = []

        while len(cities_list) >1:
            result1 = days_instances.hotestDay(cities_list[0])
            result2 = days_instances.coldestDay(cities_list[0])
            output_text.append(f"{cities_list[0].capitalize()}'s hottest day: {result1}\n{cities_list[0].capitalize()}'s coldest day: {result2}\n\n")
            cities_list.pop(0)
            result1 = 0
            result2 = 0


        #for city in cities_list:
         #   result1 = days_instances.hotestDay(city)
          #  result2 = days_instances.coldestDay(city)
           # output_text += (f"{city.capitalize()}'s hottest day: {result1}\n{city.capitalize()}'s coldest day: {result2}\n\n")
            

        # Update the Text element with the result outside the loop
        window['-OUTPUT-'].update(''.join(output_text))

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
    #{'text': 'Overall Hottest day', 'function': overall_hottest_day},



    # Add more buttons with associated functions...
]

column1 = [[sg.B(button['text'], size=(22, 3))] for button in buttons[:3]]
column2 = [[sg.B(button['text'], size=(22, 3))] for button in buttons[3:6]]
column3 = [[sg.B(button['text'], size=(22, 3))] for button in buttons[6:]]

layout = [
    [sg.Column(column1), sg.Column(column2), sg.Column(column3)],
]

window = sg.Window("Final Project", layout, margins=(200, 100))

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    # Find the button that corresponds to the pressed event
    button_pressed = next(button for button in buttons if button['text'] == event)

    # Call the associated function
    button_pressed['function']()

window.close()
