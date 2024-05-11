# SMTP
documentclass{article}
usepackage{geometry}
usepackage{lipsum} % for dummy text, you can remove this

geometry{a4paper, margin=1in}

title{Project Report Building a Basic Email Client with Python}
author{Your Name}
date{}

begin{document}

maketitle

section{Introduction}
The objective of this project was to develop a basic email client application using Python that can send and receive emails via Gmail's SMTP and IMAP protocols. The application was built using the Tkinter library for the graphical user interface (GUI) and integrated functionalities for sending and receiving emails.

section{Libraries Used}
begin{enumerate}
    item textbf{tkinter} Used for building the GUI components such as labels, entries, buttons, and frames.
    item textbf{smtplib} Utilized for sending emails via SMTP protocol.
    item textbf{imaplib} Employed for receiving emails via IMAP protocol.
    item textbf{email} Used for parsing email messages.
    item textbf{plyer} Utilized for displaying desktop notifications upon receiving new emails.
end{enumerate}

section{Installation}
begin{itemize}
    item Python Ensure Python is installed on the system. If not, it can be downloaded and installed from the official Python website (httpswww.python.org).
    item Tkinter Tkinter is included with Python, so no separate installation is required.
    item Other libraries (smtplib, imaplib, plyer) are also included in Python's standard library, so no additional installations are needed.
end{itemize}

section{Testing}
subsection{Sending Email Functionality Testing}
begin{itemize}
    item Tested the sending email functionality by providing valid sender email, password, recipient email, subject, and body. 
    item Verified that the email was sent successfully without any errors.
end{itemize}

subsection{Receiving Email Functionality Testing}
begin{itemize}
    item Tested the receiving email functionality by providing valid email address and password.
    item Verified that the application could connect to the email server, retrieve the latest email, display its content, and show a desktop notification.
end{itemize}

section{Results}
begin{itemize}
    item The application successfully sends emails using the provided sender's email credentials and recipient email.
    item The application can receive emails by connecting to the user's Gmail account and fetching the latest email.
    item Upon receiving a new email, a desktop notification is displayed with the sender and subject of the email.
end{itemize}

section{Conclusion}
In conclusion, the project achieved its objective of creating a basic email client application using Python. It provides a simple and user-friendly interface for sending and receiving emails via Gmail. While the application meets the basic requirements, there is room for further improvement and expansion, such as adding support for attachments, implementing email filtering, and enhancing the GUI for a more polished user experience. Overall, the project demonstrates the capabilities of Python libraries for email communication and GUI development.

end{document}
