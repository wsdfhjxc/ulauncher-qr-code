#!/bin/python3

qrcodeModule=True

try:
    import qrcode
except ImportError:
    qrcodeModule=False

import gi, io, sys

gi.require_version("Gdk", "3.0")
gi.require_version("Gtk", "3.0")
gi.require_version("GdkPixbuf", "2.0")

from gi.repository import Gdk, GdkPixbuf, Gio, GLib, Gtk

def show(content, popupHeight):
    window = Gtk.Window()
    window.set_title("Your QR code")
    window.set_size_request(popupHeight, popupHeight)
    window.set_resizable(False)

    if qrcodeModule:
        qrCodeImage = qrcode.make(content)
        qrCodeImageByteArray = io.BytesIO()
        qrCodeImage.save(qrCodeImageByteArray, qrCodeImage.format)

        bytes = GLib.Bytes.new(qrCodeImageByteArray.getvalue())
        pixbuf = GdkPixbuf.Pixbuf.new_from_stream_at_scale(Gio.MemoryInputStream.new_from_bytes(bytes),
                                                           width=popupHeight, height=popupHeight,
                                                           preserve_aspect_ratio=False,
                                                           cancellable=None)

        qrCodeGtkImage = Gtk.Image().new_from_pixbuf(pixbuf)
        qrCodeGtkImage.set_tooltip_text(content)
        qrCodeGtkImage.show()


        def saveImageCallback(e):
            dialog = Gtk.FileChooserDialog()
            dialog.set_modal(True)
            dialog.set_title("Save the QR code as image...")
            dialog.set_action(Gtk.FileChooserAction.SAVE)
            dialog.set_do_overwrite_confirmation(True)
            dialog.set_current_name("qrcode.png")

            filter = Gtk.FileFilter()
            filter.set_name("PNG image")
            filter.add_mime_type("image/png")
            dialog.add_filter(filter)

            dialog.add_buttons(Gtk.STOCK_SAVE, Gtk.ResponseType.OK,
                               Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)

            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                qrCodeImage.save(dialog.get_filename())

            dialog.destroy()


        saveImageMenuItemImage = Gtk.Image()
        saveImageMenuItemImage.set_from_stock(Gtk.STOCK_SAVE, 1)

        saveImageMenuItem = Gtk.ImageMenuItem()
        saveImageMenuItem.set_image(saveImageMenuItemImage)
        saveImageMenuItem.set_label("Save as image...")
        saveImageMenuItem.connect("activate", saveImageCallback)
        saveImageMenuItem.show()

        rightClickMenu = Gtk.Menu()
        rightClickMenu.append(saveImageMenuItem)


        def clickCallback(window, event):
            if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 3:
                rightClickMenu.popup(None, None, None, None, 0, Gtk.get_current_event_time())


        def keyPressCallback(window, event):
            if Gdk.ModifierType.CONTROL_MASK and Gdk.keyval_name(event.keyval) == 's':
                saveImageCallback(event)


        window.connect("button-press-event", clickCallback)
        window.connect("key-press-event", keyPressCallback)
        window.add(qrCodeGtkImage)

    else:
        errorLabel = Gtk.Label()
        errorLabel.set_markup("Oops!\n\n"
                              "The <tt>qrcode</tt> module is missing...\n\n"
                              "You can install it with:   <tt>pip install qrcode</tt>")
        errorLabel.set_justify(Gtk.Justification.CENTER)

        window.add(errorLabel)

    window.connect("destroy", lambda w: Gtk.main_quit())
    window.show_all()

    Gtk.main()


if __name__ == "__main__":
    try:
        content = str(sys.argv[1])
    except IndexError:
        content = "Nothing to see here"

    try:
        popupHeight = int(sys.argv[2])
    except IndexError:
        popupHeight = 450

    show(content, popupHeight)
