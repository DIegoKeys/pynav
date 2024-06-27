import tkinter as tk
from tkinter import ttk
from typing import Union
from .data_cursor import DataCursor

class Navigator:
    def __init__(self, tkWindow: tk.Tk):
        self.records = []
        self.tkWindow = tkWindow
        self._tree = None
        self.create_nav()

    @property
    def get_navigator_tree(self):
        return self._tree

    def get_element_by_index(self, indexOfNavElement):
        return list(self.nav_frame.children.items())[indexOfNavElement][1]

    def add_element(self, obj: Union[ttk.Button, ttk.Entry]):
        if isinstance(obj, ttk.Button):
            new_btn = ttk.Button(self.nav_frame, text=obj["text"], command=obj["command"])
            new_btn.pack(side="left")
        if isinstance(obj, ttk.Entry):
            entry = ttk.Entry(self.nav_frame)
            entry.pack(side="left")

    def fill_table(self, cursor: DataCursor):
        headers = cursor.get_headers()
        self._tree["columns"] = headers
        self._tree.column("#0", width=0, stretch=tk.NO)
        for item in headers:
            self._tree.heading(item, text=item, anchor=tk.W)

        self.records = cursor.data
        self.of_label.config(text="de " + str(len(self.records)))
        tree_id = 0
        for record in self.records:
            self._tree.insert('', 'end', iid=tree_id, values=list(record))
            tree_id += 1
        self._tree.pack(fill="both", expand=True)

    def __on_treeview_click(self, event):
        self.page_entry.delete(0, "end")
        self.page_entry.insert(0, str(int(self._tree.selection()[0]) + 1))

    def create_nav(self):
        self.nav_frame = ttk.Frame(self.tkWindow)
        self.nav_frame.pack(side="top", fill="x")

        self.first_btn = ttk.Button(self.nav_frame, text="|<", command=self.first_record)
        self.first_btn.pack(side="left")

        self.prev_btn = ttk.Button(self.nav_frame, text="<", command=self.previous_record)
        self.prev_btn.pack(side="left")

        self.page_entry = ttk.Entry(self.nav_frame, width=5)
        self.page_entry.pack(side="left")
        self.page_entry.insert(0, "1")

        self.of_label = ttk.Label(self.nav_frame, text="de " + str(len(self.records)))
        self.of_label.pack(side="left")

        self.next_btn = ttk.Button(self.nav_frame, text=">", command=self.next_record)
        self.next_btn.pack(side="left")

        self.last_btn = ttk.Button(self.nav_frame, text=">|", command=self.last_record)
        self.last_btn.pack(side="left")

        self.table_frame = ttk.Frame(self.tkWindow)
        self.table_frame.pack(fill="both", expand=True)
        self._tree = ttk.Treeview(self.table_frame)

        self._tree.bind("<ButtonRelease-1>", self.__on_treeview_click)

    def first_record(self):
        self._tree.selection_set(0)
        self.page_entry.delete(0, "end")
        self.page_entry.insert(0, str(int(self._tree.selection()[0]) + 1))

    def previous_record(self):
        try:
            self._tree.selection_set(int(self._tree.selection()[0]) - 1)
            self.page_entry.delete(0, "end")
            self.page_entry.insert(0, str(int(self._tree.selection()[0]) + 1))
        except (IndexError, tk.TclError):
            self._tree.selection_set(0)
            self.page_entry.delete(0, "end")
            self.page_entry.insert(0, str(int(self._tree.selection()[0]) + 1))

    def next_record(self):
        try:
            if int(self._tree.selection()[0]) >= len(self.records) - 1:
                self._tree.selection_set(0)
                self.page_entry.delete(0, "end")
                self.page_entry.insert(0, str(int(self._tree.selection()[0]) + 1))
            else:
                self._tree.selection_set(int(self._tree.selection()[0]) + 1)
                self.page_entry.delete(0, "end")
                self.page_entry.insert(0, str(int(self._tree.selection()[0]) + 1))
        except (IndexError, tk.TclError):
            self._tree.selection_set(0)
            self.page_entry.delete(0, "end")
            self.page_entry.insert(0, str(int(self._tree.selection()[0]) + 1))

    def last_record(self):
        self._tree.selection_set(len(self.records) - 1)
        self.page_entry.delete(0, "end")
        self.page_entry.insert(0, str(int(self._tree.selection()[0]) + 1))