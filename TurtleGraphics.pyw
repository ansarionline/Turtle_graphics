import tkinter as tk
from tkinter import ttk
from tkinter import Text,Frame,Scrollbar,RIGHT,Y,Grid,Pack,Place,LEFT,BOTH
import turtle
import threading
import re
print_ = print
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
root.title("Turtle Graphics 1.0 2024")
try:
    root.iconbitmap("T.ico")
except:
    pass

# Variables
border_width = 2
canvas_background = "#f0f0f0"
frame_background = "lightgreen"
text_background = "#ecf0f1"
button_frame_background = "#29AB87"
button_background = "green"
text_font = ("consolas", 15)
text_font_green = ("consolas", 15, "bold")
relief_style = "groove"
padding_x = 10
padding_y = 10
button_padding_x = 5
button_padding_y = 5
stop_event = threading.Event()

canvas_width,canvas_height = 100,100
text_widget_width,text_widget_height = 100,100
command_frame_height = 100

# Style Configuration
style = ttk.Style()
style.configure('TFrame', background=frame_background)
style.configure('TButton', background="green", foreground='green', font=('Helvetica', 11, 'bold'))
style.configure('TText', background=text_background, font=text_font)
style.configure('TCanvas', background=canvas_background)

# Frame (__init__)
main_frame = ttk.Frame(root, style='TFrame')
canvas_frame = ttk.Frame(main_frame, style='TFrame', relief=relief_style, borderwidth=border_width)
s_canvas_frame = ttk.Frame(canvas_frame, style='TFrame', relief=relief_style, borderwidth=border_width)
command_frame = ttk.Frame(main_frame, style='TFrame', relief=relief_style, borderwidth=border_width,width=10)
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

text_widget = ScrolledText(command_frame, bg=text_background, relief=relief_style, bd=border_width,width=50 ,
                           selectbackground="#98FF98", selectforeground="black", selectborderwidth=2,height = 1,
                            font=text_font, undo=True, maxundo=30, insertontime=200, insertofftime=200)
otp_text = ScrolledText(command_frame, bg="lightyellow", relief=relief_style, bd=border_width, fg = "darkred",height=1,width=50,
                           selectbackground="#98FF98", selectforeground="black", selectborderwidth=2, font=text_font)

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


def update_height(e=None):
        value = scale.get()
        new_height = int(value)
        text_widget.config(height=new_height)
        return
frame_background = "#e6f5e6"  # Light green for background
slider_color = "#4CAF50"       # Green for the slider
highlight_color = "#81c784"    # Lighter green for interaction
main = main_frame
bg = "lightgreen"
scale = tk.Scale(
    button_frame,
    from_=1,
    to=50,
    orient='horizontal',
    command=update_height,
    bg=frame_background,
    highlightbackground=highlight_color,
    sliderrelief='flat',
    font=('Helvetica', 12),
    width=15,
    showvalue=False
)
scale.set(5)
scale.pack(side='bottom', fill='x')
print_(scale.get())
def on_hover(e):
    scale.config(showvalue=True)
def on_leave(e):
    scale.config(showvalue=False)
scale.bind("<Leave>",on_leave)
scale.bind("<Enter>",on_hover)
def print_cmd(exp):
    otp_text.insert("end",f">> {exp}\n")
    return

def square_(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
    return
turtle_screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(turtle_screen)
t.turtlesize(stretch_wid=4, stretch_len=3, outline=1)
t.color("darkgreen")
forward = t.forward
fd = forward
backward = t.backward
bk = backward
left = t.left
lt = left
right = t.right
rt = right
goto = t.goto
setx = t.setx
sety = t.sety
circle = t.circle
ci = circle
arc = t.circle
square = square_
setpos = t.setpos
sp = setpos
setsize = t.turtlesize
sz = setsize
dot = t.dot
dt = dot
speed = t.speed
vs = speed  
pensize = t.pensize
ps = pensize
pencolor = t.pencolor
pc = pencolor
fillcolor = t.fillcolor
write = t.write
wr = write
calculate = eval
cal = calculate
print = print_cmd
pr = print
shape = t.shape
shp = shape
import time
wait = time.sleep
color = t.color  
co = color
#------------- Single-part commands -------------
penup = t.penup
pu = penup
pendown = t.pendown
pd = pendown
begin_fill = t.begin_fill
bf = begin_fill
end_fill = t.end_fill
ef = end_fill
stamp = t.stamp
clearstamp = t.clearstamp
cst = clearstamp
clearallstamps = t.clearstamps
cstl = clearallstamps
clearcmd = otp_text.delete("1.0","end")
cl = clearcmd
hide = t.hideturtle
ht = hide
show = t.showturtle
st = show
clean = t.clear
cn = clean
home = t.home
hm = home
position = t.position
pos = position
heading = t.heading
hd = heading
isdown = t.isdown
isd = isdown
bgcolor = turtle_screen.bgcolor  
sc = bgcolor
screensize = turtle_screen.screensize 
tracer = turtle_screen.tracer
update = turtle_screen.update 
shapesize = t.shapesize
delay = turtle_screen.delay  
clear = t.clear
reset = t.reset
pic = turtle_screen.bgpic

def highlight_text(event=None):
    text_widget.tag_remove("blue", "1.0", tk.END)
    text_widget.tag_remove("purple", "1.0", tk.END)
    text_widget.tag_remove("magenta", "1.0", tk.END)
    text_widget.tag_remove("function_call", "1.0", tk.END)
    text_widget.tag_remove("number", "1.0", tk.END)

    keywords = [
        "False", "None", "True", "and", "as", "assert", "async", "await", 
        "break", "class", "continue", "def", "del", "elif", "else", 
        "except", "finally", "for", "from", "global", "if", "import", 
        "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", 
        "return", "try", "while", "with", "yield"
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

    for match in re.finditer(r"\b\w+\s*\([^)]*\)", content):
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        text_widget.tag_add("function_call", start, end)

    for match in re.finditer(r"\b\d+\b", content):
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        text_widget.tag_add("number", start, end)
            
text_widget.bind("<KeyRelease>", highlight_text)
text_widget.tag_configure("purple", foreground="purple",font=text_font_green)
text_widget.tag_configure("blue", foreground="blue")
text_widget.tag_configure("magenta", foreground="green",font=text_font_green)
text_widget.tag_configure("function_call", foreground="#d14600")
text_widget.tag_configure("number", foreground="black")
highlight_text("<KeyRelease>")

def clear_t():
    t.clear()
    return

def clear_txt():
    text_widget.delete("1.0", tk.END)
    return

def disable():
    button_clt.config(state="disabled")
    button_cls.config(state="disabled")
    button_help.config(state="disabled")
    button_run1.config(state="disabled")
    text_widget.config(state="disabled")
    return

def able():
    button_clt.config(state="normal")
    button_cls.config(state="normal")
    button_help.config(state="normal")
    button_run1.config(state="normal")
    text_widget.config(state="normal")
    return

def execute_command(e=None):
    content = text_widget.get("1.0", "end").strip()
    disable()
    if len(content) == 0:
        otp_text.insert("end", f">> Nothing to execute.\n")
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
    help_window.configure(bg="lightgreen")
    help_.maxsize(1100,1000)
    help_window.pack(fill="both", expand=True,side="top",anchor='center')
    scrollbar = tk.Scrollbar(help_window)
    scrollbar.pack(side="right", fill="y")
    canvas = tk.Canvas(help_window, bg="lightgreen", yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=canvas.yview)
    content_frame = tk.Frame(canvas, bg="lightgreen")
    canvas.create_window((0, 0), window=content_frame, anchor="nw")
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    content_frame.bind("<Configure>", on_configure)
    scaler = 15
    table_frame = tk.Frame(content_frame, bg="lightgreen")
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
        ("setsize", "sz", "Set turtle size", "width, height, outline", "sz(2,2,3)"),
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
        ("shapesize", "shapesize", "Change the shape size", "stretch_wid, stretch_len, outline", "shapesize(1, 1, 1)"),
        ("delay", "delay", "Set the delay time in milliseconds", "milliseconds", "delay(100)"),
        ("reset", "reset", "Reset the turtle environment", "None", "reset"),
        ("pic", "pic", "Set the background picture", "image", "pic('background.gif')"),
    ]
    for row, command in enumerate(commands, start=1):
        for col, detail in enumerate(command):
            detail_label = tk.Label(table_frame, text=detail, font=("Helvetica", scaler),
                                    bg="lightgreen", borderwidth=2, relief="groove")
            detail_label.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)


cursor="hand2"
button_run1 = ttk.Button(button_frame, text="Run", command=execute_command,cursor=cursor)
button_help = ttk.Button(button_frame, text="Commands", command=show_help,cursor=cursor)
button_cls = ttk.Button(button_frame, text="ClearScreen", command=clear_t,cursor=cursor)
button_clt = ttk.Button(button_frame, text="ClearCmd", command=clear_txt,cursor=cursor)
text_widget.bind('<Shift-Return>',execute_command)

# Widgets (__packing__)
button_run1.pack(side='left',expand=True, fill='x', padx=button_padding_x-2, pady=button_padding_y-2)
button_help.pack(side='left',expand=True, fill='x', padx=button_padding_x-2, pady=button_padding_y-2)
button_cls.pack(side='left',expand=True, fill='x', padx=button_padding_x-2, pady=button_padding_y-2)
button_clt.pack(side='left',expand=True, fill='x', padx=button_padding_x-2, pady=button_padding_y-2)

root.mainloop()