import easyocr, os
import pyautogui, time

loc = os.path.dirname(os.path.realpath(__file__))

reader = easyocr.Reader(['en'])

result = reader.readtext(f'{loc}\\img.png')

data = []

for detection in result:
    data.append(detection[1])

print(data)
#pyautogui.write(" ".join(data), interval=0.00)

"""import whisper

model = whisper.load_model("base")
result = model.transcribe(f"{loc}/aud.mp3")

pyautogui.write(result["text"], interval=0.00)"""

'''text = """that requires a combination of academic qualifications, practical experience, strategic networking, continuous learning, and professional development. By leveraging internships, networking opportunities, conducting thorough research, tailoring job applications, mastering interview skills, and pursuing advanced education and certifications, aspiring professionals can position themselves for success in the competitive landscape of banking careers. With dedication, perseverance, and a proactive mindset, individuals can navigate the complexities of the banking industry, seize opportunities for growth and advancement, and embark on a rewarding and fulfilling career path in finance."""

time.sleep(2)

pyautogui.write(text, interval=0)'''