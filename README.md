# fleepit

Text selection keyboard layout switcher based on xclip / etc for X11 & Wayland

# Install

1. Install required packages:
  * X11: `xclip`, `xdotool`
  * Wayland: `wl-clipboard`

2. Install module: `pip install fleepit`

## With Nix:

Use this repository as a flake, or install imperatively:

```sh
nix profile install github:bitrate16/fleepit
```

# Limitations

## X11

Operation is performed in 3 steps:
* copy - copy selection buffer (primary clipboard)
* paste - write converted selection buffer into secondary (regular) clipboard
* send CTRL+V event

## Wayland

Operation is performed in 3 steps with limitations:
* copy - reads contents of primary buffer
* paste - write converted selection into secondary (regular) clipboard
* user has to manually press CTRL+V - for security reasons and/or to prevent depending on external daemon services that may expose potential keystroke injection vulnerabilities

# Usage

Sample usage for KDE:
* Add custom program shortcut in settings
* Fill something like `fleepit --mode x11 --langset qwerty-en-ru`
* Set some shortcut, for example `` CTRL+` ``

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
* COLEMAK: EN <> RU
