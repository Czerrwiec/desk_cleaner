import os
import customtkinter as ctk
import shutil
import json
from sys import argv

from pathlib import Path


path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

path = 'C:\\Users\\Cad Projekt\\Desktop'

path_01 = 'C:\\Users\\Public\\Desktop'

ctk.set_appearance_mode('System')       

images = ['.jpg', '.png', '.gif']
texts = ['.txt', '.odt', '.ods']


with open(os.path.dirname(os.path.realpath(argv[0])) + '\\' + 'config.json') as file:
    json_data = json.load(file)
    print(json_data)


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('cleaner')    
        self.geometry('200x170') 
          
        self.list_of_all_paths = []
        self.folder_list = []
        self.pdf_list = []
        self.images_list = []
        self.texts_list = []
        self.video_list = []
        self.archives_list = []


        self.sort_button = ctk.CTkButton(self, text="Sortuj pliki", font=("Noto Sans", 15), width=130, height=50)
        self.sort_button.pack(pady=(20, 10), padx=(20, 20), side="top")

        self.default_button = ctk.CTkButton(self, text="Przywróć pulpit", font=("Noto Sans", 15), width=130, height=50)
        self.default_button.pack(pady=(10, 20), padx=(20, 20), side="top")



    def make_list_from_all(self, path):
        list_of_all = []
        files = os.listdir(path)   
        for file in files:
            list_of_all.append(path + '\\' + file)

            print(file)

        return list_of_all
            # self.list_of_all_paths.append(path + '\\' + file)
        

    def delete_shortcuts(self):
        shortcuts_to_delete = []
        files = os.listdir(path_01)
        for file in files:
            if file.startswith(".4CAD") or file.startswith("CAD Decor") or file.startswith("CAD Kuchnie") or file == "Tiles Base Editor.lnk":
                shortcuts_to_delete.append(path_01 + '\\' + file)
        for item in shortcuts_to_delete:
            os.remove(item)
            


    def categorize(self):
        self.list_of_all_paths = self.make_list_from_all(path)

        for item in self.list_of_all_paths:
            if os.path.isdir(item):
                self.folder_list.append(item)

            elif item.endswith('.pdf'):
                self.pdf_list.append(item)

            elif item.endswith('.mp4'):
                self.video_list.append(item) 

            elif item.endswith('.zip'):
                self.archives_list.append(item)

            elif os.path.splitext(item)[1] in images:
                self.images_list.append(item)

            elif os.path.splitext(item)[1] in texts:
                self.texts_list.append(item)

        # self.create_folder_and_move(self.pdf_list, 'pdf_files')
        # self.create_folder_and_move(self.images_list, 'image_files')
        # self.create_folder_and_move(self.texts_list, 'text_files')
        # self.create_folder_and_move(self.video_list, 'video_files')
        # self.create_folder_and_move(self.archives_list, 'archive_files')
        


    def create_folder_and_move(self, files_list, folder_name):

        folder = path + "\\" + folder_name

        if len(files_list) > 0:
            if os.path.isdir(folder) == False:
                os.mkdir(folder)    
            for item in files_list:
                shutil.move(item, folder)



       
        # self.delete_shortcuts()
        

        


 
if __name__ == '__main__':
    app = App()
    app.categorize()
    app.mainloop()





