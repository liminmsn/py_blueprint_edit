import dearpygui.dearpygui as dpg
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.application import Application

data = {
    "select_path":""
}
def edit_blueprint(app:'Application',edit):
    def loadFile(path:str):
        if data["select_path"] != path:
            data["select_path"] = path
            edit.add_log("文件地址"+path, color=(0, 255, 0))
    edit.loadFile = loadFile
    
    def link_callback():
        pass
    def delink_callback():
        pass
    with dpg.node_editor(callback=link_callback, delink_callback=delink_callback):
        with dpg.node(label="Node 1"):
            with dpg.node_attribute(label="输入"):
                dpg.add_input_float(label="F1", width=150)
            with dpg.node_attribute(label="输出", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_input_float(label="F2", width=150)   