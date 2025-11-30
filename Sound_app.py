import tkinter as tk
import sound_module
def main():
	#use window as frame interior because legacy
	main_window = tk.Tk()
	main_window.geometry("1000x700")
	main_window.title('sound_manager')
	main_frame = sound_module.VerticalScrolledFrame(main_window)
	window = main_frame.interior
	
	#non-scrolled modules:
	def init_zero():
		sound_module.Divider(main_window, "common")
		#module eg: sound_module.Sound_module('path/to/file.mp3', main_window, loop = True/False)
		sound_module.Divider(main_window, "unit-wise")

	#scrolled modules:
	def init_one():
		#unit1
		sound_module.Divider(window, "unit1")
		#sound_module.Sound_module('path/to/file.mp3', window, loop=True/False)


	#non-scrolled:
	init_zero()
	#pack non-scrolled
	main_frame.pack(anchor=tk.NW)
	#scrolled:
	init_one()
	#init_two()...

	window.mainloop()
