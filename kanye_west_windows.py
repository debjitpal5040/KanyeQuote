"""A program that displays a Kanye West quote on a background image."""
from tkinter import Button, Canvas, PhotoImage, Tk

import requests

URL = "https://api.kanye.rest/"


def get_quote():
    """Get a quote from the Kanye West API and display it on the canvas."""
    response = requests.get(url=URL, timeout=5)
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")

canvas = Canvas(width=300, height=400)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 200, image=background_img)
quote_text = canvas.create_text(
    150,
    180,
    text="Kanye Quote Goes Here",
    width=250,
    font=("Arial", 20, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(
    image=kanye_img, highlightthickness=1, command=get_quote, bg="black"
)
kanye_button.grid(row=1, column=0)

window.mainloop()
