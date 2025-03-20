from PIL import Image
import pyautogui
import pytesseract
import os

#pyautogui.PAUSE = 0

def scan_img(solution=False, sudoku_solution=None):

    # get image
    filepath = fr"{os.path.dirname(os.path.abspath(__file__))}\Sudoku.png"
    img = Image.open(filepath)

    try:
        sudoku = pyautogui.locateOnScreen(img)
    except:
        print("Warning: Couldn't locate Image on Screen. Won't be able to Solve on Screen.")

        if solution:
            return

    # get width and height
    box_width = img.width/9
    box_height = img.height/9

    final_result = ""

    if not solution:
        print("Scanning Image...")

    first_iter = True

    for r in range(9):
        for c in range(9):

            if not solution:

                picture = img.crop((int(c*box_width), int(r*box_height), int(c*box_width+box_width), int(r*box_height+box_height)))

                pytesseract.pytesseract.tesseract_cmd =r'C:\Users\Shreyas Nair\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

                result = pytesseract.image_to_string(picture, config="--psm 6")[0:1]

                final_result += result if (result.isdigit()) else "."

            else:

                if first_iter:
                    pyautogui.click(sudoku[0] + c*box_width + box_width/2, sudoku[1] + r*box_height + box_height/2)

                    first_iter = False

                pyautogui.click(sudoku[0] + c*box_width + box_width/2, sudoku[1] + r*box_height + box_height/2)

                pyautogui.write(str(sudoku_solution[r][c]))

    return final_result

if __name__ == "__main__":
    
    print(scan_img())