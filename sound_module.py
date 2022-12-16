from just_playback import Playback
import tkinter as tk

class Sound_module():
	def __init__(self, file_name, window_arg, loop=True):
		self.audio = Playback(file_name)
		self.audio.loop_at_end(loop)
		self.audio.set_volume(1)

		self.window = window_arg

		self.frame = tk.Frame(self.window)

		self.name_label = tk.Label(self.frame, text=((file_name.split('/'))[-1])[:14])
		self.name_label.grid(row=0, column=0)

		self.slider = tk.Scale(self.frame, from_=0, to=100, orient = tk.HORIZONTAL, command = self.volume_update)
		self.slider.set(100)
		self.slider.grid(row=1, column =0)
		
		self.button_frame = tk.Frame(self.frame)
		self.button_frame.grid(row = 1, column = 1)

		self.play_button = tk.Button(self.button_frame, text = 'play/stop', command = self.button_play_stop)
		self.play_button.pack(side = tk.LEFT)
		
		self.pause_button = tk.Button(self.button_frame, text = 'pause/resume', command = self.button_pause_resume)
		self.pause_button.pack(side = tk.LEFT)
		
		self.text = tk.Text(self.frame, height =1, width=20)
		self.text.grid(row=0, column = 1)
		
		self.frame.pack(side = tk.TOP)
		
		self.update_text()

	def button_pause_resume(self):
		if self.audio.playing:
			self.audio.pause()
		else:
			self.audio.resume()

	def button_play_stop(self):
		if self.audio.active:
			self.audio.stop()
		else:
			self.audio.play()

	def volume_update(self, value=None):
		val = (self.slider.get())/100
		self.audio.set_volume(val)

	def update_text(self):
		self.text.delete("1.0", "end")
		self.text.insert(tk.END, f'{self.audio.playing}->{round(self.audio.curr_pos)}||{round(self.audio.duration)}')
		self.text.after(1, self.update_text)


