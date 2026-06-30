import re

file_path = 'c:/NAB TRAVELS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r'<img src="[^"]*" alt="Royal Muscat Tour">', r'<img src="video/image/muscutro.jpg" alt="Royal Muscat Tour">'),
    (r'<img src="[^"]*" alt="Tropical Salalah Escape">', r'<img src="video/image/tropical.jpg" alt="Tropical Salalah Escape">'),
    (r'<img src="[^"]*" alt="Magical Desert Safari">', r'<img src="video/image/magical.jpg" alt="Magical Desert Safari">'),
    (r'<img src="[^"]*" alt="Mountain Grand Canyon">', r'<img src="video/image/mountain.jpg" alt="Mountain Grand Canyon">')
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Images updated successfully!")
