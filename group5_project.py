import tkinter as tk

window = tk.Tk()
window.title("Group 5's Interview Outfit Helper")
window.geometry("900x800")
window.configure(bg="cyan")
job_types = ['Tech','Business','Trade','Retail','Creative']
interview_types = ['In-Person','Video','Over Phone']
budget_ranges = [range(0),range(1-50),range(51-150),range(151-200)]
shirt_suggestions = ['Solid shirt', 'Button-up shirt', 'Clean, collared shirt', 'Plain long sleeved',
                     'Polo shirt', 'Light sweater', 'Layered top: Jacket/Cardigan with a solid shirt']
pants_suggestions = ['Clean jeans (no rips)', 'Solid work pants', 'Chinos', 'Dress slacks', 'Knee-length Skirt']
shoes_suggestions = ['Clean sneakers', 'Work boots', 'Casual dress shoes', 'Formal dress shoes']

def on_button_click():

    popup = tk.Toplevel()
    popup.title("Outfit Results")

    label = tk.Label(popup, text="Here's what we suggest based on your selection.")
    label.pack(pady=10)

    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=5)

btn = tk.Button(window, text="Enter", command=on_button_click)
btn.grid(row=0, column=3, padx=5, pady=10)

'''
img = tk.PhotoImage(file="./images/group5.png")
label_img = tk.Label(window, image=img)
label_img.grid()

def open_link(event):
    import webbrowser
    webbrowser.open(")
link = tk.Label(window, text="Visit Pokemon.com", fg="blue", cursor="hand1")
link.grid()
link.bind("<Button-1>", open_link)
'''

heading1 = tk.Label(window, text='Choose a job type:', font=("Arial", 14))
heading1.grid(row=3, column=1, padx=5, pady=20, columnspan=5)

window.columnconfigure(0, weight=1)
window.columnconfigure(6, weight=1)

def checkbox1_function():
    if chk_state1.get() == 1:
        chk_state2.set(0)
        chk_state3.set(0)
        chk_state4.set(0)
        chk_state5.set(0)

chk_state1 = tk.BooleanVar()
checkbox1 = tk.Checkbutton(window, text="Tech", var=chk_state1, command=checkbox1_function)
checkbox1.grid(row=5, column=1, padx=5, pady=5)

def checkbox2_function():
    if chk_state2.get() == 1:
        chk_state1.set(0)
        chk_state3.set(0)
        chk_state4.set(0)
        chk_state5.set(0)

chk_state2 = tk.BooleanVar()
checkbox2 = tk.Checkbutton(window, text="Business", var=chk_state2, command=checkbox2_function)
checkbox2.grid(row=5, column=2, padx=5, pady=5)

def checkbox3_function():
    if chk_state3.get() == 1:
        chk_state1.set(0)
        chk_state2.set(0)
        chk_state4.set(0)
        chk_state5.set(0)

chk_state3 = tk.BooleanVar()
checkbox3 = tk.Checkbutton(window, text="Trade", var=chk_state3, command=checkbox3_function)
checkbox3.grid(row=5, column=3, padx=5, pady=5)

def checkbox4_function():
    if chk_state4.get() == 1:
        chk_state1.set(0)
        chk_state2.set(0)
        chk_state3.set(0)
        chk_state5.set(0)

chk_state4 = tk.BooleanVar()
checkbox4 = tk.Checkbutton(window, text="Retail", var=chk_state4, command=checkbox4_function)
checkbox4.grid(row=5, column=4, padx=5, pady=5)

def checkbox5_function():
    if chk_state5.get() == 1:
        chk_state1.set(0)
        chk_state2.set(0)
        chk_state3.set(0)
        chk_state4.set(0)

chk_state5 = tk.BooleanVar()
checkbox5 = tk.Checkbutton(window, text="Creative", var=chk_state5, command=checkbox5_function)
checkbox5.grid(row=5, column=5, padx=5, pady=5)


heading2 = tk.Label(window, text='Choose an interview type:', font=("Arial", 14))
heading2.grid(row=7, column=1, padx=5, pady=20, columnspan=5)

def checkbox6_function():
    if chk_state6.get() == 1:
        chk_state7.set(0)
        chk_state8.set(0)

chk_state6 = tk.BooleanVar()
checkbox6 = tk.Checkbutton(window, text="In-Person", var=chk_state6, command=checkbox6_function)
checkbox6.grid(row=9, column=2, padx=5, pady=5)

def checkbox7_function():
    if chk_state7.get() == 1:
        chk_state6.set(0)
        chk_state8.set(0)

chk_state7 = tk.BooleanVar()
checkbox7 = tk.Checkbutton(window, text="Video", var=chk_state7, command=checkbox7_function)
checkbox7.grid(row=9, column=3, padx=5, pady=5)

def checkbox8_function():
    if chk_state8.get() == 1:
        chk_state6.set(0)
        chk_state7.set(0)

chk_state8 = tk.BooleanVar()
checkbox8 = tk.Checkbutton(window, text="Over Phone", var=chk_state8, command=checkbox8_function)
checkbox8.grid(row=9, column=4, padx=5, pady=5)

heading3 = tk.Label(window, text='Enter your budget below:', font=("Arial", 14))
heading3.grid(row=11, column=1, padx=5, pady=15, columnspan=5)

entry = tk.Entry(window, borderwidth=3, font=("Arial", 12))
entry.grid(row=13, column=1, padx=5, pady=15, columnspan=5)

heading4 = tk.Label(window, text='Do you have any religious clothing restrictions?', font=("Arial", 14))
heading4.grid(row=15, column=1, padx=5, pady=20, columnspan=5)

def checkbox9_function():
    if chk_state9.get() == 1:
        chk_state10.set(0)

chk_state9 = tk.BooleanVar()
checkbox9 = tk.Checkbutton(window, text="Yes", var=chk_state9, command=checkbox7_function)
checkbox9.grid(row=17, column=2, padx=5, pady=5)

def checkbox10_function():
    if chk_state10.get() == 1:
        chk_state9.set(0)

chk_state10 = tk.BooleanVar()
checkbox10 = tk.Checkbutton(window, text="No", var=chk_state10, command=checkbox8_function)
checkbox10.grid(row=17, column=4, padx=5, pady=5)

heading5 = tk.Label(window, text='If yes, what are they?', font=("Arial", 12))
heading5.grid(row=18, column=1, padx=5, pady=15, columnspan=5)

entry = tk.Entry(window, borderwidth=3, font=("Arial", 12))
entry.grid(row=20, column=1, padx=5, pady=15, columnspan=5)

if job_types == ['0']:
    if interview_types == ['0']:
        if budget_ranges in range (0):

        elif budget_ranges in range (1-50):

        elif budget_ranges in range (51-150):

        elif budget_ranges in range (151-200):

    elif interview_types == ['1']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):

    elif interview_types == ['2']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):

if job_types == ['1']:
    if interview_types == ['0']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):

    elif interview_types == ['1']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):

    elif interview_types == ['2']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):
if job_types == ['2']:
    if interview_types == ['0']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):

    elif interview_types == ['1']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):

    elif interview_types == ['2']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):
if job_types == ['3']:
    if interview_types == ['0']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):

    elif interview_types == ['1']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):

    elif interview_types == ['2']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):
if job_types == ['4']:
    if interview_types == ['0']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):

    elif interview_types == ['1']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):

    elif interview_types == ['2']:
        if budget_ranges in range(0):

        elif budget_ranges in range(1 - 50):

        elif budget_ranges in range(51 - 150):

        elif budget_ranges in range(151 - 200):

window.mainloop()
