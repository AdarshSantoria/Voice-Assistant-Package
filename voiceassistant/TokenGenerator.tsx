// components/TokenGenerator.tsx
import React, { useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';

// Define props for TokenGenerator component
interface TokenGeneratorProps {
  setToken: (token: string) => void;
}

// TokenGenerator component to fetch the token
const TokenGenerator: React.FC<TokenGeneratorProps> = ({ setToken }) => {
  useEffect(() => {
    fetchToken();
  }, []);

  const fetchToken = async () => {
    try {
      const response = await fetch('https://voice-assistant-package.onrender.com/getToken', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const token = await response.text();
      setToken(token);
    } catch (error) {
      console.error('Error fetching token:', error);
    }
  };

  return (
    <View style={styles.tokenContainer}>
      <Text>Generating Token...</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  tokenContainer: {
    padding: 20,
  },
});

export default TokenGenerator;
