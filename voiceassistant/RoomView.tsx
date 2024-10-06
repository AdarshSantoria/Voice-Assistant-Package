import React, { useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useTracks, VideoTrack, isTrackReference } from '@livekit/react-native';

// RoomView component to display participants in a call and process voice commands
const RoomView: React.FC = () => {
  const tracks = useTracks();

  const handleVoiceCommand = async (audioTrack: any) => {
    if (!audioTrack || !audioTrack.publication || !audioTrack.publication.track) return;
  
    try {
      const response = await fetch('https://resilient-virtualmachine-2r8os5.sandbox.livekit.io', {
        method: 'POST', // Use POST if the server supports it
        body: JSON.stringify({
          trackId: audioTrack.publication.track.sid, // Ensure this is correct
        }),
        headers: {
          'Content-Type': 'application/json',
        },
      });
  
      // Check if the response is OK
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const { message } = await response.json();
      console.log('AI Response:', message);
    } catch (error) {
      console.error('Error handling voice command:', error);
    }
  };  

  // Process each track (audio or video)
  const renderTrack = (track: any, index: number) => {
    if (isTrackReference(track)) {
      const streamTrackID = track.publication?.track?.sid || index;
      
      // Check if the track is an audio track
      if ((track.source as string) === 'microphone') {
        handleVoiceCommand(track);
      }

      return (
        <VideoTrack 
          key={streamTrackID}
          trackRef={track} 
          style={styles.participantView}
        />
      );
    }
    return <View key={index} style={styles.participantView} />;
  };

  useEffect(() => {
    // Start processing voice commands when tracks are available
    tracks.forEach((track) => {
      if ((track.source as string) === 'microphone') {
        handleVoiceCommand(track);
      }
    });
  }, [tracks]);

  return (
    <View style={styles.roomContainer}>
      <Text>In Call...</Text>
      {tracks.map(renderTrack)}
    </View>
  );
};

const styles = StyleSheet.create({
  roomContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  participantView: {
    height: 300,
    width: '100%',
    backgroundColor: '#eee',
    marginVertical: 10,
  },
});

export default RoomView;