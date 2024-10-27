import tkinter as tk
from tkinter import (Text,Frame,Scrollbar,
                     RIGHT,Y,Grid,Pack,
                     Place,LEFT,BOTH,ttk,
                     colorchooser as cc,
                     BooleanVar as B)
from tkinter.font import families
import turtle
import re
import time
class ScrolledText(Text):
    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)

        kw.update({'yscrollcommand': self.vbar.set})
        Text.__init__(self, self.frame, **kw)
        self.pack(side=LEFT, fill=BOTH, expand=True)
        self.vbar['command'] = self.yview

        text_meths = vars(Text).keys()
        methods = vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)

# Main (__init__)
root = tk.Tk()
b = B(name="theme")
root.title("Turtle Graphics v.1.0 © 2024")
try:
    root.iconbitmap("T.ico")
except Exception:
    pass
print_ = print
scale_var = [5]
width=[5]
c_speed=[400]
font = [["consolas","15"]]
bgbg = ['lightgreen']
bgbgbg = bgbg[0]
theme = ["light"]
clr____ = tk.StringVar(name="cursor_clr")
clr____.set("green")
s_clr__ = tk.StringVar(name="select_clr")
s_clr__.set("lightgreen")

# Variables
border_width = 2
canvas_background = "#f0f0f0"
frame_background = bgbgbg
text_background = "white" if bgbgbg == "lightgreen" else "gray80"
button_frame_background = "#29AB87" if bgbgbg == "lightgreen" else "darkgreen"
text_font = (font[0][0],font[0][1])
text_font_green = (font[0][0],font[0][1], "bold")
relief_style = "groove"
padding_x = 10
padding_y = 10
button_padding_x = 5
button_padding_y = 5

style = ttk.Style()
style.configure('TFrame', background=frame_background)
style.configure('TButton',foreground='green',bg="lightgreen", font=('Helvetica', 11, 'bold'),
                relief="groove")
style.configure('TText', background=text_background, font=text_font)
style.configure('TCanvas', background=canvas_background)

canvas_width,canvas_height = 1000,1000
text_widget_width,text_widget_height = 100,100
command_frame_height = 100
# Frame (__init__)
main_frame = ttk.Frame(root, style='TFrame')
canvas_frame = ttk.Frame(main_frame, style='TFrame', relief=relief_style, borderwidth=border_width)
s_canvas_frame = ttk.Frame(canvas_frame, style='TFrame', relief=relief_style, borderwidth=border_width)
command_frame = ttk.Frame(main_frame, style='TFrame', relief=relief_style,
                          borderwidth=border_width,width=10)
button_frame = ttk.Frame(command_frame, style='TFrame', relief=relief_style, borderwidth=0)

# Frame (__packing__)
main_frame.pack(fill='both', expand=True, padx=0, pady=0)
command_frame.pack(side='left', fill='both', expand=True, padx=padding_x, pady=padding_y)
s_canvas_frame.pack(side='top', fill='both', expand=True, padx=padding_x, pady=padding_y)
canvas_frame.pack(side='right', fill='both', expand=True, padx=padding_x, pady=padding_y)
button_frame.pack(side='top', fill='x', padx=padding_x, pady=padding_y)
# Widgets (__init__)
canvas = tk.Canvas(s_canvas_frame, bg=canvas_background,cursor="plus",
                   relief=relief_style, bd=border_width)

text_widget = ScrolledText(command_frame, bg=text_background, 
                           relief=relief_style, bd=border_width,width=25 ,
                           selectbackground=s_clr__.get(),
                           height=scale_var[0],
                           font=text_font, 
                           undo=True, maxundo=100,
                           insertontime=c_speed[0],
                           insertofftime=c_speed[0],
                           tabs=1,insertwidth=width[0],
                           insertbackground=clr____.get())
def add_c(e=None,c=None):
    root.after(10,lambda : text_widget.insert("end",c))
text_widget.bind("<Tab>",lambda e:add_c(e,"   "))
text_widget.bind("<[>",lambda e:add_c(e,"]"))
text_widget.bind("<{>",lambda e:add_c(e,"}"))
text_widget.bind("<(>",lambda e:add_c(e,")"))
text_widget.bind("<'>",lambda e:add_c(e,"'"))
text_widget.bind("<\">",lambda e:add_c(e,"\""))
otp_text = ScrolledText(command_frame, bg="lightyellow", relief=relief_style, 
                        bd=border_width, fg = "darkred",height=1,width=25,
                        selectbackground="#98FF98", selectforeground="black",
                        selectborderwidth=2, font=text_font)
text_widget.insert("end","# Welcome to TurtleGraphics v.1.0 (c) 2024\n# Start coding here\n")
otp_text.insert("end",">>**Console**")
vscrollbar = tk.Scrollbar(s_canvas_frame,orient="vertical")
vscrollbar.pack(side="right", fill="y")
hscrollbar = tk.Scrollbar(s_canvas_frame,orient="horizontal")
hscrollbar.pack(side="bottom", fill="x")
canvas.pack(fill='both',expand=True)

def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", on_configure)
vscrollbar.config(command=canvas.yview)
hscrollbar.config(command=canvas.xview)
text_widget.pack(fill='both',side="top",expand=True,padx=padding_x, pady=padding_y)
otp_text.pack(fill='both',side="bottom",expand=True,padx=padding_x, pady=padding_y)


def update_height(e=None,scale=None,label=None):
        value = scale.get()
        label.config(text=f"CMD height({value})")
        new_height = int(value)
        text_widget.config(height=new_height)
        scale_var.clear()
        scale_var.append(value)
        return
frame_background = "#e6f5e6"  # Light green for background
slider_color = "#4CAF50"       # Green for the slider
highlight_color = "#81c784"    # Lighter green for interaction
main = main_frame
bg = bgbgbg
def dark(e=None):
    bgbg.clear()
    bgbg.append("darkgreen")
    style.configure('TFrame',
                    background="darkgreen",bd=0)
    otp_text.config(bg="#009f38")
    text_widget.config(bg="green")
    canvas.config(bg="#b8febb",bd=0)
    text_widget.tag_configure("purple", foreground="pink")
    text_widget.tag_configure("blue", foreground="#7fffd4")
    text_widget.tag_configure("magenta", foreground="#dda0dd")
    text_widget.tag_configure("function_call", foreground="yellow")
    text_widget.tag_configure("number", foreground="lightcyan")
    text_widget.tag_configure("comment", foreground="cyan")
    text_widget.tag_configure("exceptions", foreground="#ff8787")
    text_widget.tag_configure("lib", foreground="#adff2f")
    text_widget.tag_configure("var", foreground="blue")
    text_widget.tag_configure("string", foreground="lightbrown")
    b.set(True)
def light(e=None):
    bgbg.clear()
    bgbg.append("lightgreen")
    style.configure('TFrame',
                    background="lightgreen",bd=2)
    otp_text.config(bg="lightyellow")
    text_widget.config(bg="white")
    canvas.config(bg="white",bd=0)
    text_widget.tag_configure("purple", foreground="purple")
    text_widget.tag_configure("blue", foreground="blue")
    text_widget.tag_configure("magenta", foreground="green",font=text_font_green)
    text_widget.tag_configure("function_call", foreground="darkorange")
    text_widget.tag_configure("number", foreground="black")
    text_widget.tag_configure("comment", foreground="gray50")
    text_widget.tag_configure("exceptions", foreground="red")
    text_widget.tag_configure("lib", foreground="darkgreen")
    text_widget.tag_configure("var", foreground="blue")
    text_widget.tag_configure("string", foreground="brown")
    b.set(False) 
SCALE_VAR = [5]
WIDTH=[5]
CLR=["green"]
C_SPEEED=[400]
C_BG=["#98FF98"]
FONT=[["consolas","15"]]
def settings(e=None):
    def update_height(e=None):
            value = scale.get()
            new_height = int(value)
            text_widget.config(height=new_height)
            return
    def update_width(e=None):
        var = width_var.get()
        text_widget.config(insertwidth=var)
        return
    def update_cursor_clr(e=None):
        _,c___ = cc.askcolor(parent=a,initialcolor=clr____.get())
        if c___:
            color_.config(text=c___.__str__(),
                        bg=c___)
            text_widget.config(insertbackground=c___)
            c_e.delete("0","end")
            c_e.insert("end",c___.__str__())
        else:
            c___ = clr____.get()
            c_e.delete("0","end")
            c_e.insert("end",c___.__str__())
            print_(c___)

    def update_blinking_speed(e=None):
        var = int(blink.get())#
        text_widget.config(insertofftime=var,insertontime=var)
        return var
    def update_select_clr(e=None):
        _,c__ = cc.askcolor(parent=a,initialcolor=s_clr__.get())
        if c__:
            select_bg.config(text=c__.__str__(),bg=c__)
            text_widget.config(selectbackground=c__)
            sc_e.delete("0","end")
            sc_e.insert("end",c__.__str__())
        else:
            c__ = s_clr__.get()
            sc_e.delete("0","end")
            sc_e.insert("end",c__.__str__())
            print_(c__)
    def update_font(e=None):
        content = text_widget.get("0","end")
        text_widget.delete("0","end")
        f = font_.get().strip().replace(" ","")
        fs = font_size.get()
        text_widget.config(font=f"{f} {fs}")
        text_widget.insert("end",content)
        return f
    bgbgbg = "darkgreen" if b.get() else "lightgreen"
    a = tk.Toplevel(root,bg=bgbgbg)
    a.title("Turtle Graphics>> Settings")
    main = tk.Frame(a,bg=bgbgbg)
    theme_f = tk.Frame(main,bg=bgbgbg,
                    bd=2,relief="groove")
    theme_f.pack(fill="x",expand=True,padx=2,pady=2)
    def __change_theme__(e=None):
        aaa = theme_c.get()
        if aaa == "Turtle-Light":
            light()
            return "light"
        else:
            dark()
            return "dark"
    tk.Label(theme_f,text="Theme:",bg="lightgreen").pack(side="left")
    theme_c = ttk.Combobox(theme_f,values=["Turtle-Light","Turtle-Dark"])
    theme_c.pack(side="left",fill="x",expand=True)
    cmd = tk.LabelFrame(main,text="CMD",bg=bgbgbg,
                        bd=2,relief="groove",font="Helvetica 15 bold")
    row1 = tk.Frame(cmd,bg=bgbgbg,
                    bd=2,relief="groove")
    row2 = tk.Frame(cmd,bg=bgbgbg,
                    bd=0,relief="groove")
    row_1a = tk.Frame(cmd,bg=bgbgbg,
                    bd=2,relief="groove")
    scale_l = tk.Label(row1,text="Height:",bg=bgbgbg,font="Helvetica 12 bold")
    scale =ttk.Spinbox(row1, from_=1, to=50,font="Helvetica 12",
        command =update_height)
    font_l = tk.Label(row_1a,text="Font:",bg=bgbgbg,font="Helvetica 12 bold")
    font_   = ttk.Combobox(row_1a, values=[f.__str__() for f in families(a)],
                           postcommand =update_font)
    font_size = ttk.Spinbox(row_1a,from_=10,to=25,command=update_font)
    font_size.set(font[0][1])
    font_.set(font[0][0])
    cursor = tk.LabelFrame(row2,text="Cursor",bg=bgbgbg,
                        bd=2,relief="groove",font="Helvetica 15 bold")
    row_c0 = tk.Frame(cursor,bg=bgbgbg,
                    bd=2,relief="groove")
    row_c1 = tk.Frame(cursor,bg=bgbgbg,
                    bd=2,relief="groove")
    row_c2 = tk.Frame(cursor,bg=bgbgbg,
                    bd=2,relief="groove")
    row_c3 = tk.Frame(cursor,bg=bgbgbg,
                    bd=2,relief="groove")
    width_l = tk.Label(row_c0,text="Width:",
                       bg=bgbgbg,font="Helvetica 12 bold")
    width_var = tk.IntVar()
    width_ = ttk.Spinbox(row_c0,values=[1,2,3,4,5,6,7,8,9,10],
                          textvariable=width_var,
                          command=update_width,font="Helvetica 12")
    color_l = tk.Label(row_c1,bd=0,relief="flat",
                       text="Color:",
                       font="Helvetica 12 bold",
                       bg=bgbgbg)
    color_ = tk.Button(row_c1,text=clr____.get(),bg=clr____.get(),
                      command=update_cursor_clr,relief="solid")
    c_e = tk.Entry(a)
    blink_l = tk.Label(row_c2,text="BlinkingSpeed(ms):",
                       bg=bgbgbg,font="Helvetica 12 bold")
    v = [0,100,200,300,400,500,600,700,800,900,1000]
    blink = ttk.Spinbox(row_c2,values=v,
    command=update_blinking_speed,font="Helvetica 12")
    select_bg_l = tk.Label(row_c3,text="SelectionColor:",
                       bg=bgbgbg,font="Helvetica 12 bold")
    select_bg = tk.Button(row_c3,text=s_clr__.get(),bg=s_clr__.get(),
                      command=update_select_clr,relief="solid")
    sc_e = tk.Entry(a)

    width_.set(width[0])
    scale.set(scale_var[0])
    blink.set(c_speed[0])
    theme_c.set(theme)
    c_e.delete("0","end")
    sc_e.delete("0","end")
    c_e.insert("end",clr____.get())
    sc_e.insert("end",s_clr__.get())

    scale_l.pack(side="left",expand=False,padx=5,pady=5)
    scale.pack(side='left', fill='x',expand=True,padx=5,pady=5)
    font_l.pack(side="left",expand=False,padx=5,pady=5)
    font_.pack(side='left', fill='x',expand=True,padx=5,pady=5)
    font_size.pack(side='left', fill='x',expand=True,padx=5,pady=5)
    width_l.pack(side="left",expand=False,padx=5,pady=5)
    width_.pack(side='left', fill='x',expand=True,padx=5,pady=5)
    color_l.pack(side="left",expand=False,padx=5,pady=5)
    color_.pack(side='left', fill='x',expand=True,padx=5,pady=5)
    blink_l.pack(side="left",expand=False,padx=5,pady=5)
    blink.pack(side='left', fill='x',expand=True,padx=5,pady=5)
    select_bg_l.pack(side="left",expand=False,padx=5,pady=5)
    select_bg.pack(side='left', fill='x',expand=True,padx=5,pady=5)
     
    cmd.pack(fill=BOTH,expand=True,padx=5,pady=5)
    cursor.pack(fill=BOTH,side="top",expand=True,padx=0,pady=0)
    row1.pack(side="top",fill=BOTH,expand=True,padx=5,pady=5)
    row_1a.pack(side="top",fill=BOTH,expand=True,padx=5,pady=5)
    row2.pack(side="top",fill=BOTH,expand=True,padx=5,pady=5)
    row_c0.pack(fill="both",side="top",expand=True,padx=5,pady=5)
    row_c1.pack(fill="both",side="top",expand=True,padx=5,pady=5)
    row_c2.pack(fill="both",side="top",expand=True,padx=5,pady=5)
    row_c3.pack(fill="both",side="top",expand=True,padx=5,pady=5)
    main.pack(fill="both",padx=5,pady=5,expand=True)

    def _clear_():
        var_s = [scale_var,width,c_speed,font,theme]
        for v in var_s:
            v.clear()
    def _get_():
        s = scale.get()
        f = font_.get()
        f_= font_size.get()
        w = width_.get()
        c_= c_e.get()
        b_= blink.get()
        s_= sc_e.get()
        t = theme_c.get()
        return [s,f,f_,w,c_,b_,s_,t]
    
    def _append():
        s,f,f_,w,c_,b_,s_,t = _get_()
        scale_var.append(s)
        width.append(w)
        clr____.set(c_)
        s_clr__.set(s_)
        c_speed.append(b_)
        theme.append(t)
        font.append([f,f_])
    
    def _reset_(e=None):
        scale.set(SCALE_VAR[0])
        font_.set(FONT[0][0])
        font_size.set(FONT[0][1])
        width_.set(WIDTH[0])
        clr____.set(CLR[0])
        c_e.delete("0","end")
        sc_e.delete("0","end")
        c_e.insert("end",clr____.get())
        sc_e.insert("end","#98FF98")
        color_.config(bg=clr____.get(),text=clr____.get())
        s_clr__.set(C_BG[0])
        select_bg.config(bg="#98FF98",text="#98FF98")
        blink.set(C_SPEEED[0])
        theme_c.set("Turtle-Light")
    
    def _cancel_(e=None):
        scale.set(scale_var[0])
        font_.set(font[0][0])
        font_size.set(font[0][1])
        width_.set(width[0])
        color_.config(text=clr____.get(),bg=clr____.get())
        select_bg.config(text=s_clr__.get(),bg=s_clr__.get())
        blink.set(c_speed[0])
        theme_c.set(theme[0])
        text_widget.config(height=int(scale_var[0]),
                           font=(font[0][0],font[0][1]),
                           insertwidth=width[0],
                           insertbackground=clr____.get(),
                           insertofftime=c_speed[0],
                           insertontime=c_speed[0],
                           selectbackground=s_clr__.get())
        time.sleep(0.01)
    def _save_(e=None):
        s,f,f_,w,c_,b_,s_,t = _get_()
        try:
            with open("__settings__","x") as fff:
                fff.write(f"{s},{f},{f_},{w},{c_},{b_},{s_},{t}")
        except FileExistsError:
            with open("__settings__","w") as fff:
                fff.write(f"{s},{f},{f_},{w},{c_},{b_},{s_},{t}") 
    def okay(e=None):
            _clear_()
            _append()
            print_((_get_()))
            text_widget.config(height=int(_get_()[0]),
                            font=(_get_()[1],_get_()[2]),
                            insertwidth=_get_()[3],
                            insertbackground=_get_()[4],
                            insertofftime=_get_()[5],
                            insertontime=_get_()[5],
                            selectbackground=_get_()[6])
            __change_theme__()
            _save_()
            print_(_get_())
            print_(c_e.get()," ",clr____.get())
            print_(sc_e.get()," ",s_clr__.get())
            a.after(10,lambda : a.destroy())    
    btn_f = tk.Frame(cmd,bg=bgbgbg,
                    bd=2,relief="groove")
    btn_f.pack(fill='x',expand=True)
    cancel = tk.Button(btn_f,text="Cancel",bg="red",
                      command=_cancel_,relief="solid")
    ok = tk.Button(btn_f,text="Ok",bg="green",
                      command=okay,relief="solid")
    reset = tk.Button(btn_f,text="Reset",bg="cyan",
                      command=_reset_,relief="solid")
    ok.pack(fill="x",padx=1,pady=1,side="left",expand=True)
    cancel.pack(fill="x",padx=1,pady=1,side="left",expand=True)
    reset.pack(fill="x",padx=1,pady=1,side="left",expand=True)
    a.resizable(False,False)
    return
def themememe():
    try:
        with open("__settings__","r") as rr:
            a = rr.read().strip().split(',')
            print_(a)
            s,f,f_,w,c_,b_,s_,t = a
            if t == "Turtle-Dark":
                dark()
                b.set(True)
                theme.clear()
                theme.append("Turtle-Dark")
                scale_var.append(s)
                width.append(w)
                clr____.set(c_)
                c_speed.append(b_)
                s_clr__.set(s_)
                font.append([f,f_])
                text_widget.config(
                    height=int(s),
                    font=(f,int(f_)),
                    insertwidth=w,
                    insertbackground=c_,
                    insertofftime=b_,
                    insertontime=b_,
                    selectbackground=s_clr__.get()
                )
            else:
                light()
                b.set(False)
                theme.clear()
                theme.append("Turtle-Light")
                scale_var.append(s)
                width.append(w)
                clr____.set(c_)
                c_speed.append(b_)
                s_clr__.set(s_)
                font.append([f,f_])
                text_widget.config(
                    height=int(s),
                    font=(f,int(f_)),
                    insertwidth=w,
                    insertbackground=c_,
                    insertofftime=b_,
                    insertontime=b_,
                    selectbackground=s_clr__.get()
                )
    except FileNotFoundError:
        pass
    return
def print_cmd(exp):
    otp_text.insert("end",f">> {exp}\n")
    return

def square_(length):
    for i in range(4):
        _.forward(length)
        _.left(90)
    return
turtle_screen = turtle.TurtleScreen(canvas)
_ = turtle.RawTurtle(turtle_screen)
_.turtlesize(stretch_wid=4, stretch_len=3, outline=1)
_.color("darkgreen")
forward = _.forward
fd = forward
backward = _.backward
bk = backward
left = _.left
lt = left
right = _.right
rt = right
goto = _.goto
setx = _.setx
sety = _.sety
circle = _.circle
ci = circle
arc = _.circle
square = square_
setpos = _.setpos
sp = setpos
goto = sp
gt = goto
setsize = _.turtlesize
sz = setsize
dot = _.dot
dt = dot
speed = _.speed
vs = speed
velocity = vs  
pensize = _.pensize
ps = pensize
pencolor = _.pencolor
pc = pencolor
fillcolor = _.fillcolor
write = _.write
wr = write
calculate = eval
cal = calculate
print = print_cmd
pr = print
shape = _.shape
shp = shape
wait = time.sleep
color = _.color  
co = color
#------------- Single-part commands -------------
penup = _.penup
pu = penup
pendown = _.pendown
pd = pendown
begin_fill = _.begin_fill
bf = begin_fill
end_fill = _.end_fill
ef = end_fill
stamp = _.stamp
clearstamp = _.clearstamp
cst = clearstamp
clearallstamps = _.clearstamps
cstl = clearallstamps
def clear_cmd():
    otp_text.delete("1.0","end")
clearcmd = clear_cmd
cl = clearcmd
hide = _.hideturtle
ht = hide
show = _.showturtle
st = show
clean = _.clear
cn = clean
home = _.home
hm = home
position = _.position
pos = position
heading = _.heading
hd = heading
isdown = _.isdown
isd = isdown
bgcolor = turtle_screen.bgcolor  
sc = bgcolor
screensize = turtle_screen.screensize 
tracer = turtle_screen.tracer
update = turtle_screen.update 
shapesize = _.shapesize
delay = turtle_screen.delay  
clear = _.clear
clearscreen = clear
cs = clear
reset = _.reset
pic = turtle_screen.bgpic

def highlight_text(event=None):
    text_widget.tag_remove("blue", "1.0", tk.END)
    text_widget.tag_remove("purple", "1.0", tk.END)
    text_widget.tag_remove("magenta", "1.0", tk.END)
    text_widget.tag_remove("function_call", "1.0", tk.END)
    text_widget.tag_remove("number", "1.0", tk.END)
    text_widget.tag_remove("comment", "1.0", tk.END)
    text_widget.tag_remove("exceptions", "1.0", tk.END)
    text_widget.tag_remove("lib", "1.0", tk.END)
    text_widget.tag_remove("var", "1.0", tk.END)
    text_widget.tag_remove("signs", "1.0", tk.END)

    keywords = [
        "False", "None", "True", "and", "as", "assert", "async", "await", 
        "break", "class", "continue", "def", "del", "elif", "else", 
        "except", "finally", "from", "global", "if", "import", 
        "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", 
        "return", "try", "yield","case",
    ]
    exceptions = [
        'AssertionError','AssertionError','AttributeError',
        'BrokenPipeError','BufferError','BlockingIOError','bytearray',
        'ConnectionError','ChildProcessError','ConnectionResetError',
        'ConnectionRefusedError','ConnectionAbortedError',
        'EOFError','EnvironmentError','FileExistsError','FileNotFoundError',
        'FloatingPointError','IndexError','ImportError','IOError','IndentationError',
        'InterruptedError','IsADirectoryError','KeyError','LookupError',
        'MemoryError','ModuleNotFoundError','NameError','NotADirectoryError',
        'NotImplementedError','OSError','OverflowError','PermissionError',
        'ProcessLookupError','RuntimeError','RecursionError','ReferenceError',
        'SyntaxError','SystemError','TabError','TypeError','TimeoutError',
        'UnicodeError','UnboundLocalError','UnicodeEncodeError','UnicodeDecodeError',
        'UnicodeTranslateError','ValueError','WindowsError','ZeroDivisionError',
        'Exception'
    ]
    blue_words = [
        "forward", "fd", "backward", "bk", "left",
        "lt", "right", "rt", "goto", "setx",
        "sety", "circle", "ci", "arc", "square",
        "sq", "setpos", "sp", "setsize", "sz",
        "dot", "dt", "speed", "sp", "pensize",
        "ps", "pencolor", "pc", "fillcolor", "write",
        "wr", "calculate", "cal", "print", "pr",
        "shape", "shp", "wait", "wt", "penup", "pu",
        "pendown", "pd", "begin_fill", "bf", "color","co",
        "end_fill", "ef", "stamp", "clearstamp",
        "cst", "clearallstamps", "cstl", "clearcmd", "cl",
        "hide", "ht", "show", "st", "clean",
        "cn", "home", "hm","position", "pos", "heading", "hd", "isdown",
        "isd", "bgcolor", "sc", "title", "screensize",
        "tracer", "update", "shape", "shapesize", "speed",
        "delay", "clear", "reset", "bye", "pic","repeat"
    ]
    loops = ["for", "while","with"]
    content = text_widget.get("1.0", tk.END)
    
    for word in keywords:
        for match in re.finditer(rf"\b{word}\b", content):
            start = f"1.0+{match.start()}c"
            end = f"1.0+{match.end()}c"
            text_widget.tag_add("purple", start, end)

    for word in blue_words:
        for match in re.finditer(rf"\b{word}\b", content):
            start = f"1.0+{match.start()}c"
            end = f"1.0+{match.end()}c"
            text_widget.tag_add("blue", start, end)
            
    for word in loops:
        for match in re.finditer(rf"\b{word}\b", content):
            start = f"1.0+{match.start()}c"
            end = f"1.0+{match.end()}c"
            text_widget.tag_add("magenta", start, end)
            
    for word in exceptions:
        for match in re.finditer(rf"\b{word}\b", content):
            start = f"1.0+{match.start()}c"
            end = f"1.0+{match.end()}c"
            text_widget.tag_add("exceptions", start, end)
                
    for match in re.finditer(r"\b\w+\s*\([^)]*\)", content):
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        text_widget.tag_add("function_call", start, end)
        
    for match in re.finditer(r"\b\d+\b", content):
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        text_widget.tag_add("number", start, end) 
        
    for match in re.finditer(r"#.*", content):
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        text_widget.tag_add("comment", start, end)  
        
    for match in re.finditer(r"import .*", content):
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        text_widget.tag_add("lib", start, end)
        
    for match in re.finditer(r"from .*", content):
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        text_widget.tag_add("lib", start, end)  
            
    for match in re.finditer(r"=", content):
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        text_widget.tag_add("var", start, end) 
        
    for match in re.finditer(r"""'.'|''|""|".\"""", content):
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        text_widget.tag_add("string", start, end) 
        
text_widget.bind("<KeyRelease>", highlight_text)
text_widget.tag_configure("purple", foreground="purple")
text_widget.tag_configure("blue", foreground="blue")
text_widget.tag_configure("magenta", foreground="green",font=text_font_green)
text_widget.tag_configure("function_call", foreground="darkorange")
text_widget.tag_configure("number", foreground="black")
text_widget.tag_configure("string", foreground="white")
text_widget.tag_configure("comment", foreground="gray50")
text_widget.tag_configure("exceptions", foreground="red")
text_widget.tag_configure("lib", foreground="darkgreen")
text_widget.tag_configure("var", foreground="blue")
highlight_text("<KeyRelease>")

themememe()

def clear_t():
    _.clear()
    return

def clear_txt():
    text_widget.delete("1.0", tk.END)
    return

def disable():
    button_clt.config(state="disabled")
    button_cls.config(state="disabled")
    button_hlp.config(state="disabled")
    button_run.config(state="disabled")
    text_widget.config(state="disabled")
    return

def able():
    button_clt.config(state="normal")
    button_cls.config(state="normal")
    button_hlp.config(state="normal")
    button_run.config(state="normal")
    text_widget.config(state="normal")
    return

def execute_command(e=None):
    content = text_widget.get("1.0", "end").strip()
    disable()
    if len(content) == 0:
        otp_text.insert("end", ">> Nothing to execute.\n")
        able()
    else:
        try:
            exec(content, globals())
            able()
        except Exception as ee:
            otp_text.insert("end", f">> Error: {str(ee)}.\n")
            able()

def show_help():
    help_ = tk.Toplevel(root)
    help_.title("Help")
    help_window = tk.Frame(help_)
    help_window.configure(bg=bgbgbg)
    help_.maxsize(1100,1000)
    help_window.pack(fill="both", expand=True,side="top",anchor='center')
    scrollbar = tk.Scrollbar(help_window)
    scrollbar.pack(side="right", fill="y")
    canvas = tk.Canvas(help_window, bg=bgbgbg, yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=canvas.yview)
    content_frame = tk.Frame(canvas, bg=bgbgbg)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    content_frame.bind("<Configure>", on_configure)
    scaler = 15
    table_frame = tk.Frame(content_frame, bg=bgbgbg)
    table_frame.pack(pady=10, padx=10)
    headers = ["Command", "Abbreviation", "Purpose", "Parameters", "Example"]
    for col, header in enumerate(headers):
        header_label = tk.Label(table_frame, text=header, font=("Helvetica", scaler + 2, "bold"), bg="green", fg="white", borderwidth=2, relief="groove")
        header_label.grid(row=0, column=col, sticky="nsew", padx=1, pady=1)
    commands = [
        ("arc", "arc", "Draw arc", "radius , degrees", "arc(100,90)"),
        ("backward", "bk", "Move backward", "distance", "bk(100)"),
        ("begin_fill", "bf", "Start filling shape", "None", "bf()"),
        ("calculate", "cal", "Calculate the expression", "exp", "cal(1+2)"),
        ("circle", "ci", "Draw a circle", "radius", "ci(50)"),
        ("clean", "cn", "Clear drawing", "None", "cn()"),
        ("clearallstamps", "cstl", "Clear All Stamps turtle shape", "None", "cstl()"),
        ("clearcmd", "cl", "Clear command text", "None", "cl()"),
        ("clearscreen", "cs", "Clear screen and reset", "None", "cs()"),
        ("clearstamp", "cst", "Clear Stamp turtle shape", "None", "cst()"),
        ("dot", "dt", "Draw a dot", "size, color", "dt(20,'red')"),
        ("end_fill", "ef", "End filling shape", "None", "ef()"),
        ("forward", "fd", "Move forward", "distance", "fd(100)"),
        ("heading", "hd", "Show Direction of turtle", "None", "hd()"),
        ("hide", "ht", "Hide turtle", "None", "ht()"),
        ("home", "hm", "Go to home position", "None", "hm()"),
        ("isdown", "isd", "Tell whether the pen is down or not", "None", "isd()"),
        ("left", "lt", "Turn left", "angle", "lt(90)"),
        ("pendown", "pd", "Lower pen", "None", "pd()"),
        ("penup", "pu", "Lift pen", "None", "pu()"),
        ("pensize", "ps", "Set pen size", "size", "ps(5)"),
        ("position", "pos", "Show Position of turtle", "None", "pos()"),
        ("print", "pr", "Print the expression", "exp", "pr('Turtle Graphics')"),
        ("right", "rt", "Turn right", "angle", "rt(90)"),
        ("setpc", "pc", "Set pen color", "color", "pc('blue')"),
        ("setpos", "sp", "Set position", "x, y", "sp(100,200)"),
        ("setsc", "sc", "Set screen color", "color", "sc('yellow')"),
        ("setsize", "sz", "Set turtle size", "width, height,\noutline", "sz(2,2,3)"),
        ("shape", "shp", "Change the Shape of turtle \n ('arrow', 'turtle', \n 'circle', 'square', \n 'triangle', 'classic'.)", "None", "shp('turtle')"),
        ("show", "st", "Show turtle", "None", "st()"),
        ("speed", "sp", "Set speed", "speed", "sp(10)"),
        ("stamp", "st", "Stamp turtle shape", "None", "st()"),
        ("wait", "wt", "Wait n seconds", "n", "wt(5)"),
        ("write", "wr", "Write text", "text", "wr('Hello')"),
        ("goto", "goto", "Move turtle to x,y coordinates", "x, y", "goto(100,100)"),
        ("setx", "setx", "Set x coordinate", "x", "setx(50)"),
        ("sety", "sety", "Set y coordinate", "y", "sety(50)"),
        ("square", "sq", "Draw a square", "side length", "sq(100)"),
        ("bgcolor", "sc", "Set background color", "color", "sc('blue')"),
        ("color", "co", "Set Pen color", "color", "co('blue')"),
        ("tracer", "tracer", "Control screen updates", "n", "tracer(0)"),
        ("update", "update", "Update the turtle screen", "None", "update"),
        ("shapesize", "shapesize", "Change the shape size", "stretch_wid, stretch_len,\n outline", "shapesize(1, 1, 1)"),
        ("delay", "delay", "Set the delay time in milliseconds", "milliseconds", "delay(100)"),
        ("reset", "reset", "Reset the turtle environment", "None", "reset"),
        ("pic", "pic", "Set the background picture", "image", "pic('background.gif')"),
    ]
    for row, command in enumerate(commands, start=1):
        for col, detail in enumerate(command):
            detail_label = tk.Label(table_frame, text=detail, font=("Helvetica", scaler),
                                    bg=bgbgbg, borderwidth=2, relief="groove")
            detail_label.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

def write__(pth,code):
    with open(pth,"w") as file:
        file.write(code)
        file.close()
def notice(e=None,save_path=None):
    root.title(f"Turtle Graphics v.1.0 © 2024|*[{save_path}]*")
def clear_notice(e=None,save_path=None,code=None):
    write__(save_path,code)
    root.title(f"Turtle Graphics v.1.0 © 2024|[{save_path}]")
def save_(e=None):
    code = text_widget.get("1.0","end")
    from tkinter import filedialog as fdg
    save_pth = fdg.asksaveasfilename(filetypes=[("Turtle-Graphics-Code","*.tgc")],
                                     defaultextension=("TurtleGraphics-Code","*.tgc"))
    save_pth = f"{save_pth}.tgc" if not save_pth.endswith(".tgc") else save_pth
    clear_notice(None,save_pth,code)
    if save_pth:
        text_widget.bind("<Control-s>",lambda e:clear_notice(e,save_pth,text_widget.get("1.0","end")))
        text_widget.bind("<KeyPress>",lambda e:notice(e,save_pth))
cursor="hand2"
col1 = ttk.Frame(button_frame)
col2 = ttk.Frame(button_frame)
col3 = ttk.Frame(button_frame)
button_run = tk.Button(col1, text="  Run ▶  ",
                        command=execute_command,
                        cursor=cursor,foreground='green',
                        bg="lightgreen", font=('Helvetica', 11, 'bold'),
                        relief="groove")
button_cls = tk.Button(col2, text="ClearScreen ❌", 
                        command=clear_t,
                        cursor=cursor,foreground='green',
                        bg="lightgreen", font=('Helvetica', 11, 'bold'),
                        relief="groove")
button_clt = tk.Button(col2, text="ClearCmd ❌",
                        command=clear_txt,
                        cursor=cursor,foreground='green',
                        bg="lightgreen", font=('Helvetica', 11, 'bold'),
                        relief="groove")
button_exp = tk.Button(col3, text="SaveCode 📝",
                        command=save_,
                        cursor=cursor,foreground='green',
                        bg="lightgreen", font=('Helvetica', 11, 'bold'),
                        relief="groove")
button_hlp = tk.Button(col1, text="Help ❓",
                        command=show_help,
                        cursor=cursor,foreground='green',
                        bg="lightgreen", font=('Helvetica', 11, 'bold'),
                        relief="groove")
button_set = tk.Button(col3, text="Settings 🛠",  
                        command=settings,
                        cursor=cursor,foreground='green',
                        bg="lightgreen", font=('Helvetica', 11, 'bold'),
                        relief="groove")
text_widget.bind('<Shift-Return>',execute_command)

# Widgets (__packing__)
button_run.pack(side='top',expand=True, fill='x', padx=button_padding_x-2, pady=button_padding_y-2)
button_cls.pack(side='top',expand=True, fill='x', padx=button_padding_x-2, pady=button_padding_y-2)
button_clt.pack(side='top',expand=True, fill='x', padx=button_padding_x-2, pady=button_padding_y-2)
button_exp.pack(side='top',expand=True, fill='x', padx=button_padding_x-2, pady=button_padding_y-2)
button_hlp.pack(side='top',expand=True, fill='x', padx=button_padding_x-2, pady=button_padding_y-2)
button_set.pack(side='top',expand=True, fill='x', padx=button_padding_x-2, pady=button_padding_y-2)
col1.pack(side='left',expand=True, fill='x', padx=0, pady=0)
col2.pack(side='left',expand=True, fill='x', padx=0, pady=0)
col3.pack(side='left',expand=True, fill='x', padx=0, pady=0)
root.mainloop()
