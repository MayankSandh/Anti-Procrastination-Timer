from tkinter import Tk, LabelFrame, Label, Entry, Frame, PhotoImage, Button, FLAT, X, LEFT, RIGHT, NORMAL, DISABLED, END, Menu, Toplevel
from tkinter import simpledialog
from time import sleep
import winsound
from plyer import notification
from os import system as cmd


root = Tk()
root.title("Timothy | Easy to use Timer Application!")
root.config(bg = "#dbf3fa")
root.resizable(False, False)


# ~~~~~~~~~~~~~~~~~~~~~ TOP MENU ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def themeChanger(rootcolor, timerframecolor, timerframefg, buttonbg, buttonfg, buttonhbg, buttonhfg):
    root.config(bg = rootcolor)

    TimerFrame.config(bg = timerframecolor,fg = timerframefg)
    LabelHour.config(bg = timerframecolor,fg = timerframefg)
    LabelMinute.config(bg = timerframecolor,fg = timerframefg)
    LabelSecond.config(bg = timerframecolor,fg = timerframefg)
    ShutdownLabel.config(bg = timerframecolor,fg = timerframefg)
    

    PlayButton.config(bg = timerframecolor, activebackground = timerframecolor)
    PauseButton.config(bg = timerframecolor, activebackground = timerframecolor)
    ClearButton.config(bg = timerframecolor, activebackground = timerframecolor)

    Button1.changeTheme(defaultbg = buttonbg, defaultfg = buttonfg, hoverfg = buttonhfg, hoverbg = buttonhbg)
    Button2.changeTheme(defaultbg = buttonbg, defaultfg = buttonfg, hoverfg = buttonhfg, hoverbg = buttonhbg)
    Button3.changeTheme(defaultbg = buttonbg, defaultfg = buttonfg, hoverfg = buttonhfg, hoverbg = buttonhbg)
    Button4.changeTheme(defaultbg = buttonbg, defaultfg = buttonfg, hoverfg = buttonhfg, hoverbg = buttonhbg)
    Button5.changeTheme(defaultbg = buttonbg, defaultfg = buttonfg, hoverfg = buttonhfg, hoverbg = buttonhbg)
    Button6.changeTheme(defaultbg = buttonbg, defaultfg = buttonfg, hoverfg = buttonhfg, hoverbg = buttonhbg)


def changeThemeTo(theme):
    if theme == "light":             
        themeChanger(rootcolor = "#dbf3fa",
                    timerframecolor = "#b7e9f7",
                    timerframefg = "#000000",
                    buttonbg = "#92dff3",
                    buttonfg = "#000000",
                    buttonhfg = "#000000",
                    buttonhbg = "#92cef3")
    elif theme == "lava":      
        themeChanger(rootcolor = "#7e0130",
                    timerframecolor = "#c9283e",
                    timerframefg = "#ffc000",
                    buttonbg = "#c9283e",
                    buttonfg = "#ffc000",
                    buttonhfg = "#ffc000",
                    buttonhbg = "#DC1C13")
    elif theme == "navy":  
        themeChanger(rootcolor = "#091c32",
                    timerframecolor = "#223C5B",
                    timerframefg = "#ffffff",
                    buttonbg = "#223C5D",
                    buttonfg = "#ffffff",
                    buttonhfg = "#ffffff",
                    buttonhbg = "#324b77")
    elif theme == "carnival":  
        themeChanger(rootcolor = "#9847C4",
                    timerframecolor = "#00A9DE",
                    timerframefg = "#F7CB04",
                    buttonbg = "#471B99",
                    buttonfg = "#F7CB04",
                    buttonhfg = "#F7CB04",
                    buttonhbg = "#7D2ACF")
    elif theme == "nature":  
        themeChanger(rootcolor = "#68BB59",
                    timerframecolor = "#1E5631",
                    timerframefg = "#A4DE02",
                    buttonbg = "#1E5631",
                    buttonfg = "#A4DE02",
                    buttonhfg = "#A4DE02",
                    buttonhbg = "#4C9A2A")



TOP_MENU = Menu(root)
root.config(menu = TOP_MENU)

themes_menu = Menu(TOP_MENU, tearoff = False) 
about_menu = Menu(TOP_MENU, tearoff = False)
modes_menu = Menu(TOP_MENU, tearoff = False)

TOP_MENU.add_cascade(label = "Themes", menu = themes_menu)
TOP_MENU.add_cascade(label = "Modes", menu = modes_menu)

def about_page():
    AboutPage = Toplevel(root)
    AboutPage.resizable(False, False)
    AboutPage.title("About Me")
    about_image = PhotoImage(file ="images\\about-me.png").subsample(3, 3)
    AboutPage.iconbitmap("images/info.ico")
    AboutLabel = Label(AboutPage, image = about_image)
    AboutLabel.pack()
    AboutPage.mainloop()
TOP_MENU.add_command(label = "About", command = about_page)

themes_menu.add_command(label ="Light", command = lambda: changeThemeTo("light"))
themes_menu.add_command(label ="Lava", command = lambda: changeThemeTo("lava"))
themes_menu.add_command(label ="Navy", command = lambda: changeThemeTo("navy"))
themes_menu.add_command(label ="Carnival", command = lambda: changeThemeTo("carnival"))
themes_menu.add_command(label ="Nature", command = lambda: changeThemeTo("nature"))

modes_menu.add_command(label = "Shutdown", command = lambda: setshutdownmode("shutdown"))
modes_menu.add_command(label = "Restart", command = lambda: setshutdownmode("restart"))
modes_menu.add_command(label = "Sleep", command = lambda: setshutdownmode("sleep"))
modes_menu.add_command(label = "None", command = lambda: setshutdownmode("none"))




# ~~~~~~~~~~~~~~~ STANDARD FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~

shutdownmode = "none"
def setshutdownmode(x):
    global shutdownmode
    global ShutdownLabel
    shutdownmode = x
    if x == "none":
        ShutdownLabel.grid_forget()
    else:
        if not ShutdownLabel.winfo_manager():
            ShutdownLabel.grid(row = 2, column = 0, columnspan = 3, sticky = "w")
        ShutdownLabel['text'] = f"{x.upper()}_ENABLED"

def displayNotification(timeTitle, displayedMessage):
    from plyer import notification
    notification.notify(
        title = timeTitle,
        app_icon = "images/alarm.ico",
        app_name = "Timothy",
        message = displayedMessage,
        timeout = 30,
        toast = True
    )
    winsound.PlaySound("ringtone/default1.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

# Standard Functions for changing the text inside the respective entries.
def changeSecondEntry(text):
    SecondEntry.delete(0, END)
    SecondEntry.insert(0, text)
def changeMinuteEntry(text):
    MinuteEntry.delete(0, END)
    MinuteEntry.insert(0, text)
def changeHourEntry(text):
    HourEntry.delete(0, END)
    HourEntry.insert(0, text)

# Enables and Disable the state of the entries
def EnableAllEntries():
    SecondEntry['state'] = NORMAL
    MinuteEntry['state'] = NORMAL
    HourEntry['state'] = NORMAL

def DisableAllEntries():
    SecondEntry['state'] = DISABLED
    MinuteEntry['state'] = DISABLED
    HourEntry['state'] = DISABLED

# Executes this function when the timer hits 0:00:00
timeSet = "0:00:00"
NotificationTitle = "Time's Up Kiddo!"
NotificationMessage = f"Have a great day buddy!"
def EndCountdown():
    global shutdownmode
    if shutdownmode == "none":
        global recursionCtr
        global timeSet
        global NotificationTitle
        global NotificationMessage
        displayNotification(NotificationTitle, NotificationMessage+"\n"+timeSet)
        NotificationTitle = "Time's Up Kiddo!"
        NotificationMessage = "Have a great day buddy!"
        recursionCtr = 0
        clearTimer()
    elif shutdownmode == "sleep":
        cmd("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")
    elif shutdownmode == "restart":
        cmd("shutdown /r /t 0")
    elif shutdownmode == "shutdown":
        cmd("shutdown /s /t 0")
        

# Executed when the developer key is pressed (Right click on PlayButton)
def developerCommand(event):
    global NotificationMessage
    global NotificationTitle
    NotificationTitle = simpledialog.askstring("Developer Window", "Enter the custom title: ")
    NotificationMessage = simpledialog.askstring("Developer Window", "Enter the custom message: ")
    startTimer()

# Gives functionality to all the preset timer-buttons.
def setTimer(x):
    if "" in (SecondEntry.get(), MinuteEntry.get(),HourEntry.get()):
        changeHourEntry(0)
        changeMinuteEntry(0)
        changeSecondEntry(0)
    if len(x.split(":")) == 2:
        x = list(map(int, x.split(":")))
        changeSecondEntry(int(SecondEntry.get()) + x[-1])
        changeMinuteEntry(int(MinuteEntry.get()) + x[-2])
        changeHourEntry(int(HourEntry.get()) + 0)
    elif len(x.split(":")) == 3:
        x = list(map(int, x.split(":")))
        changeSecondEntry(int(SecondEntry.get()) + x[-1])
        changeMinuteEntry(int(MinuteEntry.get()) + x[-2])
        changeHourEntry(int(HourEntry.get()) + x[-3])
    
    # If the timer entries exceed their limits (i.e. more than 60 minutes or seconds), then the program formatsit in suitable order
    if int(SecondEntry.get()) >= 60:
        changeMinuteEntry(int(MinuteEntry.get()) + int(SecondEntry.get())//60)
        changeSecondEntry(int(SecondEntry.get())%60)

    if int(MinuteEntry.get()) >= 60:
        changeHourEntry(int(HourEntry.get()) + int(MinuteEntry.get())//60)
        changeMinuteEntry(int(MinuteEntry.get())%60)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~ 3-BUTTON FUNCTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Gives functionality to the play/start button.If the pauseStatus is True, then only will the countdown begin.
pauseStatus = False
recursionCtr = 0
def startTimer(*event): # FUNCTION OF THE PLAY_BUTTON
    global pauseStatus
    global recursionCtr
    global timeSet
    if recursionCtr == 0:
        recursionCtr+=1
        timeSet = "{:02d}:{:02d}:{:02d}".format(int(HourEntry.get()), int(MinuteEntry.get()), int(SecondEntry.get()))
    try:
        PlayButton['state'] = DISABLED
    # checks the pauseStatus of the Timer
        if pauseStatus:
            EnableAllEntries()
        else:
            Second = int(SecondEntry.get())
            Minute = int(MinuteEntry.get())
            Hour = int(HourEntry.get())
            # Actual Timer ~ Checks whether the 0`0`0` has been reached, or else continue the clock
            if int(SecondEntry.get()) == int(MinuteEntry.get()) == int(HourEntry.get()) == 0:
                EndCountdown()
                PlayButton['state'] = NORMAL
            else:
                EnableAllEntries()
                if not int(SecondEntry.get()):
                    # If seconds become 0
                    changeSecondEntry(59)
                    # If minute becomes 0
                    if not Minute:
                        changeHourEntry(Hour-1)
                        changeMinuteEntry(59)
                    else:
                        changeMinuteEntry(Minute-1)
                    # Looping the function
                    SecondEntry.after(1000, startTimer)
                    DisableAllEntries()
                else:
                    changeSecondEntry(Second-1)
                    SecondEntry.after(1000, startTimer)
                    DisableAllEntries()
    except:
        PlayButton['state'] = NORMAL


# Gives functionality to the cancel button by setting all the entries to " ", causing the startTimer func. to except error and stop.  
def clearTimer(): # FUNCTION OF THE CANCEL BUTTON 
    EnableAllEntries()
    changeHourEntry("")
    changeMinuteEntry("")
    changeSecondEntry("")

# Gives functionality to the pause button by setting toggling the pauseStatus of the button.
def pauseTimer(): # FUNCTION OF THE PAUSE BUTTON
    global pauseStatus
    if pauseStatus:
        pauseStatus = False
        PlayButton['state'] = NORMAL
    else:
        pauseStatus = True
        PlayButton['state'] = DISABLED
    


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ UPPER COUNTDOWN DISPLAY FRAME ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Creates the main Timer Setup Frame
TimerFrame = LabelFrame(root, text = "    Enter  the  Time: ", font =  "BebasNeue-Regular 30", padx = 20, pady = 10, fg = "black", bg = "#b7e9f7",bd = 0)
TimerFrame.pack(padx = (40, 30), pady = (30, 20))

# Displays the Label of the Entries
LabelHour = Label(TimerFrame, text = "Hour", bg = "#b7e9f7", font = "BebasNeue-Regular 19")
LabelHour.grid(row = 0, column = 0, stick = "nw", padx = 20)
LabelMinute = Label(TimerFrame, text = "Minute", bg = "#b7e9f7", font = "BebasNeue-Regular 19")
LabelMinute.grid(row = 0, column = 1, stick = "nw", padx = 20)
LabelSecond = Label(TimerFrame, text = "Seconds", bg = "#b7e9f7", font = "BebasNeue-Regular 19")
LabelSecond.grid(row = 0, column = 2, stick = "nw", padx = 20)

ShutdownLabel = Label(TimerFrame, text = "", bg = "#b7e9f7", font = "Helvetica 17 bold")
ShutdownLabel.grid(row = 2, column = 0, columnspan = 3, sticky = "w")

# Displays the entries of Hour, Minute and Second
HourEntry = Entry(TimerFrame, width = 5, font = "Helvetica 40")
HourEntry.grid(padx = 20, pady = (7, 20),row =1, column = 0)
MinuteEntry = Entry(TimerFrame, width = 5, font = "Helvetica 40")
MinuteEntry.grid(padx = 20, pady = (7, 20), row =1, column = 1)
SecondEntry = Entry(TimerFrame, width = 5, font = "Helvetica 40")
SecondEntry.grid(padx = 20, pady = (7, 20), row =1, column = 2)

HourEntry.focus_set()
SecondEntry.bind("<Return>", startTimer)
MinuteEntry.bind("<Return>", startTimer)
HourEntry.bind("<Return>", startTimer)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TIMER CONTROL BUTTONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Frame holding the 3 buttons, pause - play - cancel
ButtonFrame = Frame(TimerFrame, bg = "#b7e9f7")
ButtonFrame.grid(row = 2, column = 2)

# Play Button
Play_image = PhotoImage(file ="images\\play-button.png").subsample(8, 8)
PlayButton = Button(ButtonFrame, image = Play_image, bg = "#b7e9f7", relief = FLAT, command = startTimer, activebackground = "#b7e9f7", bd = 0)
PlayButton.grid(row = 0, column = 0)
PlayButton.bind("<Button-3>", developerCommand)

# Cancel Button
Cancel_image = PhotoImage(file ="images\\cancel-button.png").subsample(8, 8)
ClearButton = Button(ButtonFrame, image = Cancel_image, bg = "#b7e9f7", relief = FLAT, command = clearTimer, activebackground = "#b7e9f7", bd = 0)
ClearButton.grid(row = 0, column = 1)

# Pause Button
Pause_image = PhotoImage(file ="images\\pause.png").subsample(8, 8)
PauseButton = Button(ButtonFrame, image = Pause_image, bg = "#b7e9f7", relief = FLAT, command = pauseTimer, activebackground = "#b7e9f7", bd = 0)
PauseButton.grid(row = 0, column = 2)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TIMER TILES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TimerTiles(Button):
    def __init__(self, master, **kwargs):
        Button.__init__(self, master = master, **kwargs)
        
        self.defaultbg = "#92dff3"
        self.defaultfg = "#000000"
        self.hoverbg = "#92cef3"
        self.hoverfg = "#000000"
        # self.activebg = "#298fca"
        # self.activefg = "white"

        self['bg'] = self.defaultbg     
        self['fg'] = self.defaultfg     
        self["relief"] = FLAT
        self.bind("<Enter>", self.hover_in)
        self.bind("<Leave>", self.hover_out)
        # self['activebackground'] = self.activebg 
        # self['activeforeground'] = self.activefg
        self["command"] = lambda: setTimer(self['text'])
        self['font'] = "BebasNeue-Regular 30"
        self["anchor"] = "w"
        self["padx"] = 10
        self['bd'] = 0
        
    def hover_out(self, event):
        self['bg'] = self.defaultbg     
        self['fg'] = self.defaultfg 
    def hover_in(self, event):
        self['bg'] = self.hoverbg
        self['fg'] = self.hoverfg
    
    def changeTheme(self, defaultbg, defaultfg, hoverbg, hoverfg):
        self.defaultbg = defaultbg
        self.defaultfg = defaultfg
        self.hoverbg = hoverbg
        self.hoverfg = hoverfg
        self['bg'] = self.defaultbg
        self['fg'] = self.defaultfg


# Frame for 5:00
Button1 = TimerTiles(root, text  = "5:00", anchor = "w", padx = 10)
Button1.pack(fill = X, expand = True, pady = (10, 0), padx = 20)

# Frame for 10:00
Button2 = TimerTiles(root, text  = "10:00", anchor = "w", padx = 10)
Button2.pack(fill = X, expand = True, pady = (10, 0), padx = 20)

# Frame for 15:00
Button3 = TimerTiles(root, text  = "15:00", anchor = "w", padx = 10)
Button3.pack(fill = X, expand = True, pady = (10, 0), padx = 20)

# Frame for 20:00
Button4 = TimerTiles(root, text  = "20:00", anchor = "w", padx = 10)
Button4.pack(fill = X, expand = True, pady = (10, 0), padx = 20)

# Frame for 30:00
Button5 = TimerTiles(root, text  = "30:00", anchor = "w", padx = 10)
Button5.pack(fill = X, expand = True, pady = (10, 0), padx = 20)

# Frame for 1:00:00
Button6 = TimerTiles(root, text  = "1:00:00", anchor = "w", padx = 10)
Button6.pack(fill = X, expand = True, pady = (10, 30), padx = 20)

with open("settings/changeDefaultTheme.txt", "r") as file:
    defaultTheme = file.read().lower()
try:
    changeThemeTo(defaultTheme)
except:
    changeThemeTo("light")

with open("settings/changeDefaultMode.txt", "r") as file:
    defaultMode = file.read().lower()
try:
    setshutdownmode(defaultMode)
except:
    setshutdownmode("none")


root.mainloop()