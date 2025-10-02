from tkinter import messagebox
from messages.errors import ErrorMessages
from messages.successes import SuccessMessages
from utils.pdf_exporter import export_file_list_to_pdf
class FileManagerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.upload_button.config(command=self.upload_file)
        self.view.delete_button.config(command=self.delete_file)
        self.view.export_button.config(command=self.export_pdf)
        self.refresh_file_list()

    def upload_file(self):
        try:
            path = self.view.select_file()
            filename, saved_path = self.model.save_file(path)
            messagebox.showinfo("موفقیت", SuccessMessages.SUCCESS_FILE_UPLOAD)
            self.refresh_file_list()
        except Exception as e:
            messagebox.showerror("خطا", ErrorMessages.ERROR_FILE_UPLOAD + str(e))

    def delete_file(self):
        try:
            file_id = self.view.get_selected_file_id()
            self.model.delete_file(file_id)
            messagebox.showinfo("موفقیت", SuccessMessages.SUCCESS_FILE_DELETE)
            self.refresh_file_list()
        except Exception as e:
            messagebox.showerror("خطا", ErrorMessages.ERROR_FILE_DELETE + str(e))
    
    def export_pdf(self):
        try:
            file_list = self.model.get_all_files()
            export_file_list_to_pdf(file_list)
            messagebox.showinfo("موفقیت", SuccessMessages.SUCCESS_PUBLISH_PDF)
        except Exception as e:
            messagebox.showerror("خطا", ErrorMessages.ERROR_PUBLISH_PDF + str(e))
    
    def refresh_file_list(self):
        files = self.model.get_all_files()
        self.view.update_file_list(files)
