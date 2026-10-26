import dearpygui.dearpygui as dpg
import os
from src.store import store
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.application import Application

data={
    "select_file_path":""
}

def edit_sidebar(app:'Application',edit):
    dpg.add_text("项目资源", color=(200, 200, 200))
    dpg.add_separator()
    with dpg.child_window(width=-1, height=-1, border=False, tag="project_tree_container"):
        def load_project(dir_path: str):
            # print(f"开始加载项目目录: {dir_path}")
            if dpg.does_item_exist("project_tree_container"):
                dpg.delete_item("project_tree_container", children_only=True)

            def open_file(file_path:str):
                if edit.loadFile:
                    if data["select_file_path"] != file_path:
                        data["select_file_path"] = file_path
                        edit.loadFile(file_path)
            
            def build_tree(current_path, parent_container):
                try:
                    items = os.listdir(current_path)
                    items.sort(key=lambda x: (not os.path.isdir(os.path.join(current_path, x)), x.lower()))
                    for item in items:
                        full_path = os.path.normpath(os.path.join(current_path, item))
                        print(full_path)
                        if os.path.isdir(full_path):
                            with dpg.tree_node(label=item, parent=parent_container):
                                build_tree(full_path, dpg.last_item())
                        elif os.path.isfile(full_path) and item.endswith(".ts"):
                            dpg.add_selectable(
                                label=item, 
                                parent=parent_container,
                                callback=lambda: open_file(full_path))
                except PermissionError:
                    print(f"没有权限访问: {current_path}")
            root_name = os.path.basename(os.path.normpath(dir_path))
            with dpg.tree_node(label=root_name, default_open=True, parent="project_tree_container"):
                build_tree(dir_path, dpg.last_item())
    load_project(store["project_dir"])