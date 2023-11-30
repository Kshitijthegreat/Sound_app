def main():
	import tkinter as tk
	import sound_module

	window = tk.Tk()
	window.geometry("1000x700")
	window.title('sound_manager')

	def init_zero():
		#common skit end music
		divider1 = sound_module.Divider(window, "Common")

	def init_one():
		divider2 = sound_module.Divider(window, "Mayat")
		module1 = sound_module.Sound_module('sound_files/edited/mayat/gauravSangitache.mp3', window)
		module2 = sound_module.Sound_module('sound_files/edited/mayat/oDuniyaKeRakhwale.mp3', window)
		
	def init_two():
		divider3 = sound_module.Divider(window, "Taval Ashram")
		module3 = sound_module.Sound_module('sound_files/edited/tavalAshram/googlePaySuccessSound.mp3', window, loop=False)
		module4 = sound_module.Sound_module('sound_files/edited/tavalAshram/SpiritualMusic.mp3', window)
		
	def init_three():
		divider4 = sound_module.Divider(window, "Patte Tithe Thatte")
		module5 = sound_module.Sound_module('sound_files/edited/patteTitheThatte/emotionalSadFluteMusic.mp3', window, loop=False)
		module6 = sound_module.Sound_module('sound_files/edited/patteTitheThatte/yehDostiHumNahiTodenge.mp3', window, loop=False)
		module7 = sound_module.Sound_module('sound_files/edited/patteTitheThatte/patteTitheThatteTitle_new.mp3', window, loop=False)
		
		#module13 = sound_module.Sound_module('sound_files/recorded_faster.mp3', window, loop=False)
		#module3 = sound_module.Sound_module('sound_files/one/Ambulance_siren.mp3', window)
		#module11 = sound_module.Sound_module('sound_files/one/tick_tick.mp3', window)
		#module4 = sound_module.Sound_module('sound_files/one/nokia_ringtone_edited.mp3', window)
		#module5 = sound_module.Sound_module('sound_files/one/land_line.mp3', window)
		#module6 = sound_module.Sound_module('sound_files/one/pakhavaj_1.mp3', window)
		#module8 = sound_module.Sound_module('sound_files/one/prakash_bolat_hota.mp3', window, loop=False)
		#module9 = sound_module.Sound_module('sound_files/one/recorded_original.mp3', window, loop=False)
		#module7 = sound_module.Sound_module('sound_files/one/painful_beep.mp3', window)
		#module10 = sound_module.Sound_module('sound_files/one/recorded_edited.mp3', window, loop=False)

	#inits = [init_one, init_two]
	#try:
	#	inp = int(input('1->Godva\n2->natak_2\n>'))
	#	(inits[inp-1])()
	#except:
	#	(inits[0])()
	init_zero()
	init_one()
	init_two()
	init_three()
	window.mainloop()

if __name__=='__main__':
	main()