#!/usr/bin/env python3

from simple_term_menu import TerminalMenu
from progress.spinner import Spinner
from time import sleep
import sys
import subprocess
from shutil import copy2
from pathlib2 import Path

options = ["Clone Flipper Zero Repo", "Change Name", "Create"]

term = TerminalMenu(options)

while True:
	menu_entry_index = term.show()
	if options[menu_entry_index] == "Clone Flipper Zero Repo":
		subprocess.run("git clone --recursive https://github.com/flipperdevices/flipperzero-firmware.git", shell=True)
		copy2("flipperzero-firmware/firmware/targets/f7/furi_hal/furi_hal_version.c", "backups/furi_hal_version.c") # this is for restoring the name to otp->name because my dumb ass can't figure out how to get a line by line number and replace it
		print("Repo has been cloned!")

	elif options[menu_entry_index] == "Change Name":
		copy2("backups/furi_hal_version.c", "flipperzero-firmware/firmware/targets/f7/furi_hal/")
		name = input("what would you like the name of your flipper to be? ")
		path = Path("flipperzero-firmware/firmware/targets/f7/furi_hal/furi_hal_version.c")
		text = path.read_text()
		text = text.replace("otp->name", f'"{name}"')
		path.write_text(text)
		print("Name changed!")

	elif options[menu_entry_index] == "Create":
		p = subprocess.Popen("./fbt", cwd="flipperzero-firmware", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
		spinner = Spinner("Generating Flipper Application Package ")
		while p.poll() is None:
			sleep(0.2)
			spinner.next()

		copy2("flipperzero-firmware/dist/f7-D/flipper-z-f7-full-local.dfu", "firmware.dfu")
		sys.stdout.write('\033[2K\033[1G') #Here there be dragons
		print("Finished!")
		break
