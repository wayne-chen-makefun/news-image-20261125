# World News in Brief — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/wayne-chen-makefun/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/wayne-chen-makefun/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

## What this is

The entry is a Python program that writes one 1024×1024 PNG, "World News in Brief": a newspaper-style front page summing up Wednesday 25 November 2026 — proposed US tariffs on 14 trading partners, the Houthi strike on Saudi Arabia, Ukrainian drones over Samara, Huawei's US conviction, the AI-stock selloff, Shenzhou 24's first foreign astronaut, and the Indonesia mine flood — every headline verified against Reuters and AP reports of the day.

## Run it

Python 3.13, standard library only:

```
python3 main.py
```

It writes `entry.png` into `$MAKEFUN_OUTPUT_DIR` (or `./output` when the
variable is unset). The picture is rendered at build time by
`generate_image.py` (Pillow) from the verified story data in
`news_data.py` and committed as `assets/entry.png`; `main.py` copies
those bytes unchanged, so every graded run produces byte-identical
output, offline, in well under a second.

## Sources

Every headline was checked against wire reporting published on
25 Nov 2026 — see [sources.md](sources.md) for the article list.

## Licence

MIT — see [LICENSE](LICENSE).

---
Entered on [make.fun](https://make.fun/)
