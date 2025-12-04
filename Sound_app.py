import tkinter as tk
import sound_module


class soundFile:
	def __init__(self, str):
		self.path = (str.split(","))[0]
		self.loop = ( (str.split(","))[1] == "1" )

class unitFile:
	def __init__(self, str):
		split_str = str.split("\n")
		self.soundFiles = []
		self.unitName=split_str[0]
		for i in range(1,len(split_str)):
			self.soundFiles.append(soundFile(split_str[i]))


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

#with open('fileSave.txt') as f: F_txt=f.read()
#F_unitSplit=F_txt.split("::")

if __name__=="__main__":
	
	uf = unitFile("name\npath/to/file1.mp3,1\npath/to/file2.mp3,0")
	print(uf.unitName, uf.soundFiles[0].path, uf.soundFiles[0].loop)