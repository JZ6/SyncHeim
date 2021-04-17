# import os
# print (os.getenv('LOCALAPPDATA'))

from pathlib import Path

user_home = Path.home()
valheim_dir = Path(user_home,'AppData','LocalLow','IronGate','Valheim')
wsl_to_win = {
	'/home/sushinocode': '/mnt/c/Users/thesu/'
}
if not valheim_dir.exists():
	valheim_dir = Path(wsl_to_win[str(user_home)], 'AppData', 'LocalLow', 'IronGate', 'Valheim')

def to_local(world_name):
	pass

def to_remote(world_name: str):
	glob_pattern = f'worlds/{world_name}.*'
	for world in valheim_dir.glob(glob_pattern):
		if 'steam_autocloud' in world.as_posix():
			continue
		print(world)

'''
sushinocode@All-You-Can-Eat ~/repo/SyncHeim (su_local_no_freedom_to_reach.wip)$ python -c 'import sync; sync.to_remote("gme2moon")'
/mnt/c/Users/thesu/AppData/LocalLow/IronGate/Valheim/worlds/gme2moon.db
/mnt/c/Users/thesu/AppData/LocalLow/IronGate/Valheim/worlds/gme2moon.db.old
/mnt/c/Users/thesu/AppData/LocalLow/IronGate/Valheim/worlds/gme2moon.fwl
/mnt/c/Users/thesu/AppData/LocalLow/IronGate/Valheim/worlds/gme2moon.fwl.old
'''