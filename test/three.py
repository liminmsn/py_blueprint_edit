from tree_sitter import Language, Parser
import tree_sitter_typescript as tsts

TS_LANGUAGE = Language(tsts.language_typescript())
parser = Parser(TS_LANGUAGE)

# 解析代码
source_code = b"""
interface User {
    name: string;
    age: number;
}

function greet(user: User): string {
    return `Hello, ${user.name}`;
}
"""

tree = parser.parse(source_code)
root_node = tree.root_node

print(root_node)

def walk(node, depth=0):
    print("  " * depth + node.type)
    for child in node.children:
        walk(child, depth + 1)

walk(root_node)