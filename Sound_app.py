import tkinter as tk
import sound_module
def main():
	
	window = tk.Tk()
	window.geometry("1000x700")
	window.title('sound_manager')

	def init_zero():
		#common skit end music
		divider1 = sound_module.Divider(window, "Common")
		module1 = sound_module.Sound_module('sound_files/edited/misc/t1_skitEndMusic.mp3', window)

	
	init_zero()
	window.mainloop()
