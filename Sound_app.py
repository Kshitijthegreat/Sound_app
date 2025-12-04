import tkinter as tk
import sound_module


class soundFile:
	def __init__(self, str):
		self.path = (str.split(','))[0]
		self.loop = ( (str.split(','))[1] == '1' )

class unitFile:
	def __init__(self, str, window):
		self.window = window
		split_str = str.split('\n')
		self.soundFiles = []
		self.unitName=split_str[0]
		for i in range(1,len(split_str)):
			self.soundFiles.append(soundFile(split_str[i]))
	
	def init(self):
		sound_module.Divider(self.window, self.unitName)
		for file in self.soundFiles:
			sound_module.Sound_module(file.path, self.window, file.loop)


def main():
	#use window as frame interior because legacy
	main_window = tk.Tk()
	main_window.geometry("1000x700")
	main_window.title('sound_manager')
	main_frame = sound_module.VerticalScrolledFrame(main_window)
	window = main_frame.interior
	
	with open('fileSave.txt') as f: F_txt=f.read()
	#remove EOL characters from end of file
	while F_txt[-1] == '\n':
		F_txt = F_txt[:-1]
	
	F_unitSplit=F_txt.split('\n::\n')
	
	NonScrolled = unitFile(F_unitSplit[0], main_window)
	NonScrolled.init()
	main_frame.pack(anchor=tk.NW)
	F_unitSplit.pop(0)
	ScrolledList = []
	for i in range(len(F_unitSplit)):
		ScrolledList.append(unitFile(F_unitSplit[i], window))
		ScrolledList[i].init()

	window.mainloop()


if __name__=="__main__":
	#
	main_window = tk.Tk()
	main_window.geometry("1000x700")
	main_window.title('sound_manager')
	main_frame = sound_module.VerticalScrolledFrame(main_window)
	window = main_frame.interior
	#
	
	with open('fileSave.txt') as f: F_txt=f.read()
	#remove EOL characters from end of file
	while F_txt[-1] == '\n':
		F_txt = F_txt[:-1]
	
	F_unitSplit=F_txt.split('\n::\n')
	
	NonScrolled = unitFile(F_unitSplit[0], main_window)
	NonScrolled.init()
	main_frame.pack(anchor=tk.NW)
	F_unitSplit.pop(0)
	ScrolledList = []
	for i in range(len(F_unitSplit)):
		ScrolledList.append(unitFile(F_unitSplit[i], window))
		ScrolledList[i].init()
	
	window.mainloop()
