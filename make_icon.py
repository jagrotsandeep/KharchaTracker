from PIL import Image, ImageDraw, ImageFont
import os

sizes = {
    'mipmap-mdpi':     48,
    'mipmap-hdpi':     72,
    'mipmap-xhdpi':    96,
    'mipmap-xxhdpi':   144,
    'mipmap-xxxhdpi':  192,
}

for folder, size in sizes.items():
    path = f'app/src/main/res/{folder}'
    os.makedirs(path, exist_ok=True)

    img  = Image.new('RGB', (size, size), '#1a2035')
    draw = ImageDraw.Draw(img)

    # Circle background
    margin = size // 8
    draw.ellipse(
        [margin, margin, size-margin, size-margin],
        fill='#162447'
    )

    # Rupee symbol
    font_size = size // 2
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', font_size)
    except:
        font = ImageFont.load_default()

    text = '₹'
    bbox = draw.textbbox((0,0), text, font=font)
    tw   = bbox[2] - bbox[0]
    th   = bbox[3] - bbox[1]
    x    = (size - tw) // 2
    y    = (size - th) // 2 - size//10

    draw.text((x, y), text, fill='#00d4ff', font=font)

    img.save(f'{path}/ic_launcher.png')
    print(f'Created {path}/ic_launcher.png ({size}x{size})')

print('All icons created!')
