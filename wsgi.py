
"""WSGI production entry point for SkillSwap."""

import os
from app import create_app

env = os.environ.get("FLASK_ENV", "production")
app = create_app(env)

if __name__ == "__main__":
    from app.extensions import socketio
    socketio.run(app)
