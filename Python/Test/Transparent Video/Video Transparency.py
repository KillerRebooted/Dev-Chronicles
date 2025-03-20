import cv2
import numpy as np
import os
import tkinter as tk
from PIL import Image, ImageTk
from ffpyplayer.player import MediaPlayer
import time

# Get absolute video path
cur_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(cur_dir, "Mahoraga.mp4")

# Open video file
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Start Tkinter root window
root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.attributes("-alpha", 0.1)  # Transparency effect
root.configure(bg="black")

# Create Label for video display
video_label = tk.Label(root, bg="black")
video_label.pack(fill=tk.BOTH, expand=True)

frame_count = 0  # Track frames
audio_started = False  # Track if audio has started
audio_finished = False  # Track if audio has finished
start_time = time.time()  # Get the starting time

player = None  # Player will be initialized after 1 second

# Get video FPS and set frame delay for ultra-fast playback
fps = cap.get(cv2.CAP_PROP_FPS)
frame_delay = int((1000 / fps) * 0.05)  # 95% faster playback

def update_frame():
    global frame_count, player, audio_started, audio_finished

    ret, frame = cap.read()
    if not ret:
        # Stop video and close window when video ends
        cap.release()
        if player:
            player.close_player()
        root.destroy()
        return

    frame_count += 1

    # Skip every alternate frame to speed up playback
    if frame_count % 2 == 0:
        root.after(1, update_frame)  # Minimal delay to maintain loop
        return

    # Start audio playback after 1 second
    if not audio_started and time.time() - start_time >= 1:
        player = MediaPlayer(video_path)
        audio_started = True

    # Sync audio but stop requesting frames if audio has finished
    if player and not audio_finished:
        audio_frame, val = player.get_frame()
        if val == "eof":  # Audio finished
            player.close_player()
            audio_finished = True  # Prevent restarting audio

    # Apply transparency effect
    alpha = 1  # Transparency level
    frame = frame.astype(np.float32) / 255.0
    background = np.zeros_like(frame)
    frame = cv2.addWeighted(frame, alpha, background, 1 - alpha, 0)
    frame = (frame * 255).astype(np.uint8)

    # Convert frame to Tkinter-compatible format
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA))
    img = ImageTk.PhotoImage(img)

    # Update video label
    video_label.configure(image=img)
    video_label.image = img

    # Schedule next frame update
    root.after(max(1, frame_delay), update_frame)

# Start video loop
update_frame()

# Run Tkinter loop
root.mainloop()

# Cleanup
cv2.destroyAllWindows()