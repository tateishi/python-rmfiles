import shutil
from pathlib import Path

from fire import Fire


def hello():
    print("Hello, World.")


TMP_DIR = Path("~/wks/tmp/test").expanduser()


def demo1_main():
    print(TMP_DIR)


def demo1():
    Fire(demo1_main)


def demo2_main():
    src = TMP_DIR / "test.pdf"
    dst = TMP_DIR / "test_2.pdf"
    print(f"copy file {src} -> {dst}")
    shutil.copy(src, dst)


def demo2():
    Fire(demo2_main)


def demo3_main():
    srcdir = TMP_DIR
    dstdir = TMP_DIR.parent / "test2"
    print(f"copytree {srcdir} -> {dstdir}")
    shutil.copytree(srcdir, dstdir)


def demo3():
    Fire(demo3_main)


def demo4_main():
    path = TMP_DIR.parent / "test2"
    print(f"rmtree {path}")
    shutil.rmtree(path)


def demo4():
    Fire(demo4_main)


def demo5_main():
    path = TMP_DIR
    items = list(path.rglob("*.pdf"))
    print(f"*.pdf = {items}")
    for i, item in enumerate(items):
        if item.is_dir():
            print(i, "D", item)
            shutil.rmtree(item)
        elif item.is_file():
            print(i, "F", item)
            item.unlink()


def demo5():
    Fire(demo5_main)
