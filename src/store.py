from typing import cast
from src.util.os_dir import root_dir
import json
import os

store = {
    "top_project":False,
    "project_dir":"",
    "project_history":[]
}

path = root_dir("resources","store.json")
if os.path.isfile(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        store.update(data)
else:
     print("本地暂无store.json文件")

def save_local():
    with open(path,"w",encoding="utf-8") as f:
            json.dump(store,f,ensure_ascii=False,indent=4)
def store_project_dir_set(path:str):
    store["project_dir"] = path
    save_local()

def store_project_history_add(path:str):
    history = cast(list, store["project_history"])
    if path not in history:
        history.append(path)
        save_local()