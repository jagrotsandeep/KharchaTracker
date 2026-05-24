from PIL import Image
import os

src = 'icon_source.png'
sizes = {
    'app/src/main/res/mipmap-mdpi':    48,
    'app/src/main/res/mipmap-hdpi':    72,
    'app/src/main/res/mipmap-xhdpi':   96,
    'app/src/main/res/mipmap-xxhdpi':  144,
    'app/src/main/res/mipmap-xxxhdpi': 192,
}

img = Image.open(src).convert('RGBA')
for folder, size in sizes.items():
    os.makedirs(folder, exist_ok=True)
    resized = img.resize((size, size), Image.LANCZOS)
    resized.save(f'{folder}/ic_launcher.png')
    print(f'✅ {size}x{size} done!')

print('\nSab icons ready!')
