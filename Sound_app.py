import tkinter as tk
import sound_module
def main():
	#use window as frame interior because legacy
	main_window = tk.Tk()
	main_window.geometry("1000x700")
	main_window.title('sound_manager')
	main_frame = sound_module.VerticalScrolledFrame(main_window)
	window = main_frame.interior
	
	def init_zero():
		#common skit end music
		#sound_module.Divider(main_window, "Common")
		#sound_module.Sound_module('sound_files/edited/misc/t_ghanta.mp3', main_window)
		#sound_module.Sound_module('sound_files/edited/misc/t_Nandi[instrumental].mp3', main_window)
		#sound_module.Sound_module('sound_files/edited/misc/t_Nandi.mp3', main_window, loop=False)
		#sound_module.Sound_module('sound_files/edited/misc/t0_BHJTitleTrack.mp3', main_window, loop=False)
		#sound_module.Sound_module('sound_files/edited/misc/t1_skitEndMusic.mp3', main_window, loop=False)
		#sound_module.Sound_module('sound_files/edited/misc/t2_blackoutToComparingMusic.mp3', main_window)
		sound_module.Divider(main_window, "Skit-wise")
	def init_one():
		#mayat
		sound_module.Divider(window, "Mayat")
		#sound_module.Sound_module('sound_files/edited/mayat/t1_sadFunnyMusic.mp3', window, loop=False)
		#sound_module.Sound_module('sound_files/edited/mayat/t2_donkeyNoise.mp3', window, loop=False)
		#sound_module.Sound_module('sound_files/edited/mayat/t3_annaAnna.mp3', window)
		#sound_module.Sound_module('sound_files/edited/mayat/t4_zoAvadtoSarvala.mp3', window)
		#sound_module.Sound_module('sound_files/edited/mayat/t5_oDuniyaKeRakhwale.mp3', window)
		#sound_module.Sound_module('sound_files/edited/mayat/t6_gauravSangitacha.mp3', window)


	init_zero()
	#pack this later because init_zero contains common Sound_modules
	main_frame.pack(anchor=tk.NW)
	init_one()
	window.mainloop()
