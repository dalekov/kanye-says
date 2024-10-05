from tkinter import *
import requests

def get_quote():
    data = requests.get("https://api.kanye.rest").json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote, font=("Arial", 20, "bold", "italic"))

root = Tk()
root.title("Kanye Says...")
root.config(padx=50, pady=50)


canvas = Canvas(width=300, height=414)
bg_image = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=bg_image)
quote_text = canvas.create_text(150, 207, width=250, text="Kanye quote here...", fill="white")
canvas.grid(column=0, row=0)

button_image = PhotoImage(file="kanye.png")
kanye_button = Button(image=button_image, highlightthickness=0, command=get_quote)
kanye_button.grid(column=0, row=1)

root.mainloop()
