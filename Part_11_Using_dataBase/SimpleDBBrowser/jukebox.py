import sqlite3
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

conn = sqlite3.connect("music.db")


class ScrollBox(tkinter.Listbox):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky,
                     rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse',
                            rowspan=rowspan, columnspan=columnspan, **kwargs)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(ScrollBox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)
        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.sql_select = 'SELECT ' + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_select += " ORDER BY " + ",".join(sort_order)
        else:
            self.sql_select += " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def requery(self):

        self.cursor.execute(self.sql_select)

        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])


def get_albums(event):
    lb = event.widget
    index = lb.curselection()[0]

    artist_name = lb.get(index),

    artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name = ?", artist_name).fetchone()

    alist = []
    for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ? ORDER BY albums.name", artist_id):
        alist.append(row[0])

    albumLV.set(tuple(alist))
    songLV.set(("Choose an album...", ))


def get_songs(event):
    lb = event.widget
    index = lb.curselection()[0]
    album_name = lb.get(index),

    album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name = ?", album_name).fetchone()

    alist = []

    for row in conn.execute("SELECT songs.title FROM songs WHERE songs.album = ? ORDER BY songs.track", album_id):
        alist.append(row[0])

    songLV.set(tuple(alist))


mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browser")
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=2)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ======= labels =======
tkinter.Label(mainWindow, text='Artists').grid(row=0, column=0)
tkinter.Label(mainWindow, text='Albums').grid(row=0, column=1)
tkinter.Label(mainWindow, text='Songs').grid(row=0, column=2)

# ====== Artist Listbox ======
artistList = DataListBox(mainWindow, conn, 'artists', 'name')
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

artistList.requery()

artistList.bind('<<ListboxSelect>>', get_albums)

# ====== Albums Listbox ======
albumLV = tkinter.Variable(mainWindow)
albumLV.set(('Choose an artist', ))
albumList = DataListBox(mainWindow, conn, 'albums', 'name')
albumList.requery()
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

albumList.bind('<<ListboxSelect>>', get_songs)

# ====== Song Listbox ======
songLV = tkinter.Variable(mainWindow)
songLV.set(('Choose an album', ))
songList = DataListBox(mainWindow, conn, 'songs', 'title')
songList.requery()
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

# ====== Main Loop ======
# albumLV .set(tuple(range(1, 100)))
mainWindow.mainloop()
print("closing database connection")
conn.close()
