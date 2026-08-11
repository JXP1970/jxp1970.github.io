"""Erzeugt das og:image (1200x630) fuer jxp1970.github.io.

Farben und Schriften sind aus index.html uebernommen, damit die Vorschau-Kachel
wie die Seite selbst aussieht.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG      = '#f4f1ea'   # --bg
CARD    = '#fffdf8'   # --card
INK     = '#2b2924'   # --ink
MUTED   = '#6f6a60'   # --muted
LINE    = '#e4ded1'   # --line
ACCENT  = '#3b6d43'   # --accent
SOFT    = '#e7efe4'   # --accent-soft

F = os.path.join(os.environ['WINDIR'], 'Fonts')
def font(name, size): return ImageFont.truetype(os.path.join(F, name), size)

serif_b  = font('georgiab.ttf', 74)
sans     = font('segoeui.ttf', 27)
sans_b   = font('segoeuib.ttf', 24)
pill_f   = font('segoeuib.ttf', 19)
emoji_f  = font('seguiemj.ttf', 76)

img = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(img)

# Akzentstreifen oben
d.rectangle([0, 0, W, 8], fill=ACCENT)

# ── Linke Spalte ────────────────────────────────────────────────────────────
x = 84

# Pill "MEINE APPS"
label = 'M E I N E   A P P S'
tw = d.textlength(label, font=pill_f)
d.rounded_rectangle([x, 108, x + tw + 44, 108 + 44], radius=22, fill=SOFT)
d.text((x + 22, 108 + 22), label, font=pill_f, fill=ACCENT, anchor='lm')

# Ueberschrift
d.text((x, 196), 'Kleine Helfer,', font=serif_b, fill=INK)
d.text((x, 286), 'ein Ort',        font=serif_b, fill=INK)

# Unterzeile
d.text((x, 408), '15 kleine Web-Apps – sie laufen direkt', font=sans, fill=MUTED)
d.text((x, 446), 'im Browser, nichts zu installieren.',    font=sans, fill=MUTED)

# URL
d.text((x, 516), 'jxp1970.github.io', font=sans_b, fill=ACCENT)

# ── Rechte Spalte: Kachelraster ─────────────────────────────────────────────
TILE, GAP, COLS = 128, 20, 3
gw = COLS * TILE + (COLS - 1) * GAP
gx = W - 84 - gw
gy = (H - (2 * TILE + GAP)) // 2 + 4

emojis = ['\U0001F54A', '\U0001F3BC', '\U0001F5E3',
          '\U0001F3D7', '\U0001F5C2', '\U0001F310']

for i, e in enumerate(emojis):
    cx = gx + (i % COLS) * (TILE + GAP)
    cy = gy + (i // COLS) * (TILE + GAP)
    d.rounded_rectangle([cx, cy, cx + TILE, cy + TILE],
                        radius=28, fill=CARD, outline=LINE, width=2)
    d.text((cx + TILE // 2, cy + TILE // 2 + 4), e,
           font=emoji_f, embedded_color=True, anchor='mm')

out = sys.argv[1]
img.save(out, 'PNG', optimize=True)
print(f'{out}  {img.size[0]}x{img.size[1]}  {os.path.getsize(out)/1024:.0f} KB')
