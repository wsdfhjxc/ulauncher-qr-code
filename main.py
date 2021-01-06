from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction

import subprocess


class QRCodeExtension(Extension):
    def __init__(self):
        super(QRCodeExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        content = event.get_argument()
        onEnterAction = DoNothingAction() if not content \
                   else ExtensionCustomAction(content, keep_app_open=False)

        return RenderResultListAction([ExtensionResultItem(icon="images/icon.png",
                                       name="Generate a QR code",
                                       description="Content: %s" % (content or "N/A"),
                                       on_enter=onEnterAction)])


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        content = event.get_data()
        popupHeight = extension.preferences["popupHeight"]
        subprocess.call(["./popup.py", content, str(popupHeight)])


if __name__ == "__main__":
    QRCodeExtension().run()
