import time
from stream import Stream

guild_id = 578558255392096256
channel_id = 839833383756365834

s = Stream(guild_id, channel_id)
s.load_video("./tmp/video")
s.open_guild()
s.join()
s.start()
s.play()

time.sleep(20)

s.pause()
s.stop()