import bots

#This should be the "master" bot who has all abilities and only one owner, which is the controller, aka me/yourself
#if you want more bots you must spawn more bots from this master bot
b1 = bots.Bot(name="demon2", thrId=2, ablBits=(-1 & 0xFFFFFFFF), channels='#thepit')
#overrides the thread.start method so that it is a threaded bot
b1.start()
