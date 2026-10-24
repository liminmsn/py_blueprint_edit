import dearpygui.dearpygui as dpg

def edit_blueprint(app):
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