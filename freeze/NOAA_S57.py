import sys
import os
from PySide2 import QtWidgets, QtGui

from hyo2.abc.app.app_style import AppStyle
from hyo2.abc.lib.lib_info import LibInfo
from hyo2.abc.app.app_info import AppInfo
from hyo2.abc.app.dialogs.noaa_s57.noaa_s57 import NOAAS57Dialog
from hyo2.abc.lib.logging import set_logging


set_logging(ns_list=["hyo2.abc", ])

app = QtWidgets.QApplication([])
app.setApplicationName('NOAA S57')
app.setOrganizationName("HydrOffice")
app.setOrganizationDomain("hydroffice.org")
app.setStyleSheet(AppStyle.load_stylesheet())

d = NOAAS57Dialog(lib_info=LibInfo(), app_info=AppInfo())
d.setWindowIcon(QtGui.QIcon(os.path.join(AppInfo().app_media_path, "noaa_support.png")))
d.show()

sys.exit(app.exec_())
