import sys
from src.application import Application

if __name__ == "__main__":
    app = Application()
    print("准备运行")
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n程序已被手动中断，正在退出...")
        sys.exit(0)
