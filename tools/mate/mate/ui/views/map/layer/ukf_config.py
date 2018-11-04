import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc

import uuid

from mate.ui.views.map.layer.ukf_config_view import Ui_UKFConfig
from mate.ui.views.map.layer.layer_config import LayerConfig, LayerConfigMeta
import mate.net.nao as nao
import mate.net.utils as net_utils
import mate.ui.utils as ui_utils


class UKFConfig(qtw.QWidget, LayerConfig, metaclass=LayerConfigMeta):
    def __init__(self, layer, parent, update_callback, nao: nao.Nao):
        super(UKFConfig, self).__init__(parent)

        self.nao = nao
        self.layer = layer
        self.update_callback = update_callback
        self.identifier = uuid.uuid4()

        self.ui = Ui_UKFConfig()
        self.ui.setupUi(self)

        if self.layer["settings"] is None:
            self.layer["settings"] = {
                "center_x": 5.2,
                "center_y": -3.7,
                "ukf": {
                    "key": "Brain.UKFPositionKnowledge"
                }
            }

        self.settings_to_ui = {
            "center_x": (
                lambda: self.ui.spin_center_x.value(),
                lambda value: self.ui.spin_center_x.setValue(value)),
            "center_y": (
                lambda: self.ui.spin_center_y.value(),
                lambda value: self.ui.spin_center_y.setValue(value)),
            "ukf": (
                lambda:  {
                    "key": self.ui.cbx_Key.currentText()},
                lambda settings: [
                    self.ui.cbx_Key.setCurrentText(settings["key"])])
            }

        self.ui.cbx_Key.completer().setFilterMode(qtc.Qt.MatchContains)
        self.ui.cbx_Key.completer().setCompletionMode(
            qtw.QCompleter.PopupCompletion)

        self.ui.btnAccept.pressed.connect(self.accept)
        self.ui.btnDiscard.pressed.connect(self.discard)

        self.reset_widgets()
        if self.nao.is_connected():
            self.connect(self.nao)

    def connect(self, nao: nao.Nao):
        self.nao = nao
        self.fill_cbx()
        self.nao.debug_protocol.subscribe_msg_type(
            net_utils.DebugMsgType.list, self.identifier, self.fill_cbx)

    def closeEvent(self, event):
        if self.nao.is_connected():
            self.nao.debug_protocol.unsubscribe_msg_type(
                net_utils.DebugMsgType.list, self.identifier)

    def reset_widgets(self):
        self.ui.nameLineEdit.setText(self.layer["name"])
        self.ui.enabledCheckBox.setChecked(self.layer["enabled"])

        for key in self.layer["settings"]:
            self.settings_to_ui[key][1](self.layer["settings"][key])

    def fill_cbx(self):
        ui_utils.init_cbx(
            self.ui.cbx_Key,
            self.layer["settings"]["ukf"]["key"],
            self.nao.debug_data)

    def accept(self):
        self.layer["name"] = self.ui.nameLineEdit.text()
        self.layer["enabled"] = self.ui.enabledCheckBox.isChecked()

        for key in self.layer["settings"]:
            self.layer["settings"][key] = self.settings_to_ui[key][0]()

        self.update_callback()

    def discard(self):
        self.reset_widgets()
