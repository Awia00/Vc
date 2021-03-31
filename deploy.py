import os
import subprocess
import os
from pathlib import Path
from conanfile import VcConan

def deploy(channel = "stable", remote="alipes-hosted"):
    curdir = Path().absolute()

    build_dir = curdir / "build"
    try:
        os.chdir(build_dir)
        
        user_channel = f"alipes/{channel}"
        subprocess.check_call("conan install ..")
        subprocess.check_call(f"conan create .. {user_channel}")
        subprocess.check_call(f"conan upload {VcConan.name}/{VcConan.version}@{user_channel} -r {remote}")
    finally:
        os.chdir(curdir)

if __name__ == "__main__":
    deploy()