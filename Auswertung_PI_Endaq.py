# -*- coding: utf-8 -*-
'''
Created on Tue Feb 14 15:28:32 2023

@author: Gaiselmann
'''

import numpy as np
import matplotlib.pyplot as plt
# import scipy as sp
from scipy.signal import savgol_filter, find_peaks
# import math
# from math import factorial
import pandas as pd
import tkinter as tk
from tkinter import ttk as ttk, filedialog, StringVar
import os
from PIL import ImageTk, Image
import sys
# from colorama import Fore, Style
# import math

versionNumber ='Version 1.1'
versionDate = ' (Date 14.02.2024)'

def __init__():
    print('Evaluating Perfomance Index measurement \t'  + versionNumber + versionDate +'\t Author: Gaiselmann')
__init__()

'''
UI: 
Auswählen von Datei
Auswählen von Pfad wo gespeichert werden soll
Eingabe unter welchem Namen das gespeichert werden soll
Mit Button beenden
Pop-Up Messungsanzahl
Anzeige Plot
Berechnung und Speichern von Excel und PNG

Kalibrierung
!!!!!
Zu Beginn jeder Messung: 
System 15 sekunden liegen lassen
!!!!!
von Sekunde 5 - 10 Mittelwert der Resultierernden: Sollte ca. 1g sein. 
den dann auf 9.81 m/s² bringen und dann ... oder ned
wieder auf 0 bringen... ODER???
dann die ganzen komischen Berechnungen und so 

Performance Index Berechnung = Reboundhöhe (mm) **Faktor *1000 /(Maximale Beschleunigung in g)
Performance Index Faktor : 1.4
'''

def set_rebound():
    if rebound_entry.get()=='':
        print('no height entered.')
    
    else: 
        global rebound_height
        global rebound_set
        rebound_set = 'manual'
        rebound_height = int(rebound_entry.get())
        print('Reboundheight set at '+str(rebound_height)+' mm.')
        rebound_entry.grid_forget()
        MhButton.grid_forget()
        rebound_label.destroy()
        
def getvalues():
    if name_entry.get()=='':
        print('no name entered.')
    else: 
        global name
        name = name_entry.get()
        # button1.grid_forget()
        root1.destroy()
    
def saveAndExit():
    root_setup.destroy()
    
def saveAndExit2():
    root_setup2.destroy()
    
def stopProgram():
    root2.destroy() 
    sys.exit('Program stopped')

def RemoveCheck():
    global removeCheck
    removeCheck = True
    RemButton.grid_forget()
    # removeButton.destroy()
    
# def removeMeasurement(temp1):
    
#     # MeasurementsToBeRemoved=[]
#     MeasurementsToBeRemoved.append(temp1)
    
    



def setString(msg):
    # global sensorType
    sensorType=msg
    print(sensorType)

    
class RootWindow:
    
    # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox

        
    def quit_and_destroy(self):
        self.root.quit()
        self.root.destroy()
        
    def quit_and_stop(self):
        self.root.quit()
        self.root.destroy()
        sys.exit('Programm gestoppt.')

    def __init__(self, root,title,backgrnd):
        self.root = root
        self.root.title(title)
        self.root.configure(background=backgrnd)
        self.root.protocol('WM_DELETE_WINDOW', lambda: self.quit_and_destroy())

    def addQuitButton(self,gridRow,gridClmn):
        self.quit_button = tk.Button(self.root, text='Speichern & Beenden', command=self.quit_and_destroy, bg=color_green, fg = 'black', highlightthickness=2, width=w3,height=ch5, font=(customFont1,int(fs-2)))
        self.quit_button.grid(row=gridRow,column=gridClmn, padx=4 , pady=8)
        return self.quit_button
    
    def addStopButton(self,gridRow,gridClmn):
        # os.remove(plot_path_percent)
        self.stop_button = tk.Button(self.root, text='Stop', command=self.quit_and_stop, bg='red', fg = 'black', highlightthickness=2, width=w3,height=ch5, font=(customFont1,int(fs-2)))
        self.stop_button.grid(row=gridRow,column=gridClmn)
        return self.stop_button

    def addStringButton(self,msg,cmd,gridRow,gridClmn):
        self.Button = tk.Button(self.root, text=msg, command=lambda: setString(cmd), font=customFont1, width=ch1, height=ch5, foreground='black', background=ET_Blau_Hell)
        self.Button.grid(row=gridRow,column=gridClmn,padx=4, pady=4)
    
    def create_setup_label_combobox(self,root, text, default_value, values):
        global row_counter

        label = tk.Label(root, text=text, font=(customFont1, fs), anchor=tk.CENTER, bg='white',fg='#333333', borderwidth=3,  relief='solid' )
        label.grid(column=0, row=row_counter, pady=4, padx=8)
        
        if (type(default_value)==str):
            variable = tk.StringVar(root)
        elif (type(default_value)==int):
            variable = tk.IntVar(root)
        elif (type(default_value)==float):
            variable = tk.DoubleVar(root)
        variable.set(default_value)
        
        # style= ttk.Style()
        # style.theme_use('clam')
        # style.configure("TCombobox", fieldbackground= "orange", background= "white")


        combobox = ttk.Combobox(root, textvariable=variable, values=values, font=customFont1)
        combobox.config(width=8)
        combobox.grid(column=1, row=row_counter, pady=4, padx=8)
        
        row_counter += 1
        
        return variable

customFont1=('Verdana')


'Grundlagen Werte'

# fs1 = 14 #FontSize
# fs2=20
ch1=12
ch2=8
ch3=4
ch4=2
ch5=1
w1=27
w2=93
w3=20
w4=17
w5=24
w6=37
wc=0

windowSize=15
rebound_set = 'auto'
lw = 2 #linewidth
# factor_PI = 1.4 #Performance Index Berechnung
KugelArt = 20
# sensorType ='Endaq'
distanceSingleMeasurementsPeaks=10000
bw = 4 #borderwidth
w1 = 5 #Width1
w2 = 8 #Width2
# w3 = 25 #Width3
fs = 14 #FontSize
fs2=20
ET_Blau= '#0068B4'
ET_Blau_Hell = '#6496B4'
# factor_us=1.6666666666667 * 10**-8 #Microsekunden
Color_grey='#696969'
color_orange='#CC7722'
color_red='#B46464'
color_green='#64B464'
color_blue='#89CFF0'
color_yellow='#E1C16E'
namerange=19
image_path  = 'H:/Technik/Gaiselmann/Wichtige Words und Excels und Skripte/Eurotramp_Logo.png'


global MeasurementsToBeRemoved
MeasurementsToBeRemoved =[]

'Variablen für Peaks Findung'

height_peaks=2
distance_peaks=50
prominence_peaks=3
width_peaks=50

row_counter=0
j = 0
'''
!!!!!
'''
bounces = 1
inwards = 1
inwards2 = 1
grenze = -0.89 # ganz wichtig ... Wird immer wieder angepasst
'''
!!!!!
'''
# checkMSG = 'No'
checkCalibrate= 'Yes'
checkEinzelmessungen = 'No'
calcPerfIndex='Yes'
checkFindPeaks = 'No'
checkMoreData = 'No'
checkFileChecker = 'No'
checkFilter='Yes'
checkRebound ='Yes'
checkMore='No'

global removeCheck
removeCheck = False
#TO DO 

# FILTER AND CALIBRATION

'Pop-Up Variablen Einstellung'

root_setup = tk.Tk()
app_setup=RootWindow(root_setup, 'Configure', Color_grey)
    # Title_setup=tk.Label(root_setup, text='Setup Vorspannung', font=(customFont1, 16, 'bold', 'underline'),fg='#CC7722', bg=Color_grey, anchor=tk.CENTER)
    # Title_setup.grid(row=row_counter, columnspan=2,pady=5)
    
    
# root_setup.configure(background=ET_Blau_Hell)
Title_setup=tk.Label(root_setup, text='Setup', font=(customFont1, fs2, 'bold', 'underline'),fg='#CC7722', bg=Color_grey, anchor=tk.CENTER)
Title_setup.grid(row=row_counter, columnspan=2,pady=5)
row_counter+=1
variable_Kugel=app_setup.create_setup_label_combobox(root_setup, ' Weight of sphere ', KugelArt, [20, 60])
# variable_sensorType=app_setup.create_setup_label_combobox(root_setup, ' Sensor type ', sensorType, ['Endaq', 'Yost'])

variable_CheckFindPeaks=app_setup.create_setup_label_combobox(root_setup, ' Setup searching peaks ', checkFindPeaks, [ 'Yes', 'No'])
variable_CheckFilter=app_setup.create_setup_label_combobox(root_setup, ' Savgol-filter', checkFilter, [ 'Yes', 'No'])
# variable_checkMSG=app_setup.create_setup_label_combobox(root_setup, ' Check Errors ', checkMSG, [ 'Yes', 'No'])
variable_checkMoreData=app_setup.create_setup_label_combobox(root_setup, ' Show more data ', checkMoreData, [ 'Yes', 'No'])
variable_checkMore=app_setup.create_setup_label_combobox(root_setup, ' Check more data ', checkMore, [ 'Yes', 'No'])


variable_checkCalibrate=app_setup.create_setup_label_combobox(root_setup, ' Calibrate seconds 5 - 10 ', checkCalibrate, [ 'Yes', 'No'])
variable_checkEinzelmessungen=app_setup.create_setup_label_combobox(root_setup, ' Check single measurements ', checkEinzelmessungen, [ 'Yes', 'No'])
variable_calcPerfIndex=app_setup.create_setup_label_combobox(root_setup, ' Calculate Performance Index ', calcPerfIndex, [ 'Yes', 'No'])
variable_checkRebound=app_setup.create_setup_label_combobox(root_setup, ' Check Rebound ', checkRebound, [ 'Yes', 'No'])


button1=tk.Button(root_setup, text='Save and Continue', bg=color_green, fg = 'black', highlightbackground='black', highlightthickness=2, width=20, font=(customFont1, int(fs)), command = lambda:saveAndExit())
button1.grid(column=0, columnspan=2, pady=4, padx=8)

# button_setup.grid_rowconfigure(1, weight=1)
# button_setup.grid_columnconfigure(1, weight=1)

buttonExit1=tk.Button(root_setup, text= 'Cancel', bg=color_red, fg = 'black', width=10, font=(customFont1, fs), command=lambda:[root_setup.destroy() , sys.exit('Program stopped')])
buttonExit1.grid(column=0, columnspan=2, padx=4, pady=4)
    
root_setup.mainloop()

KugelArt=variable_Kugel.get()
# sensorType =variable_sensorType.get()

if KugelArt == 20:
    factor_PI = 1.4
elif KugelArt == 60:
    factor_PI = 1.25

# factor_PI=variable_factorPI.get()


# checkMSG=variable_checkMSG.get()
checkCalibrate=variable_checkCalibrate.get()
checkEinzelmessungen=variable_checkEinzelmessungen.get()
checkFindPeaks=variable_CheckFindPeaks.get()
checkMoreData =variable_checkMoreData.get()
checkMore =variable_checkMore.get()

checkFilter=variable_CheckFilter.get()
checkRebound=variable_checkRebound.get()


if checkFindPeaks=='Yes':
    row_counter=0
    
    root_setup2= tk.Tk()
    app_setup2=RootWindow(root_setup2, 'Configure Peaks', Color_grey)

    Title_setup=tk.Label(root_setup2, text='Setup Peaks', font=(customFont1, fs2, 'bold', 'underline'),fg='#CC7722', bg=Color_grey, anchor=tk.CENTER)
    Title_setup.grid(row=row_counter, columnspan=2,pady=5)
    root_setup2.grid_rowconfigure(0, weight=1)
    root_setup2.grid_columnconfigure(0, weight=1)

    row_counter+=1
    variable_fileChecker=app_setup2.create_setup_label_combobox(root_setup2, ' Check File and Savepath ', checkFileChecker, [ 'Yes', 'No'])
    variable_height=app_setup2.create_setup_label_combobox(root_setup2, ' Height Peaks ', height_peaks, [2,3,4,5,6,7])
    variable_distance=app_setup2.create_setup_label_combobox(root_setup2,  ' Distance Peaks ', distance_peaks, [25, 50, 100, 150])
    variable_prominence=app_setup2.create_setup_label_combobox(root_setup2, ' Prominence Peaks ', prominence_peaks, [2,3,4,5])
    variable_width=app_setup2.create_setup_label_combobox(root_setup2, ' Width Peaks ', width_peaks, [10, 25, 50, 100, 150])
    variable_bounces=app_setup2.create_setup_label_combobox(root_setup2, ' Bounces ', bounces, [1,2,3,4,5])
    variable_inwards=app_setup2.create_setup_label_combobox(root_setup2, ' Inwards ', inwards, [-2,-1,0,1,2,3,4,5])
    variable_inwards2=app_setup2.create_setup_label_combobox(root_setup2, ' Inwards2 ', inwards2, [-2,-1,0,1,2,3,4,5])

    variable_grenze=app_setup2.create_setup_label_combobox(root_setup2, ' Limit ', grenze, [-.5,-.75,-.8, -.85, -.9, -.95, -1])
    variable_windowSize=app_setup2.create_setup_label_combobox(root_setup2, ' Windwow Size ', windowSize, [1,15,25, 50])
    
    button_setup=tk.Button(root_setup2, text='Save and Continue', bg=color_green, fg = 'black',justify=tk.CENTER, highlightbackground='black', highlightthickness=2, width=20, font=(customFont1, int(fs)), command = lambda:saveAndExit2())
    button_setup.grid(row=row_counter, padx=4, pady=8, columnspan=2)
    button_setup.grid_rowconfigure(1, weight=1)
    button_setup.grid_columnconfigure(1, weight=1)
    row_counter+=1
    buttonExit2=tk.Button(root_setup2, text= 'Cancel', bg=color_red, fg = 'black', width=10, font=(customFont1, fs), command=lambda:[root_setup2.destroy() , sys.exit('Program stopped')])
    buttonExit2.grid(row=row_counter, columnspan=2, padx=4, pady=4)
    
    root_setup2.mainloop()
    
        
    height_peaks=variable_height.get()
    distance_peaks=variable_distance.get()
    prominence_peaks=variable_prominence.get()
    width_peaks=variable_width.get()
    bounces=variable_bounces.get()
    inwards=variable_inwards.get()
    inwards2=variable_inwards.get()
    grenze=variable_grenze.get()
    checkFileChecker=variable_fileChecker.get()
    windowSize=variable_windowSize.get()

'Pop-Up Messung und Speicherort'

file = tk.filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File')
save_path = tk.filedialog.askdirectory(title='Select Folder to Save') 

if checkFileChecker == 'Yes' and (file=='' or save_path ==''):
    file = tk.filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File (again)')

    save_path = tk.filedialog.askdirectory(title='Select Folder to Save (again)') 

global sensorType
sensorType=''
df=pd.read_csv(file, sep=',', header=0, )
if len(df.columns)==7:
    sensorType='Yost'
    if checkFindPeaks !='Yes':
        height_peaks=4 
        distance_peaks=80
        width_peaks=10
        grenze = -0.7
        inwards=-2
        inwards2 =-1
        windowSize=25
                
    df.columns=(['CorrX','CorrY','CorrZ','RawX','RawY','RawZ','Time_us'])
    namerange=26
    distanceSingleMeasurementsPeaks=1200
    factor_us=1.6666666666667 * 10**-8 #Microsekunden
    time1=np.array((df.Time_us*factor_us)*60)
    res=np.array(np.sqrt(np.square(df.CorrX)+np.square(df.CorrY)+np.square(df.CorrZ)))
  
if len(df.columns)==4:
    sensorType='Endaq'
    df.columns=(['Time','X', 'Y','Z'])
    time1 = np.array(df.Time)

    namerange=19
    distanceSingleMeasurementsPeaks=10000
    # res=[]
    # res1.append(np.sqrt(np.square(df.X)+np.square(df.Y)+np.square(df.Z))) 
    res=np.array(np.sqrt(np.square(df.X)+np.square(df.Y)+np.square(df.Z)))


# if sensorType=='':
#     SelectSensorUser=input('Couldn`t set sensortype. Select manually (e=endaq, y=yost).\n')
#     # while SelectSensorUser!='e' or SelectSensorUser!='y':
#     #     SelectSensorUser=input('Try Again!\n')
#     if SelectSensorUser=='e':
#         sensorType='Endaq'
#         df.columns=(['Time','X', 'Y','Z'])
#         time1 = np.array(df.Time)

#         namerange=19
#         distanceSingleMeasurementsPeaks=10000
#         # res=[]
#         # res1.append(np.sqrt(np.square(df.X)+np.square(df.Y)+np.square(df.Z))) 
#         res=np.array(np.sqrt(np.square(df.X)+np.square(df.Y)+np.square(df.Z)))
    
#     if SelectSensorUser=='y':
#         sensorType='Yost'
#         if checkFindPeaks !='Yes':
#             height_peaks=4 
#             distance_peaks=80
#             width_peaks=10
#             grenze = -0.7
#             inwards=-2
#             inwards2 =-1
                    
#         df.columns=(['CorrX','CorrY','CorrZ','RawX','RawY','RawZ','Time_us'])
#         namerange=26
#         distanceSingleMeasurementsPeaks=1200
#         factor_us=1.6666666666667 * 10**-8 #Microsekunden
#         time1=np.array((df.Time_us*factor_us)*60)
#         res=np.array(np.sqrt(np.square(df.CorrX)+np.square(df.CorrY)+np.square(df.CorrZ)))
    
print('Sensor Type: '+ sensorType +'\n')

root1 = tk.Tk()
root1.configure(background=Color_grey)
root1.title('Information Performance Index')
# root1.withdraw()
# root1.deiconify()
s1=ttk.Style(root1)
s2=ttk.Style(root1)
root1.lift()


tk.Label(root1, text=' Filename ',font=(customFont1, fs),bg=color_yellow,highlightbackground=color_yellow, borderwidth=2, relief='solid').grid(column=0, row=0, pady=4, padx=8)
tk.Label(root1, text=' '+file[-namerange:]+' ', font=(customFont1, fs),  bg=color_yellow,highlightbackground=color_yellow, borderwidth=2, relief='solid').grid(column=1, row=0, pady=4, padx=8)
tk.Label(root1, text=' Savepath ', font=(customFont1, fs),  bg=color_yellow,highlightbackground=color_yellow, borderwidth=2, relief='solid').grid(column=0, row=1, pady=4, padx=8)
tk.Label(root1, text=' '+save_path+' ', font=(customFont1, fs), bg=color_yellow,highlightbackground=color_yellow, borderwidth=2, relief='solid').grid(column=1, row=1, pady=4, padx=8)
tk.Label(root1, text=' Name ', font=(customFont1, fs),  bg=color_blue, borderwidth=2, highlightbackground=color_blue,relief='solid').grid(column=0, row=2, pady=4, padx=8)
rebound_label=tk.Label(root1, font=(customFont1, fs), text=' Rebound height ', bg=color_blue,highlightbackground=color_blue, borderwidth=2, relief='solid')
rebound_label.grid(column=0, row=3, pady=4, padx=8)

# img_ET=Image.open(image_path)
# img_ET1=img_ET.resize((236, 60))
# my_img1=ImageTk.PhotoImage(img_ET1)
# ttk.Label(root1, image = my_img1,anchor='n').grid(column = 2,row=0, rowspan=2, padx=10, pady=2) 

name_entry=tk.Entry(textvariable = StringVar(), bg=color_blue, width=22, justify=tk.CENTER, font=(customFont1, fs),highlightbackground='black', highlightthickness=3)
name_entry.grid(column=1, row=2, pady=4, padx=8)

rebound_entry=tk.Entry(textvariable = StringVar(), bg=color_blue, width=12, justify=tk.CENTER, font=(customFont1, fs),highlightbackground='black', highlightthickness=3)
rebound_entry.grid(column=1, row=3, pady=4, padx=8)

MhButton = tk.Button(root1, text ='Set Rebound Height (mm)', bg=color_blue, fg = 'black', highlightbackground='black', highlightthickness=2, width=24, font=(customFont1, int(fs)), command = lambda:set_rebound())
MhButton.grid(column=0, columnspan=2, row=4, pady=4, padx=8)

button1=tk.Button(root1, text='Save and Continue', bg=color_green, fg = 'black', highlightbackground='black', highlightthickness=2, width=20, font=(customFont1, int(fs)), command = lambda:getvalues())
button1.grid(column=0, columnspan=2, pady=4, padx=8)

buttonExit3=tk.Button(root1, text= 'Cancel', bg=color_red, fg = 'black', width=10, font=(customFont1, fs), command=lambda:[root1.destroy() , sys.exit('Program stopped')])
buttonExit3.grid(columnspan=2, padx=4, pady=4)
    

root1.mainloop()


if checkFilter=='Yes':
    res_filtered = savgol_filter(res, windowSize, 5)
    print('Data filtered with a window size of ' +str(windowSize)+ '.')
else:
    res_filtered=res
    print('Data was not filtered.')

# res_filtered = savitzky_golay(res, 15, 5) #     (y, window_size, order)
res_filtered_minus1 = res_filtered -1 #hier 1 g abziehen
#res_filtered_minus1_m_s_2=res_filtered*9.81

if (checkCalibrate=='Yes'):
    if sensorType=='Yost':
        ruhe=np.mean(res_filtered_minus1[5000:10000])
    elif sensorType=='Endaq':
        ruhe=np.mean(res_filtered_minus1[20000:40000])
    print('Calibrated between seconds 5 and 10 with a value of '+str(round(ruhe,2))+'g.')
else: 
    ruhe=0
    print('Measurement was not calibrated.')
res_filtered_minus1_cal = res_filtered_minus1-ruhe

'Peaks Finden -> Messungsanzahl'
# peaks_filtered=find_peaks(res,height=3.5, threshold=[0,10], distance=100, prominence=4, width=20, wlen=None, rel_height=0.5, plateau_size=None)
# peaks_filtered=find_peaks(res_filtered_minus1_cal, height=4, threshold=[0,10], distance=100, prominence=4, width=50, wlen=None, rel_height=0.5, plateau_size=None)#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html
peaks_filtered=find_peaks(res_filtered_minus1_cal, height=height_peaks, threshold=[0,40], distance=distance_peaks, prominence=prominence_peaks, width=width_peaks, wlen=None, rel_height=0.5, plateau_size=None)#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html

diff=np.diff(peaks_filtered[0])
loc=np.asarray(diff>distanceSingleMeasurementsPeaks).nonzero()

loc=loc[0]+1 #+1 weils bei diff verloren geht -> Käpsele ... weiß zwar nimmer was ich damit mein aber bast 
loc = np.insert(loc,0,0)

diff_loc=np.diff(loc)
np.append(diff_loc,len(diff)-loc[-1]+1)
# global loc_new
loc_new=np.delete(loc,np.where(diff_loc < bounces)) #wenn weniger als X Bounces Messung löschen
loc_new_removed=loc_new
n=len(loc_new)
measurements = np.arange(1,n+1)

'Plot Ungefiltert und Gefiltert'
plt.ioff()
# plt.figure()
fig, ax = plt.subplots()
line1, = ax.plot(res, label='Acceleration RES '+name, linewidth=lw)
line2, = ax.plot(res_filtered_minus1_cal, label='Acceleration RES',color='red', linewidth=lw)
# line3, = ax.plot(test, label='Acceleration Filter Test',color='green', linewidth=lw)
# line4, = ax.plot(test2, label='Acceleration Filter Test savgol py',color='yellow', linewidth=lw)
ax.axhline(y=grenze,color='black')
ax.set_title(name+' PI')
ax.set_xlabel('Frame')
ax.set_ylabel('Acceleration (g)')
ax.set_ylim(-1, 10)
ax.grid(True)
ax.legend(loc='upper left')
fig.savefig(save_path +'/'+ name + '.png')
# plt.ion()

'Pop-Up Anzahl Messungen'
root2 = tk.Tk()
root2.configure(background=Color_grey)
root2.title('Check measurements')
img_accel=Image.open(save_path +'/'+ name + '.png')
img_accel1=img_accel.resize((768, 572))
my_img2=ImageTk.PhotoImage(img_accel1)
tk.Label(root2, image = my_img2,highlightbackground='black', highlightthickness=2).grid(column = 0, row=0, padx=10, pady=8)
tk.Label(root2, text= str(n) + ' measurements found.',background = Color_grey,foreground=color_orange,highlightbackground=color_orange,highlightthickness=2, font=(customFont1, fs2)).grid(column=0, row=1, padx=4, pady=8)
button2=tk.Button(root2, text= 'Confirm and Continue', bg=color_green, fg = 'black', width=20, font=(customFont1, fs), command=lambda:root2.destroy())
button2.grid(column=0, row=2, padx=4, pady=4)

exitButton=tk.Button(root2, text= 'Stop', bg=color_red, fg = 'black', width=10, font=(customFont1, fs), command=lambda:stopProgram())
exitButton.grid(column=0, row=3, padx=4, pady=4)

# tk.Label(root2, text='Remove measurement?',background = Color_grey,foreground=color_orange, font=(customFont1, fs)).grid(column=0, row=4, padx=4, pady=8)
# comboboxRemove = ttk.Combobox(root2, textvariable='', values=list((range(int(1),int(len(loc_new)+1)))), font=customFont1)
# comboboxRemove.config(width=8)
# comboboxRemove.grid(column=0, row=5, pady=4, padx=8)

RemButton = tk.Button(root2, text ='Remove Measurements', bg=color_orange, fg = 'black', highlightbackground='black', highlightthickness=2, width=20, font=(customFont1, fs), command = lambda:RemoveCheck())
RemButton.grid(column=0, row=6, padx=4, pady=8)

root2.mainloop()

os.remove(save_path +'/'+ name + '.png')

'Berechnung Rebound'
# Wer bei den Variablen noch durchblickt: Herzlichen Glückwunsch!
firstbounce, relevant_accel, relevant_time, first, last, time, airtime1, airtime2, airtime, zeit, hoehe, airbourne, mean_airbourne = [],[],[],[],[],[],[],[],[],[],[],[],[]

# df.Time.reset_index
if checkRebound=='Yes':
    for i in range(len(loc_new)):
        j=loc_new[i]
        firstbounce.append(res_filtered_minus1_cal[peaks_filtered[0][j]:peaks_filtered[0][j+1]]) #von peak 1 bis peak 2 -> relevanter Bereich
        relevant_time.append(time1[peaks_filtered[0][j]:peaks_filtered[0][j+1]]) #Zeit relevanter Bereich
        relevant_accel.append(np.where(firstbounce[i] <= grenze)) #suchen wo Beschleunigung unter Grenze
        first.append(relevant_accel[i][0][0]+inwards) #Erster Wert Beschleunigung unter Grenze
        last.append(relevant_accel[i][0][-1]-inwards2) #Letzter Wert Beschleunigung unter Grenze
        airbourne.append(firstbounce[i][first[i]:last[i]])
        mean_airbourne.append(np.mean(airbourne[i]))
        
        time.append(relevant_time[i][first[i]:last[i]])
        airtime1.append(time[i][0])
        airtime2.append(time[i][-1])
        airtime.append((airtime2[i]-airtime1[i])/2) #schon halbiert
    
        zeit.append(airtime[i])
        hoehe=np.append(hoehe, round(((0.5 * -9.81* zeit[i]**2) * - 1 * 1000),4))
else: 
    for i in range(len(loc_new)):
        j=loc_new[i]
        firstbounce.append(res_filtered_minus1_cal[peaks_filtered[0][j]:peaks_filtered[0][j]+4000]) #von peak 1 bis peak 2 -> relevanter Bereich

        hoehe=np.append(hoehe,0)

'Figures zur Überprüfung Start und Endpunkt Freier Fall'

buttonRemoveMeasurement=[]

if (checkEinzelmessungen=='Yes' or removeCheck):
    plt.ion()
    for i in range(len(loc_new)):
        fig1,ax1 = plt.subplots()
        ax1.plot(firstbounce[i], label='Firstbounce',color='blue', linewidth=lw)
        ax1.axhline(y=grenze,color='black')
        ax1.set_title('Measuremnt: ' +str(i+1))
        ax1.grid(True)
    if removeCheck:
        rootRemove = tk.Tk()
        rootRemove.configure(background=Color_grey)
        
        rootRemove.title('Remove Measurements')
        tk.Label(rootRemove, text= 'Select measurements to be removed.',background = Color_grey,foreground=color_orange, font=(customFont1, fs)).grid(column=0,  padx=4, pady=8)
        for k in range(len(loc_new)):
            # intButtonRemove.append(k+1)
            
            buttonRemoveMeasurement.append((tk.Button(rootRemove, text= 'M'+str(k+1) , bg=color_green, fg = 'black', width=4, font=(customFont1, fs), command=lambda k=k:[MeasurementsToBeRemoved.append(k), buttonRemoveMeasurement[k].grid_forget()])))
            buttonRemoveMeasurement[k].grid(column=0,  padx=4, pady=4)
            
        exitButton=tk.Button(rootRemove, text= 'Stop', bg=color_red, fg = 'black', width=10, font=(customFont1, fs), command=lambda:rootRemove.destroy())
        exitButton.grid(column=0, padx=4, pady=4)
        rootRemove.mainloop()
        
        
        loc_new=np.delete(loc_new,MeasurementsToBeRemoved)
        measurements=np.delete(measurements,MeasurementsToBeRemoved)
        
        MeasurementsToBeRemoved_User = [m+1 for m in MeasurementsToBeRemoved]
        MeasurementsToBeRemoved_User.sort()
        
        if len(MeasurementsToBeRemoved_User)>1:
            print('Measurements '+ ' and '.join(str(l) for l in MeasurementsToBeRemoved_User)+ ' removed.') 
        elif len(MeasurementsToBeRemoved_User)==1:
            print('Measurement '+ ''.join(str(l) for l in MeasurementsToBeRemoved_User)+ ' removed.') 
            
        firstbounce, relevant_accel, relevant_time, first, last, time, airtime1, airtime2, airtime, zeit, hoehe, airbourne, mean_airbourne,hoehe2 = [],[],[],[],[],[],[],[],[],[],[],[],[],[]
        
        if checkRebound=='Yes':
            for i in range(len(loc_new)):
                j=loc_new[i]
                firstbounce.append(res_filtered_minus1_cal[peaks_filtered[0][j]:peaks_filtered[0][j+1]]) #von peak 1 bis peak 2 -> relevanter Bereich
                relevant_time.append(time1[peaks_filtered[0][j]:peaks_filtered[0][j+1]]) #Zeit relevanter Bereich
                relevant_accel.append(np.where(firstbounce[i] <= grenze)) #suchen wo Beschleunigung unter Grenze
                first.append(relevant_accel[i][0][0]+inwards) #Erster Wert Beschleunigung unter Grenze
                # last.append(relevant_accel[i][0][-1]-2) #Letzter Wert Beschleunigung unter Grenze
                last.append(relevant_accel[i][0][-1]-inwards2) #Letzter Wert Beschleunigung unter Grenze
    
                airbourne.append(firstbounce[i][first[i]:last[i]])
                mean_airbourne.append(np.mean(airbourne[i]))
                
                time.append(relevant_time[i][first[i]:last[i]])
                airtime1.append(time[i][0])
                airtime2.append(time[i][-1])
                airtime.append((airtime2[i]-airtime1[i])/2) #schon halbiert
    
                zeit.append(airtime[i])
                hoehe=np.append(hoehe, round(((0.5 * -9.81* zeit[i]**2) * - 1 * 1000),4))
        else: 
              for i in range(len(loc_new)):
                  j=loc_new[i]
                  firstbounce.append(res_filtered_minus1_cal[peaks_filtered[0][j]:peaks_filtered[0][j]+4000]) #von peak 1 bis peak 2 -> relevanter Bereich

                  hoehe=np.append(hoehe,0)
            
plt.ioff()     



'Berechnung Max G'
mean_mean_airbourne=1+np.mean(mean_airbourne)
#maxg = np.around(peaks_filtered[1]['peak_heights'][loc]-mean_mean_airbourne, decimals = 4)
#Ich setzte den Airbourne auf -1 g; weil das so sein sollte eigentlich und zieh dann die 0.1-0.2 g von dem Wert ab... sollte man eigentlich lassen oder? 
#Sensor wurde ja schon 'Kalibriert'

maxg = np.around(peaks_filtered[1]['peak_heights'][loc_new], decimals = 4)
#das vllt nicht gefiltert?! is glaub wurscht

eindringtiefe,fallfirstbounce,fallrelevant_time,fallrelevant_accel, fallfirst,falllast,fallairbourne, falltime, fallairtime1, fallairtime2, fallairtime, fallzeit,fallhoehe, fallgeschwindigkeit=[],[],[],[],[],[],[],[],[],[],[],[],[],[]

if checkMore =='Yes':
    for i in range(len(loc_new)): 
        j=loc_new[i]
        fallfirstbounce.append(res_filtered_minus1_cal[peaks_filtered[0][j]-distanceSingleMeasurementsPeaks:peaks_filtered[0][j]])
        
        fallrelevant_time.append(time1[peaks_filtered[0][j]-distanceSingleMeasurementsPeaks:peaks_filtered[0][j]]) #Zeit relevanter Bereich
        fallrelevant_accel.append(np.where(fallfirstbounce[i] <= grenze)) #suchen wo Beschleunigung unter Grenze
        fallfirst.append(fallrelevant_accel[i][0][0]+inwards) #Erster Wert Beschleunigung unter Grenze
        falllast.append(fallrelevant_accel[i][0][-1]-inwards) #Letzter Wert Beschleunigung unter Grenze
        fallairbourne.append(fallfirstbounce[i][first[i]:last[i]])
        # mean_airbourne.append(np.mean(airbourne[i]))
        
        falltime.append(fallrelevant_time[i][fallfirst[i]:falllast[i]])
        fallairtime1.append(falltime[i][0])
        fallairtime2.append(falltime[i][-1])
        fallairtime.append((fallairtime2[i]-fallairtime1[i])) #schon halbiert
    
        fallzeit.append(fallairtime[i])
        fallhoehe.append(round(((0.5 * -9.81* fallzeit[i]**2) * - 1 * 1000),4))
        fallgeschwindigkeit.append(round((( -9.81* fallzeit[i]) * - 1),2))
        eindringtiefe.append(round(((fallgeschwindigkeit[i]**2)/(maxg[i]*9.81))*1000,2))#stimmt nicht

'Berechnung Mittelwerte/Median'
mean_max_g = np.mean(maxg)
std_max_g = np.std(maxg)
mean_height = np.mean(hoehe)
std_height = np.std(hoehe)
med_max_g = np.median(maxg)
med_height = np.median(hoehe)


if rebound_set == 'manual':
    hoehe2=rebound_height
    if KugelArt == 20: 
        perf_indexs2=(((hoehe2/1000)**factor_PI)*1000)/maxg #20kg
    elif KugelArt == 60: 
        perf_indexs2=(hoehe2/(maxg**factor_PI)) #60kg
    # perf_indexs2=(((hoehe2/1000)**factor_PI)*1000)/maxg
    mean_PI2 = np.mean(perf_indexs2)
    std_PI2=np.std(perf_indexs2)
    
'Berechnung PI'
if KugelArt == 20: 
    perf_indexs1=(((hoehe/1000)**factor_PI)*1000)/maxg #20kg

elif KugelArt == 60: 
    perf_indexs1=(hoehe/(maxg**factor_PI)) #60kg

mean_PI = np.mean(perf_indexs1)
std_PI=np.std(perf_indexs1)

if mean_PI > 95:
    color='#D70040'
    wertung='High Performance'
else:
    color='#2E8B57'
    wertung='Park Trampoline'

'Pop-Up Performance Index'
root3 = tk.Tk()
root3.configure(background=Color_grey)
root3.title('Auswertung '+ name) 
tk.Label(root3, text='Result', foreground=color, highlightbackground=color_orange, width=w3, background = Color_grey, font=(customFont1, fs2+10,'underline' ), anchor=tk.CENTER).grid(column=0, row=0, padx=4, pady=8, columnspan=2)
tk.Label(root3, text='Used measurements', highlightthickness=4, foreground=color_orange, highlightbackground=color_orange, width=w3, background = Color_grey, font=(customFont1, fs2 ), anchor=tk.CENTER).grid(column=0, row=1, padx=4, pady=8)
tk.Label(root3, text=len(loc_new) , highlightthickness=4,foreground=color_orange, highlightbackground=color_orange, width=w2, background = Color_grey, font=(customFont1, fs2), anchor=tk.CENTER).grid(column=1, row=1, padx=4, pady=8)
tk.Label(root3, text='AVG Rebound [mm]', highlightthickness=4,foreground=color_orange, highlightbackground=color_orange, width=w3, background = Color_grey, font=(customFont1, fs2), anchor=tk.CENTER).grid(column=0, row=2, padx=4, pady=8)
tk.Label(root3, text=round(mean_height,2), highlightthickness=4,foreground=color_orange, highlightbackground=color_orange, width=w2, background = Color_grey, font=(customFont1, fs2), anchor=tk.CENTER).grid(column=1, row=2, padx=4, pady=8)
tk.Label(root3, text='Median acceleration [g]', highlightthickness=4,foreground=color_orange, highlightbackground=color_orange,  width=w3, background = Color_grey, font=(customFont1, fs2), anchor=tk.CENTER).grid(column=0, row=3, padx=4, pady=8)
tk.Label(root3, text=round(mean_max_g,2), highlightthickness=4,foreground=color_orange, highlightbackground=color_orange, width=w2, background = Color_grey, font=(customFont1, fs2), anchor=tk.CENTER).grid(column=1, row=3, padx=4, pady=8)
tk.Label(root3, text='AVG Perfomance Index', highlightthickness=4,foreground=color_orange, highlightbackground=color_orange, width=w3, background = Color_grey, font=(customFont1, fs2), anchor=tk.CENTER).grid(column=0, row=4, padx=4, pady=8)
tk.Label(root3, text=round(mean_PI,2) ,highlightthickness=4,foreground=color_orange, highlightbackground=color_orange, width=w2, background = Color_grey, font=(customFont1, fs2), anchor=tk.CENTER).grid(column=1, row=4, padx=4, pady=8)
if rebound_set == 'manual':
    tk.Label(root3, text='Rebound height (Laser): ', highlightthickness=4,foreground=color_orange, highlightbackground=color_orange, width=w3, background = Color_grey, font=(customFont1, fs2), anchor=tk.CENTER).grid(column=0, row=5, padx=4, pady=8)
    tk.Label(root3, text=rebound_height ,highlightthickness=4,foreground=color_orange, highlightbackground=color_orange, width=w2, background = Color_grey, font=(customFont1, fs2), anchor=tk.CENTER).grid(column=1, row=5, padx=4, pady=8)

# img_ET=Image.open(image_path)
# img_ET1=img_ET.resize((236, 60))
# my_img1=ImageTk.PhotoImage(img_ET1)
# tk.Label(root3, image = my_img1,background = ET_Blau_Hell).grid(column = 3, row=0, rowspan=2, padx=4, pady=8) 
tk.Label(root3, text=' Rating: ' + wertung , background = Color_grey, highlightthickness=4, highlightbackground= color, foreground=color, font=(customFont1, fs2+10), anchor=tk.CENTER).grid(column=0, row=6, columnspan=2, padx=4, pady=8)
button3=tk.Button(root3, text= 'Save and Exit', bg=color, fg = 'black', width=16, font=(customFont1, fs+2), command=lambda:root3.destroy(), anchor=tk.CENTER)#color_green
button3.grid(column=0, row=7,columnspan=2, padx=4, pady=8)

root3.mainloop()

# os.remove(save_path +'/'+ name + '2.png')

'Tabelle erzeugen und speichern'
if rebound_set == 'manual':
    if checkMoreData == 'Yes':
        ergebnistab_gesamt = pd.DataFrame({'Measurement': measurements, 'Fallhöhe (mm)':fallhoehe, 'Fallgeschwindigkeit (m/s)':fallgeschwindigkeit,'Eindringtiefe (mm)':eindringtiefe, 'Rebound Height (mm)': hoehe, 'Max Acceleration (g)': maxg  ,'Performance Index1' : perf_indexs1,'Performance Index2 (Laser)' : perf_indexs2})
        ergebnistab_mean=pd.DataFrame({'Measurement':'AVG', 'Rebound Height (mm)': mean_height, 'Max Acceleration (g)': mean_max_g  ,'Performance Index1' : mean_PI, 'Performance Index2 (Laser)' : mean_PI2}, index=range(1))
        ergebnistab_std= pd.DataFrame({'Measurement':'STD','Rebound Height (mm)': std_height, 'Max Acceleration (g)': std_max_g  ,'Performance Index1' : std_PI,'Performance Index2 (Laser)' : std_PI2}, index=range(1))
        ergebnistab_rebound = pd.DataFrame({'Measurement':'Reboundhoehe (Laser)','Rebound Height (mm)': rebound_height}, index=range(1))
        ergebnistab_gesamt= pd.concat([ergebnistab_gesamt, ergebnistab_mean, ergebnistab_std, ergebnistab_rebound])
    else:
        ergebnistab_gesamt = pd.DataFrame({'Measurement': measurements, 'Rebound Height (mm)': hoehe, 'Max Acceleration (g)': maxg  ,'Performance Index1' : perf_indexs1,'Performance Index2 (Laser)' : perf_indexs2})
        ergebnistab_mean=pd.DataFrame({'Measurement':'AVG', 'Rebound Height (mm)': mean_height, 'Max Acceleration (g)': mean_max_g  ,'Performance Index1' : mean_PI, 'Performance Index2 (Laser)' : mean_PI2}, index=range(1))
        ergebnistab_std= pd.DataFrame({'Measurement':'STD','Rebound Height (mm)': std_height, 'Max Acceleration (g)': std_max_g  ,'Performance Index1' : std_PI,'Performance Index2 (Laser)' : std_PI2}, index=range(1))
        ergebnistab_rebound = pd.DataFrame({'Measurement':'Reboundhoehe (Laser)','Rebound Height (mm)': rebound_height}, index=range(1))
        ergebnistab_gesamt= pd.concat([ergebnistab_gesamt, ergebnistab_mean, ergebnistab_std, ergebnistab_rebound]) 
else:
    if checkMoreData == 'Yes':
        ergebnistab_gesamt = pd.DataFrame({'Measurement': measurements, 'Fallhöhe (mm)':fallhoehe, 'Fallgeschwindigkeit (m/s)':fallgeschwindigkeit,'Eindringtiefe (mm)':eindringtiefe, 'Rebound Height (mm)': hoehe, 'Max Acceleration (g)': maxg  ,'Performance Index' : perf_indexs1})    
        ergebnistab_mean=pd.DataFrame({'Measurement':'AVG', 'Rebound Height (mm)': mean_height, 'Max Acceleration (g)': mean_max_g  ,'Performance Index' : mean_PI}, index=range(1))
        ergebnistab_std= pd.DataFrame({'Measurement':'STD','Rebound Height (mm)': std_height, 'Max Acceleration (g)': std_max_g  ,'Performance Index' : std_PI}, index=range(1))
        ergebnistab_gesamt= pd.concat([ergebnistab_gesamt, ergebnistab_mean, ergebnistab_std])
    else:
        ergebnistab_gesamt = pd.DataFrame({'Measurement': measurements, 'Rebound Height (mm)': hoehe, 'Max Acceleration (g)': maxg  ,'Performance Index' : perf_indexs1})    
        ergebnistab_mean=pd.DataFrame({'Measurement':'AVG', 'Rebound Height (mm)': mean_height, 'Max Acceleration (g)': mean_max_g  ,'Performance Index' : mean_PI}, index=range(1))
        ergebnistab_std= pd.DataFrame({'Measurement':'STD','Rebound Height (mm)': std_height, 'Max Acceleration (g)': std_max_g  ,'Performance Index' : std_PI}, index=range(1))
        ergebnistab_gesamt= pd.concat([ergebnistab_gesamt, ergebnistab_mean, ergebnistab_std])
ergebnistab_gesamt.to_excel(save_path +'/'+ name +'.xlsx', index=False)
os.startfile(save_path +'/'+ name +'.xlsx')
# if (checkMSG == 'Yes'):
#     input('press any key...') 
sys.exit('Program succesfully finished.')

'''THE END'''
# if sensorType=='Yost':
    
#     data = np.loadtxt(file, delimiter=",")
#     if min(data[:,6])<0:
#         sensorcheck=input('are you sure that this is a yostlabs textfile? y/n \n')
#         if sensorcheck!='y':
#             sensorType='Endaq'
#             df=pd.read_csv(file, sep=',', header=0, names=['Time','X', 'Y','Z'])
#             time1 = np.array(df.Time)
#             namerange=19
#             distanceSingleMeasurementsPeaks=10000
#             # res=[]
#             # res1.append(np.sqrt(np.square(df.X)+np.square(df.Y)+np.square(df.Z))) 
#             res=np.array(np.sqrt(np.square(df.X)+np.square(df.Y)+np.square(df.Z)))
#         else:
#             if checkFindPeaks !='Yes':
#                 height_peaks=4 
#                 distance_peaks=80
#                 width_peaks=10
#                 grenze = -0.6
#                 inwards=1
            
#             x = np.array(data[:, 0])
#             y = np.array(data[:, 1])
#             z = np.array(data[:, 2])
#             xRaw = np.array(data[:, 3])
#             yRaw = np.array(data[:, 4])
#             zRaw = np.array(data[:, 5])
#             zeit = np.array(data[:, -1]) #letzte Spalte = Zeit
#             factor_us=1.6666666666667 * 10**-8 #Microsekunden
#             time1=(zeit*factor_us)*60
#             res = np.empty(len(x))
            
#             for i in range(0, len(x)):
#                 res[i] = math.sqrt(x[i]**2+y[i]**2+z[i]**2)
#             namerange=26
#             distanceSingleMeasurementsPeaks=1200
#     else:
#         if checkFindPeaks !='Yes':
#             height_peaks=4 
#             distance_peaks=80
#             width_peaks=10
#             grenze = -0.6
#             inwards=1
        
#         x = np.array(data[:, 0])
#         y = np.array(data[:, 1])
#         z = np.array(data[:, 2])
#         xRaw = np.array(data[:, 3])
#         yRaw = np.array(data[:, 4])
#         zRaw = np.array(data[:, 5])
#         zeit = np.array(data[:, -1]) #letzte Spalte = Zeit
#         factor_us=1.6666666666667 * 10**-8 #Microsekunden
#         time1=(zeit*factor_us)*60
#         res = np.empty(len(x))
        
#         for i in range(0, len(x)):
#             res[i] = math.sqrt(x[i]**2+y[i]**2+z[i]**2)
#         namerange=26
#         distanceSingleMeasurementsPeaks=1200
    
# elif sensorType=='Endaq':
#     df=pd.read_csv(file, sep=',', header=0, names=['Time','X', 'Y','Z'])
#     time1 = np.array(df.Time)
#     namerange=19
#     distanceSingleMeasurementsPeaks=10000
#     # res=[]
#     # res1.append(np.sqrt(np.square(df.X)+np.square(df.Y)+np.square(df.Z))) 
#     res=np.array(np.sqrt(np.square(df.X)+np.square(df.Y)+np.square(df.Z)))
