import just_playback
import tkinter as tk
Playback = just_playback.Playback
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
		self.frame.pack(side = tk.TOP, padx = 0, pady=1)
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
				self.volume_update()

	def button_play_stop(self):
		#play/stop button function
		if self.audio.active:
			self.audio.stop()
		else:
			if self.track_enable:
				self.audio.play()
				self.volume_update()

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
	

class VerticalScrolledFrame(tk.Frame):
		def __init__(self, parent, *args, **kw):
			tk.Frame.__init__(self, parent, *args, **kw)

			# Create a canvas object and a vertical scrollbar for scrolling it.
			vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
			vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
			canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           yscrollcommand=vscrollbar.set)
			canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
			vscrollbar.config(command=canvas.yview)

			# Reset the view
			canvas.xview_moveto(0)
			canvas.yview_moveto(0)

			# Create a frame inside the canvas which will be scrolled with it.
			self.interior = interior = tk.Frame(canvas)
			interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=tk.NW)

			# Track changes to the canvas and frame width and sync them,
			# also updating the scrollbar.
			def _configure_interior(event):
				# Update the scrollbars to match the size of the inner frame.
				size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
				canvas.config(scrollregion="0 0 %s %s" % size)
				if interior.winfo_reqwidth() != canvas.winfo_width():
					# Update the canvas's width to fit the inner frame.
					canvas.config(width=interior.winfo_reqwidth())
			interior.bind('<Configure>', _configure_interior)

			def _configure_canvas(event):
				if interior.winfo_reqwidth() != canvas.winfo_width():
					# Update the inner frame's width to fill the canvas.
					canvas.itemconfigure(interior_id, width=canvas.winfo_width())
			canvas.bind('<Configure>', _configure_canvas)		
		