# 4Coder Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restrart Nautilus, and enjoy :)
#
# This script was written by cra0zy and adapted by cmarincia and is released to the public domain

from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to 4Coder, the absolute path always works
FOURCODER = '/home/catalin/Documents/4coder/4coder/4ed'

# what name do you want to see in the context menu?
FOURCODERNAME = '4Coder'

class FourCoderExtension(GObject.GObject, Nautilus.MenuProvider):
    def launch_four_coder(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '
        call(FOURCODER + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, window, files):
        item = Nautilus.MenuItem(
            name='4CoderOpen',
            label='Open In ' + FOURCODERNAME,
            tip='Opens the selected files with 4Coder'
        )
        item.connect('activate', self.launch_four_coder, files)
        return [item]

    def get_background_items(self, window, file_):
        item = Nautilus.MenuItem(
            name='4CoderOpenBackground',
            label='Open ' + FOURCODERNAME + ' Here',
            tip='Opens 4Coder in the current directory'
        )
        item.connect('activate', self.launch_four_coder, [file_])
        return [item]
