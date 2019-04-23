import subprocess
cmd = "mecab neko.txt -o neko.txt.mecab"
subprocess.call(cmd.split())
