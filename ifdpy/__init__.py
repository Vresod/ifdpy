import requests
import json
import sys

api_url = "https://discord.com/api/v8"

class Discord:
	"""
	Does the discord stuff. Most functions that do requests accept setting the `raw` argument to True to get the request as opposed to the text in it.
	"""
	def __init__(self,token:str,bot = True):
		if not bot:
			print("WARNING: Automating a non-bot user is forbidden by Discord and may result in an account termination.",file=sys.stderr)
		self.token = "Bot " + token if bot else token
		self.authorization = {"Authorization":self.token}
	def send(self,channelid:int,data:dict,raw:bool=False):
		"""
		Sends a message in the channel specified by channel_id.
		"""
		r = requests.post(f"{api_url}/channels/{channelid}/messages",json=data,headers=self.authorization)
		return r if raw else json.loads(r.text)
	def get_guild(self,guild_id:int,raw:bool=False):
		"""
		Returns a guild
		"""
		r = requests.get(f"{api_url}/users/@me/guilds/{guild_id}",headers=self.authorization)
		return r if raw else json.loads(r.text)
	def get_channel(self,channel_id:int,raw:bool=False):
		"""
		Returns a channel
		"""
		r = requests.get(f"{api_url}/channels/{channel_id}")
		return r if raw else json.loads(r.text)
def embed_builder(*args,**kwargs):
	"""
	Generates sendable embed for send function.
	"""
	if len(args) >= 1:
		kwargs["title"] = args[0]
	if len(args) >= 2:
		kwargs["description"] = args[1]
	return kwargs