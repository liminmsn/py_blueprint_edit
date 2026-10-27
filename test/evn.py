import sys

print("解释器路径:", sys.executable)
print("环境前缀:", sys.prefix)
print("基础前缀:", sys.base_prefix)

if sys.prefix != sys.base_prefix:
    print("✅ 当前处于虚拟环境")
    print("虚拟环境地址:", sys.prefix)
else:
    print("❌ 当前是全局 Python 环境")