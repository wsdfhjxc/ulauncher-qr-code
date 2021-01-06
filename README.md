# QR Code

This is a Ulauncher extension for generating QR codes.

## Table of Contents

- [Installation](#installation)
  - [Requirements](#requirements)
  - [Ulauncher's GUI](#ulaunchers-gui)
  - [Manually from source](#manually-from-source)
- [Configuration and usage](#configuration-and-usage)
- [License](#license)

## Installation

### Requirements

The `qrcode` Python module is required. You can install it with:

```
pip install qrcode
```

### Ulauncher's GUI

1. Open Ulauncher's settings and the "Extensions" tab
2. Click "Add extension" button
3. Paste this URL: `https://github.com/wsdfhjxc/ulauncher-qr-code`
4. Click "Add" button – the extension will be installed

### Manually from source

The extensions' directory is located at:

```
$HOME/.local/share/ulauncher/extensions
```

Either download the ZIP archive and unpack it, or just clone the repository there.

## Configuration and usage

You can configure the trigger keyword and the popup's height in the extension settings.

To generate a QR code, use the keyword (default is `qr`), then type/paste the desired content, and press enter.

The opened popup image can be scanned with a smartphone, or saved locally (context menu or Ctrl+S).

## License

[GNU General Public License v3.0](LICENSE)
