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
		sound_module.Divider(main_window, "Common")
		sound_module.Sound_module('sound_files/edited/misc/t_Nandi.mp3', main_window, loop=False)
		sound_module.Sound_module('sound_files/edited/misc/t0_BHJTitleTrack.mp3', main_window, loop=False)
		sound_module.Sound_module('sound_files/edited/misc/t1_skitEndMusic.mp3', main_window, loop=False)
		sound_module.Sound_module('sound_files/edited/misc/t2_blackoutToComparingMusic.mp3', main_window)
		sound_module.Divider(main_window, "Skit-wise")
	def init_one():
		#mayat
		sound_module.Divider(window, "Mayat")
		sound_module.Sound_module('sound_files/edited/mayat/t1_sadFunnyMusic.mp3', window, loop=False)
		sound_module.Sound_module('sound_files/edited/mayat/t2_donkeyNoise.mp3', window, loop=False)
		sound_module.Sound_module('sound_files/edited/mayat/t3_annaAnna.mp3', window)
		sound_module.Sound_module('sound_files/edited/mayat/t4_zoAvadtoSarvala.mp3', window)
		sound_module.Sound_module('sound_files/edited/mayat/t5_oDuniyaKeRakhwale.mp3', window)
		sound_module.Sound_module('sound_files/edited/mayat/t6_gauravSangitacha.mp3', window)
	def init_two():
		#Mission Successful
		sound_module.Divider(window, "MissionSuccessful")
		sound_module.Sound_module('sound_files/edited/missionSuccessful/t1_shalechiGhanta.mp3', window, loop=False)
		sound_module.Sound_module('sound_files/edited/missionSuccessful/t2_chatteringMusic.mp3', window)
		sound_module.Sound_module('sound_files/edited/missionSuccessful/t3_dipariDipang.mp3', window)
		sound_module.Sound_module('sound_files/edited/missionSuccessful/t4-5-6_subjectChangeMusic.mp3', window)
	def init_three():
		#mulgiBaghnyachaKaryakram
		sound_module.Divider(window, "MulgiBaghnyachaKaryakram")
		sound_module.Sound_module('sound_files/edited/mulgiBaghnyachaKaryakram/t1_kandePohe.mp3', window, loop=False)
		sound_module.Sound_module('sound_files/edited/mulgiBaghnyachaKaryakram/t2_retiwalaNavraPahije.mp3', window, loop=False)
		sound_module.Sound_module('sound_files/edited/mulgiBaghnyachaKaryakram/t3_naSangatachAaj.mp3', window, loop=False)
		sound_module.Sound_module('sound_files/edited/mulgiBaghnyachaKaryakram/t4_dholki.mp3', window)
	def init_four():
		#patteTitheThatte
		sound_module.Divider(window, "patteTitheThatte")
		sound_module.Sound_module('sound_files/edited/patteTitheThatte/t1_patteTitheThatteTitle_new.mp3', window, loop=False)
		sound_module.Sound_module('sound_files/edited/patteTitheThatte/t2_yehDostiHumNahiTodenge.mp3', window, loop=False)
		sound_module.Sound_module('sound_files/edited/patteTitheThatte/t3_emotionalSadFluteMusic.mp3', window)
		sound_module.Sound_module('sound_files/edited/patteTitheThatte/t4_endingMusic.mp3', window, loop=False)
	def init_five():
		#tavalAshram
		sound_module.Divider(window, "tavalAshram")
		sound_module.Sound_module('sound_files/edited/tavalAshram/t1_spiritualMusic.mp3', window)
		sound_module.Sound_module('sound_files/edited/tavalAshram/t2_lifebuoy.mp3', window, loop=False)
		sound_module.Sound_module('sound_files/edited/tavalAshram/t3_KokilaAwaj.mp3', window, loop=False)
		sound_module.Sound_module('sound_files/edited/tavalAshram/t4_templeBell.mp3', window, loop=False)
		sound_module.Sound_module('sound_files/edited/tavalAshram/t5_news.mp3', window, loop=False)

	init_zero()
	#pack this later because init_zero contains common Sound_modules
	main_frame.pack()
	init_one()
	init_two()
	init_three()
	init_four()
	init_five()
	window.mainloop()
