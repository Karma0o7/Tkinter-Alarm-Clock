# Required Modules
import tkinter
import tkinter.ttk
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
hour.set("00")
hrs = tkinter.ttk.Combobox(frame, textvariable=hour, values= ['00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'], width=5)
hrs.pack(side=tkinter.LEFT,padx=5)


# Button for Minutes
minute = tkinter.StringVar(root)
minute.set("00")
mins = tkinter.ttk.Combobox(frame, textvariable=minute, values=['00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60'], width=5)
mins.pack(side=tkinter.LEFT,padx=5)

# Button for Seconds
second = tkinter.StringVar(root)
second.set("00")
secs = tkinter.ttk.Combobox(frame, textvariable=second, values=['00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60'], width=5)
secs.pack(side=tkinter.LEFT,padx=5)

tkinter.Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()
