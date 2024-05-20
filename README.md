# SMTP Mail Client with GUI and Notifications

## Overview

This project is an SMTP Mail Client application designed to send and receive emails with a user-friendly graphical user interface (GUI) and notification system. The application is built using Java for the backend and JavaFX for the GUI, providing a robust and intuitive platform for managing emails.

## Features

- **Send Emails**: Compose and send emails using the SMTP protocol.
- **Receive Emails**: Fetch and display emails from an inbox using POP3/IMAP.
- **User Authentication**: Secure login system to access email accounts.
- **Email Notifications**: Real-time notifications for new emails.
- **GUI Interface**: Intuitive and responsive interface built with JavaFX.
- **Email Attachments**: Support for sending and receiving email attachments.
- **Email Formatting**: Rich text formatting options for composing emails.

## Installation

To set up the SMTP Mail Client on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/smtp-mail-client.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd smtp-mail-client
    ```

3. **Set up the project environment**:
    - Ensure you have Java Development Kit (JDK) installed (Java 8 or higher).
    - Ensure you have a build tool like Apache Maven or Gradle installed.
    - Configure your email server settings in `config.properties`.

4. **Build and run the application**:
    - Using Maven:
        ```bash
        mvn clean install
        mvn exec:java -Dexec.mainClass="com.example.smtp.MailClient"
        ```
    - Using Gradle:
        ```bash
        gradle build
        gradle run
        ```

## Usage

### GUI Interface

- **Login Page**: Enter your email credentials to log in.
- **Inbox**: View a list of received emails with sender, subject, and timestamp.
- **Compose Email**: Create and send a new email. Include attachments and apply rich text formatting.
- **Email View**: Read emails in a detailed view with options to reply, forward, or delete.
- **Notifications**: Receive desktop notifications for new emails.




