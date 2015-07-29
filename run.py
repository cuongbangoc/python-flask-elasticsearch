#!env/bin/python3
from app import app
from config import config as cfg
app.run(debug=True, host=cfg.APP_HOST, port=cfg.APP_PORT)
