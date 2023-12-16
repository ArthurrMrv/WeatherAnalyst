import tkinter as tk
from Days import Days

# open a tkinter window
window = tk.Tk()
window.title("Weather App")
window.geometry("800x600")

# create a Days object
days = Days()
days.loadTemp("/Users/arthurmorvan/Desktop/Final_Project/data_temperature.txt")
days.loadTemp("/Users/arthurmorvan/Desktop/Final_Project/Paris_data_climate.txt")

# save the correlationmatrix in a file
days.saveCorrelationMatrix("correlation_matrix.png", *list(days.getCityNames()))

#display an image on the tkinter window
canvas = tk.Canvas(window, width = 1000, height = 800)
canvas.pack()
img = tk.PhotoImage(file="correlation_matrix.png")
canvas.create_image(400, 300, image=img)

# display the tkinter window
window.mainloop()
