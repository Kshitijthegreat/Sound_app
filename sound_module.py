from just_playback import Playback
import tkinter as tk

class Sound_module():
	def __init__(self, file_name, window_arg, loop=True):
		#load the audio, create the audio instance
		self.audio = Playback(file_name)
		self.audio.loop_at_end(loop)
		self.audio.set_volume(1)
		self.track_enable = False
		#define window object
		self.window = window_arg
		#create the background frame
		self.background_frame = tk.Frame(self.window, background = 'red')
		self.background_frame.pack(side = tk.TOP, anchor = tk.NW)
		#create the main frame
		self.frame = tk.Frame(self.background_frame)
		self.frame.pack(side = tk.TOP, padx = 0, pady=4)
		#create track enable button
		self.enable_button = tk.Button(self.frame, text = 'enable/disable', command = self.enable_button_func)
		self.enable_button.grid(row=0, column = 1)
		#create playback seek entry box and button
		self.playback_seek_entry = tk.Entry(self.frame)
		self.playback_seek_entry.grid(row = 0, column = 5)
		self.playback_seek_entry_button = tk.Button(self.frame, text = 'seek', command = self.playback_seek)
		self.playback_seek_entry_button.grid(row =0, column = 7)
		#create the track name label
		self.name_label = tk.Label(self.frame, text=((file_name.split('/'))[-1])[:15], width = 15, height = 2)
		self.name_label.grid(row = 0, column = 0)
		#create the volume slider
		self.slider = tk.Scale(self.frame, from_=0, to=100, orient = tk.HORIZONTAL, command = self.volume_update)
		self.slider.set(100)
		self.slider.grid(row=0, column =2)
		#create extra frame for formatting play/stop and pause/resume buttons
		self.button_frame = tk.Frame(self.frame)
		self.button_frame.grid(row = 0, column = 3)
		#create play/stop button
		self.play_button = tk.Button(self.button_frame, text = 'play/stop', command = self.button_play_stop)
		self.play_button.pack(side = tk.LEFT)
		#create pause/resume button
		self.pause_button = tk.Button(self.button_frame, text = 'pause/resume', command = self.button_pause_resume)
		self.pause_button.pack(side = tk.LEFT)
		#create the text box to indicate current condition(playing/not playing) and display playback point
		self.text = tk.Text(self.frame, height =1, width=40)
		self.text.grid(row=0, column = 4)
		#call the update_text method to start the text update loop
		self.update_text()

	def button_pause_resume(self):
		#pause/resume button function
		if self.audio.playing:
			self.audio.pause()
		else:
			if self.track_enable:
				self.audio.resume()

	def button_play_stop(self):
		#play/stop button function
		if self.audio.active:
			self.audio.stop()
		else:
			if self.track_enable:
				self.audio.play()

	def volume_update(self, value = None):
		#volume slider function
		self.audio.set_volume((self.slider.get())/100)

	def playback_seek(self):
		try:
			self.audio.seek(int(self.playback_seek_entry.get()))
			self.playback_seek_entry.delete(0, 'end')
		except:
			pass

	def update_text(self):
		#text updater function
		self.text.delete("1.0", "end")
		self.text.insert(tk.END, f'enabled:{self.track_enable}||playing:{self.audio.playing}->{round(self.audio.curr_pos)}||{round(self.audio.duration)}')
		self.text.after(1, self.update_text)

	def enable_button_func(self):
		if self.track_enable:
			self.track_enable = False
			self.audio.stop()
		else:
			self.track_enable = True


class Divider():
	def __init__(self, window_arg, _text):
		#define window object
		self.window = window_arg
		#create the background frame
		self.background_frame = tk.Frame(self.window, background = 'red')
		self.background_frame.pack(side = tk.TOP, anchor = tk.NW)
		#create the main frame
		self.frame = tk.Frame(self.background_frame)
		self.frame.pack(side = tk.TOP, padx = 5, pady=4)
		
		self.name_label = tk.Label(self.frame, text=_text, width = 15, height = 2)
		self.name_label.pack(side=tk.TOP, padx=0, pady=0)
	

		
		