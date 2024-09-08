import markdown
import tkinter as tk
from tkinter import scrolledtext

def update_preview():
    markdown_text = input_text.get("1.0", tk.END)
    html_text = markdown.markdown(markdown_text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, html_text)

# Create the main window
window = tk.Tk()
window.title("Markdown Previewer")

# Create the input text area
input_text = scrolledtext.ScrolledText(window, height=10)
input_text.pack()

# Create the output text area
output_text = scrolledtext.ScrolledText(window, height=10)
output_text.pack()

# Create the update button
update_button = tk.Button(window, text="Update Preview", command=update_preview)
update_button.pack()

# Start the main loop
window.mainloop()