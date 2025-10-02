from db.db_connection import Database
from db.db_schema import create_tables
from model.FileModel import FileModel
from view.FileManagerView import FileManagerView
from controller.FileManagerController import FileManagerController

def main():
    # اتصال به دیتابیس
    db = Database()
    create_tables(db)

    # ساخت اجزای MVC
    model = FileModel(db)
    view = FileManagerView()
    controller = FileManagerController(model, view)

    # اجرای رابط کاربری
    view.run()

    # بستن اتصال دیتابیس در پایان
    db.close()

if __name__ == "__main__":
    main()
