#!/usr/bin/env python3

from simple_term_menu import TerminalMenu
from progress.spinner import Spinner
import time
import sys
import os

options = ["Change Name", "Create"]

term = TerminalMenu(options)
menu_entry_index = term.show()
if options[menu_entry_index] == "Create":
	spinner = Spinner("Generating Flipper Application Package ")
	for i in range(20):
		time.sleep(0.2)
		spinner.next()

	sys.stdout.write('\033[2K\033[1G') #Here there be dragons
	print("finished!")
