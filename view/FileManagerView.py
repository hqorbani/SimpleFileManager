import ttkbootstrap as ttk
from tkinter import filedialog
from tkinter import messagebox

class FileManagerView:
    def __init__(self):
        self.root = ttk.Window(themename="flatly")
        self.root.title("مدیریت فایل‌ها")
        self.root.geometry("600x400")

        self.upload_button = ttk.Button(self.root, text="بارگذاری فایل")
        self.upload_button.pack(pady=10)

        self.delete_button = ttk.Button(self.root, text="حذف فایل انتخاب‌شده")
        self.delete_button.pack(pady=10)

        self.file_listbox = ttk.Treeview(self.root, columns=("ID", "Filename"), show="headings")
        self.file_listbox.heading("ID", text="شناسه")
        self.file_listbox.heading("Filename", text="نام فایل")
        self.file_listbox.pack(fill="both", expand=True, padx=10, pady=10)

    def select_file(self):
        return filedialog.askopenfilename()

    def get_selected_file_id(self):
        selected = self.file_listbox.selection()
        if selected:
            return int(self.file_listbox.item(selected[0])["values"][0])
        else:
            raise Exception("هیچ فایلی انتخاب نشده است.")

    def update_file_list(self, files):
        for item in self.file_listbox.get_children():
            self.file_listbox.delete(item)
        for file in files:
            self.file_listbox.insert("", "end", values=(file[0], file[1]))

    def run(self):
        self.root.mainloop()
