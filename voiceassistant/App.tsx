import React, { useState, useEffect } from 'react';
import { View, Button, StyleSheet } from 'react-native';
import { AudioSession, LiveKitRoom } from '@livekit/react-native';
import TokenGenerator from './TokenGenerator';
import RoomView from './RoomView';

// Define the WebSocket URL
const wsURL = "wss://voice-assistant-p9sapy6b.livekit.cloud"; // Replace with your LiveKit URL

const App: React.FC = () => {
  const [token, setToken] = useState<string>('');
  const [inCall, setInCall] = useState<boolean>(false);

  useEffect(() => {
    const startAudioSession = async () => {
      await AudioSession.startAudioSession();
    };

    startAudioSession();
    return () => {
      AudioSession.stopAudioSession();
    };
  }, []);

  const handleCall = () => {
    setInCall(true);
  };

  return (
    <View style={styles.container}>
      {!token ? (
        <TokenGenerator setToken={setToken} />
      ) : inCall ? (
        <LiveKitRoom
          serverUrl={wsURL}
          token={token}
          connect={true}
          options={{ adaptiveStream: { pixelDensity: 'screen' } }}
          audio={true}
          video={false} // Only for voice calls
        >
          <RoomView />
        </LiveKitRoom>
      ) : (
        <Button title="Start Voice Call" onPress={handleCall} />
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default App;
