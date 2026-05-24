from PIL import Image, ImageDraw, ImageFont
import os

sizes = {
    'mipmap-mdpi':    48,
    'mipmap-hdpi':    72,
    'mipmap-xhdpi':   96,
    'mipmap-xxhdpi':  144,
    'mipmap-xxxhdpi': 192,
}

def make_icon(size):
    img  = Image.new('RGBA', (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)

    # Rounded rectangle background — gradient feel
    r = size // 5
    draw.rounded_rectangle([0, 0, size, size],
        radius=r, fill='#1a2035')

    # Inner glow circle
    pad = size // 8
    draw.ellipse([pad, pad, size-pad, size-pad],
        fill='#162447', outline='#00d4ff',
        width=max(2, size//30))

    # BIG Rupee symbol
    font_size = int(size * 0.52)
    try:
        font = ImageFont.truetype(
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
            font_size)
    except:
        font = ImageFont.load_default()

    text = '₹'
    bbox = draw.textbbox((0,0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (size - tw) // 2 - bbox[0]
    ty = (size - th) // 2 - bbox[1] - size//15

    # Shadow
    draw.text((tx+2, ty+2), text,
        fill='#0a0f1e', font=font)
    # Main text
    draw.text((tx, ty), text,
        fill='#00d4ff', font=font)

    # "KT" small badge bottom right
    badge_size = size // 4
    bx = size - badge_size - size//12
    by = size - badge_size - size//12
    draw.rounded_rectangle(
        [bx, by, bx+badge_size, by+badge_size],
        radius=badge_size//4, fill='#00d4ff')

    try:
        sf = int(badge_size * 0.5)
        sf_font = ImageFont.truetype(
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', sf)
    except:
        sf_font = ImageFont.load_default()

    draw.text((bx + badge_size//2 - sf//2,
               by + badge_size//2 - sf//2),
              'K', fill='#1a2035', font=sf_font)

    return img

for folder, size in sizes.items():
    path = f'app/src/main/res/{folder}'
    os.makedirs(path, exist_ok=True)
    icon = make_icon(size)
    icon.save(f'{path}/ic_launcher.png')
    print(f'✅ {path}/ic_launcher.png ({size}x{size})')

print('\nSab icons ready!')
