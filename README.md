# Voice Assistant App

## Overview

Voice Assistant is a React Native application that allows users to make voice calls using LiveKit. This app leverages the capabilities of LiveKit to facilitate real-time communication and process voice commands. It provides a seamless experience for initiating calls and interacting with voice data.

## Features

- **Voice Calls**: Initiate and participate in voice calls using LiveKit.
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

```bash
LIVEKIT_URL=wss://your-livekit-url
```

Start the Application

```bash
npm run start
```
For Android:

```bash
npm run android
```

For iOS:

```bash
npm run ios
```

### Usage
1. **Generate Token**: Upon launching the app, it will automatically fetch a token required for connecting to LiveKit from the server hosted at [https://voice-assistant-package.onrender.com/getToken](https://voice-assistant-package.onrender.com/getToken).
2. **Start a Voice Call**: Tap the "Start Voice Call" button to initiate a call.
3. **Voice Commands**: During the call, any audio captured through the microphone will be sent to the backend for processing.
4. **AI Agent Playground**: You can test AI commands at the AI agent playground: [https://resilient-virtualmachine-2r8os5.sandbox.livekit.io](https://resilient-virtualmachine-2r8os5.sandbox.livekit.io).

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
Any other libraries or resources we may have used or referenced.

```This README provides a comprehensive overview of our Voice Assistant App, including installation instructions, usage guidelines, and contribution details.```
