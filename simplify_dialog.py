# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SimplifyDialog
                                 A QGIS plugin
 Manage and analyse networks via GDAL
                             -------------------
        begin                : 2017-06-07
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
    os.path.dirname(__file__), 'simplify_dialog.ui'))

class SimplifyDialog(QtGui.QDialog, FORM_CLASS):
    Algorithm = None
    Tolerance = None
    Ratio = None

    def __init__(self, parent=None):
        super(SimplifyDialog, self).__init__(parent)
        self.setupUi(self)
        self.comboBox.addItems(['Douglas-Peucker', 'Visvalingam'])
        self.comboBox.currentIndexChanged.connect(self.comboBoxChanged)
        self.button_box.accepted.connect(self.okClicked)
        self.label_3.hide()
        self.editRatio.hide()

    def my_exec_(self):
        return self.exec_()

    def comboBoxChanged(self):
        self.Algorithm = self.comboBox.currentIndex()

        if self.Algorithm == 0:
            self.label_2.show()
            self.editTolerance.show()
            self.label_3.hide()
            self.editRatio.hide()
        if self.Algorithm == 1:
            self.label_2.hide()
            self.editTolerance.hide()
            self.label_3.show()
            self.editRatio.show()

    def okClicked(self):
        self.Algorithm = self.comboBox.currentIndex()
        self.Tolerance = self.editTolerance.text()
        self.Ratio = self.editRatio.text()
