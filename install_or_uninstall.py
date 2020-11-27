#!/usr/bin/python3

from quick_tools.stylors import *
from quick_tools.design import menu
from quick_tools.utils import rsh, sh, cl, reg

cl()
print(f"\n{sb}{cb}Scrcpy:{nn}")

choice = menu("Install", "Uninstall", mask=f"  {sb}{cg}{{i}}) {cb}{{p}}{nn}")

if choice == 1:

	print(f"{sb}{cg}\nLoading...\n{nn}")
	scrcpy = rsh("curl https://github.com/Genymobile/scrcpy/releases/")
	scrcpy = reg(scrcpy, "scrcpy v([.\d]+)</a>")

	v = menu(*scrcpy, mask=f"  {sb}{cg}{{i}}) {cb}v{{p}}{nn}") - 1

	scrcpy_link = f"https://github.com/Genymobile/scrcpy/archive/v{scrcpy[v]}.zip"
	server_link = f"https://github.com/Genymobile/scrcpy/releases/download/v{scrcpy[v]}/scrcpy-server-v{scrcpy[v]}"
	rsh(f"rm -rf *{scrcpy[v]}*")

	print(sb, cg)
	for link in (scrcpy_link, server_link):
		print(link)
		sh(f"wget -q --show-progress {link}")

	rsh(f"unzip v{scrcpy[v]}.zip")
	rsh(f"mv scrcpy-server-v{scrcpy[v]} scrcpy-{scrcpy[v]}/scrcpy-server")

	sh(
	f"""
	cd scrcpy-{scrcpy[v]}

	meson build --buildtype release --strip -Db_lto=true  -Dprebuilt_server=scrcpy-server
	cd build

	ninja
	sudo ninja install

	"""
	)

	rsh("mkdir ~/.local/share/icons")
	rsh("mkdir ~/.local/share/applications")

	sh("cp scrcpy-icon.png ~/.local/share/icons")
	sh("cp scrcpy.desktop ~/.local/share/applications")

	print(f"{sb}{cg}Scrcpy Installed{nn}")

else:
	sh(f"sudo rm -rf /usr/local/*/scrcpy*")
	sh("rm ~/.local/share/icons/scrcpy-icon.png")
	sh("rm ~/.local/share/applications/scrcpy.desktop")
	
	print(f"{sb}{cr}Scrcpy Uninstalled{nn}")

