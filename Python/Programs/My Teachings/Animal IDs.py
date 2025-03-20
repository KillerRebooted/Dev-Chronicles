datastring = """
Animals {
    idAnimal
    nameAnimal
    animalk45lil69lhfr5942lk[name="Jazz"]
    animal6ljkjh[name="Pinky"]
    animal595s422d1252g55[name="Steven"]
    animalko5854hg[name="David"]
    animalko5854hg[name="Oty"]
    animalko5854hg[name="Dan"]
}
"""

import re

ID = re.search(r'(?<=animal)(.*?)(?=\[)', datastring).group(1)

print(ID)
