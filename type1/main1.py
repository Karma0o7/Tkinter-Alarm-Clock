# Required Modules
import tkinter
import threading
import winsound
import datetime
import time

# Create Object
root = tkinter.Tk()

# Set geometry
root.geometry("400x200")

# Use Threading
def Threading():
    t1=threading.Thread(target=alarm)
    t1.setDaemon(True)
    t1.start()

# The main function
def alarm():
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait
        time.sleep(1)

        #Get Current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)

        # Check Condition for alarm to ring
        if current_time == set_alarm_time:
            print("Time to Wakey Wakey!")
            # Play audion for alarm
            winsound.PlaySound("ALARM1.wav",winsound.SND_ASYNC)
            break

# Tkinter: Add Labels, Frame, Button, Optionmenus
tkinter.Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
tkinter.Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()

frame = tkinter.Frame(root)
frame.pack()

# Button for Hours
hour = tkinter.StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
hrs = tkinter.OptionMenu(frame, hour, *hours)
hrs.pack(side=tkinter.LEFT)

# Button for Minutes
minute = tkinter.StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
mins = tkinter.OptionMenu(frame, minute, *minutes)
mins.pack(side=tkinter.LEFT)

# Button for Seconds
second = tkinter.StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
secs = tkinter.OptionMenu(frame, second, *seconds)
secs.pack(side=tkinter.LEFT)

tkinter.Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()
