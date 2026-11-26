"""Verified world-news stories of Wednesday, 25 November 2026.

Every headline and summary below was checked against wire reporting
published on 25 Nov 2026 (Reuters and The Associated Press).  See
sources.md for the article list.  No story is included that was not
found in a source that was actually opened during research.
"""

DATE_LINE = "Wednesday, November 25, 2026"

LEAD = {
    "tag": "TRADE - TOP STORY",
    "headline": "US Proposes New Tariffs on 14 Trading Partners",
    "summary": (
        "Washington's Section 301 probe targets 'structural excess "
        "industrial capacity,' with the highest new duties aimed at China; "
        "the EU, Japan, South Korea and Taiwan are also listed. A comment "
        "period could push them into January."
    ),
    "source": "Reuters",
}

STORIES = [
    {
        "tag": "MIDDLE EAST",
        "headline": "Houthis Attack Saudi Refinery and Riyadh District",
        "summary": (
            "Houthis struck the Ras Tanura refinery and Riyadh's financial "
            "district; Saudi defences downed four drones, wounding 11."
        ),
        "source": "Reuters",
    },
    {
        "tag": "UKRAINE WAR",
        "headline": "Ukrainian Drones Hit Samara; Putin Vows Retaliation",
        "summary": (
            "Drones hit industrial sites in Russia's Samara region - 145 "
            "downed, one killed - as Putin pledged retaliation for Kyiv's "
            "refinery campaign."
        ),
        "source": "Reuters",
    },
    {
        "tag": "BUSINESS & LAW",
        "headline": "US Jury Convicts Huawei of Stealing Trade Secrets",
        "summary": (
            "A New York jury found the Chinese tech giant guilty of "
            "conspiracy to steal trade secrets and bank fraud after a "
            "two-month trial."
        ),
        "source": "Reuters / AP",
    },
    {
        "tag": "MARKETS",
        "headline": "AI Selloff Hammers Asia; Nvidia Slides 5.9%",
        "summary": (
            "South Korea's KOSPI plunged about 6% and Taiwan fell 5% as the "
            "AI rally unravelled. The Dow closed above 50,000 for the "
            "first time."
        ),
        "source": "Reuters / AP",
    },
    {
        "tag": "SPACE",
        "headline": "Shenzhou 24 Takes First Foreign Astronaut to Tiangong",
        "summary": (
            "Pakistani astronaut Muhammad Zeeshan Ali flew with Tang "
            "Hongbo and Wu Yi - the first foreign crew member on China's "
            "space station."
        ),
        "source": "Associated Press",
    },
    {
        "tag": "INDONESIA",
        "headline": "Flood at Gold Mine Kills 9, Leaves 17 Trapped",
        "summary": (
            "Rescuers raced to reach miners trapped after flooding hit an "
            "unauthorized gold mine in Indonesia; at least nine are dead."
        ),
        "source": "Associated Press",
    },
]

FOOTER_SOURCES = "Sources: Reuters - The Associated Press"
FOOTER_NOTE = "Every headline verified against wire reports published on 25 Nov 2026."
