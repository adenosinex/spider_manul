


import os


def get_dst_path( ):
    # dst=\\Synology\xx
    with open("config.cfg", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith("dst="):
            return line.strip().split("=", 1)[1]
    return "."
def mv(src, dst):
    import shutil
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.move(src, dst)
def run():
    dst = get_dst_path()
    print("dst=", dst)
    cnt=0
    for i in os.listdir("."):
        if i.endswith(".txt"):
            mv(i, dst)
            cnt+=1
    print("移动了", cnt, "个文件")

if __name__ == "__main__":
    
    run()