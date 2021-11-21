# Luu Minh Tri, 20/11/2021
# MAIN.PY -- run file for application

import gui
import os

def main():
    os.chdir('.')
    app = gui.App()
    app.run()

if __name__ == "__main__":
    main()