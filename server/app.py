from __future__ import annotations
import logging
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
# Set up logging
logger = logging.getLogger("my-worker")
logger.setLevel(logging.INFO)
async def entrypoint(ctx: JobContext):
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
        api_key='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'
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
if __name__ == "__main__":
    # Run the application with the provided entrypoint function
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, ws_url='wss://voice-assistant-p9sapy6b.livekit.cloud', api_key='APIzwZ76quC5NNT', api_secret='yaAeVpGXBZfIr5xyOXaGZ1PX3eM7H1MTLMR97pXcD2rA'))
