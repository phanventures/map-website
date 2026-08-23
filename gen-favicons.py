#!/usr/bin/env python3
"""Generate the mranhphan.com favicon set from the brand AP mark.

Source: brand/AP Icon.png (black A + orange P on white, heavy padding).
Trims to ink bounds, centers on a white rounded tile so the black A stays
legible on dark browser chrome, then emits every size.

    python3 gen-favicons.py
"""
import os
from PIL import Image, ImageChops, ImageDraw

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "brand", "AP Icon.png")
INSET, RADIUS = 0.16, 0.22

def trimmed_mark():
    im = Image.open(SRC).convert("RGB")
    diff = ImageChops.difference(im, Image.new("RGB", im.size, (255, 255, 255)))
    return im.crop(diff.convert("L").point(lambda v: 255 if v > 12 else 0).getbbox())

def icon(mark, size):
    canvas = Image.new("RGB", (size, size), (255, 255, 255))
    avail = int(size * (1 - INSET * 2))
    w, h = mark.size
    s = min(avail / w, avail / h)
    nw, nh = max(1, int(w * s)), max(1, int(h * s))
    canvas.paste(mark.resize((nw, nh), Image.LANCZOS), ((size - nw) // 2, (size - nh) // 2))
    canvas = canvas.convert("RGBA")
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * RADIUS), fill=255)
    canvas.putalpha(mask)
    return canvas

mark = trimmed_mark()
for name, px in [("favicon-16.png", 16), ("favicon-32.png", 32),
                 ("apple-touch-icon.png", 180), ("icon-192.png", 192), ("icon-512.png", 512)]:
    icon(mark, px).save(os.path.join(ROOT, name))
icon(mark, 256).save(os.path.join(ROOT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
print("favicons written from", os.path.relpath(SRC, ROOT))
