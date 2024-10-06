from __future__ import annotations
import os
import logging
from flask import Flask, request, jsonify
from livekit import rtc
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    WorkerOptions,
    cli,
    llm,
)
from livekit.agents.multimodal import MultimodalAgent
from livekit.plugins import openai
import threading

# Set up logging
logger = logging.getLogger("myagent")
logger.setLevel(logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Global variable to store the assistant instance
assistant = None

async def entrypoint(ctx: JobContext):
    global assistant
    logger.info("starting entrypoint")

    # Connect to the LiveKit context
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Wait for a participant to join the room
    participant = await ctx.wait_for_participant()

    # Configure the model using OpenAI's RealtimeModel
    model = openai.realtime.RealtimeModel(
        instructions="You are a helpful assistant and you love kittens",
        voice="shimmer",
        temperature=0.8,
        modalities=["audio", "text"],
    )

    # Set up the MultimodalAgent
    assistant = MultimodalAgent(model=model)
    assistant.start(ctx.room)

    logger.info("starting agent")

    # Initialize the conversation with the participant
    session = model.sessions[0]
    session.conversation.item.create(
        llm.ChatMessage(
            role="user",
            content="Please begin the interaction with the user in a manner consistent with your instructions.",
        )
    )

    # Create a response to initiate the conversation
    session.response.create()

@app.route('/voice-command', methods=['POST'])
def handle_voice_command():
    data = request.json
    track_id = data.get('trackId')
    
    # Here you can process the voice command using the track_id
    response_message = process_voice_command(track_id)  # Implement this function based on your logic
    
    return jsonify({'message': response_message})

def process_voice_command(track_id):
    # Implement the logic to handle the voice command based on track_id
    return f"Processed command for track ID: {track_id}"

def run_flask():
    app.run(host='0.0.0.0', port=5000)  # Make sure to choose a suitable port

if __name__ == "__main__":
    # Start the Flask app in a separate thread
    threading.Thread(target=run_flask).start()

    # Run the application with the provided entrypoint function
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, ws_url='wss://voice-assistant-p9sapy6b.livekit.cloud', api_key='APIzwZ76quC5NNT', api_secret='yaAeVpGXBZfIr5xyOXaGZ1PX3eM7H1MTLMR97pXcD2rA'))