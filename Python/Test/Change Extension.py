from pathlib import Path
p = Path(r'C:\Users\rashm\OneDrive\Desktop\op.txt')
p.rename(p.with_suffix('.exe'))