import tkinter as tk

window = tk.Tk()
window.title("Group 5's Interview Outfit Helper")
window.geometry("900x800")
window.configure(bg="gray")
job_types = ['Tech','Business','Trade','Retail','Creative']
interview_types = ['In-Person','Video','Over Phone']
budget_ranges = ['0', '1-50','51-150','151-200', '201-300']
shirt_suggestions = ['Solid shirt', 'Button-up shirt', 'Clean, collared shirt', 'Plain long sleeved',
                     'Polo shirt', 'Light sweater', 'Layered top: Jacket/Cardigan with a solid shirt']
pants_suggestions = ['Clean jeans (no rips)', 'Solid work pants', 'Chinos', 'Casual slacks', 'Dress slacks']
shoes_suggestions = ['Clean sneakers', 'Sturdy Boots or Shoes', 'Casual dress shoes', 'Formal dress shoes']

clothing_restrictions = ['Religious Exemption', 'Disability', 'Fabric Sensory']
religious_exemptions = ['Turban', 'Hijab', 'Yarmulke']
disability_restrictions = ['Wheelchair', 'Amputee', 'Mental/Learning', 'Overweight', 'Surgery Related Bodily Changes']
fabric_alternatives = ['Cotton', 'Bamboo', 'Modal', 'Lycra', 'Viscose or Rayon', 'Soft wool Alt.']

def on_button_click():
    suggestion = get_recommendation()
    alternate_suggestion = get_alternatives()

    popup = tk.Toplevel()
    popup.title("Outfit Results")

    label = tk.Label(popup, text="Here's what I suggest based on your selection: ")
    label.pack(pady=10)

    label1 = tk.Label(popup, text=suggestion)
    label1.pack(pady=10)

    label2 = tk.Label(popup, text=alternate_suggestion)
    label2.pack(pady=10)

    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=5)

btn = tk.Button(window, text="Enter", command=on_button_click)
btn.grid(row=0, column=3, padx=10, pady=15)

heading1 = tk.Label(window, text='Choose a job type:', font=("Arial", 14))
heading1.grid(row=3, column=1, padx=10, pady=10, columnspan=5)

jobChoice = tk.StringVar(value="NotSelected")

index1 = 1
for jobtype in job_types:
    rb = tk.Radiobutton(window, text=jobtype, variable=jobChoice, value=jobtype)
    rb.grid(row=4, column=index1, padx=10, pady=5)
    index1 = index1 + 1

window.columnconfigure(0, weight=1)
window.columnconfigure(6, weight=1)

heading2 = tk.Label(window, text='Choose an interview type:', font=("Arial", 14))
heading2.grid(row=7, column=1, padx=5, pady=20, columnspan=5)

interviewChoice = tk.StringVar(value="NotSelected")

index2 = 2
for interviewtype in interview_types:
    rb = tk.Radiobutton(window, text=interviewtype, variable=interviewChoice, value=interviewtype)
    rb.grid(row=8, column=index2, padx=10, pady=5)
    index2 = index2 + 1

heading3 = tk.Label(window, text='Enter your budget below:', font=("Arial", 14))
heading3.grid(row=11, column=1, padx=5, pady=15, columnspan=5)

budgetChoice = tk.StringVar(value="NotSelected")

index3 = 1
for budget in budget_ranges:
    rb = tk.Radiobutton(window, text=budget, variable=budgetChoice, value=budget)
    rb.grid(row=12, column=index3, padx=10, pady=5)
    index3 = index3 + 1

heading4 = tk.Label(window, text="Do you have any clothing restrictions or disabilities?", font=("Arial", 14))
heading4.grid(row=14, column=1, padx=5, pady=15, columnspan=5)

alternateChoice = tk.StringVar(value="NotSelected")

index4 = 2
for alternatives in clothing_restrictions:
    rb = tk.Radiobutton(window, text=alternatives, variable=alternateChoice, value=alternatives)
    rb.grid(row=15, column=index4, padx=10, pady=5)
    index4 = index4 + 1



def get_recommendation():
    suggestion = "Nothing was entered, please make a selection."

    if jobChoice.get() == job_types[0]:  # Tech
        if interviewChoice.get() == interview_types[0]:  # In Person
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = "Since your budget is 0; use the cleanest, nicest thing in your closet."
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[4] + ", " + pants_suggestions[0] +
                              ", and either " + shoes_suggestions[0] + " or " + shoes_suggestions[2])
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[4] + " or " + shirt_suggestions[5] + ", either "
                              + pants_suggestions[0] + " or " + pants_suggestions[2] + ", and either " + shoes_suggestions[0] + " or " + shoes_suggestions[2])
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = "I recommend that you wear: " + shirt_suggestions[5] + ", " + pants_suggestions[2] + ", and " + shoes_suggestions[2]
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = "I recommend that you wear: " + shirt_suggestions[5] + ", " + pants_suggestions[2] + ", and " + shoes_suggestions[2]

        elif interviewChoice.get() == interview_types[1]:  # Via Zoom
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = "Since your budget is 0; use the cleanest, nicest thing in your closet."
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[4] + ", " + pants_suggestions[0] +
                              ", and either " + shoes_suggestions[0] + " or " + shoes_suggestions[2])
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[4] + " or " + shirt_suggestions[5] + ", either "
                              + pants_suggestions[0] + " or " + pants_suggestions[2] + ", and either " + shoes_suggestions[0] + " or " + shoes_suggestions[2])
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = "I recommend that you wear: either a " + shirt_suggestions[4] + " or " + shirt_suggestions[5] + ", " + pants_suggestions[2] + ", and " + shoes_suggestions[2]
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = "I recommend that you wear: either a " + shirt_suggestions[4] + " or " + shirt_suggestions[5] + ", " + pants_suggestions[2] + ", and " + shoes_suggestions[2]

        elif interviewChoice.get() == interview_types[2]:  # Over the Phone
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = ("Since your budget is 0; use the cleanest, nicest thing in your closet. "
                              "They may not see you, but being nicely dressed can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[4] + ", " + pants_suggestions[0] +
                              ", and either " + shoes_suggestions[0] + " or " + shoes_suggestions[2] +
                              ". They may not see you, but being nicely dressed can help boost confidence")
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[4] + " or " + shirt_suggestions[5] + ", either "
                              + pants_suggestions[0] + " or " + pants_suggestions[2] + ", and either " + shoes_suggestions[0] + " or " + shoes_suggestions[2])
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear: " + shirt_suggestions[5] + ", " + pants_suggestions[2] + ", and " + shoes_suggestions[2] +
                              ". They may not see you, but being nicely dressed can help boost confidence")
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear: " + shirt_suggestions[5] + ", " + pants_suggestions[2] + ", and " + shoes_suggestions[2] +
                              ". They may not see you, but being nicely dressed can help boost confidence")

    elif jobChoice.get() == job_types[1]:  # Business
        if interviewChoice.get() == interview_types[0]:  # In Person
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = "Since your budget is 0; use the cleanest, nicest thing in your closet."
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[1] + ", " + pants_suggestions[3] +
                              ", and " + shoes_suggestions[3])
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[1] + ", " + pants_suggestions[3] +
                              ", and " + shoes_suggestions[3])
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[1] + ", " + pants_suggestions[3] +
                              ", and " + shoes_suggestions[3])
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[1] + ", " + pants_suggestions[3] +
                              ", and " + shoes_suggestions[3])

        elif interviewChoice.get() == interview_types[1]:  # Via Zoom
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = "Since your budget is 0; use the cleanest, nicest thing in your closet."
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[1] + ", " + pants_suggestions[3] +
                              ", and " + shoes_suggestions[3])
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[1] + ", " + pants_suggestions[3] +
                              ", and " + shoes_suggestions[3])
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[1] + ", " + pants_suggestions[3] +
                              ", and " + shoes_suggestions[3])
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[1] + ", " + pants_suggestions[3] +
                              ", and " + shoes_suggestions[3])

        elif interviewChoice.get() == interview_types[2]:  # Over the Phone
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = ("Since your budget is 0; use the cleanest, nicest thing in your closet. "
                              "They may not see you, but dressing nicely can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[1] + ", " + pants_suggestions[3] +
                              ", and " + shoes_suggestions[3] + ". They may not see you, but dressing nicely can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[1] + ", " + pants_suggestions[3] +
                              ", and " + shoes_suggestions[3] + ". They may not see you, but dressing nicely can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[1] + ", " + pants_suggestions[3] +
                              ", and " + shoes_suggestions[3] + ". They may not see you, but dressing nicely can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[1] + ", " + pants_suggestions[3] +
                              ", and " + shoes_suggestions[3] + ". They may not see you, but dressing nicely can help boost confidence.")

    elif jobChoice.get() == job_types[2]:  # Trade
        if interviewChoice.get() == interview_types[0]:  # In Person
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = "Since your budget is 0; use the cleanest, nicest thing in your closet."
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[2] + " or " + shirt_suggestions[3]
                              + ", " + pants_suggestions[0] + " or " + pants_suggestions[1] + ", and " + shoes_suggestions[1])
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[2] + " or " + shirt_suggestions[3]
                              + ", " + pants_suggestions[0] + " or " + pants_suggestions[1] + ", and " + shoes_suggestions[1])
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[2] + " or " + shirt_suggestions[3]
                              + ", " + pants_suggestions[0] + " or " + pants_suggestions[1] + ", and " + shoes_suggestions[1])
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[2] + " or " + shirt_suggestions[3]
                              + ", " + pants_suggestions[0] + " or " + pants_suggestions[1] + ", and " + shoes_suggestions[1])

        elif interviewChoice.get() == interview_types[1]:  # Via Zoom
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = "Since your budget is 0; use the cleanest, nicest thing in your closet."
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[2] + " or " + shirt_suggestions[3]
                              + ", " + pants_suggestions[0] + " or " + pants_suggestions[1] + ", and " + shoes_suggestions[1])
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[2] + " or " + shirt_suggestions[3]
                              + ", " + pants_suggestions[0] + " or " + pants_suggestions[1] + ", and " + shoes_suggestions[1])
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[2] + " or " + shirt_suggestions[3]
                              + ", " + pants_suggestions[0] + " or " + pants_suggestions[1] + ", and " + shoes_suggestions[1])
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[2] + " or " + shirt_suggestions[3]
                              + ", " + pants_suggestions[0] + " or " + pants_suggestions[1] + ", and " + shoes_suggestions[1])

        elif interviewChoice.get() == interview_types[2]:  # Over the Phone
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = ("Since your budget is 0; use the cleanest, nicest thing in your closet. "
                              "They may not see you, but dressing nicely can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[2] + " or " + shirt_suggestions[3]
                              + ", " + pants_suggestions[0] + " or " + pants_suggestions[1] + ", and " + shoes_suggestions[1]
                              + "They may not see you, but dressing nicely can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[2] + " or " + shirt_suggestions[3]
                              + ", " + pants_suggestions[0] + " or " + pants_suggestions[1] + ", and " + shoes_suggestions[1]
                              + "They may not see you, but dressing nicely can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[2] + " or " + shirt_suggestions[3]
                              + ", " + pants_suggestions[0] + " or " + pants_suggestions[1] + ", and " + shoes_suggestions[1]
                              + "They may not see you, but dressing nicely can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear: either a " + shirt_suggestions[2] + " or " + shirt_suggestions[3]
                              + ", " + pants_suggestions[0] + " or " + pants_suggestions[1] + ", and " + shoes_suggestions[1]
                              + "They may not see you, but dressing nicely can help boost confidence.")

    elif jobChoice.get() == job_types[3]:  # Retail
        if interviewChoice.get() == interview_types[0]:  # In Person
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = "Since your budget is 0; use the cleanest, nicest thing in your closet."
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear a: " + shirt_suggestions[0] + ", " + pants_suggestions[0]
                              + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear a: " + shirt_suggestions[1] + ", " + pants_suggestions[0]
                              + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear a: " + shirt_suggestions[2] + ", " + pants_suggestions[0]
                              + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear a: " + shirt_suggestions[2] + ", " + pants_suggestions[0]
                              + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])

        elif interviewChoice.get() == interview_types[1]:  # Via Zoom
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = "Since your budget is 0; use the cleanest, nicest thing in your closet."
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear a: " + shirt_suggestions[0] + ", " + pants_suggestions[0]
                              + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear a: " + shirt_suggestions[1] + ", " + pants_suggestions[0]
                              + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear a: " + shirt_suggestions[2] + ", " + pants_suggestions[0]
                              + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear a: " + shirt_suggestions[2] + ", " + pants_suggestions[0]
                              + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])

        elif interviewChoice.get() == interview_types[2]:  # Over the Phone
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = ("Since your budget is 0; use the cleanest, nicest thing in your closet. "
                              "They may not see you, but dressing nicely can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear a: " + shirt_suggestions[0] + ", " + pants_suggestions[0]
                              + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0] +
                              "They may not see you, but dressing nicely can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear a: " + shirt_suggestions[1] + ", " + pants_suggestions[0]
                              + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0] +
                              "They may not see you, but dressing nicely can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear a: " + shirt_suggestions[2] + ", " + pants_suggestions[0]
                              + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0] +
                              "They may not see you, but dressing nicely can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear a: " + shirt_suggestions[2] + ", " + pants_suggestions[0]
                              + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0] +
                              "They may not see you, but dressing nicely can help boost confidence.")

    elif jobChoice.get() == job_types[4]:  # Creative
        if interviewChoice.get() == interview_types[0]:  # In Person
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = "Since your budget is 0; use the cleanest, nicest thing in your closet."
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear: either a" + shirt_suggestions[4] + " or " + shirt_suggestions[6]
                              + ", either " + pants_suggestions[0] + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear: either a" + shirt_suggestions[4] + " or " + shirt_suggestions[6]
                              + ", either " + pants_suggestions[0] + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear: either a" + shirt_suggestions[4] + " or " + shirt_suggestions[6]
                              + ", either " + pants_suggestions[0] + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear: either a" + shirt_suggestions[4] + " or " + shirt_suggestions[6]
                              + ", either " + pants_suggestions[0] + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])

        elif interviewChoice.get() == interview_types[1]:  # Via Zoom
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = "Since your budget is 0; use the cleanest, nicest thing in your closet."
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear: either a" + shirt_suggestions[4] + " or " + shirt_suggestions[6]
                              + ", either " + pants_suggestions[0] + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear: either a" + shirt_suggestions[4] + " or " + shirt_suggestions[6]
                              + ", either " + pants_suggestions[0] + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear: either a" + shirt_suggestions[4] + " or " + shirt_suggestions[6]
                              + ", either " + pants_suggestions[0] + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear: either a" + shirt_suggestions[4] + " or " + shirt_suggestions[6]
                              + ", either " + pants_suggestions[0] + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0])

        elif interviewChoice.get() == interview_types[2]:  # Over the Phone
            if budgetChoice.get() == budget_ranges[0]:
                suggestion = ("Since your budget is 0; use the cleanest, nicest thing in your closet. "
                              "They may not see you, but being nicely dressed can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[1]:
                suggestion = ("I recommend that you wear: either a" + shirt_suggestions[4] + " or " + shirt_suggestions[6]
                              + ", either " + pants_suggestions[0] + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0]
                              + "They may not see you, but being nicely dressed can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[2]:
                suggestion = ("I recommend that you wear: either a" + shirt_suggestions[4] + " or " + shirt_suggestions[6]
                              + ", either " + pants_suggestions[0] + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0]
                              + "They may not see you, but being nicely dressed can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[3]:
                suggestion = ("I recommend that you wear: either a" + shirt_suggestions[4] + " or " + shirt_suggestions[6]
                              + ", either " + pants_suggestions[0] + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0]
                              + "They may not see you, but being nicely dressed can help boost confidence.")
            elif budgetChoice.get() == budget_ranges[4]:
                suggestion = ("I recommend that you wear: either a" + shirt_suggestions[4] + " or " + shirt_suggestions[6]
                              + ", either " + pants_suggestions[0] + " or " + pants_suggestions[3] + ", and " + shoes_suggestions[0]
                              + "They may not see you, but being nicely dressed can help boost confidence.")

    return suggestion

def get_alternatives():
    alternate_suggestion = "Nothing was entered."
    if alternateChoice.get() == clothing_restrictions[0]:
        alternate_suggestion = ("Depending on your religion, we suggest one of these: " + religious_exemptions[0] + ", "
                                 + religious_exemptions[1] + ", or a " + religious_exemptions[2])
    elif alternateChoice.get() == clothing_restrictions[1]:
      #  if disability_restrictions ==
        alternate_suggestion = ("If you are disabled and need an alternative, we suggest wearing clothing that is comfortable and easy to "
                                "get on without much help. Also, for certain surgery related issues, we also recommend using darker clothing.")
    elif alternateChoice.get() == clothing_restrictions[2]:
        alternate_suggestion = ("If you have issues with certain fabrics, we suggest one of these alternative fabrics: \n"
                                + fabric_alternatives[0] + ", " + fabric_alternatives[1] + ", " + fabric_alternatives[2] + ", " + fabric_alternatives[3] +
                                ", " + fabric_alternatives[4] + ", or for those particularly susceptible to regular wool; a" + fabric_alternatives[5])

    return alternate_suggestion


window.mainloop()
