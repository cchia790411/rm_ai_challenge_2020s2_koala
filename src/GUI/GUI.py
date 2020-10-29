#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.5
#  in conjunction with Tcl version 8.6
#    Oct 27, 2020 01:20:33 PM +1100  platform: Windows NT

import sys
from image_processing import *
from tkinter import filedialog
from PIL import ImageTk,Image
from filemanagement import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import GUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    GUI_support.set_Tk_var()
    top = Toplevel1 (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

# ===============================================
# change image based on the slider value
def slider_show_image(value):
    top = GUI_support.w
    top.image_file_state.set_current_img_num(int(value) - 1)
    top.image_label.configure(image=top.image_file_state.get_current_img())
    # Show output if the images were already labelled.
    if len(top.image_file_state.labelled_images) > 0:
        write_output(top.Output, top.image_file_state.labelled_images[int(value) - 1])
# ===============================================

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1500x700") # top.geometry("1500x660")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(False,  False)
        # top.geometry("1198x802+266+116")
        # top.minsize(120, 1)
        # top.maxsize(3844, 1061)
        # top.resizable(1,  1)
        top.title("Object Detection Algorithm Evaluation Tool")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame_Top = tk.Frame(top)
        self.Frame_Top.place(relx=0.015, rely=0.012, relheight=0.131, relwidth=0.755)
        self.Frame_Top.configure(relief='groove')
        self.Frame_Top.configure(borderwidth="2")
        self.Frame_Top.configure(relief="groove")
        self.Frame_Top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.015, rely=0.15, relheight=0.818, relwidth=0.755)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.774, rely=0.153, relheight=0.605, relwidth=0.210)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")

        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.774, rely=0.767, relheight=0.202, relwidth=0.210)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        self.Slider = tk.Scale(self.Frame_Top, from_=0.0, to=100.0)
        self.Slider.place(relx=0.376, rely=0.090, relwidth=0.23, relheight=0.0
                , height=57, bordermode='ignore')
        self.Slider.configure(activebackground="#ececec")
        self.Slider.configure(background="#d9d9d9")
        self.Slider.configure(state=DISABLED, command=slider_show_image)    # do image showing
        self.Slider.configure(cursor="fleur")
        self.Slider.configure(foreground="#000000")
        self.Slider.configure(highlightbackground="#d9d9d9")
        self.Slider.configure(highlightcolor="black")
        self.Slider.configure(orient="horizontal")
        self.Slider.configure(troughcolor="#d9d9d9")

        # image show =================================
        self.image_file_state = ImageFileState()
        self.image_label = tk.Label(top)
        self.image_label.place(relx=0.015, rely=0.15, relheight=0.818, relwidth=0.755)
        # =============================================

        # self.Label1 = tk.Label(top)
        # self.Label1.place(relx=0.803, rely=0.15, height=32, relwidth=0.169)
        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.033, rely=0.023, height=32, relwidth=0.931)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#808080")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Output Data''')

        # self.Output = tk.Text(top)
        # self.Output.place(relx=0.803, rely=0.19, relheight=0.358, relwidth=0.169)
        self.Output = tk.Text(self.Frame2)
        self.Output.place(relx=0.033, rely=0.085, relheight=0.890, relwidth=0.931)
        self.Output.configure(background="white")
        self.Output.configure(font="TkTextFont")
        self.Output.configure(foreground="black")
        self.Output.configure(highlightbackground="#d9d9d9")
        self.Output.configure(highlightcolor="black")
        self.Output.configure(insertbackground="black")
        self.Output.configure(relief="flat")
        self.Output.configure(selectbackground="blue")
        self.Output.configure(selectforeground="white")
        self.Output.configure(wrap="word")
        # self.Output.configure(state=DISABLED)
        scroll = tk.Scrollbar(top, command=self.Output.yview)
        self.Output.configure(yscrollcommand=scroll.set)

        # self.Console_Label = tk.Label(top)
        # self.Console_Label.place(relx=0.803, rely=0.798, height=32, relwidth=0.169)
        self.Console_Label = tk.Label(self.Frame3)
        self.Console_Label.place(relx=0.033, rely=0.069, height=32, relwidth=0.931)
        self.Console_Label.configure(activebackground="#f9f9f9")
        self.Console_Label.configure(activeforeground="black")
        self.Console_Label.configure(background="#808080")
        self.Console_Label.configure(disabledforeground="#a3a3a3")
        self.Console_Label.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Console_Label.configure(foreground="#ffffff")
        self.Console_Label.configure(highlightbackground="#d9d9d9")
        self.Console_Label.configure(highlightcolor="black")
        self.Console_Label.configure(text='''Console Output''')

        # self.Console = tk.Text(top)
        # self.Console.place(relx=0.803, rely=0.835, relheight=0.131
        #         , relwidth=0.169)
        self.Console = tk.Text(self.Frame3)
        self.Console.place(relx=0.033, rely=0.280, relheight=0.625, relwidth=0.931)
        self.Console.configure(background="white")
        self.Console.configure(cursor="fleur")
        self.Console.configure(font="TkTextFont")
        self.Console.configure(foreground="black")
        self.Console.configure(highlightbackground="#d9d9d9")
        self.Console.configure(highlightcolor="black")
        self.Console.configure(insertbackground="black")
        self.Console.configure(relief="flat")
        self.Console.configure(selectbackground="blue")
        self.Console.configure(selectforeground="white")
        self.Console.configure(wrap="word")

        self.Left_Arrow = tk.Button(self.Frame_Top)
        self.Left_Arrow.place(relx=0.431, rely=0.565, height=32, width=47)
        self.Left_Arrow.configure(activebackground="#ececec")
        self.Left_Arrow.configure(activeforeground="#000000")
        self.Left_Arrow.configure(background="#000000")
        self.Left_Arrow.configure(state=DISABLED, command=lambda: prev_image(self.Slider, self.image_label, self.image_file_state))    # prev image
        self.Left_Arrow.configure(disabledforeground="#a3a3a3")
        self.Left_Arrow.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Left_Arrow.configure(foreground="#ffffff")
        self.Left_Arrow.configure(highlightbackground="#d9d9d9")
        self.Left_Arrow.configure(highlightcolor="black")
        self.Left_Arrow.configure(pady="0")
        self.Left_Arrow.configure(text='''<''')

        self.Right_Arrow = tk.Button(self.Frame_Top)
        self.Right_Arrow.place(relx=0.498, rely=0.565, height=32, width=47)
        self.Right_Arrow.configure(activebackground="#ececec")
        self.Right_Arrow.configure(activeforeground="#000000")
        self.Right_Arrow.configure(background="#000000")
        self.Right_Arrow.configure(state=DISABLED, command=lambda: next_image(self.Slider, self.image_label, self.image_file_state))   # next image
        self.Right_Arrow.configure(disabledforeground="#a3a3a3")
        self.Right_Arrow.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Right_Arrow.configure(foreground="#ffffff")
        self.Right_Arrow.configure(highlightbackground="#d9d9d9")
        self.Right_Arrow.configure(highlightcolor="black")
        self.Right_Arrow.configure(pady="0")
        self.Right_Arrow.configure(text='''>''')

        self.TSeparator1 = ttk.Separator(self.Frame_Top)
        self.TSeparator1.place(relx=0.341, rely=0.143,  relheight=0.714)
        self.TSeparator1.configure(orient="vertical")

        # ==================== combobox for algorithm choice =========================
        options = ["YOLO-v4-tiny"]
        self.TCombobox1 = ttk.Combobox(self.Frame_Top, values=options, state='readonly')
        self.TCombobox1.place(relx=0.033, rely=0.476, relheight=0.295
                , relwidth=0.169)
        self.TCombobox1.configure(font="-family {Segoe UI} -size 9")
        self.TCombobox1.configure(textvariable=GUI_support.combobox)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.current(0)

        self.Algorithm_Label = tk.Label(self.Frame_Top)
        self.Algorithm_Label.place(relx=0.033, rely=0.286, height=22, relwidth=0.169)
        self.Algorithm_Label.configure(activebackground="#f9f9f9")
        self.Algorithm_Label.configure(activeforeground="black")
        self.Algorithm_Label.configure(background="#808080")
        self.Algorithm_Label.configure(cursor="fleur")
        self.Algorithm_Label.configure(disabledforeground="#a3a3a3")
        self.Algorithm_Label.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Algorithm_Label.configure(foreground="#ffffff")
        self.Algorithm_Label.configure(highlightbackground="#d9d9d9")
        self.Algorithm_Label.configure(highlightcolor="black")
        self.Algorithm_Label.configure(text='''Algorithm''')

        self.Run = tk.Button(self.Frame_Top)
        self.Run.place(relx=0.221, rely=0.377, height=34, width=77)
        self.Run.configure(activebackground="#ececec")
        self.Run.configure(activeforeground="#000000")
        self.Run.configure(background="#000000")
        self.Run.configure(state=DISABLED, command = lambda: image_detect(self.image_file_state)) # Detecting the images
        self.Run.configure(cursor="fleur")
        self.Run.configure(disabledforeground="#a3a3a3")
        self.Run.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Run.configure(foreground="#ffffff")
        self.Run.configure(highlightbackground="#d9d9d9")
        self.Run.configure(highlightcolor="black")
        self.Run.configure(pady="0")
        self.Run.configure(text='''Run''')

        # menu =======================================
        self.menubar = tk.Menu(top)
        # create a pulldown menu, and add it to the menu bar
        self.filemenu = Menu(self.menubar, tearoff=0)

        self.filemenu.add_command(label="Upload Images", command = lambda: upload_images(self.Slider, self.image_label, self.image_file_state, self.Run, self.Left_Arrow, self.Right_Arrow, self.Output))
        self.filemenu.add_command(label="Upload weights, names and config files as a .zip", command=lambda: upload_config_files(self.image_file_state))
        self.filemenu.add_command(label="Export Output", command=lambda: export_file(self.image_file_state.export_content))

        self.menubar.add_cascade(label="File", menu=self.filemenu)

        top.config(menu=self.menubar)
        # =============================================

if __name__ == '__main__':
    vp_start_gui()





