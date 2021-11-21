# Luu Minh Tri, 20/11/2021
# GUI.PY -- graphic user interface for application
# ** require tkinter

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as msgb

from exec import Exec

import time
from threading import Thread
import queue

APP_TITLE = 'Bài tập lớn MM&ANM đề tài 1 (20/11/2021)'
APP_SIZE = '900x520'
APP_AUTHORS = '''
1. Lưu Minh Trí, 1811298
2. Lê Đình Duy, 1810861
3. Đinh Thái Vinh, 1713964
4. Dương Quân Bảo, 1927003
'''
APP_CONTACT = '''
Repository: https://github.com/ume16/cypher-encrypt-decrypt
Email: tri.luuminh@hcmut.edu.vn
'''
class App: 
    def __init__(self):
        self.app = tk.Tk()
        self.app.title(APP_TITLE)
        self.app.geometry(APP_SIZE)
        self.app.resizable(False, False)
        self.app.config(menu=self.initMenu())

        self.initCypherTypes()
        self.initKeyTypes()
        self.initStatus()
        self.initInputText()
        self.initHandlingBtn()

    def run(self):
        self.app.mainloop()

    def showAuthor(self):
        msgb.showinfo(title='Tác giả', message=APP_AUTHORS)

    def showLicense(self):
        msgb.showinfo(title='Liên hệ', message=APP_CONTACT)

    def readfile(self):
        file = fd.askopenfile(filetypes=[("Text files", "*.txt")])
        if file is not None:
            path = file.name
            f = open(path, mode='r', encoding="utf8")
            text = f.read()
            f.close()

            self.plainText.delete("1.0", "end")
            self.plainText.insert("1.0", text)
        
            # self.statusLabel.config('Đọc file thành công')

    def savefile(self):
        file = fd.asksaveasfile(filetypes=[("Text files", "*.txt")])
        if file is not None:
            filepath = file.name
            with open(filepath, "w", encoding="utf8") as f:
                f.write(self.cypherText.get("1.0", "end-1c"))
                f.close()

                # self.statusLabel.config('Lưu file thành công')

    def initMenu(self):
        menu = tk.Menu(self.app)

        file = tk.Menu(menu, tearoff=0)
        file.add_command(label='Mở file', command=self.readfile)
        file.add_command(label='Lưu file', command=self.savefile)
        file.add_command(label='Thoát', command=self.app.quit)
        menu.add_cascade(label='File', menu=file)

        about = tk.Menu(menu, tearoff=0)
        about.add_command(label='Tác giả', command=self.showAuthor)
        about.add_command(label='Thông tin liên hệ', command=self.showLicense)
        menu.add_cascade(label='Thông tin', menu=about)

        return menu

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

    def initStatus(self):
        frame = tk.Frame(self.app)
        frame.grid(column=0, row=3, padx=10, sticky='W')

        self.statusLabel = ttk.Label(frame, text='Sẵn sàng', foreground='green')
        self.statusLabel.grid(column=0, row=3, sticky='W')

    def initInputText(self):
        frame = tk.Frame(self.app)
        frame.grid(column=0, row=4, padx=10, pady=5, sticky='W')

        plainLabel = ttk.Label(frame, text='Bản rõ')
        plainLabel.grid(column=0, row=4, sticky='W')

        self.plainText = tk.Text(frame, height=12, width=40)
        self.plainText.grid(column=0, row=5, padx=10, pady=10, sticky='W')

        cypherLabel = ttk.Label(frame, text='Bản mã')
        cypherLabel.grid(column=1, row=4, sticky='W')

        self.cypherText = tk.Text(frame, height=12, width=40)
        self.cypherText.grid(column=1, row=5, padx=10, pady=10, sticky='W')

        # frame.place(in_=self.app, anchor='c', relx=.5, rely=.5)

    def initHandlingBtn(self):
        frame = tk.Frame(self.app)
        frame.grid(column=0, row=5, padx=5, pady=5)

        encryptBtn = tk.Button(frame, text='Mã hóa', command=self.encrypt)
        encryptBtn.grid(column=0, row=5, padx=5, pady=5)

        decryptBtn = tk.Button(frame, text='Giải mã', command=self.decryptThread)
        decryptBtn.grid(column=1, row=5, padx=5, pady=5)

        # frame.place(in_=self.app, anchor='c', relx=.5, rely=.85)

    def encrypt(self):
        self.statusLabel.config(text='Đang mã hóa ...', foreground='red')
        self.app.update()

        start = time.time()
        type = self.cypherTypes.get()
        plainMsg = self.plainText.get("1.0", "end-1c")
        if self.caesarKey.get("1.0", "end-1c") != '':
            cKey = int(self.caesarKey.get("1.0", "end-1c"))
        if self.railKey.get("1.0", "end-1c") != '':
            rKey = int(self.railKey.get("1.0", "end-1c"))
        encryptedMsg = ''
        if type == 'Caesar':
            encryptedMsg = Exec.caesarEncode(plainMsg, cKey)
        elif type == 'Rail Fence':
            encryptedMsg = Exec.railfenceEncode(plainMsg, rKey)
        else:
            encryptedMsg = Exec.jointEncode(plainMsg, cKey, rKey)

        self.cypherText.delete('1.0', 'end-1c')
        self.cypherText.insert('1.0', encryptedMsg)

        status = 'Mã hóa thành công trong ' + "{:.4f}".format(time.time() - start) + 's'
        self.statusLabel.config(text=status, foreground='green')

    def decryptThread(self):
        thread = Thread(target=self.decrypt)
        thread.start()

    def decrypt(self):
        self.statusLabel.config(text='Đang giải mã ...', foreground='red')
        self.app.update()

        start = time.time()
        cipherMsg = self.cypherText.get('1.0', 'end-1c')
        cKey, rKey, plainMsg = Exec.decrypt(cipherMsg)

        self.caesarKey.delete('1.0', 'end-1c')
        self.caesarKey.insert('1.0', cKey)

        self.railKey.delete('1.0', 'end-1c')
        self.railKey.insert('1.0', rKey)

        self.plainText.delete('1.0', 'end-1c')
        self.plainText.insert('1.0', plainMsg)

        status = 'Giải mã thành công trong ' + "{:.4f}".format(time.time() - start) + 's'
        self.statusLabel.config(text=status, foreground='green')