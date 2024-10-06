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
import asyncio

# Set up logging
logger = logging.getLogger("voice_assistant")
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Global variable to store the assistant instance
assistant = None

async def entrypoint(ctx: JobContext):
    global assistant
    logger.info("Starting voice assistant entrypoint")

    # Connect to the LiveKit room
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Wait for the first participant to join the room
    participant = await ctx.wait_for_participant()
    logger.info(f"Participant {participant.identity} has joined")

    # Configure the model using OpenAI's RealtimeModel
    model = openai.realtime.RealtimeModel(
        instructions="You are a helpful assistant that provides concise, informative answers. Avoid unnecessary details.",
        voice="shimmer",  # You can choose other voices OpenAI provides
        temperature=0.7,
        modalities=["audio", "text"],
    )

    # Set up the MultimodalAgent to manage the interaction
    assistant = MultimodalAgent(model=model)
    assistant.start(ctx.room)
    logger.info("Voice assistant has started")

    # Start a conversation with the participant
    session = model.sessions[0]
    session.conversation.item.create(
        llm.ChatMessage(
            role="user",
            content="How can I assist you today?",
        )
    )

    # Generate the first response
    session.response.create()

@app.route('/voice-command', methods=['POST'])
def handle_voice_command():
    data = request.json
    track_id = data.get('trackId')

    if not track_id:
        return jsonify({'error': 'trackId is missing'}), 400

    # Process the voice command based on the track_id
    response_message = process_voice_command(track_id)
    return jsonify({'message': response_message})

def process_voice_command(track_id):
    # Implement the logic to handle the voice command based on track_id
    # This is a placeholder for your command processing logic
    return f"Processed command for track ID: {track_id}"

def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    # Start the Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Run the LiveKit worker with the entrypoint function
    cli.run_app(WorkerOptions(
        entrypoint_fnc=entrypoint, 
        ws_url='wss://voice-assistant-p9sapy6b.livekit.cloud', 
        api_key=os.getenv('APIzwZ76quC5NNT'),
        api_secret=os.getenv('yaAeVpGXBZfIr5xyOXaGZ1PX3eM7H1MTLMR97pXcD2rA')
    ))
