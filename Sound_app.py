def main():
	import tkinter as tk
	import sound_module

	window = tk.Tk()
	window.geometry("400x700")
	window.title('sound_manager')
	def init_one():
		module1 = sound_module.Sound_module('sound_files/police_siren.mp3', window)
		module2 = sound_module.Sound_module('sound_files/background_edited.mp3', window)
		module3 = sound_module.Sound_module('sound_files/Ambulance_siren.mp3', window)
		module4 = sound_module.Sound_module('sound_files/nokia_ringtone_edited.mp3', window)
		module5 = sound_module.Sound_module('sound_files/land_line.mp3', window)
		module6 = sound_module.Sound_module('sound_files/pakhavaj_1.mp3', window)
		module7 = sound_module.Sound_module('sound_files/painful_beep.mp3', window)
		module8 = sound_module.Sound_module('sound_files/buffer_1.mp3', window, loop=False)
		module9 = sound_module.Sound_module('sound_files/buffer_2.mp3', window, loop=False)
		module10 = sound_module.Sound_module('sound_files/buffer_3.mp3', window, loop=False)
	def init_two():
		pass
	inp = int(input('1->Godva\n2->natak_2\n>'))
	inits = [init_one, init_two]
	(inits[inp-1])()
	window.mainloop()
if __name__=='__main__':
	main()