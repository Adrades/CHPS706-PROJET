import os
import subprocess

print(os.path.basename(os.path.normpath('/folderA/folderB/folderC/titactoe.py')))
print(os.path.splitext('/home/ray/Desktop/706 - PERFORMIA/Protocol/CHPS706-PROJET/exegame/dist/tictactoe/tictactoe'))


"""
os.system("python3 ./tictactoe.py")

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)

"""

