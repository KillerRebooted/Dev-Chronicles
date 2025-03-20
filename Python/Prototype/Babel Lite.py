from PIL import Image, ImageTk
import cv2, os, time
import customtkinter as ctk
import numpy as np

def center(win, screen_resolution, animation_time):

    x1, y1 = 0, 0

    while x1 != screen_resolution[0] or y1 != screen_resolution[1]:

        if x1 != screen_resolution[0]: x1 += screen_resolution[0]/(animation_time*10)
        if y1 != screen_resolution[1]: y1 += screen_resolution[1]/(animation_time*10)

        win.geometry(f"{int(x1)}x{int(y1)}")

        x2 = win.winfo_screenwidth()//2 - win.winfo_width()//2
        y2 = win.winfo_screenheight()//2 - win.winfo_height()//2

        win.geometry(f"+{x2}+{y2}")

        time.sleep(0.008)
        win.update()

def main():

    global frame

    frame = ctk.CTkFrame(win, bg_color="#1f1f1f", fg_color="#0f0f0f", width=0.1*w, height=0.1*h, corner_radius=50)
    frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    gen_img = ctk.CTkButton(frame, bg_color="#1f1f1f", text="Generate Image", command=click)
    gen_img.pack()

    win.mainloop()

def click():

    encode_img(r'D:\My Files\Coding Files\Python\Prototype\Test Image.jpeg')

    interpret_img(read_img())

def encode_img(path):

    img = Image.open(path)#.resize((1920, 1080)) # Can be many different formats.
    img = np.array(img)
    img = img[:, :, ::-1].copy()

    f = open("test.txt", "w+", encoding="utf-8")
    f.write(f"{len(img[0])}x{len(img)} ")

    image = ctk.CTkLabel(frame, text="", image=ctk.CTkImage(dark_image=Image.fromarray(img[:, :, ::-1][:1]), size=(1024, 1024)))
    image.pack()

    row_no=1

    for row in img:

        for pixel in row:

            for pixel_color in pixel:
                f.write(chr(pixel_color+1000))

        if row_no % 10 == 0:

            image.configure(image=ctk.CTkImage(dark_image=Image.fromarray(img[:, :, ::-1][:row_no]), size=(1024, 1024)))
            win.update()

        row_no += 1

    cv2.destroyAllWindows()

    f.close()

def read_img():

    f = open("test.txt", "r", encoding="utf-8")
    code = f.read().split()
    f.close()
    os.remove("test.txt")

    res = [int(i) for i in code[0].split("x")]
    code = code[1]

    img = []
    rgbs = []

    for index in range(0, len(code), 3):
        rgbs.append([ord(code[index])-1000, ord(code[index+1])-1000, ord(code[index+2])-1000])

        if len(rgbs) == res[0]:
            img.append(rgbs)
            rgbs = []

    img = np.uint8(img)
            
    return img

def interpret_img(img):

    image = ctk.CTkLabel(frame, text="", image=ctk.CTkImage(dark_image=Image.fromarray(img[:, :, ::-1]), size=(1024, 1024)))
    image.pack()

if __name__ == "__main__":

    win = ctk.CTk(fg_color="#121212")
    win.title("Babel Lite")
    win.geometry("0x0")

    w = win.winfo_screenwidth()
    h = win.winfo_screenheight()

    center(win, (w, h), 2)
    win.attributes('-fullscreen', True)

    main()

#for i in range(1000, 1000+256):
    #print(f"{i-1000}: '{chr(i)}'")