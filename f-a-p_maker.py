#!/usr/bin/env python3

from simple_term_menu import TerminalMenu
from progress.spinner import Spinner
import time
import sys
import subprocess
import shutil

options = ["Change Name", "Create"]

term = TerminalMenu(options)
menu_entry_index = term.show()
if options[menu_entry_index] == "Create":
	p = subprocess.Popen("./fbt", cwd="../flipperzero-firmware", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
	spinner = Spinner("Generating Flipper Application Package ")
	while True:
		time.sleep(0.2)
		spinner.next()
		poll = p.poll()
		if poll is None:
			continue
		else:
			break

	shutil.copy2("../flipperzero-firmware/dist/f7-D/flipper-z-f7-full-local.dfu", "firmware.dfu")
	sys.stdout.write('\033[2K\033[1G') #Here there be dragons
	print("finished!")
