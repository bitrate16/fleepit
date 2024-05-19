# fleepit

Text seleciton keyboard layout switcher based on xclip / etc for X11 & wayland

# Install

1. Install required packages:
  * X11: `xclip`, `xdotool`

2. install module: `pip install fleepit`

# Usage

Sample usage for KDE:
* Add custom program shortcut in settings
* Fill something like `fleepit --mode x11 --langset qwerty-en-ru`
* Set some shortcut, for example `CTRL+` `

# Langset file

Sample langset file:

```json

{
    "langset": [
        "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,.~!#%&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>",
        "ё1234567890-=йцукенгшщзхъ\\фывапролджэячсмитьбюЁ!№%?*()_+ЙЦУКЕНГШЩЗХЪ/ФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
    ]
}

```

# Support

Current list of language convertations:
* QWERTY: EN <> RU
