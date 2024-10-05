# server.py
import os
from livekit import api
from flask import Flask

app = Flask(__name__)

@app.route('/getToken')
def getToken():
  token = api.AccessToken('APIzwZ76quC5NNT', 'yaAeVpGXBZfIr5xyOXaGZ1PX3eM7H1MTLMR97pXcD2rA') \
    .with_identity("identity") \
    .with_name("my name") \
    .with_grants(api.VideoGrants(
        room_join=True,
        room="my-room",
    ))
  return token.to_jwt()

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')