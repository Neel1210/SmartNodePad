from tkinter import filedialog
import os
import threading
import speech_recognition as s

class Model:
    def __init__(self):
        self.url = ""
        self.key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.offset = 5

    def save_file(self, msg):

        if self.url:
            print(self.url)
            print("a")
            filename, file_extension = os.path.splitext(self.url)
            if file_extension in '.ntxt':
                content = msg
                encrypted = self.encrypt(content)
                with open(self.url, 'w', encoding='utf-8') as fw:
                    fw.write(encrypted)
            else:
                content = msg
                with open(self.url, 'w', encoding='utf-8') as fw:
                    fw.write(content)
        else:
            print("b")
            print(self.url)
            # self.url = filedialog.asksaveasfile(mode='w', defaultextension='.ntxt',
            #                                     filetypes=([("All Files", "*.*"),
            #                                                 ("Text Documents", "*.txt")]))
            self.url = filedialog.askopenfilename(title='Select File',
                                                  filetypes=[("Text Documents", "*.*")])
            with open(self.url, 'w', encoding='utf-8') as fw:

                print(self.url)
                content2 = msg
                encrypted = self.encrypt(content2)

                fw.write(encrypted)
                fw.close()

    def save_as(self, msg1):

        content = msg1
        encrypted = self.encrypt(content)

        self.url = filedialog.asksaveasfile(mode='w', defaultextension='.ntxt',
                                            filetypes=([("All Files", "*.*"), ("Text Documents", "*.txt")]))
        self.url.write(encrypted)
        self.url.close()

    def open_file(self):

        self.url = filedialog.askopenfilename(title='Select File',
                                              filetypes=[("Text Documents", "*.*")])
        return self.url


    def new_file(self):
        self.url = ""

    def read_file(self):
        self.url=self.open_file()
        base = os.path.basename(self.url)
        filename, file_extension = os.path.splitext(self.url)

        if file_extension in '.ntxt':

            fi = open(self.url, "r")
            msg1 = fi.read()
            decrypted = self.decrypt(msg1)
            fi.close()
            return decrypted, base



        else:

            fi = open(self.url, "r")
            msg1 = fi.read()
            fi.close()
            return msg1, base

    def encrypt(self,plaintext):

        result = ''

        for l in plaintext:
            try:
                i = (self.key.index(l) + self.offset) % 62
                result += self.key[i]
            except ValueError:
                result += l

        return result

    def decrypt(self,ciphertext):

        result = ''

        for l in ciphertext:
            try:
                i = (self.key.index(l) - self.offset) % 62
                result += self.key[i]
            except ValueError:
                result += l

        return result

    # def saySomething(self):
    #
    #     t = threading.Thread(target=self.takeQuery)
    #
    #     t.start()

    def takeQuery(self):

        sr = s.Recognizer()
        sr.pause_threshold = 1
        print("speak")
        with s.Microphone() as m:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            return query
