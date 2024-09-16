import os
import shutil
import tkinter as tk


class FileOrganiser:
        
    def __init__(self):    

        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("File Type Organiser")

        self.label1 = tk.Label(self.root, text="File Type Organiser", font=('Arial', 18))
        self.label1.pack(padx=20, pady=10)

        self.label2 = tk.Label(self.root, text="Input folder/directory path:", font=('Arial', 15,))
        self.label2.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=1)
        self.textbox.pack(padx=20)

        self.button = tk.Button(self.root, text="Enter", font=('Arial', 15), command=self.organise)
        self.button.pack(pady=5)

        self.root.mainloop()


    def organise(self):
        
        path = self.textbox.get('1.0', tk.END).strip()

        if not os.path.exists(path):
            print(f"Path '{path}' does not exist.")
            return
        
        files = os.listdir(path)

        for file in files:
            if os.path.isdir(os.path.join(path, file)):
                continue

            filename, extention = os.path.splitext(file)
            extention = extention [1:]

            if extention:
                ext_folder = os.path.join(path, extention)
                if not os.path.exists(ext_folder):
                    os.makedirs(ext_folder)

                shutil.move(os.path.join(path, file), os.path.join(ext_folder, file))


FileOrganiser()



#   Old function
#
#        path = input("Enter Directory")
#        files = os.listdir(path)
#
#        for file in files:
#            filename,extention = os.path.splitext(file)
#            extention = extention[1:]
#            
#            if os.path.exists(path+ '/' +extention):
#                shutil.move(path+ '/' +file, path+ '/' +extention+ '/' +file)
#            else:
#                os.makedirs(path+ '/' +extention)
#                shutil.move(path+ '/' +file, path+ '/' +extention+ '/' +file)