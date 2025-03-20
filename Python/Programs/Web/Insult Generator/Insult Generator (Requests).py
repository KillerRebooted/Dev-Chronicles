
import requests

def insult(name):
    
    insult = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=text").text
    
    return f"{name.upper()}, {insult}"

if __name__ == "__main__":
    print(insult("Rick Astley"))