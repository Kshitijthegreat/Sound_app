def main():
	import tkinter as tk
	import sound_module

	window = tk.Tk()
	window.geometry("500x500")
	window.title('sound_manager')
	module1 = sound_module.Sound_module('sound_files/police_siren.mp3', window)
	module2 = sound_module.Sound_module('sound_files/background_edited.mp3', window)
	module3 = sound_module.Sound_module('sound_files/Ambulance_siren.mp3', window)
	module4 = sound_module.Sound_module('sound_files/nokia_ringtone_edited.mp3', window)
	module5 = sound_module.Sound_module('sound_files/land_line.mp3', window)
	module6 = sound_module.Sound_module('sound_files/pakhavaj_1.mp3', window)
	module7 = sound_module.Sound_module('sound_files/painful_beep.mp3', window)
	window.mainloop()
if __name__=='__main__':
	main()