import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, messagebox
import NotePadController
import traceback


class Notepad:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry('1200x800')
        self.root.title('MyNotePad')
        self.root.wm_iconbitmap('icons/icon.ico')
        self.main_menu = tk.Menu()
        self.new_icon = tk.PhotoImage(file='icons/new.png')
        self.open_icon = tk.PhotoImage(file='icons/open.png')
        self.save_icon = tk.PhotoImage(file='icons/save.png')
        self.save_as_icon = tk.PhotoImage(file='icons/save_as.png')
        self.exit_icon = tk.PhotoImage(file='icons/exit.png')
        self.file = tk.Menu(self.main_menu, tearoff=False)
        self.copy_icon = tk.PhotoImage(file='icons/copy.png')
        self.paste_icon = tk.PhotoImage(file='icons/paste.png')
        self.cut_icon = tk.PhotoImage(file='icons/cut.png')
        self.clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
        self.find_icon = tk.PhotoImage(file='icons/find.png')
        self.edit = tk.Menu(self.main_menu, tearoff=False)
        self.tool_bar_icon = tk.PhotoImage(file='icons/tool_bar.png')
        self.status_bar_icon = tk.PhotoImage(file='icons/status_bar.png')
        self.view = tk.Menu(self.main_menu, tearoff=False)
        self.light_default_icon = tk.PhotoImage(file='icons/light_default.png')
        self.light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
        self.dark_icon = tk.PhotoImage(file='icons/dark.png')
        self.red_icon = tk.PhotoImage(file='icons/red.png')
        self.monokai_icon = tk.PhotoImage(file='icons/monokai.png')
        self.night_blue_icon = tk.PhotoImage(file='icons/night_blue.png')
        self.color_theme = tk.Menu(self.main_menu, tearoff=False)
        self.theme_choice = tk.StringVar()
        self.color_icons = (
            self.light_default_icon, self.light_plus_icon, self.dark_icon, self.red_icon, self.monokai_icon,
            self.night_blue_icon)
        self.color_dict = {
            'Light Default ': ('#000000', '#ffffff'),
            'Light Plus': ('#474747', '#e0e0e0'),
            'Dark': ('#c4c4c4', '#2d2d2d'),
            'Red': ('#2d2d2d', '#ffe8e8'),
            'Monokai': ('#d3b774', '#474747'),
            'Night Blue': ('#ededed', '#6b9dc2')
        }
        self.main_menu.add_cascade(label='File', menu=self.file)
        self.main_menu.add_cascade(label='Edit', menu=self.edit)
        self.main_menu.add_cascade(label='View', menu=self.view)
        self.main_menu.add_cascade(label='Color Theme', menu=self.color_theme)
        self.tool_bar = ttk.Label(self.root)
        self.tool_bar.pack(side=tk.TOP, fill=tk.X)
        ## font box
        self.font_tuple = tk.font.families()
        self.font_family = tk.StringVar()
        self.font_box = ttk.Combobox(self.tool_bar, width=30, textvariable=self.font_family, state='readonly')
        self.font_box['values'] = self.font_tuple
        self.font_box.current(self.font_tuple.index('Arial'))
        self.font_box.grid(row=0, column=0, padx=5)
        ## size box
        self.size_var = tk.IntVar()
        self.font_size = ttk.Combobox(self.tool_bar, width=14, textvariable=self.size_var, state='readonly')
        self.font_size['values'] = tuple(range(8, 81))
        self.font_size.current(4)
        self.font_size.grid(row=0, column=1, padx=5)
        ## bold button
        self.bold_icon = tk.PhotoImage(file='icons/bold.png')
        self.bold_btn = ttk.Button(self.tool_bar, image=self.bold_icon)
        self.bold_btn.grid(row=0, column=2, padx=5)
        ## italic button
        self.italic_icon = tk.PhotoImage(file='icons/italic.png')
        self.italic_btn = ttk.Button(self.tool_bar, image=self.italic_icon)
        self.italic_btn.grid(row=0, column=3, padx=5)
        ## underline button
        self.underline_icon = tk.PhotoImage(file='icons/underline.png')
        self.underline_btn = ttk.Button(self.tool_bar, image=self.underline_icon)
        self.underline_btn.grid(row=0, column=4, padx=5)
        ## font color button
        self.font_color_icon = tk.PhotoImage(file='icons/font_color.png')
        self.font_color_btn = ttk.Button(self.tool_bar, image=self.font_color_icon)
        self.font_color_btn.grid(row=0, column=5, padx=5)
        ## align left
        self.align_left_icon = tk.PhotoImage(file='icons/align_left.png')
        self.align_left_btn = ttk.Button(self.tool_bar, image=self.align_left_icon)
        self.align_left_btn.grid(row=0, column=6, padx=5)
        ## align center
        self.align_center_icon = tk.PhotoImage(file='icons/align_center.png')
        self.align_center_btn = ttk.Button(self.tool_bar, image=self.align_center_icon)
        self.align_center_btn.grid(row=0, column=7, padx=5)
        ## align right
        self.align_right_icon = tk.PhotoImage(file='icons/align_right.png')
        self.align_right_btn = ttk.Button(self.tool_bar, image=self.align_right_icon)
        self.align_right_btn.grid(row=0, column=8, padx=5)
        ## mike
        self.mike_icon = tk.PhotoImage(file='icons/microphone.png')
        self.mike_btn = ttk.Button(self.tool_bar, image=self.mike_icon)
        self.mike_btn.grid(row=0, column=9, padx=5)
        # -------------------------------------&&&&&&&& End toolbar  &&&&&&&&&&& ----------------------------------
        ############################################## text editor ###################################################
        self.text_editor = tk.Text(self.root)
        self.text_editor.config(wrap='word', relief=tk.FLAT)

        self.scroll_bar = tk.Scrollbar(self.root)
        self.text_editor.focus_set()
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_editor.pack(fill=tk.BOTH, expand=True)
        self.scroll_bar.config(command=self.text_editor.yview)
        self.text_editor.config(yscrollcommand=self.scroll_bar.set)

        # font family and font size functionality
        self.current_font_family = 'Arial'
        self.current_font_size = 12
        self.font_box.bind("<<ComboboxSelected>>", self.change_font)
        self.font_size.bind("<<ComboboxSelected>>", self.change_fontsize)
        self.bold_btn.configure(command=self.change_bold)
        self.italic_btn.configure(command=self.change_italic)
        self.underline_btn.configure(command=self.change_underline)
        self.root.config(menu=self.main_menu)

        self.file.add_command(label='New', image=self.new_icon, compound=tk.LEFT, accelerator='Ctrl+N',
                              command=self.new_file)
        self.url = ''
        self.file.add_command(label='Open', image=self.open_icon, compound=tk.LEFT, accelerator='Ctrl+O',
                              command=self.open_file)
        self.file.add_command(label='Save', image=self.save_icon, compound=tk.LEFT, accelerator='Ctrl+S',
                              command=self.save_file)
        self.file.add_command(label='Save As', image=self.new_icon, compound=tk.LEFT, accelerator='Alt+S',
                              command=self.save_as)
        self.file.add_command(label='Exit', image=self.exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q',
                              command=self.exit_func)
        self.text_changed = False
        self.text_editor.bind('<<Modified>>', self.changed)
        self.status_bar = ttk.Label(self.root, text='Status Bar')
        self.status_bar.pack(side=tk.BOTTOM)
        self.count = 0
        self.show_statusbar = tk.BooleanVar()
        self.show_statusbar.set(True)
        self.show_toolbar = tk.BooleanVar()
        self.show_toolbar.set(True)
        for i in self.color_dict:
            self.color_theme.add_radiobutton(label=i, image=self.color_icons[self.count], variable=self.theme_choice,
                                             compound=tk.LEFT, command=self.change_theme)
            self.count += 1
        self.view.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=0, variable=self.show_toolbar,
                                  image=self.tool_bar_icon,
                                  compound=tk.LEFT, command=self.hide_toolbar)
        self.view.add_checkbutton(label='Status Bar', onvalue=1, offvalue=False, variable=self.show_statusbar,
                                  image=self.status_bar_icon, compound=tk.LEFT, command=self.hide_statusbar)

        self.edit.add_command(label='Copy', image=self.copy_icon, compound=tk.LEFT, accelerator='Ctrl+C',
                              command=lambda: self.text_editor.event_generate("<Control c>"))
        self.edit.add_command(label='Paste', image=self.paste_icon, compound=tk.LEFT, accelerator='Ctrl+V',
                              command=lambda: self.text_editor.event_generate("<Control v>"))
        self.edit.add_command(label='Cut', image=self.cut_icon, compound=tk.LEFT, accelerator='Ctrl+X',
                              command=lambda: self.text_editor.event_generate("<Control x>"))
        self.edit.add_command(label='Clear All', image=self.clear_all_icon, compound=tk.LEFT, accelerator='Alt+X',
                              command=lambda: self.text_editor.delete(1.0, tk.END))
        self.edit.add_command(label='Find', image=self.find_icon, compound=tk.LEFT, accelerator='Ctrl+F',
                              command=self.find_func)
        self.root.bind("<Control-n>", self.new_file)
        self.root.bind("<Control-N>", self.new_file)
        self.root.bind("<Control-o>", self.open_file)
        self.root.bind("<Control-O>", self.open_file)
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-S>", self.save_file)
        self.root.bind("<Alt-s>", self.save_as)
        self.root.bind("<Alt-S>", self.save_as)
        self.root.bind("<Control-q>", self.exit_func)
        self.root.bind("<Control-Q>", self.exit_func)
        self.root.bind("<Control-f>", self.find_func)
        self.root.bind("<Control-F>", self.find_func)
        self.font_color_btn.configure(command=self.change_font_color)
        self.align_right_btn.configure(command=self.align_right)
        self.align_center_btn.configure(command=self.align_center)
        self.align_left_btn.configure(command=self.align_left)
        self.mike_btn.configure(command=self.saySomething)
        self.root.bind("<Control-a>", lambda e: self.saySomething())
        self.root.bind("<Control-A>", lambda e: self.saySomething())
        self.notepadContrller = NotePadController.Controller()

    def saySomething(self):
        try:
            self.takeAudio = self.notepadContrller.saysomeThing()
            print(self.takeAudio)
            if self.takeAudio == "":
                messagebox.showinfo("say again", "speech not recognize!!")
            elif self.takeAudio == 'open file':
                self.open_file()
            elif self.takeAudio == 'save file':
                self.save_file()
            elif self.takeAudio == 'new file':
                self.new_file()
            elif self.takeAudio == 'file save':
                self.save_as()
            elif self.takeAudio == 'close app':
                self.exit_func()
            elif self.takeAudio == 'text bold':
                self.change_bold()
            elif self.takeAudio == 'text italic':
                self.change_italic()
            elif self.takeAudio == 'search':
                self.find_func()
            elif self.takeAudio == 'hide statusbar':
                self.hide_statusbar()
            elif self.takeAudio == 'hide toolbar':
                self.hide_toolbar()

            else:
                messagebox.showerror("Error", "audio not match")
        except Exception as e:
            print("exception in this", e)
            print("not recognized")

    def align_left(self):

        text_content = self.text_editor.get(1.0, 'end')
        self.text_editor.tag_config('left', justify=tk.LEFT)
        self.text_editor.delete(1.0, tk.END)
        self.text_editor.insert(tk.INSERT, text_content, 'left')

    def align_center(self):

        text_content = self.text_editor.get(1.0, 'end')
        self.text_editor.tag_config('center', justify=tk.CENTER)
        self.text_editor.delete(1.0, tk.END)
        self.text_editor.insert(tk.INSERT, text_content, 'center')

    def align_right(self):

        text_content = self.text_editor.get(1.0, 'end')
        self.text_editor.tag_config('right', justify=tk.RIGHT)
        self.text_editor.delete(1.0, tk.END)
        self.text_editor.insert(tk.INSERT, text_content, 'right')

    def change_font_color(self):

        color_var = tk.colorchooser.askcolor()
        self.text_editor.configure(fg=color_var[1])

    def find(self):
        word = self.find_input.get()
        self.text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = self.text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                self.text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                self.text_editor.tag_config('match', foreground='red', background='yellow')

    def replace(self):
        word = self.find_input.get()
        self.replace_text = self.replace_input.get()
        self.content = self.text_editor.get(1.0, tk.END)
        self.new_content = self.content.replace(word, self.replace_text)
        self.text_editor.delete(1.0, tk.END)
        self.text_editor.insert(1.0, self.new_content)

    def find_func(self, event=None):
        self.find_dialogue = tk.Toplevel()
        self.find_dialogue.geometry('450x250+500+200')
        self.find_dialogue.title('Find')
        self.find_dialogue.resizable(0, 0)

        ## frame
        self.find_frame = ttk.LabelFrame(self.find_dialogue, text='Find/Replace')
        self.find_frame.pack(pady=20)

        ## labels
        self.text_find_label = ttk.Label(self.find_frame, text='Find : ')
        self.text_replace_label = ttk.Label(self.find_frame, text='Replace')

        ## entry
        self.find_input = ttk.Entry(self.find_frame, width=30)
        self.replace_input = ttk.Entry(self.find_frame, width=30)

        ## button
        self.find_button = ttk.Button(self.find_frame, text='Find', command=self.find)
        self.replace_button = ttk.Button(self.find_frame, text='Replace', command=self.replace)

        ## label grid
        self.text_find_label.grid(row=0, column=0, padx=4, pady=4)
        self.text_replace_label.grid(row=1, column=0, padx=4, pady=4)

        ## entry grid
        self.find_input.grid(row=0, column=1, padx=4, pady=4)
        self.replace_input.grid(row=1, column=1, padx=4, pady=4)

        ## button grid
        self.find_button.grid(row=2, column=0, padx=8, pady=4)
        self.replace_button.grid(row=2, column=1, padx=8, pady=4)

        self.find_dialogue.mainloop()

    def hide_toolbar(self):

        if self.show_toolbar:
            self.tool_bar.pack_forget()
            self.show_toolbar = False
        else:
            self.text_editor.pack_forget()
            self.status_bar.pack_forget()
            self.tool_bar.pack(side=tk.TOP, fill=tk.X)
            self.text_editor.pack(fill=tk.BOTH, expand=True)
            self.status_bar.pack(side=tk.BOTTOM)
            self.show_toolbar = True

    def hide_statusbar(self):

        if self.show_statusbar:
            self.status_bar.pack_forget()
            self.show_statusbar = False
        else:
            self.status_bar.pack(side=tk.BOTTOM)
            self.show_statusbar = True

    def change_theme(self):

        self.chosen_theme = self.theme_choice.get()
        self.color_tuple = self.color_dict.get(self.chosen_theme)
        self.fg_color, bg_color = self.color_tuple[0], self.color_tuple[1]
        self.text_editor.config(background=bg_color, fg=self.fg_color)

    def changed(self, event=None):

        if self.text_editor.edit_modified():
            self.text_changed = True
            words = len(self.text_editor.get(1.0, 'end-1c').split())
            characters = len(self.text_editor.get(1.0, 'end-1c'))
            self.status_bar.config(text=f'Characters : {characters} Words : {words}')
        self.text_editor.edit_modified(False)

    def exit_func(self, event=None):

        try:
            if self.text_changed:
                mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
                if mbox is True:
                    content = self.text_editor.get(1.0, tk.END)
                    self.notepadContrller.save_as(content)
                    self.root.destroy()

                elif mbox is False:
                    self.root.destroy()
            else:
                self.root.destroy()
        except:
            print(traceback.format_exc())

    def save_as(self, event=None):
        try:
            content = self.text_editor.get(1.0, tk.END)
            self.notepadContrller.save_as(content)
        except:
            print(traceback.format_exc())

    def save_file(self, event=None):
        try:
            content = self.text_editor.get(1.0, tk.END)
            self.notepadContrller.save_file(content)
        except:
            print(traceback.format_exc())

    def open_file(self, event=None):
        try:
            self.msg, self.base = self.notepadContrller.read_file()

            self.text_editor.delete(1.0, tk.END)
            self.text_editor.insert(1.0, self.msg)
            self.root.title(self.base)

        except FileNotFoundError:
            print(traceback.format_exc())
        except:
            print(traceback.format_exc())

    def new_file(self, event=None):
        self.notepadContrller.new_file()
        self.root.title("MyNotePad")
        self.text_editor.delete(1.0, tk.END)

    def change_font(self, event=None):

        self.current_font_family = self.font_family.get()
        self.text_editor.configure(font=(self.current_font_family, self.current_font_size))

    def change_fontsize(self, event=None):

        self.current_font_size = self.size_var.get()
        self.text_editor.configure(font=(self.current_font_family, self.current_font_size))

    def change_bold(self):

        self.text_property = tk.font.Font(font=self.text_editor['font'])
        if self.text_property.actual()['weight'] == 'normal':
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'bold'))
        if self.text_property.actual()['weight'] == 'bold':
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'normal'))

    def change_italic(self):

        self.text_property = tk.font.Font(font=self.text_editor['font'])
        if self.text_property.actual()['slant'] == 'roman':
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'italic'))
        if self.text_property.actual()['slant'] == 'italic':
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'normal'))

    def change_underline(self):

        self.text_property = tk.font.Font(font=self.text_editor['font'])
        if self.text_property.actual()['underline'] == 0:
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'underline'))
        if self.text_property.actual()['underline'] == 1:
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'normal'))

    def run(self):
        self.root.mainloop()


obj = Notepad()
obj.run()
