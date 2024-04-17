import tkinter

def click_button():
    weight = float(entry.get())
    height = float(entry2.get()) / 100

    if weight == "" or height == "":
        print("Please entry weight and height!")
    else:
        bmi = weight / (height * height)
        print("Your BMI is :", bmi)

        if bmi < 18.5:
            print("You are weak!")
        elif bmi >= 18.5 and bmi < 25:
            print("You are normal!")
        elif bmi >= 25 and bmi < 30:
            print("You are fat!")
        elif bmi >= 30:
            print("You are obese!")
        else:
            print("Wrong Entry. Please check you wrote!")



window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=250,height=200)
window.config(padx=30,pady=30)

label = tkinter.Label(text="Enter your weight(kg)")
label.pack()

entry = tkinter.Entry(width=10)
entry.pack()

label2 = tkinter.Label(text="Enter your height(cm)")
label2.pack()

entry2 = tkinter.Entry(width=10)
entry2.pack()


button = tkinter.Button(text="Calculate",command=click_button)
button.pack()


window.mainloop()