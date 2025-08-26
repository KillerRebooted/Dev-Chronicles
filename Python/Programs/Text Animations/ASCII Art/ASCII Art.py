import numpy as np
from PIL import Image
import cv2
from rembg import remove
import os
import time

os.system("cls")

ascii = r""" $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^. """

# Create a directory to store the frames
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Convert video to frames
def video_to_frames(video_path, output_dir):
    # Create the output directory
    create_directory(output_dir)

    # Open the video file
    vidcap = cv2.VideoCapture(video_path)
    
    if not vidcap.isOpened():
        print("Error: Could not open video file.")
        return

    frame_count = 0
    success, image = vidcap.read()

    while success:
        # Save the frame as a JPG image
        frame_filename = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, remove(image))
        
        # Read the next frame
        success, image = vidcap.read()
        frame_count += 1

        print(f"{frame_count} Frames Extracted", end="\r")
    
    vidcap.release()
    print(f"Finished. Extracted {frame_count} frames.")

def ascii_art(image):
    try:
        img = Image.open(image)
    except FileNotFoundError:
        print(f"Error: The file at {image} was not found.")
        exit()

    gray_img = img.convert("L")
    resized_gray_img = gray_img.resize((120, 50))
    gray_array = np.array(resized_gray_img)

    for r in range(gray_array.shape[0]):
        for c in range(gray_array.shape[1]):
            pixel = gray_array[r, c]
            ascii_char = ascii[int((pixel/256)*len(ascii))%len(ascii)]
            print(ascii_char, end="")
        print()

video_file = rf"{__file__.removesuffix(os.path.basename(__file__))}\test.mp4"
output_folder = rf"{__file__.removesuffix(os.path.basename(__file__))}\Data"

if not os.path.exists(output_folder):
    video_to_frames(video_file, output_folder)

os.system("cls")

for image in os.listdir(output_folder):
    print(f"\x1b[{70}A\r", end="")
    ascii_art(image=os.path.join(output_folder, image))
    time.sleep(0.02)