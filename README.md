# NFC Task Manager

## Overview

NFC Task Manager is a hybrid project that combines the power of a Raspberry Pi
and a mobile app to create a desk-based task manager. The system allows users
to create tasks on their mobile phone and transfer them to a Raspberry Pi
through NFC (Near Field Communication). The Raspberry Pi, equipped with a
touchscreen, will display and manage the tasks. Users can navigate through the
task list and remove tasks once completed.

## Features

- **Task Creation:** Create tasks on the mobile app with a title, priority level,
  due date, and description.
- **NFC Transfer**: Seamlessly transfer tasks from the mobile app to the
  Raspberry Pi using NFC.
- **Task Management:** Display tasks on the Raspberry Pi's touchscreen, navigate
  through the list, and remove tasks from the active list once completed.

## Technologies Used

- **Raspberry Pi 4b:** The core hardware that powers the desk task manager.
- **NFC Hat PN532:** NFC communication module for transferring tasks between
  the mobile app and the Raspberry Pi.
- **Freenove 5" Touchscreen:** Display interface for interacting with the task
  manager on the Raspberry Pi.
- **Python:** Backend programming languages used to manage tasks and NFC
  communication.
- **React-Native:** Framework for developing the cross-platform mobile app.

## Getting Started

### Prerequisites

- Raspberry Pi 4b with Raspian OS installed,
- NFC Hat PN532,
- Freenove 5" Touchscreen,
- Mobile device with NFC capability (most smartphones today have NFC capabilities),
- Node.js installed for React-Native development.

### Setup

1. **Hardware Assembly:**

- Attach the NFC Hat PN532 to the Raspberry Pi's GPIO pins.
- Connect the Freenove 5" touchscreen to the Raspberry Pi.
  _A more detailed assembly guide will be available soon_

2. **Software Installation:**

- Clone the repository:

  ```bash
  git clone https://github.com/Sp0k/NFCTM.git
  ```

- Navigate to the project directory:

  ```bash
  cd NFCTM
  ```

- Install required Python dependencies:

  ```bash
  pip install -r RPi/requirements.txt
  ```

- Set up the React-Native mobile app:

  ```bash
  cd mobile
  npm install
  ```

- Build and run the React-Native app on your mobile device.

3. **Running the Project:**

- Run the backend on the Raspberry Pi:

  ```bash
  cd RPi
  python3 main.py
  ```

- Use the mobile app to create tasks and transfer them to the Raspberry Pi via NFC.

## Usage

1. **Create a Task:** Open the mobile app, create a task with the necessary
   details, and save it.
2. **Transfer Task:** Place your mobile device near the NFC reader on the
   Raspberry Pi to transfer the task.
3. **Manage Tasks:** Use the touchscreen on the Raspberry Pi to view and manage
   your tasks.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please reach out to [contact@gabsavard.com](mailto:contact@gabsavard.com)
