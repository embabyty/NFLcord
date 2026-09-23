# NFLcord Themes

Vencord themes for all **32 NFL teams**, each dressed in its official team colors.
Pick your team, drop the file into Vencord, and Discord buttons, mentions,
links, badges, and highlights take on your team's identity. Works in both
dark and light mode.

## Install

**Vencord (desktop):**

1. Download or clone this repo.
2. In Discord, go to `Settings → Themes → Open Themes Folder`.
3. Copy `themes/<your-team>.theme.css` into that folder.
4. Back in `Settings → Themes`, enable it. Use only one NFLcord theme at a time.

**Vencord (web):**

1. Go to `Settings → Themes → Upload Theme` and select your team's file.

**BetterDiscord:** the files use the standard `.theme.css` header format, so they
can also be dropped into BetterDiscord's `themes` folder.

## Customize

Every theme exposes its palette as CSS variables, so you can tweak it in
Vencord QuickCSS (`Settings → Themes → QuickCSS`) without editing the file:

```css
:root {
  --nfl-accent: #ff0000;      /* buttons, badges, brand */
  --nfl-accent-text: #ffffff; /* text on the accent */
  --nfl-link: #ff0000;        /* links */
  --nfl-logo: url("https://i.imgur.com/your-image.png"); /* home button */
}
```

> Note: custom `--nfl-logo` URLs must be hosted on Vencord's allowlist
> (GitHub, Imgur, etc.), otherwise Discord blocks them from loading.

## Themes

| Team | Abbr | Division | Accent | Secondary |
| ---- | ---- | -------- | ------ | --------- |
| [Arizona Cardinals](themes/arizona-cardinals.theme.css) | ARI | NFC West | Cardinal Red `#97233F` | Desert Gold `#FFB612` |
| [Atlanta Falcons](themes/atlanta-falcons.theme.css) | ATL | NFC South | Red `#A71930` | Silver `#A5ACAF` |
| [Baltimore Ravens](themes/baltimore-ravens.theme.css) | BAL | AFC North | Purple `#241773` | Metallic Gold `#9E7C0C` |
| [Buffalo Bills](themes/buffalo-bills.theme.css) | BUF | AFC East | Royal Blue `#00338D` | Red `#C60C30` |
| [Carolina Panthers](themes/carolina-panthers.theme.css) | CAR | NFC South | Panther Blue `#0085CA` | Silver `#BFC0BF` |
| [Chicago Bears](themes/chicago-bears.theme.css) | CHI | NFC North | Burnt Orange `#C83803` | Midnight Navy `#0B162A` |
| [Cincinnati Bengals](themes/cincinnati-bengals.theme.css) | CIN | AFC North | Orange `#FB4F14` | Black `#000000` |
| [Cleveland Browns](themes/cleveland-browns.theme.css) | CLE | AFC North | Orange `#FF3C00` | Brown `#311D00` |
| [Dallas Cowboys](themes/dallas-cowboys.theme.css) | DAL | NFC East | Royal Blue `#003594` | Silver `#869397` |
| [Denver Broncos](themes/denver-broncos.theme.css) | DEN | AFC West | Orange `#FB4F14` | Navy `#002244` |
| [Detroit Lions](themes/detroit-lions.theme.css) | DET | NFC North | Honolulu Blue `#0076B6` | Silver `#B0B7BC` |
| [Green Bay Packers](themes/green-bay-packers.theme.css) | GB | NFC North | Dark Green `#203731` | Gold `#FFB612` |
| [Houston Texans](themes/houston-texans.theme.css) | HOU | AFC South | Battle Red `#A71930` | Deep Steel Blue `#03202F` |
| [Indianapolis Colts](themes/indianapolis-colts.theme.css) | IND | AFC South | Speed Blue `#002C5F` | Gray `#A2AAAD` |
| [Jacksonville Jaguars](themes/jacksonville-jaguars.theme.css) | JAX | AFC South | Teal `#006778` | Gold `#D7A22A` |
| [Kansas City Chiefs](themes/kansas-city-chiefs.theme.css) | KC | AFC West | Red `#E31837` | Gold `#FFB81C` |
| [Las Vegas Raiders](themes/las-vegas-raiders.theme.css) | LV | AFC West | Silver `#A5ACAF` | Black `#000000` |
| [Los Angeles Chargers](themes/los-angeles-chargers.theme.css) | LAC | AFC West | Powder Blue `#0080C6` | Sunshine Gold `#FFC20E` |
| [Los Angeles Rams](themes/los-angeles-rams.theme.css) | LAR | NFC West | Royal Blue `#003594` | Sol Yellow `#FFA300` |
| [Miami Dolphins](themes/miami-dolphins.theme.css) | MIA | AFC East | Aqua `#008E97` | Orange `#FC4C02` |
| [Minnesota Vikings](themes/minnesota-vikings.theme.css) | MIN | NFC North | Purple `#4F2683` | Gold `#FFC62F` |
| [New England Patriots](themes/new-england-patriots.theme.css) | NE | AFC East | Red `#C60C30` | Nautical Blue `#002244` |
| [New Orleans Saints](themes/new-orleans-saints.theme.css) | NO | NFC South | Old Gold `#D3BC8D` | Black `#101820` |
| [New York Giants](themes/new-york-giants.theme.css) | NYG | NFC East | Blue `#0B2265` | Red `#A71930` |
| [New York Jets](themes/new-york-jets.theme.css) | NYJ | AFC East | Gotham Green `#125740` | White `#FFFFFF` |
| [Philadelphia Eagles](themes/philadelphia-eagles.theme.css) | PHI | NFC East | Midnight Green `#004C54` | Silver `#A5ACAF` |
| [Pittsburgh Steelers](themes/pittsburgh-steelers.theme.css) | PIT | AFC North | Gold `#FFB612` | Black `#101820` |
| [San Francisco 49ers](themes/san-francisco-49ers.theme.css) | SF | NFC West | 49ers Red `#AA0000` | Gold `#B3995D` |
| [Seattle Seahawks](themes/seattle-seahawks.theme.css) | SEA | NFC West | Action Green `#69BE28` | College Navy `#002244` |
| [Tampa Bay Buccaneers](themes/tampa-bay-buccaneers.theme.css) | TB | NFC South | Red `#D50A0A` | Bucco Orange `#FF7900` |
| [Tennessee Titans](themes/tennessee-titans.theme.css) | TEN | AFC South | Titans Blue `#4B92DB` | Titans Red `#C8102E` |
| [Washington Commanders](themes/washington-commanders.theme.css) | WSH | NFC East | Burgundy `#5A1414` | Gold `#FFB612` |

## What each theme changes

- Team logo as the Discord home button (top of the server list)
- Brand/accent color (buttons, toggles, sliders, badges, unread indicators)
- Hover/active shades derived from the accent for readable feedback
- Links and mentions in the secondary team color
- Soft team-tinted backgrounds for mentions, highlights, and selected rows
- Text selection in team colors
- On-accent text (black or white) chosen per team for WCAG AA contrast

Backgrounds are left at Discord defaults on purpose, so readability never
suffers — the team identity comes through the accents.

## Regenerating

All themes are generated from `tools/build.py` (team data + one shared
template), so a fix applies to every team at once:

```sh
python tools/build.py
```

Logos live in `assets/logos/` (one PNG per team) and are loaded from this
repo via `raw.githubusercontent.com`, which is on Vencord's image allowlist —
no extra setup needed once pushed. If the default branch is ever renamed,
update `LOGO_BRANCH` in `tools/build.py` and rebuild.

Team logos are trademarks of the NFL and the respective franchises; this is
an unofficial fan project.
