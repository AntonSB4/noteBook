from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.geometry('800x600+600+200')
root.title('Notepad')


def about_program():
    messagebox.showinfo(title='About Notepad', message='Program Notepad\nversion 0.1')


def notepad_quit():
    answer = messagebox.askyesno(title='Quit', message='Close the program?')
    if answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title='Choice file', filetypes=(('Text files', '*.txt'),
                                                                           ('All files', '*.*')))
    if file_path:
        text_area.delete("1.0", END)
        with open(file_path, 'r', encoding='utf-8') as file:
            text_area.insert("1.0", file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(title='Save file', filetypes=(('Text files', '*.txt'),
                                                                           ('All files', '*.*')))
    with open(file_path, 'w', encoding='utf-8') as file:
        new_text = text_area.get('1.0', END)
        file.write(new_text)


def cheng_theme(theme):
    text_area['bg'] = theme_colors[theme]['text_bg']
    text_area['fg'] = theme_colors[theme]['text_fg']
    text_area['insertbackground'] = theme_colors[theme]['cursor']
    text_area['selectbackground'] = theme_colors[theme]['select_bg']


main_menu = Menu(root)
root.config(menu=main_menu)

# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Quit', command=notepad_quit)
main_menu.add_cascade(label='File', menu=file_menu)

# Other
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label='Light Theme', command=lambda: cheng_theme('light'))
theme_menu_sub.add_command(label='Dark Theme', command=lambda: cheng_theme('dark'))
theme_menu.add_cascade(label='Theme', menu=theme_menu_sub)
theme_menu.add_command(label='About', command=about_program)
main_menu.add_cascade(label='Other', menu=theme_menu)


text = Frame(root)
text.pack(fill=BOTH, expand=1)

theme_colors = {
    "dark": {
        "text_bg": "#545d45", "text_fg": "#fff", "cursor": "#edf878", "select_bg": "#4e5a45"
    },
    "light": {
        "text_bg": "#fff", "text_fg": "#000", "cursor": "#8000ff", "select_bg": "#777"

    }
}

text_area = Text(text, bg=theme_colors['dark']['text_bg'], fg=theme_colors['dark']['text_fg'], padx=15, pady=10,
                 wrap=WORD, insertbackground=theme_colors['dark']['cursor'],
                 selectbackground=theme_colors['dark']['select_bg'], spacing3=10, font=('Arial', 12))
text_area.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(text, command=text_area.yview)
scroll.pack(fill=Y, side=LEFT)
text_area.config(yscrollcommand=scroll.set)

root.mainloop()
