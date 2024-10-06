# Voice Assistant App

## Overview

Voice Assistant is a React Native application that allows users to make voice calls using LiveKit. This app leverages the capabilities of LiveKit to facilitate real-time communication and process voice commands. It provides a seamless experience for initiating calls and interacting with voice data.

## Features

- **Voice Calls**: Initiate and participate in voice calls using LiveKit.
- **Token Generation**: Automatically fetches access tokens for securing the call sessions.
- **Voice Command Processing**: Sends audio track data to a specified endpoint for processing voice commands.

## Installation

### Prerequisites

- Node.js (v14 or later)
- React Native environment set up (React Native CLI, Android Studio, or Xcode for iOS)
- LiveKit account and a valid WebSocket URL

### Clone the Repository

```bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```

### Install Dependencies

```bash
npm install
```

### Setup Environment Variables

- Create a .env file in the root directory and define the necessary environment variables. Ensure to set the correct LiveKit WebSocket URL:

arduino
LIVEKIT_URL=wss://your-livekit-url
Start the Application
bash
Copy code
npm run start
For Android:

bash
Copy code
npm run android
For iOS:

```bash
npm run ios
```

### Usage
- Generate Token: Upon launching the app, it will automatically fetch a token required for connecting to LiveKit.
- Start a Voice Call: Tap the "Start Voice Call" button to initiate a call.
- Voice Commands: During the call, any audio captured through the microphone will be sent to the backend for processing.

### Components

#### App
- The main component that manages the application's state, including audio session management and initiating calls.

#### TokenGenerator
- Responsible for fetching the access token required to connect to the LiveKit room.

#### RoomView
- Displays the participants in the call and processes voice commands based on audio tracks received.

#### Dependencies
- @livekit/react-native: For LiveKit functionalities.
- react-native: The core library for building the application.
- Other dependencies as specified in package.json.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any features, improvements, or bug fixes.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
LiveKit for providing the real-time communication platform.
Any other libraries or resources you may have used or referenced.
css

This README provides a comprehensive overview of your Voice Assistant App, including installation instructions, usage guidelines, and contribution details.
