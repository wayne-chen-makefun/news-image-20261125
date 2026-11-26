#!/usr/bin/env python3
"""Render assets/entry.png: one 1024x1024 infographic that sums up the
world news of Wednesday, 25 November 2026.

This script is the build-time generator.  It is run once by the author
(with Pillow available) to produce the committed asset
``assets/entry.png``.  The graded entrypoint, ``main.py``, uses only
the Python standard library and copies that asset to the output
directory, so the graded run needs no network, no fonts and no
third-party packages, and always writes identical bytes.

Layout: a newspaper front page.  A masthead with the date, one lead
story across the full width, then the remaining six stories in a
two-column grid, each with a section tag, a bold headline and a
one-to-two-line factual summary, and a footer crediting the sources.
"""

from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFont

import news_data

SIZE = 1024
MARGIN = 52
INK = (26, 26, 40)
PAPER = (247, 243, 234)
NAVY = (18, 32, 64)
ACCENT = (165, 32, 32)
GREY = (96, 96, 104)
RULE = (26, 26, 40)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
SERIF_BOLD = str(FONT_DIR / "DejaVuSerif-Bold.ttf")
SANS = str(FONT_DIR / "DejaVuSans.ttf")
SANS_BOLD = str(FONT_DIR / "DejaVuSans-Bold.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured with the real font."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def centered(draw, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((SIZE - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def draw_story(draw, x, y, width, story, headline_size, summary_size,
               headline_lines_max=3, summary_lines_max=4):
    """Draw one story block; return the y just below it."""
    tag_f = font(SANS_BOLD, 19)
    draw.text((x, y), story["tag"], font=tag_f, fill=ACCENT)
    y += 26
    head_f = font(SANS_BOLD, headline_size)
    for line in wrap(draw, story["headline"], head_f, width)[:headline_lines_max]:
        draw.text((x, y), line, font=head_f, fill=INK)
        y += int(headline_size * 1.16)
    y += 6
    sum_f = font(SANS, summary_size)
    for line in wrap(draw, story["summary"], sum_f, width)[:summary_lines_max]:
        draw.text((x, y), line, font=sum_f, fill=(52, 52, 62))
        y += int(summary_size * 1.22)
    y += 4
    src_f = font(SANS, 15)
    draw.text((x, y), "- " + story["source"], font=src_f, fill=GREY)
    return y + 21


def main():
    img = Image.new("RGB", (SIZE, SIZE), PAPER)
    draw = ImageDraw.Draw(img)
    width = SIZE - 2 * MARGIN

    # --- Masthead ---------------------------------------------------
    y = 22
    centered(draw, y, "T H E   W O R L D   I N   O N E   I M A G E",
             font(SANS_BOLD, 19), ACCENT)
    y = 48
    centered(draw, y, "World News in Brief", font(SERIF_BOLD, 54), NAVY)
    y = 114
    centered(draw, y, news_data.DATE_LINE, font(SANS, 24), GREY)
    y = 150
    draw.line([(MARGIN, y), (SIZE - MARGIN, y)], fill=RULE, width=5)
    draw.line([(MARGIN, y + 8), (SIZE - MARGIN, y + 8)], fill=RULE, width=2)

    # --- Lead story --------------------------------------------------
    y = 172
    y = draw_story(draw, MARGIN, y, width, news_data.LEAD,
                   headline_size=35, summary_size=21,
                   headline_lines_max=2, summary_lines_max=3)
    y += 0
    draw.line([(MARGIN, y), (SIZE - MARGIN, y)], fill=RULE, width=2)
    y += 14

    # --- Grid: two columns, three rows -------------------------------
    col_w = (width - 36) // 2
    col_x = [MARGIN, MARGIN + col_w + 36]
    row_starts = []
    stories = news_data.STORIES
    for row in range(3):
        row_y = y
        row_starts.append(row_y)
        bottoms = []
        for col in range(2):
            story = stories[row * 2 + col]
            bottoms.append(draw_story(draw, col_x[col], row_y, col_w, story,
                                      headline_size=24, summary_size=18,
                                      headline_lines_max=3, summary_lines_max=3))
        y = max(bottoms) + 2
        if row < 2:
            draw.line([(MARGIN, y), (SIZE - MARGIN, y)], fill=(196, 190, 174), width=1)
            y += 10

    # --- Footer -------------------------------------------------------
    footer_y = SIZE - 74
    draw.line([(MARGIN, footer_y), (SIZE - MARGIN, footer_y)], fill=RULE, width=3)
    centered(draw, footer_y + 12, news_data.FOOTER_SOURCES, font(SANS_BOLD, 20), NAVY)
    centered(draw, footer_y + 40, news_data.FOOTER_NOTE, font(SANS, 17), GREY)

    out = Path(__file__).resolve().parent / "assets" / "entry.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, format="PNG", optimize=True)
    print("wrote", out, out.stat().st_size, "bytes; content bottom at y =", y)


if __name__ == "__main__":
    main()
