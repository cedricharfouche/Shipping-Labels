from cgitb import text
from pickle import TRUE
from PyPDF2 import PdfReader, PdfWriter,Transformation
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import *
import os
from pathlib import Path


root = tk.Tk()
root.title('Label Merger')
root.resizable(True, True)
root.geometry('400x150')
file = ""



def FBA_label():
   #file = fd.askopenfilename(mode='r', filetypes=[('PDF Files', '*.')])
    file = fd.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:  # Check if a file was selected
        print(f"Selected file: {file}")  # Placeholder for further action with the selected PDF file
    #file = fd.askopenfilename()
    file_name = os.path.basename(file)
    output_file_name = f"{os.path.splitext(file_name)[0]}-merged.pdf"
    reader = PdfReader(file)
    writer = PdfWriter()
    downloads_folder = str(Path.home() / "Downloads")
    output_file_path = os.path.join(downloads_folder, output_file_name)

    #newpage = writer.addBlankPage(288,576)
    count = -1


    if reader.numPages<=2:

            page1 = reader.pages[0]
            p1Trans= Transformation().scale(0.8).translate(10,-130)
            page1.add_transformation(p1Trans)

            page2 = reader.pages[1]
        #p2Trans = Transformation().translate(30,170)

        #page2.add_transformation(p2Trans)
            newpage =   writer.addBlankPage(width=page1.mediaBox.getWidth(),
                    height=page1.mediaBox.getHeight()+ 150)
        #page1.merge_page(page2,True)

            newpage.mergePage(page1)
            newpage.mergeScaledTranslatedPage(page2,1,10,215,True)

            with open(output_file_path, "wb") as fp:
                writer.write(fp)

            tk.messagebox.showinfo("PDF Merge", f"New PDF '{output_file_name}' created successfully!")


    elif reader.numPages >2:
            UPSwidth = reader.pages[1].mediaBox.getWidth()
            labelHeight = reader.pages[0].mediaBox.getHeight()

            while count < reader.numPages-1:
                page2 = reader.pages[count+1]
                #page2 = reader.pages[count +1]
                if count % 2 !=0:
                    #page1 = reader.pages[count]
                    #p2Trans= Transformation().scale(1,1).translate(10,215)
                    page1 = reader.pages[count+2]
                    #page2.add_transformation(p2Trans)
                    
                
                    newpage =   writer.addBlankPage(width=UPSwidth,
                        height=labelHeight+ 150)
                    newpage.mergeScaledTranslatedPage(page1,1,10,215,True)
                    newpage.mergeScaledTranslatedPage(page2,.9,10,-130,False)
                if count != reader.numPages: count+=1
            
            with open(output_file_path, "wb") as fp:
                writer.write(fp)

            tk.messagebox.showinfo("PDF Merge", f"New PDF '{output_file_name}' created successfully!")
               
                
def TikTok_label():
   #file = fd.askopenfilename(mode='r', filetypes=[('PDF Files', '*.')])
    file = fd.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:  # Check if a file was selected
        print(f"Selected file: {file}")  # Placeholder for further action with the selected PDF file
    #file = fd.askopenfilename()
    file_name = os.path.basename(file)
    output_file_name = f"{os.path.splitext(file_name)[0]}-merged.pdf"
    reader = PdfReader(file)
    writer = PdfWriter()
    downloads_folder = str(Path.home() / "Downloads")
    output_file_path = os.path.join(downloads_folder, output_file_name)

    #newpage = writer.addBlankPage(288,576)
    count = -1


    if reader.numPages<=2:

            page1 = reader.pages[0]
            p1Trans= Transformation().scale(1).translate(10,25)
            page1.add_transformation(p1Trans)

            page2 = reader.pages[1]
        #p2Trans = Transformation().translate(30,170)

        #page2.add_transformation(p2Trans)
            newpage =   writer.addBlankPage(width=page1.mediaBox.getWidth(),
                    height=page2.mediaBox.getHeight())
        #page1.merge_page(page2,True)

            newpage.mergePage(page1)
            newpage.mergeScaledTranslatedPage(page2,.95,10,-325,False)

            with open(output_file_path, "wb") as fp:
                writer.write(fp)

            tk.messagebox.showinfo("PDF Merge", f"New PDF '{output_file_name}' created successfully!")


    elif reader.numPages >2:
            UPSwidth = reader.pages[1].mediaBox.getWidth()
            labelHeight = reader.pages[0].mediaBox.getHeight() 

            while count < reader.numPages-1:
                page2 = reader.pages[count+1]
                
                if count % 2 !=0:
             
                    page1 = reader.pages[count+2]
                    
                
                    newpage =   writer.addBlankPage(width=UPSwidth ,
                        height=labelHeight)
                    newpage.mergeScaledTranslatedPage(page2,1,10,25,False)
                    newpage.mergeScaledTranslatedPage(page1,.95,10,-325,False)
                if count != reader.numPages: count+=1
            
            with open(output_file_path, "wb") as fp:
                writer.write(fp)

            tk.messagebox.showinfo("PDF Merge", f"New PDF '{output_file_name}' created successfully!")

style = tk.ttk.Style()
style.configure('TButton', font=('Roboto', 12), foreground='white', background='red')


browse_button = tk.ttk.Button(root, text="FBA label", command=FBA_label, style='TButton')
browse_button.pack(pady=10)

browse_button = tk.ttk.Button(root, text="TikTok label", command=TikTok_label, style='TButton')
browse_button.pack(pady=10)


root.mainloop()

  
