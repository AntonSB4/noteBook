from tkinter import *

root = Tk()
root.geometry('800x600+1000+600')
root.title('Notebook')

# menu = Frame(root, bg='#1F252A', height=40)
# menu.pack(fill=X)
text = Frame(root)
text.pack(fill=BOTH, expand=1)


text_aria = Text(text, bg='#545d45', fg='#fff', padx=15, pady=10, wrap=WORD,
                 insertbackground='#edf878', selectbackground="#4e5a45", spacing3=10)
text_aria.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(text, command=text_aria.yview)
scroll.pack(fill=Y, side=LEFT)
text_aria.config(yscrollcommand=scroll.set)

root.mainloop()
