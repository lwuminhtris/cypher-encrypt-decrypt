# Luu Minh Tri, 20/11/2021
# GUI.PY - graphic user interface for application
# ** require tkinter

import tkinter as tk
from tkinter import ttk
from exec import Exec

APP_TITLE = 'Bài tập lớn MM&ANM số 1 (20/11/2021)'
APP_SIZE = '900x500'
AUTHORS = '''Sinh viên thực hiện:
                1. Lưu Minh Trí, 1811298
                2. Lê Đình Duy, '''

class App: 
    def __init__(self):
        self.app = tk.Tk()
        self.app.title(APP_TITLE)
        self.app.geometry(APP_SIZE)
        self.app.resizable(False, False)

        self.initCypherTypes()
        self.initKeyTypes()
        self.initInputText()
        self.initHandlingBtn()


    def run(self):
        self.app.mainloop()

    def initCypherTypes(self):
        frame = tk.Frame(self.app)
        frame.grid(column=0, row=0, padx=5, pady=10, sticky='W')

        label = ttk.Label(frame, text='Loại mã hóa')
        label.grid(column=0, row=0, padx=5, pady=0) 

        cypherTypes = ['Caesar', 'Rail Fence', 'Caesar và Rail Fence kết hợp']

        self.cypherTypes = ttk.Combobox(frame, state='readonly', justify=tk.LEFT, width=40)
        self.cypherTypes['values'] = cypherTypes
        self.cypherTypes.grid(column=1, row=0, sticky='W')

        # frame.place(in_=self.app, anchor='c', relx=.5, rely=.05)

    def initKeyTypes(self):
        frame = tk.Frame(self.app)
        frame.grid(column=0, row=1, padx=0, pady=0, sticky='W')

        caesarLabel = ttk.Label(frame, text='Khóa Caesar')
        caesarLabel.grid(column=0, row=1, padx=10, pady=0, sticky='W')

        self.caesarKey = tk.Text(frame, height=1, width=40)
        self.caesarKey.grid(column=1, row=1, sticky='W')

        railLabel = ttk.Label(frame, text='Khóa Rail Fence')
        railLabel.grid(column=0, row=2, padx=10, pady=10, sticky='W')

        self.railKey = tk.Text(frame, height=1, width=40)
        self.railKey.grid(column=1, row=2, sticky='W')

        # frame.place(in_=self.app, anchor='c', relx=.5, rely=.15)

    def initInputText(self):
        frame = tk.Frame(self.app)
        frame.grid(column=0, row=3, padx=10, pady=10, sticky='W')

        plainLabel = ttk.Label(frame, text='Bản rõ')
        plainLabel.grid(column=0, row=3, sticky='W')

        self.plainText = tk.Text(frame, height=12, width=40)
        self.plainText.grid(column=0, row=4, padx=10, pady=10, sticky='W')

        cypherLabel = ttk.Label(frame, text='Bản mã')
        cypherLabel.grid(column=1, row=3, sticky='W')

        self.cypherText = tk.Text(frame, height=12, width=40)
        self.cypherText.grid(column=1, row=4, padx=10, pady=10, sticky='W')

        # frame.place(in_=self.app, anchor='c', relx=.5, rely=.5)

    def initHandlingBtn(self):
        frame = tk.Frame(self.app)
        frame.grid(column=0, row=5, padx=5, pady=5)

        encryptBtn = tk.Button(frame, text='Mã hóa', command=self.encrypt)
        encryptBtn.grid(column=0, row=5, padx=5, pady=5)

        decryptBtn = tk.Button(frame, text='Giải mã', command=self.decrypt)
        decryptBtn.grid(column=1, row=5, padx=5, pady=5)

        # frame.place(in_=self.app, anchor='c', relx=.5, rely=.85)

    def encrypt(self):
        type = self.cypherTypes.get()
        encryptedMsg = ''
        if type == 'Caesar':
            encryptedMsg = Exec.caesarEncode(self.plainText.get("1.0", "end-1c"), int(self.caesarKey.get("1.0", "end-1c")))
        elif type == 'Rail Fence':
            encryptedMsg = Exec.railfenceEncode(self.plainText.get("1.0", "end-1c"), int(self.railKey.get("1.0", "end-1c")))
        elif type == 'Caesar và Rail Fence kết hợp':
            pass

        self.cypherText.delete('1.0', 'end-1c')
        self.cypherText.insert('1.0', encryptedMsg)

    def decrypt(self):
        type = self.cypherTypes.get()
        decryptedMsg = ''
        if type == 'Caesar':
            decryptedMsg = Exec.caesarDecode(self.cypherText.get("1.0", "end-1c"), int(self.caesarKey.get("1.0", "end-1c")))
        elif type == 'Rail Fence':
            decryptedMsg = Exec.railfenceDecode(self.cypherText.get("1.0", "end-1c"), int(self.railKey.get("1.0", "end-1c")))
        elif type == 'Caesar và Rail Fence kết hợp':
            pass

        self.plainText.delete('1.0', 'end-1c')
        self.plainText.insert('1.0', decryptedMsg)