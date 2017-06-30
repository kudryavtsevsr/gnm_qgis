# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ChangeDialog
                                 A QGIS plugin
 Manage and analyse networks via GDAL
                             -------------------
        begin                : 2017-06-29
        git sha              : $Format:%H$
        copyright            : (C) 2017 by NextGIS
        email                : info@nextgis.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from qgis.core import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'change_dialog.ui'))

class ChangeDialog(QtGui.QDialog, FORM_CLASS):
    Layout = None

    def __init__(self, layouts, layout):
        super(ChangeDialog, self).__init__()
        self.setupUi(self)
        self.button_box.accepted.connect(self.okClicked)
        self.comboBox.addItems(layouts)
        self.comboBox.setCurrentIndex(layouts.index(layout))

    def my_exec_(self):
        return self.exec_()

    def okClicked(self):
        self.Layout = self.comboBox.currentText()