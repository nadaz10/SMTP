import tkinter as tk
from tkinter import messagebox
from SendRec import send_email
from SendRec import receive_email
def send_email_gui():
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    recipient_email = recipient_email_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0", tk.END)
    
    send_email(sender_email, sender_password, recipient_email, subject, body)

def receive_email_gui():
    email_address = email_address_entry.get()
    password = password_entry.get()
    
    receive_email(email_address, password)

root = tk.Tk()
root.title("Email Client")

# Sending Email Section
sending_frame = tk.LabelFrame(root, text="Send Email")
sending_frame.pack(padx=10, pady=10, fill="both", expand="yes")

sender_email_label = tk.Label(sending_frame, text="Your Email:")
sender_email_label.grid(row=0, column=0, sticky="e")
sender_email_entry = tk.Entry(sending_frame)
sender_email_entry.grid(row=0, column=1)

sender_password_label = tk.Label(sending_frame, text="Your Password:")
sender_password_label.grid(row=1, column=0, sticky="e")
sender_password_entry = tk.Entry(sending_frame, show="*")
sender_password_entry.grid(row=1, column=1)

recipient_email_label = tk.Label(sending_frame, text="Recipient Email:")
recipient_email_label.grid(row=2, column=0, sticky="e")
recipient_email_entry = tk.Entry(sending_frame)
recipient_email_entry.grid(row=2, column=1)

subject_label = tk.Label(sending_frame, text="Subject:")
subject_label.grid(row=3, column=0, sticky="e")
subject_entry = tk.Entry(sending_frame)
subject_entry.grid(row=3, column=1)

body_label = tk.Label(sending_frame, text="Body:")
body_label.grid(row=4, column=0, sticky="ne")
body_entry = tk.Text(sending_frame, height=5, width=30)
body_entry.grid(row=4, column=1, padx=5, pady=5)

send_button = tk.Button(sending_frame, text="Send Email", command=send_email_gui)
send_button.grid(row=5, columnspan=2)

# Receiving Email Section
receiving_frame = tk.LabelFrame(root, text="Receive Email")
receiving_frame.pack(padx=10, pady=10, fill="both", expand="yes")

email_address_label = tk.Label(receiving_frame, text="Your Email:")
email_address_label.grid(row=0, column=0, sticky="e")
email_address_entry = tk.Entry(receiving_frame)
email_address_entry.grid(row=0, column=1)

password_label = tk.Label(receiving_frame, text="Your Password:")
password_label.grid(row=1, column=0, sticky="e")
password_entry = tk.Entry(receiving_frame, show="*")
password_entry.grid(row=1, column=1)

receive_button = tk.Button(receiving_frame, text="Receive Email", command=receive_email_gui)
receive_button.grid(row=2, columnspan=2)

root.mainloop()
