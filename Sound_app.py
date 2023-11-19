def main():
	import tkinter as tk
	import sound_module

	window = tk.Tk()
	window.geometry("1000x700")
	window.title('sound_manager')

	def init_one():
		pass
		#module1 = sound_module.Sound_module('sound_files/one/police_siren.mp3', window)
		#module2 = sound_module.Sound_module('sound_files/one/background_edited.mp3', window)
		#announcement
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
	
	def init_two():
		pass
		#module7 = sound_module.Sound_module('sound_files/two/goli_mar.mp3', window)
		#module3 = sound_module.Sound_module('sound_files/two/gotya_title.mp3', window, loop=False)
		#module6 = sound_module.Sound_module('sound_files/two/chadi_lage.mp3', window)
		#module1 = sound_module.Sound_module('sound_files/two/chipndale.mp3', window)
		#module8 = sound_module.Sound_module('sound_files/two/yahan_ke_sikandar.mp3', window)
		#module4 = sound_module.Sound_module('sound_files/two/Teen_deviya.mp3', window, loop=False)
		#module5 = sound_module.Sound_module('sound_files/two/sanai.mp3', window)
		#module2 = sound_module.Sound_module('sound_files/two/flute.mp3', window, loop=False)

	#inits = [init_one, init_two]
	#try:
	#	inp = int(input('1->Godva\n2->natak_2\n>'))
	#	(inits[inp-1])()
	#except:
	#	(inits[0])()
	window.mainloop()

if __name__=='__main__':
	main()