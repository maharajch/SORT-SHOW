#!/usr/bin/env python
# coding: utf-8

# In[29]:


from tkinter import *
from tkinter import ttk
import random
from bubble_sort import bubble

#initialising root
root = Tk()
root.title("Sorting Algorithms Visualizer")
root.maxsize(900,600)
root.config(bg="Black")

select_alg= StringVar()
data=[]

#Generating Bar function
def generate():
    
    global data
   
    minval = int(minEntry.get())
    maxval = int(maxEntry.get())
    sizeval = int(sizeEntry.get())
    
    
    #if minval < 0 : minval = 0
    #if maxval > 100 : maxval = 100
    #if sizeval > 60 or sizeval < 3 : sizeval = 30
    #if  minval > maxval : minval, maxval = maxval, minval
    
    
    data= []
    for _ in range(sizeval):
        data.append(random.randrange(minval,maxval+1))
    
    drawData(data, ['Red' for x in range(len(data))])
    

    
def drawData(data, colorlist):
    canvas.delete("all")
    can_height = 380
    can_width = 550
    x_width = can_width/(len(data) +1)
    offset = 30
    spacing = 10
    normalizedata = [i / max(data) for i in data]
    
    for i, height in enumerate(normalizedata):
        #top left corner
        x0 = i*x_width + offset + spacing
        y0 = can_height - height*340
        
        #bottom right corner
        x1 = ((i+1)*x_width) + offset
        y1 = can_height
        
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i])
        canvas.create_text(x0+2, y0, anchor=SE, text=str(data[i]))
    root.update_idletasks()
    
    
    
def start_algorithm():
    global data
    bubble(data, drawData, speedbar.get())
    
    
    
    
    
#Creating User interface frame and basic layout

UI_frame=Frame(root,width=600,height=200,bg="Grey")
UI_frame.grid(row=0,column=0,padx=10,pady=5)

canvas = Canvas(root, width=600, height=380)
canvas.grid(row=1, column=0, padx=10, pady=5)

#Creating user interface area

#row[0]

Label(UI_frame,text="ALGORITHM", bg='Grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algmenu= ttk.Combobox(UI_frame,textvariable=select_alg, values=["Bubble Sort","Quick Sort"])
algmenu.grid(row=0, column=1, padx=5, pady=5)
algmenu.current(0)

#Start Button
Button(UI_frame,text="START",bg="ORANGE", command=start_algorithm).grid(row=1, column=3, padx=5, pady=5)

#Speed Bar
speedbar= Scale(UI_frame, from_= 0.10, to= 2.0, length=100, digits=2, resolution=0.2, orient= HORIZONTAL, label="Select Speed")
speedbar.grid(row=0, column=2, padx=5, pady=5)



#row[1]


sizeEntry= Scale(UI_frame, from_=3, to=60, resolution=1, orient=HORIZONTAL, label="Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)


minEntry= Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Minimun Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)


maxEntry= Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Maximun Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)


#generate button
Button(UI_frame,text="Generate",bg="Red", command=generate).grid(row=0, column=3, padx=5, pady=5)

root.mainloop()


# In[ ]:





# In[ ]:




