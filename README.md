# TCP Client Application

A simple TCP Client application built using Python's `socket` library and `tkinter` for the GUI. This client allows users to connect to a TCP server, send messages, and view responses within a GUI.

## Features

- Connect to a TCP server using an IP address and port.
- Send messages to the server through a GUI interface.
- View the message history in a scrollable text area.
- Disconnect from the server safely.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python installations)
  
## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/TCP-Client.git
   cd TCP-Client
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Usage

1. Enter the IP address and port of the TCP server you'd like to connect to (defaults are `127.0.0.1` and `8080`).
2. Click the "Connect" button to establish a connection with the server.
3. Once connected, you can send messages through the "Message" input field and click "Send" to transmit them.
4. The message history will be displayed in the log area.
5. Click "Disconnect" to terminate the connection.

## Code Structure

- `TCPClientApp`: The main class responsible for the GUI and TCP client logic.
  - `setup_ui()`: Initializes the user interface with input fields, buttons, and a message log.
  - `connect_to_server()`: Connects to the server using the provided IP and port.
  - `disconnect_from_server()`: Safely disconnects from the server.
  - `send_message()`: Sends a message to the server and logs it.

## Screenshots

![image](https://github.com/user-attachments/assets/f1ed4950-459e-4696-a1a8-e1fc0bee5a46)


## Contributing

Feel free to fork this repository, make improvements, and submit pull requests!
