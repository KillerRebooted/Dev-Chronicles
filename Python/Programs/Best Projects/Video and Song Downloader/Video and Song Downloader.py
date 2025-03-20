import tkinter as tk
from tkinter.ttk import Progressbar
import os

clear = lambda: os.system('cls')

try:

	from pytube import YouTube, Playlist
	from pytube import Search as search
	from pytube.cli import on_progress
	import requests

except:
	
	os.system("pip install pytube")
	os.system("pip install requests")

	from pytube import YouTube, Playlist
	from pytube import Search as search
	from pytube.cli import on_progress
	import requests

clear()

def Video_Options():

	def video_hover_func(i):

		global video_selected

		buttons[i].configure(bg = "#0062ff")

		video_selected = tk.Label(text = f"Channel Name: {video_author[i]} | Publish Date: {video_publish_date[i]} {video_publish_month[i]}, {video_publish_year[i]} | Views: {video_views[i]} | Video Length: {video_lengths[i]}", font = ("Courier", 12, "bold"))
		video_selected.pack()

	def video_leave_func(i):

		buttons[i].configure(bg = "white")

		video_selected.destroy()

	if Search.get(1.0, "end-1c") in ["", "What Videos/Songs do you want to Download?"]:

		return

	Videos = Search.get(1.0, "end-1c").split("\n")

	Videos_Selected = []
	playlists_selected = []

	if Value.get() == "Video":

		download_video = True

	else:

		download_video = False

	for Video in Videos:

		for widget in win.winfo_children():

			widget.destroy()

		if Video == "":

			continue

		if ("list" in Video) and (("playlist?" in Video) or ("watch?v" in Video)) and ("https://www.youtube.com/" in Video):

			playlists_selected.append(Video)
			
		elif ("/sp" in Video.strip()):

			playlists_selected.append(Video.removeprefix("/sp").strip())

		else:

			progress_bar = Progressbar(win, length = 500, mode = 'determinate')
			progress_bar.pack(pady = 5)

			videos = search(Video).results[:10]

			total_loading = len(videos)*5
			loading = 0

			video_titles = []
			video_lengths = []

			video_publish_dates = []
			video_views = []
			video_author = []

			for video in videos:

				video_titles.append(video.title)
				loading += 1
				progress_bar['value'] = loading/total_loading * 100
				
				try:
					Percentage.destroy()
				except:
					pass

				Percentage = tk.Label(text = f"{int(loading/total_loading*100)}%")
				Percentage.configure(background = "#121212", foreground = "#fff", font = ("Courier", 18, "bold"))
				Percentage.pack()
				
				win.update()
				
				video_lengths.append(video.length)
				loading += 1
				progress_bar['value'] = loading/total_loading * 100
				
				Percentage.destroy()
				Percentage = tk.Label(text = f"{int(loading/total_loading*100)}%")
				Percentage.configure(background = "#121212", foreground = "#fff", font = ("Courier", 18, "bold"))
				Percentage.pack()
				
				win.update()

				video_publish_dates.append(str(video.publish_date))
				loading += 1
				progress_bar['value'] = loading/total_loading * 100

				Percentage.destroy()
				Percentage = tk.Label(text = f"{int(loading/total_loading*100)}%")
				Percentage.configure(background = "#121212", foreground = "#fff", font = ("Courier", 18, "bold"))
				Percentage.pack()

				win.update()

				video_views.append(f"{video.views:,}")
				loading += 1
				progress_bar['value'] = loading/total_loading * 100
				
				Percentage.destroy()
				Percentage = tk.Label(text = f"{int(loading/total_loading*100)}%")
				Percentage.configure(background = "#121212", foreground = "#fff", font = ("Courier", 18, "bold"))
				Percentage.pack()

				win.update()

				video_author.append(video.author)
				loading += 1
				progress_bar['value'] = loading/total_loading * 100

				Percentage.destroy()
				Percentage = tk.Label(text = f"{int(loading/total_loading*100)}%")
				Percentage.configure(background = "#121212", foreground = "#fff", font = ("Courier", 18, "bold"))
				Percentage.pack()

				win.update()
			
			video_lengths = [f"{l//3600:02}:{(l%3600)//60:02}:{(l%3600)%60:02}" for l in video_lengths]

			months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

			video_publish_date = []
			video_publish_month = []
			video_publish_year = []

			for date in video_publish_dates:
	
				video_publish_date.append(date[8:10])
				video_publish_month.append(months[int(date[5:7])-1])
				video_publish_year.append(date[:4])

			progress_bar.destroy()
			Percentage.destroy()

			buttons = []

			def Video_Selected(i):

				Videos_Selected.append(f"https://www.youtube.com/watch?v={videos[i].video_id}")

			for i in range(len(videos)):

				var = tk.IntVar()
				btn = tk.Button(text = video_titles[i], height = int(win.winfo_screenheight()/432), width = int(win.winfo_screenwidth()/15.36), bg = "white", activebackground = "#4089ff", command = lambda i=i: [var.set(1), Video_Selected(i)])
				btn.bind("<Enter>", lambda e, i=i: video_hover_func(i))
				btn.bind("<Leave>", lambda e, i=i: video_leave_func(i))
				btn.configure(font = ("Courier", 18, "bold"))
				btn.pack(pady = 3)

				buttons.append(btn)
			
			win.wait_variable(var)

	win.destroy()

	if Value.get() == "Video":

		print("Separate Videos:\n")

	else:

		print("Separate Audios:\n")

	for Video in Videos_Selected:

		video_download_location = f"{current_file_loc}Videos and Songs\\Unlisted Downloads"

		if not os.path.exists(video_download_location):
	
			os.mkdir(video_download_location)

		url = YouTube(Video, on_progress_callback = on_progress)

		if not download_video:

			video = url.streams.filter(only_audio = True).first()
			video_extension = "mp3"

		else:

			video = url.streams.filter(only_audio = False).get_highest_resolution()
			video_extension = "mp4"

		Invalid = ["<", ">", ":", '"', "\\", "|", "/", "?", "*"]

		New_File_Name = ""

		for i in url.title:

			if not i in Invalid:

				New_File_Name += i

		File_Name = New_File_Name

		print(f"Downloading {File_Name}...")

		video.download(video_download_location, filename = f"{File_Name}.{video_extension}")
		print()

	print("\n\nPlaylists:\n")

	for playlist in playlists_selected:

		if "youtube" in playlist:

			playlist_to_download = Playlist(playlist)

			playlist_title = playlist_to_download.title

			Invalid = ["<", ">", ":", '"', "\\", "|", "/", "?", "*"]

			New_Playlist_Title = ""
	
			for i in playlist_title:
	
				if not i in Invalid:
	
					New_Playlist_Title += i
	
			playlist_title = New_Playlist_Title

			if not os.path.exists(f"{current_file_loc}Videos and Songs\\YouTube Playlists\\"):
	
				os.mkdir(f"{current_file_loc}Videos and Songs\\YouTube Playlists\\")
				os.mkdir(f"{current_file_loc}Videos and Songs\\YouTube Playlists\\{playlist_title}")

			elif not os.path.exists(f"{current_file_loc}Videos and Songs\\YouTube Playlists\\{playlist_title}"):

				os.mkdir(f"{current_file_loc}Videos and Songs\\YouTube Playlists\\{playlist_title}")

			playlist_download_location = f"{current_file_loc}Videos and Songs\\YouTube Playlists\\{playlist_title}"

			print(f"Downloading {playlist_title}\n")
	
			for Video in playlist_to_download:
	
				url = YouTube(Video, on_progress_callback = on_progress)
	
				if not download_video:
	
					video = url.streams.filter(only_audio = True).first()
					video_extension = "mp3"
	
				else:
	
					video = url.streams.filter(only_audio = False).get_highest_resolution()
					video_extension = "mp4"
	
				New_File_Name = ""
	
				for i in url.title:
	
					if i not in Invalid:
	
						New_File_Name += i
	
				File_Name = New_File_Name
	
				print(f"Downloading {File_Name} from Youtube Playlist: {playlist_title}...")
	
				video.download(f"{playlist_download_location}", filename = f"{File_Name}.{video_extension}")
	
				print()
	
			print(f"{playlist_title} Playlist Downloaded\n\n\n")
			print()

		else:

			with open(f"{__file__.removesuffix(os.path.basename(__file__))}{playlist}.txt") as f:
				songs = f.readlines()

			songs_to_download = []
			songs_artists =[]
				
			for i in songs:
				url = requests.get(i.removesuffix("\n")).text

				start_song = "<title>"
				j = url.find(start_song)
				song_to_download = url[j + len(start_song) : j + len(start_song) + url[j+len(start_song) : j+len(start_song)+200].index(' - song') ]

				start_author = "song and lyrics by "
				k = url.find(start_author)
				song_artists = url[k + len(start_author) : k + len(start_author) + url[k+len(start_author) : k+len(start_author)+200].index(' |') ]

				song_to_download = song_to_download.replace("&amp;", "&").replace("&#x27;", "'").replace("&quot;", '"')
				song_artists = song_artists.replace("&amp;", "&").replace("&#x27;", "'").replace("&quot;", '"')

				songs_to_download.append(song_to_download)
				songs_artists.append(song_artists)
			
			playlist_title = playlist

			Invalid = ["<", ">", ":", '"', "\\", "|", "/", "?", "*"]

			New_Playlist_Title = ""
	
			for i in playlist_title:
	
				if i not in Invalid:
	
					New_Playlist_Title += i
	
			playlist_title = New_Playlist_Title

			if not os.path.exists(f"{current_file_loc}Videos and Songs\\Spotify Playlists\\"):
	
				os.mkdir(f"{current_file_loc}Videos and Songs\\Spotify Playlists\\")
				os.mkdir(f"{current_file_loc}Videos and Songs\\Spotify Playlists\\{playlist_title}")

			elif not os.path.exists(f"{current_file_loc}Videos and Songs\\Spotify Playlists\\{playlist_title}"):

				os.mkdir(f"{current_file_loc}Videos and Songs\\Spotify Playlists\\{playlist_title}")

			song_download_location = f"{current_file_loc}Videos and Songs\\Spotify Playlists\\{playlist_title}"

			print(f"Downloading {playlist_title}...\n")

			for Video in songs_to_download:

				video = search(f"{Video} by {songs_artists[songs_to_download.index(Video)]}").results[0]

				url = YouTube(f"https://www.youtube.com/watch?v={video.video_id}", on_progress_callback = on_progress)

				if not download_video:

					video = url.streams.filter(only_audio = True).first()
					video_extension = "mp3"

				else:

					video = url.streams.filter(only_audio = False).get_highest_resolution()
					video_extension = "mp4"

				Invalid = ["<", ">", ":", '"', "\\", "|", "/", "?", "*"]

				New_File_Name = ""

				for i in songs_to_download[songs_to_download.index(Video)]:

					if i not in Invalid:

						New_File_Name += i

				File_Name = New_File_Name

				num = songs_to_download.index(Video)+1

				if num < 10:

					num = f"000{num}"

				elif num < 100:

					num = f"00{num}"

				elif num < 1000:

					num = f"0{num}"
	
				if not any(num in filename for filename in os.listdir(song_download_location)):
					print(f"Downloading {File_Name} from Spotify Playlist: {playlist_title}...")
					video.download(f"{song_download_location}", filename = f"{num} {File_Name}.{video_extension}")

					print()
	
			print(f"{playlist_title} Playlist Downloaded\n\n\n")
			print()

def main():

	global win, Search, File_Selection, current_file_loc, Value

	def focus_in(event):

		if Search.cget("fg") == "#9e8475":

			Search.delete(1.0, "end")

		Search.configure(fg = "#fff")

	def focus_out(event):

		if Search.get(1.0, "end-1c") == "":

			Search.insert(tk.END, "What Videos/Songs do you want to Download?")
			Search.configure(fg = "#9e8475")

	current_file_loc = f"{__file__.removesuffix(os.path.basename(__file__))}"

	if not os.path.exists(f"{current_file_loc}Videos and Songs"):
	
		os.mkdir(f"{current_file_loc}Videos and Songs")

	win = tk.Tk()
	win.title("Video and Song Downloader")
	win.configure(background = "#121212")
	win.attributes("-fullscreen", True)
	win.bind("<Escape>", lambda event: win.destroy())
	
	Text = tk.Label(text = "Type the Videos/Songs to be Downloaded in Different Lines")
	Text.configure(background = "#121212", foreground = "#fff", font = ("Courier", 18, "bold"))
	Text.pack()

	Value = tk.StringVar()
	Value.set("Audio")

	File_Selection = tk.OptionMenu(win, Value, "Audio", "Video")
	File_Selection.pack()
	
	Search = tk.Text()
	Search.bind("<FocusIn>", focus_in)
	Search.bind("<FocusOut>", focus_out)
	Search.insert(tk.END, "What Videos/Songs do you want to Download?")
	Search.configure(font = ("Times New Roman", 14, "bold"), background = "#121212", fg="#9e8475")
	Search.pack()

	Continue = tk.Button(text = "Continue", height = 2, width = 20, activebackground = "#4089ff", command = Video_Options)
	Continue.configure(font = ("Courier", 12, "bold"))
	Continue.pack()
	
	win.mainloop()

if __name__ == "__main__":

	main()
