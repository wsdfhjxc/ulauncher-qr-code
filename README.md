# QR Code

This is a Ulauncher extension for generating QR codes.

## Table of Contents

- [Screenshot](#screenshot)
- [Installation](#installation)
  - [Requirements](#requirements)
  - [Ulauncher's GUI](#ulaunchers-gui)
  - [Manually from source](#manually-from-source)
- [Configuration and usage](#configuration-and-usage)
- [License](#license)

## Screenshot

![Screenshot](images/screenshot.gif)

## Installation

### Requirements

The `qrcode` Python module is required. You can install it with: `pip install qrcode`

### Ulauncher's GUI

1. Open Ulauncher's settings and the "Extensions" tab
2. Click "Add extension" button
3. Paste this URL: `https://github.com/wsdfhjxc/ulauncher-qr-code`
4. Click "Add" button – the extension will be installed

### Manually from source

The extensions' directory is located at: `$HOME/.local/share/ulauncher/extensions`

Go to that location, and while being inside, just `git clone` this repository.

## Configuration and usage

You can configure the trigger keyword and the popup's size in the extension's settings.

To generate a QR code, use the keyword (default is `qr`), then type/paste the desired content, and press Enter.

The opened popup image can be scanned with a smartphone, or saved locally (context menu or <kbd>Ctrl</kbd><kbd>S</kbd>).

## License

[GNU General Public License v3.0](LICENSE)
