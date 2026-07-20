#manages apis <3
from SandEngine.Libs import *

DISCORD_CLIENT_ID = "1528705424616984668"
def init_apis():


    RPC = Presence(DISCORD_CLIENT_ID)
    RPC.connect()

    RPC.update(
        state="Creating something new...",
        details="Playing",
        large_image="Assets/icon",
        large_text="Simverra"
    )