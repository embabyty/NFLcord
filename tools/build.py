#!/usr/bin/env python3
"""Generate the 32 NFLcord Vencord themes from official team color data.

Run:  python tools/build.py
Output: themes/<slug>.theme.css (one per NFL team)
"""
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "themes"

# NOTE: logo URLs point at this repo on GitHub (raw.githubusercontent.com is on
# Vencord's image allowlist). LOGO_BRANCH must match the default branch,
# otherwise the home-button logos will not resolve.
LOGO_BRANCH = "vencord"
LOGO_BASE = f"https://raw.githubusercontent.com/embabyty/NFLcord/{LOGO_BRANCH}/assets/logos"

# Channel-list background = team tint mixed into Discord's sidebar base.
# Kept subtle on purpose so channel names stay readable everywhere.
SIDEBAR_DARK_BASE = "#2B2D31"
SIDEBAR_LIGHT_BASE = "#F2F3F5"
SIDEBAR_DARK_RATIO = 0.22
SIDEBAR_LIGHT_RATIO = 0.24

# name, slug, abbr, division, primary, primaryName, secondary, secondaryName,
# accent (main interactive color), link (link/mention base color), tint override
TEAMS = [
    dict(name="Arizona Cardinals", slug="arizona-cardinals", abbr="ARI", division="NFC West",
         primary="#97233F", primaryName="Cardinal Red", secondary="#FFB612", secondaryName="Desert Gold",
         accent="#97233F", link="#FFB612"),
    dict(name="Atlanta Falcons", slug="atlanta-falcons", abbr="ATL", division="NFC South",
         primary="#A71930", primaryName="Red", secondary="#000000", secondaryName="Black",
         accent="#A71930", link="#A5ACAF", linkName="Silver"),
    dict(name="Baltimore Ravens", slug="baltimore-ravens", abbr="BAL", division="AFC North",
         primary="#241773", primaryName="Purple", secondary="#9E7C0C", secondaryName="Metallic Gold",
         accent="#241773", link="#9E7C0C"),
    dict(name="Buffalo Bills", slug="buffalo-bills", abbr="BUF", division="AFC East",
         primary="#00338D", primaryName="Royal Blue", secondary="#C60C30", secondaryName="Red",
         accent="#00338D", link="#C60C30"),
    dict(name="Carolina Panthers", slug="carolina-panthers", abbr="CAR", division="NFC South",
         primary="#0085CA", primaryName="Panther Blue", secondary="#101820", secondaryName="Black",
         accent="#0085CA", link="#BFC0BF", linkName="Silver"),
    dict(name="Chicago Bears", slug="chicago-bears", abbr="CHI", division="NFC North",
         primary="#0B162A", primaryName="Midnight Navy", secondary="#C83803", secondaryName="Burnt Orange",
         accent="#C83803", link="#C83803"),
    dict(name="Cincinnati Bengals", slug="cincinnati-bengals", abbr="CIN", division="AFC North",
         primary="#FB4F14", primaryName="Orange", secondary="#000000", secondaryName="Black",
         accent="#FB4F14", link="#FB4F14"),
    dict(name="Cleveland Browns", slug="cleveland-browns", abbr="CLE", division="AFC North",
         primary="#311D00", primaryName="Brown", secondary="#FF3C00", secondaryName="Orange",
         accent="#FF3C00", link="#FF3C00"),
    dict(name="Dallas Cowboys", slug="dallas-cowboys", abbr="DAL", division="NFC East",
         primary="#003594", primaryName="Royal Blue", secondary="#869397", secondaryName="Silver",
         accent="#003594", link="#869397"),
    dict(name="Denver Broncos", slug="denver-broncos", abbr="DEN", division="AFC West",
         primary="#FB4F14", primaryName="Orange", secondary="#002244", secondaryName="Navy",
         accent="#FB4F14", link="#FB4F14"),
    dict(name="Detroit Lions", slug="detroit-lions", abbr="DET", division="NFC North",
         primary="#0076B6", primaryName="Honolulu Blue", secondary="#B0B7BC", secondaryName="Silver",
         accent="#0076B6", link="#B0B7BC"),
    dict(name="Green Bay Packers", slug="green-bay-packers", abbr="GB", division="NFC North",
         primary="#203731", primaryName="Dark Green", secondary="#FFB612", secondaryName="Gold",
         accent="#203731", link="#FFB612"),
    dict(name="Houston Texans", slug="houston-texans", abbr="HOU", division="AFC South",
         primary="#03202F", primaryName="Deep Steel Blue", secondary="#A71930", secondaryName="Battle Red",
         accent="#A71930", link="#A71930"),
    dict(name="Indianapolis Colts", slug="indianapolis-colts", abbr="IND", division="AFC South",
         primary="#002C5F", primaryName="Speed Blue", secondary="#A2AAAD", secondaryName="Gray",
         accent="#002C5F", link="#A2AAAD"),
    dict(name="Jacksonville Jaguars", slug="jacksonville-jaguars", abbr="JAX", division="AFC South",
         primary="#006778", primaryName="Teal", secondary="#D7A22A", secondaryName="Gold",
         accent="#006778", link="#D7A22A"),
    dict(name="Kansas City Chiefs", slug="kansas-city-chiefs", abbr="KC", division="AFC West",
         primary="#E31837", primaryName="Red", secondary="#FFB81C", secondaryName="Gold",
         accent="#E31837", link="#FFB81C"),
    dict(name="Las Vegas Raiders", slug="las-vegas-raiders", abbr="LV", division="AFC West",
         primary="#000000", primaryName="Black", secondary="#A5ACAF", secondaryName="Silver",
         accent="#A5ACAF", link="#A5ACAF", tint="#A5ACAF"),
    dict(name="Los Angeles Chargers", slug="los-angeles-chargers", abbr="LAC", division="AFC West",
         primary="#0080C6", primaryName="Powder Blue", secondary="#FFC20E", secondaryName="Sunshine Gold",
         accent="#0080C6", link="#FFC20E"),
    dict(name="Los Angeles Rams", slug="los-angeles-rams", abbr="LAR", division="NFC West",
         primary="#003594", primaryName="Royal Blue", secondary="#FFA300", secondaryName="Sol Yellow",
         accent="#003594", link="#FFA300"),
    dict(name="Miami Dolphins", slug="miami-dolphins", abbr="MIA", division="AFC East",
         primary="#008E97", primaryName="Aqua", secondary="#FC4C02", secondaryName="Orange",
         accent="#008E97", link="#FC4C02"),
    dict(name="Minnesota Vikings", slug="minnesota-vikings", abbr="MIN", division="NFC North",
         primary="#4F2683", primaryName="Purple", secondary="#FFC62F", secondaryName="Gold",
         accent="#4F2683", link="#FFC62F"),
    dict(name="New England Patriots", slug="new-england-patriots", abbr="NE", division="AFC East",
         primary="#002244", primaryName="Nautical Blue", secondary="#C60C30", secondaryName="Red",
         accent="#C60C30", link="#C60C30"),
    dict(name="New Orleans Saints", slug="new-orleans-saints", abbr="NO", division="NFC South",
         primary="#D3BC8D", primaryName="Old Gold", secondary="#101820", secondaryName="Black",
         accent="#D3BC8D", link="#D3BC8D"),
    dict(name="New York Giants", slug="new-york-giants", abbr="NYG", division="NFC East",
         primary="#0B2265", primaryName="Blue", secondary="#A71930", secondaryName="Red",
         accent="#0B2265", link="#A71930"),
    dict(name="New York Jets", slug="new-york-jets", abbr="NYJ", division="AFC East",
         primary="#125740", primaryName="Gotham Green", secondary="#FFFFFF", secondaryName="White",
         accent="#125740", link="#125740"),
    dict(name="Philadelphia Eagles", slug="philadelphia-eagles", abbr="PHI", division="NFC East",
         primary="#004C54", primaryName="Midnight Green", secondary="#A5ACAF", secondaryName="Silver",
         accent="#004C54", link="#A5ACAF"),
    dict(name="Pittsburgh Steelers", slug="pittsburgh-steelers", abbr="PIT", division="AFC North",
         primary="#FFB612", primaryName="Gold", secondary="#101820", secondaryName="Black",
         accent="#FFB612", link="#FFB612"),
    dict(name="San Francisco 49ers", slug="san-francisco-49ers", abbr="SF", division="NFC West",
         primary="#AA0000", primaryName="49ers Red", secondary="#B3995D", secondaryName="Gold",
         accent="#AA0000", link="#B3995D"),
    dict(name="Seattle Seahawks", slug="seattle-seahawks", abbr="SEA", division="NFC West",
         primary="#002244", primaryName="College Navy", secondary="#69BE28", secondaryName="Action Green",
         accent="#69BE28", link="#69BE28"),
    dict(name="Tampa Bay Buccaneers", slug="tampa-bay-buccaneers", abbr="TB", division="NFC South",
         primary="#D50A0A", primaryName="Red", secondary="#FF7900", secondaryName="Bucco Orange",
         accent="#D50A0A", link="#FF7900"),
    dict(name="Tennessee Titans", slug="tennessee-titans", abbr="TEN", division="AFC South",
         primary="#0C2340", primaryName="Titans Navy", secondary="#4B92DB", secondaryName="Titans Blue",
         accent="#4B92DB", link="#C8102E", linkName="Titans Red"),
    dict(name="Washington Commanders", slug="washington-commanders", abbr="WSH", division="NFC East",
         primary="#5A1414", primaryName="Burgundy", secondary="#FFB612", secondaryName="Gold",
         accent="#5A1414", link="#FFB612"),
]

TEMPLATE = Template("""/**
 * @name NFLcord • $name
 * @author NFLcord
 * @version 1.0.0
 * @description $name ($abbr · $division) — $colorway. Part of the NFLcord collection covering all 32 NFL teams.
 * @source https://github.com/embabyty/NFLcord
 */

/* NFLcord • $name ($abbr · $division)
 * Colors: $accentName $accent / $linkName $link (primary $primary, secondary $secondary)
 * Customize in Vencord QuickCSS, e.g.:
 * :root { --nfl-accent: #ff0000; --nfl-accent-text: #ffffff; }
 * :root { --nfl-logo: url("https://i.imgur.com/your-image.png"); }
 * Vesktop acrylic transparency (Settings → Window → Background Material):
 * :root { --glass-opacity: 0.55; }  (then fully restart Discord)
 * Full-transparency dark-acrylic preset (QuickCSS): see presets/ in the repo.
 */

:root {
  --nfl-primary: $primary;
  --nfl-secondary: $secondary;
  --nfl-accent: $accent;
  --nfl-accent-hover: $hover;
  --nfl-accent-active: $active;
  --nfl-accent-text: $accentText;
  --nfl-tint: $tint;
  --nfl-link: $link;
  --nfl-logo: url("$logoUrl");
  --glass-blur: 20px;
  --glass-radius: 14px;
  /* Backdrop opacity. Keep 1 normally; lower it (e.g. 0.55) in QuickCSS when
     using Vesktop's Background Material (Acrylic) so the blurred wallpaper
     shows through. A restart is required after changing that setting. */
  --glass-opacity: 1;
}

.theme-light,
.theme-dark {
  /* legacy brand scale */
  --brand-experiment: var(--nfl-accent) !important;
  --brand-experiment-360: var(--nfl-accent-hover) !important;
  --brand-experiment-400: var(--nfl-accent-hover) !important;
  --brand-experiment-430: var(--nfl-accent) !important;
  --brand-experiment-460: var(--nfl-accent) !important;
  --brand-experiment-500: var(--nfl-accent) !important;
  --brand-experiment-530: var(--nfl-accent) !important;
  --brand-experiment-560: var(--nfl-accent-hover) !important;
  --brand-experiment-600: var(--nfl-accent-active) !important;
  --brand-experiment-630: var(--nfl-accent-active) !important;
  --brand-345: var(--nfl-accent-hover) !important;
  --brand-360: var(--nfl-accent-hover) !important;
  --brand-400: var(--nfl-accent-hover) !important;
  --brand-430: var(--nfl-accent) !important;
  --brand-460: var(--nfl-accent) !important;
  --brand-500: var(--nfl-accent) !important;
  --brand-500-hsl: $accentHsl !important;
  --brand-530: var(--nfl-accent) !important;
  --brand-560: var(--nfl-accent-hover) !important;
  --brand-560-hsl: $hoverHsl !important;
  --brand-600: var(--nfl-accent-active) !important;
  --brand-600-hsl: $activeHsl !important;
  --brand-630: var(--nfl-accent-active) !important;

  /* controls, buttons, badges (solid fills use the pure accent) */
  --control-brand-foreground: var(--nfl-accent) !important;
  --background-brand: var(--nfl-accent) !important;
  --background-accent: var(--nfl-accent) !important;
  --button-brand-background: var(--nfl-accent) !important;
  --button-brand-background-hover: var(--nfl-accent-hover) !important;
  --button-brand-background-active: var(--nfl-accent-active) !important;
  --button-brand-text: var(--nfl-accent-text) !important;
  --button-filled-brand-background: var(--nfl-accent) !important;
  --button-filled-brand-background-hover: var(--nfl-accent-hover) !important;
  --button-filled-brand-background-active: var(--nfl-accent-active) !important;
  --button-filled-brand-text: var(--nfl-accent-text) !important;
  --badge-brand-bg: var(--nfl-accent) !important;
  --badge-brand-text: var(--nfl-accent-text) !important;
  --focus-primary: var(--nfl-accent) !important;
  --border-brand: color-mix(in srgb, var(--nfl-accent) 60%, transparent) !important;

  /* soft surfaces keep the team hue at low opacity */
  --mention-background: color-mix(in srgb, var(--nfl-accent) 26%, transparent) !important;
  --background-mentioned: color-mix(in srgb, var(--nfl-accent) 16%, transparent) !important;
  --background-mentioned-hover: color-mix(in srgb, var(--nfl-accent) 24%, transparent) !important;
  --background-message-highlight: color-mix(in srgb, var(--nfl-accent) 12%, transparent) !important;
  --background-message-highlight-hover: color-mix(in srgb, var(--nfl-accent) 18%, transparent) !important;

  /* channel list (and member/settings) rows in full team color.
     Selected mixes the accent toward the on-accent text color so the row
     looks solid while the channel name stays readable on every team. */
  --background-modifier-hover: color-mix(in srgb, var(--nfl-accent) 18%, transparent) !important;
  --background-modifier-active: color-mix(in srgb, var(--nfl-accent) 32%, transparent) !important;
  --background-modifier-selected: color-mix(in srgb, var(--nfl-accent) 62%, var(--nfl-accent-text)) !important;
}

/* text on top of backgrounds: nudge the hue toward white/black per mode */
.theme-dark {
  --nfl-sidebar: $sidebarDark;
  /* whole-UI translucent surfaces (chat, headers, inputs, popouts, modals) */
  --glass-chat: color-mix(in srgb, color-mix(in srgb, var(--nfl-tint) 14%, #191c23) 78%, transparent) !important;
  --glass-float: color-mix(in srgb, #20232c 84%, transparent) !important;
  --background-primary: var(--glass-chat) !important;
  --background-secondary: color-mix(in srgb, var(--nfl-sidebar) 68%, transparent) !important;
  --background-secondary-alt: color-mix(in srgb, var(--nfl-sidebar) 60%, transparent) !important;
  --background-tertiary: var(--glass-chat) !important;
  --background-floating: var(--glass-float) !important;
  --modal-background: var(--glass-float) !important;
  --modal-footer-background: transparent !important;
  --home-background: var(--glass-chat) !important;
  --channeltextarea-background: color-mix(in srgb, #26282f 72%, transparent) !important;
  --input-background: color-mix(in srgb, #1d1f26 70%, transparent) !important;
  --background-message-hover: color-mix(in srgb, var(--nfl-accent) 9%, transparent) !important;
  --glass-backdrop:
    radial-gradient(1100px 750px at 12% -8%, color-mix(in srgb, var(--nfl-accent) 30%, transparent), transparent 62%),
    radial-gradient(950px 700px at 108% 108%, color-mix(in srgb, var(--nfl-tint) 32%, transparent), transparent 60%),
    linear-gradient(160deg, rgba(17, 20, 27, var(--glass-opacity)) 0%, rgba(11, 14, 20, var(--glass-opacity)) 55%, rgba(12, 15, 22, var(--glass-opacity)) 100%) !important;
  --glass-bg: color-mix(in srgb, var(--nfl-sidebar) 58%, transparent) !important;
  --glass-edge: rgba(255, 255, 255, 0.09) !important;
  --glass-highlight: rgba(255, 255, 255, 0.10) !important;
  --text-brand: color-mix(in srgb, var(--nfl-accent) 60%, white) !important;
  --text-link: color-mix(in srgb, var(--nfl-link) 80%, white) !important;
  --mention-foreground: color-mix(in srgb, var(--nfl-accent) 45%, white) !important;
}

.theme-light {
  --nfl-sidebar: $sidebarLight;
  /* whole-UI translucent surfaces (chat, headers, inputs, popouts, modals) */
  --glass-chat: color-mix(in srgb, color-mix(in srgb, var(--nfl-tint) 12%, #f4f5f8) 80%, transparent) !important;
  --glass-float: color-mix(in srgb, #ffffff 86%, transparent) !important;
  --background-primary: var(--glass-chat) !important;
  --background-secondary: color-mix(in srgb, var(--nfl-sidebar) 68%, transparent) !important;
  --background-secondary-alt: color-mix(in srgb, var(--nfl-sidebar) 60%, transparent) !important;
  --background-tertiary: var(--glass-chat) !important;
  --background-floating: var(--glass-float) !important;
  --modal-background: var(--glass-float) !important;
  --modal-footer-background: transparent !important;
  --home-background: var(--glass-chat) !important;
  --channeltextarea-background: color-mix(in srgb, #ebedef 75%, transparent) !important;
  --input-background: color-mix(in srgb, #e3e5e8 72%, transparent) !important;
  --background-message-hover: color-mix(in srgb, var(--nfl-accent) 9%, transparent) !important;
  --glass-backdrop:
    radial-gradient(1100px 750px at 12% -8%, color-mix(in srgb, var(--nfl-accent) 22%, transparent), transparent 62%),
    radial-gradient(950px 700px at 108% 108%, color-mix(in srgb, var(--nfl-tint) 26%, transparent), transparent 60%),
    linear-gradient(160deg, rgba(238, 240, 245, var(--glass-opacity)) 0%, rgba(226, 230, 238, var(--glass-opacity)) 55%, rgba(223, 227, 235, var(--glass-opacity)) 100%) !important;
  --glass-bg: color-mix(in srgb, var(--nfl-sidebar) 50%, rgba(255, 255, 255, 0.5)) !important;
  --glass-edge: rgba(15, 20, 30, 0.10) !important;
  --glass-highlight: rgba(255, 255, 255, 0.55) !important;
  --text-brand: color-mix(in srgb, var(--nfl-accent) 78%, black) !important;
  --text-link: color-mix(in srgb, var(--nfl-link) 78%, black) !important;
  --mention-foreground: color-mix(in srgb, var(--nfl-accent) 80%, black) !important;
}

/* ===== liquid glass: whole Discord UI =====
 * A team-tinted backdrop glows behind the app. The server rail, channel
 * list, member list, and chat become floating frosted-glass panels, while
 * every other surface (headers, inputs, popouts, modals, settings, friends)
 * turns translucent through the variables above.
 * Blur is kept to the mostly-static outer panels for performance; the chat
 * column stays unblurred so scrolling stays smooth and messages readable.
 * NOTE: single-underscore substring selectors (e.g. guilds_) match both the
 * current (guilds_abc12) and legacy (guilds__abc12) Discord class formats. */
body {
  background: var(--glass-backdrop) !important;
}

html,
#app-mount,
#app-mount > div,
#app-mount > div > div,
#app-mount [class*="app_"],
#app-mount [class*="app-"],
#app-mount [class*="bg_"],
#app-mount [class*="bg-"] {
  background: transparent !important;
}

[class*="guilds_"],
[class*="sidebarList_"],
[class*="membersWrap_"] {
  background: var(--glass-bg) !important;
  backdrop-filter: blur(var(--glass-blur)) saturate(1.25);
  -webkit-backdrop-filter: blur(var(--glass-blur)) saturate(1.25);
  border-radius: var(--glass-radius);
  overflow: hidden;
  box-shadow:
    inset 0 0 0 1px var(--glass-edge),
    inset 0 1px 0 var(--glass-highlight),
    0 12px 32px rgba(0, 0, 0, 0.35);
}

[class*="guilds_"] {
  margin: 10px 0 10px 10px;
}

[class*="sidebarList_"] {
  margin: 10px;
}

[class*="membersWrap_"] {
  margin: 10px 10px 10px 0;
}

/* chat column as a floating panel (translucent, unblurred for smooth scroll) */
[class*="chat_"] {
  background: var(--glass-chat) !important;
  border-radius: var(--glass-radius);
  overflow: hidden;
  margin: 10px 10px 10px 0;
  box-shadow:
    inset 0 0 0 1px var(--glass-edge),
    inset 0 1px 0 var(--glass-highlight),
    0 12px 32px rgba(0, 0, 0, 0.35);
}

/* inner containers must not repaint over the glass */
[class*="guilds_"] div[class*="scroller_"],
[class*="sidebarList_"] div[class*="container_"],
[class*="sidebarList_"] div[class*="scroller_"],
[class*="membersWrap_"] > div {
  background: transparent !important;
}

::selection {
  background: var(--nfl-accent) !important;
  color: var(--nfl-accent-text) !important;
}

/* team logo as the Discord home button (top of the server list) */
[data-list-item-id="guildsnav___home"] > [class*="childWrapper_"],
[class*="tutorialContainer_"] [class*="childWrapper_"] {
  background-color: transparent !important;
  background-image: var(--nfl-logo) !important;
  background-size: 88% !important;
  background-position: center !important;
  background-repeat: no-repeat !important;
}

[data-list-item-id="guildsnav___home"] [class*="childWrapper_"] > svg,
[class*="tutorialContainer_"] [class*="childWrapper_"] > svg {
  display: none !important;
}
""")


def hex_to_rgb(h: str) -> tuple:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb) -> str:
    return "#{:02X}{:02X}{:02X}".format(*[round(min(255, max(0, c))) for c in rgb])


def mix_hex(h1: str, h2: str, t: float) -> str:
    a, b = hex_to_rgb(h1), hex_to_rgb(h2)
    return rgb_to_hex(tuple(x + (y - x) * t for x, y in zip(a, b)))


def _lin(c: float) -> float:
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(h: str) -> float:
    r, g, b = hex_to_rgb(h)
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(h1: str, h2: str) -> float:
    l1, l2 = luminance(h1), luminance(h2)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def hex_to_hsl_triplet(h: str) -> str:
    r, g, b = [c / 255.0 for c in hex_to_rgb(h)]
    mx, mn = max(r, g, b), min(r, g, b)
    l = (mx + mn) / 2
    if mx == mn:
        return f"0 0% {l * 100:.1f}%"
    d = mx - mn
    s = d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)
    if mx == r:
        hue = (g - b) / d + (6 if g < b else 0)
    elif mx == g:
        hue = (b - r) / d + 2
    else:
        hue = (r - g) / d + 4
    return f"{hue * 60:.1f} {s * 100:.1f}% {l * 100:.1f}%"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for t in TEAMS:
        accent = t["accent"].upper()
        if luminance(accent) >= 0.35:
            hover = mix_hex(accent, "#000000", 0.10)
            active = mix_hex(accent, "#000000", 0.20)
        else:
            hover = mix_hex(accent, "#FFFFFF", 0.14)
            active = mix_hex(accent, "#FFFFFF", 0.26)
        accent_text = (
            "#FFFFFF"
            if contrast(accent, "#FFFFFF") >= contrast(accent, "#000000")
            else "#000000"
        )
        link = t["link"].upper()
        link_name = t.get("linkName", t["secondaryName"])
        accent_name = t.get("accentName", t["primaryName"] if accent == t["primary"].upper() else t["secondaryName"])
        if link == accent:
            colorway = f"{accent_name} {accent} throughout"
        else:
            colorway = f"{accent_name} {accent} with {link_name} {link}"
        tint = t.get("tint", t["primary"]).upper()
        if tint in ("#000000", "#FFFFFF"):
            tint = accent
        sidebar_dark = mix_hex(tint, SIDEBAR_DARK_BASE, 1 - SIDEBAR_DARK_RATIO)
        sidebar_light = mix_hex(tint, SIDEBAR_LIGHT_BASE, 1 - SIDEBAR_LIGHT_RATIO)
        css = TEMPLATE.substitute(
            name=t["name"], abbr=t["abbr"], division=t["division"],
            primary=t["primary"].upper(), secondary=t["secondary"].upper(),
            accent=accent, hover=hover, active=active, accentText=accent_text,
            tint=tint, link=link, linkName=link_name, colorway=colorway,
            accentName=accent_name, logoUrl=f"{LOGO_BASE}/{t['slug']}.png",
            sidebarDark=sidebar_dark, sidebarLight=sidebar_light,
            accentHsl=hex_to_hsl_triplet(accent),
            hoverHsl=hex_to_hsl_triplet(hover),
            activeHsl=hex_to_hsl_triplet(active),
        )
        path = OUT / f"{t['slug']}.theme.css"
        path.write_text(css, encoding="utf-8")
        print(f"wrote {path.name}  accent={accent} text={accent_text} "
              f"({contrast(accent, accent_text):.2f}:1)")
    print(f"\nDone: {len(TEAMS)} themes in {OUT}")


if __name__ == "__main__":
    main()
