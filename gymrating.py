# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:45:34 2023

@author: lanuo
"""

#Let's say I want to make a mood tracker that logs my mood on a rating 1-5 with a GUI that displays the date and rating
#.1 The interface has to ask the user about their mood
    #There needs to be user input; create a window and input button
        #this input needs to be logged and called back up to the interface 
#2. A library must hold the user input data
#3. Display the data in the library via a bar graph  or through date and rating

import tkinter as tk
from datetime import datetime
import csv
import os
#Submit an answer function
def submit():
    rating = entry.get()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #Store the user input, date and time in a dictionary
    entry_data = {"Rating" : rating, "Date": current_time}
    
    #Append the data to a list (for demonstration purposes)
    data_list.append(entry_data)
    
    #Save the data to a csv file
    save_to_csv()
    
    #Show a pop-up message
    checkAndShowPopup()

def save_to_csv():
    #Get the script directory
    script_dir = os.path.dirname(r'C:\Users\lanuo\.spyder-py3\user_ratings.csv')
        
    #Define the csv file pathj
    csv_file = os.path.join(script_dir, "user_ratings.csv")
    
    #Define the csv file name

    csv_file = "user_ratings.csv"
    
    #Write the data to the CSV file
    with open(csv_file, mode="a", newline="") as file:
        fieldnames = ["Rating", "Date"]
        writer= csv.DictWriter(file, fieldnames = fieldnames)
        
        #Write header if the file is empty
        if file.tell() == 0:
            writer.writeheader()
            
        #Write the user input data
        for entry_data in data_list:
            writer.writerow(entry_data)
            
 #Create a pop up after submission that says '1% better everyday'
def checkAndShowPopup():
    popup = tk.Toplevel(window)
    popup.title("Submission Complete")
    popup.geometry("200x100")
    
    popup_label = tk.Label(popup, text= "1% better everyday")
    popup_label.pack()

    #Close popup after 3000 milliseconds(3 seconds)
    popup.after(3000, popup.destroy)
#Create a window display
window = tk.Tk()

#Ask for user input
question_label = tk.Label(window, text= "One a scale from 1-5, how was your gym session today?")
question_label.pack() #this will make sure the label pops up

#Add a widget for user_input
entry = tk.Entry(window)
entry.pack()

#Submit button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

#List to store user input data
data_list = []


    


#Make the window bigger
window.geometry("300x100")


#Run the main loop
window.mainloop()
