import time

import logging
logging.basicConfig(level=logging.INFO)

from src.config import host, port, password
from obswebsocket import obsws, requests  # noqa: E402

ws = obsws(host, port, password)
try:
    ws.connect()
    print("[Success] OBS Connection Established")
except:
    print("[ERROR] OBS Not connected")

def get_scenes():
    scenes = ws.call(requests.GetSceneList())
    all_scenes = []
    for s in scenes.getScenes():
        name = s['name']
        all_scenes.append(name)
    print("\nAll Available Scenes\n")
    print(all_scenes, "\n")
    return all_scenes

def switch_connection(name):
    ws.call(requests.SetCurrentScene(name))

def close_obs_connection():
    ws.disconnect()
    print("[Success] OBS Disconnected")
