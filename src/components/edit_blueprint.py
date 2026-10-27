from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.application import Application
from pathlib import Path
import dearpygui.dearpygui as dpg
import tree_sitter_typescript as tsts
from tree_sitter import Language, Parser

data = {
    "select_path": "",
    "source": None,      # bytes
    "ast": None,         # tree-sitter root Node
    "errors": [],        # [(type, line, col), ...]
}

TS_LANGUAGE = Language(tsts.language_typescript())
_TS_PARSER = Parser(Language(tsts.language_typescript()))
_TSX_PARSER = Parser(Language(tsts.language_tsx()))

def _text(node) -> str:
    """用原始 bytes 切片取节点文本（tree-sitter 节点只有字节偏移）"""
    src = data["source"]
    if src is None or node is None:
        return ""
    return src[node.start_byte:node.end_byte].decode("utf-8", errors="replace")


def _preview(node, limit: int = 40) -> str:
    t = _text(node).replace("\n", " ").strip()
    return t if len(t) <= limit else t[:limit] + "..."

def _format_ast_tree(node, depth: int = 0, max_depth: int | None = None):
    """把 AST 节点树格式化成 [(缩进文本, 深度), ...]，供日志逐行输出"""
    lines = []
    if max_depth is not None and depth > max_depth:
        return lines
    indent = "  " * depth
    label = node.type
    if node.child_count == 0:  # 叶子节点带上源码预览，便于辨认
        preview = _preview(node, 30)
        if preview:
            label += f" [{preview}]"
    lines.append((indent + label, depth))
    for child in node.children:
        lines.extend(_format_ast_tree(child, depth + 1, max_depth))
    return lines

def _get_parser(path: Path) -> Parser:
    return _TSX_PARSER if path.suffix.lower() == ".tsx" else _TS_PARSER

def _collect_errors(node, out):
    if node.type == "ERROR" or node.is_missing:
        line, col = node.start_point
        out.append((node.type, line + 1, col + 1))
    for c in node.children:
        _collect_errors(c, out)

def edit_blueprint(app:'Application',edit):
    def loadFile(path: str) -> bool:
        try:
            p = Path(path)
            if not p.exists():
                raise FileNotFoundError(f"文件不存在：{p.resolve()}")
            if not p.is_file():
                raise IsADirectoryError(f"不是文件：{p.resolve()}")

            source = p.read_bytes()
            tree = _get_parser(p).parse(source)
            root = tree.root_node

            errors: list = []
            if root.has_error:
                _collect_errors(root, errors)

            data["select_path"] = str(p)
            data["source"] = source
            data["ast"] = root
            data["errors"] = errors

            edit.add_log(f"打开文件：{p}", color=(0, 255, 0))
            # === 新增：打印 AST 节点树 ===
            edit.add_log("AST 节点树：", color=(150, 200, 255))
            for line, depth in _format_ast_tree(root, max_depth=6):
                # 按层交替颜色，方便肉眼区分层级
                color = (180, 220, 255) if depth % 2 == 0 else (140, 180, 220)
                edit.add_log(line, color=color)

            if errors:
                edit.add_log(f"⚠️ 语法错误 {len(errors)} 处", color=(255, 255, 0))
                for etype, line, col in errors[:10]:
                    edit.add_log(f"    {etype} @ {line}:{col}", color=(255, 200, 0))
            return True

        except Exception as e:
            edit.add_log(f"加载失败：{e}", color=(255, 0, 0))
            return False
    edit.loadFile = loadFile

    def link_callback():
        pass
    def delink_callback():
        pass
    with dpg.node_editor(callback=link_callback, delink_callback=delink_callback):
        pass
        # with dpg.node(label="Node 1"):
        #     with dpg.node_attribute(label="输入"):
        #         dpg.add_input_float(label="F1", width=150)
        #     with dpg.node_attribute(label="输出", attribute_type=dpg.mvNode_Attr_Output):
        #         dpg.add_input_float(label="F2", width=150)