from googletrans import Translator
from gtts import gTTS
from tkinter import *

try:
    
    root=Tk()
    root.title('Translator')
    root.geometry('600x280')
    root.config(bg='black')
    my_bg=PhotoImage(file="bg.png")
    label_1=Label(root,image=my_bg)
    label_1.place(x=13,y=10)


    e1=Entry(root,bg='white',fg='black',font=('Arial',23,'bold'))
    e1.place(x=17,y=20)

    def convert_language():
        a1=e1.get()
        t1= Translator()
        t2=click_option.get()
        global wr
        wr=str(a1)

        if t2=="English":
            convert="en"
        elif t2=='German':
            convert='de'
        elif t2=='French':
            convert='fr'
        elif t2=='Spanish':
            convert='es'
      
        trans_text=t1.translate(a1,dest=convert)
        trans_text=trans_text.text
        ob1= gTTS(text=trans_text ,slow=False ,lang=convert)
        label_2.config(text=trans_text)
        global lb
        lb=str(trans_text)

        file=open('translator.txt','a')
        file.write('user serached for: ')
        file.write(wr)
        file.write('\n')
        file.write('translated text of your desired language is:')
        file.write(lb)
        file.write('\n')
        file.close()

    
    choices=['English','German','French','Spanish']

    click_option=StringVar()
    click_option.set('Select language')


    list_drop=OptionMenu(root,click_option,*choices)
    list_drop.configure(background='black',foreground='white',font=('Arial',15,'bold'))
    list_drop.place(x=370,y=20)


    label_2=Label(root,text='\t\t\t\t\t\t',bg='black',fg='red',font=('Arial',40,'bold'))
    label_2.place(x=0,y=120)
    label_2=Label(root,text='Translated Text',bg='black',fg='white',font=('Arial',26,'bold'))    
    label_2.place(x=180,y=120)


    Button_1=Button(root,text='Translate',bg='#1b03a3',fg='white',font=('Arial',25,'bold'),command=convert_language)
    Button_1.place(x=220,y=200)

    
except NameError:
    print('Name error occured')
except IndexError:
    print('Index error occured') 
except IOError:
    print('Index error occured')
except SyntaxError:
    print('Index error occured')
except ValueError:
    print('Value error occured')
except AssertionError:
    print('Assertion error occured')    
except :
    print('Something went wrong please enter the correct value')
    

root.mainloop()

