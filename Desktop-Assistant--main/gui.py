from tkinter import*
from PIL import Image , ImageTk
import action 
import spech_to_text 


def User_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> "+send+"\n")
    if bot != None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
          root.destroy()  
          

def ask():

    ask_val= spech_to_text.spech_to_text()
    bot_val = action.Action(ask_val)
    text.insert(END, "Me --> "+ask_val+"\n") 
    if bot_val != None:
       text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()

def delete_text():
    text.delete("1.0", "end")


root = Tk()
root.geometry("750x785")
root.title("Desktop Assistant")
root.resizable(False,False)
root.config(bg="light yellow")

  


# Main Frame
Main_frame = LabelFrame(root , padx=100 ,  pady=7 , borderwidth=3 ,  relief="raised")
Main_frame.config(bg="yellow")
Main_frame.grid(row = 0 ,  column= 1 ,  padx= 75 ,  pady =  10)

# Text Lable 
Text_lable = Label(Main_frame, text = "Desktop AI Assistant" , font=("comic Sans ms" ,  14 , "bold" ))
Text_lable.grid(row=0 ,  column=0 , padx=20 , pady= 10)


# Image 
Display_Image = ImageTk.PhotoImage(Image.open("C:\\Users\\gkroh\\OneDrive\\Desktop\\My works\\Desktop-Assistant--main\\image\\assitant.png"))


image_label = Label(Main_frame, image= Display_Image, height= 300, width=400)
image_label.grid(row=1, column= 0, pady=20)



# Add a text space

text = Text(root, font=('courier 13 bold'), bg='#356695')
text.grid(row=2, column=0 )
text.place(x=90, y=435, width=580, height=100)




# Add a entry space
entry1 = Entry(root, justify = CENTER)
entry1.place(x=150 , y = 570 , width= 450, height= 40)



# Add a text button1
button1 =  Button(root,  text="ASK" , bg="red" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=ask)
button1.place(x= 70, y= 650)

# Add a text button2
button2 =  Button(root,  text="Send" , bg="red" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=User_send)
button2.place(x= 300, y= 650)

# Add a text button3
button3 = Button(root, text="Delete", bg="red" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=delete_text)
button3.place(x= 500, y= 650)

root.mainloop()