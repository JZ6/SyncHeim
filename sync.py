# import os
# print (os.getenv('LOCALAPPDATA'))

from pathlib import Path

def to_local(world_name):
	user_home = Path.home()
	valheim_dir = Path(user_home,'AppData','LocalLow','IronGate','Valheim')

	glob_pattern = f'worlds/{world_name}.*'
	for world in valheim_dir.glob(glob_pattern):
		print(world)
	 

def to_remote():
	pass
