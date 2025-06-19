from tkinter import *
import tkinter as tk

#Create a window
import clipboard

app = Tk()
buttons = []

def copy(text):
    print("copy pressed..")
    clipboard.copy(text)
    # if (str(buttons[1]['state']) == 'disabled'):
    # entry1_button.configure(state = 'normal')



#Entry
entry_text = StringVar()
entry_label =  Label(app, text='Text to Save : ', font=('bold',14), pady=20)
entry_label.grid(row=0, column=0, sticky=W)
entry = Entry(app, width=120,textvariable=entry_text)
entry.grid(row=0, column=1)

# extry1_text = "systemctl status PNMMicroServices@"
# entry1 = Label(app, text=extry1_text).grid(column=0, row=3)
# entry1_button = tk.Button(app, text="copy", command=lambda : copy(extry1_text))
# # buttons.append(entry1_button)
# entry1_button.grid(column=1, row=3)

cmd_list = ['systemctl status PNMMicroServices@1', 'systemctl status PNMMicroServices@2','source /opt/local/alias']
copy_icon = PhotoImage(file = r"copy-icon.png")
for index, cmd in enumerate(cmd_list):
    Label(app, text=str(index+1)+'. '+cmd, font=(4), pady=2).grid(column=0, row=3+index)
    Button(app, image = copy_icon, command=lambda cmdq=cmd : copy(cmdq)).grid(column=1, row=3+index)


#Entries
#entries = Listbox(app, )


#App Attributes
app.title("Multi Clipboard")
app.geometry('1000x500')


#Run the app
app.mainloop()