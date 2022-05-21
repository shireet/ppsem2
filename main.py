import tkinter as tk
from detect import *
from search import *
from tkinter.ttk import *
import webbrowser
from tkinter import filedialog as fd

root = tk.Tk()
root.title("List App")
root.geometry("400x400")

list_data = []
links = []
def clicked():

    listbox.insert(tk.END, content.get())
    list_data.append(content.get())
    content.set("")

def delete():

    listbox.delete(0, tk.END)
    list_data.clear()


def delete_selected():

    selected = listbox.get(listbox.curselection())
    listbox.delete(tk.ANCHOR)
    list_data.remove(selected)



def callback(url):
    webbrowser.open_new_tab(url)



def new_window(links):
    win = tk.Toplevel(root)
    win.title("Links")
    win.geometry("400x250")
    Label(win, text="Links to recipe").pack()
    listbox = tk.Listbox(win, height=15, width=25)
    listbox.pack()
    for i in links:
        listbox.insert(tk.END, i)
        listbox.bind("<Button-1>", lambda e :
        callback(i))

def file():
    global list_data
    filename = fd.askopenfilename()
    list_data = detect(filename)
    list_data = list(set(list_data))
    if len(list_data) != 0:
        go()

def go():

    links = make(list_data)
    if len(links)>0:
        new_window(links)
    else:
        Label(text="No recipes found").pack()




content = tk.StringVar()
entry = tk.Entry(root, textvariable=content)
entry.pack()


button = tk.Button(root, text="Add Item", command=clicked)
button.pack()


button_delete = tk.Button(text="Delete", command=delete)
button_delete.pack()


button_delete_selected = tk.Button(text="Delete Selected", command=delete_selected)
button_delete_selected.pack()


listbox = tk.Listbox(root)
listbox.pack()


button_search = tk.Button(text="Search", command=go)
button_search.pack()


button_file = tk.Button(text="import a file", command=file)
button_file.pack()


root.mainloop()