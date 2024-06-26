import tkinter as tk

def start_move(event):
    # 紀錄滑鼠初始位置
    root.x = event.x
    root.y = event.y

def do_move(event):
    # 計算滑鼠移動距離，並更新視窗位置
    deltax = event.x - root.x
    deltay = event.y - root.y
    new_x = root.winfo_x() + deltax
    new_y = root.winfo_y() + deltay
    root.geometry(f"+{new_x}+{new_y}")

def test():
    L2.configure(text=repeat.get())
    print(type(repeat.get()))

root = tk.Tk()
root.geometry("200x200+800+300")
root.resizable(0, 0)
root.title('ARAM 掛機')

# 設置視窗置頂
root.attributes("-topmost", True)

# 無邊框
# root.overrideredirect(True)

# 透明背景
# root.wm_attributes("-transparentcolor", "aqua")
root.configure(bg='aqua')

# 裝飾
L1 = tk.Label(root, bg='lightgray', width=20)
L1.pack(padx=10, pady=10)

# 重複幾次
repeat = tk.Entry(root)
repeat.pack(padx=10, pady=10)

# 開始按鈕
B1 = tk.Button(root, text='開始', command=test)
B1.pack(padx=10, pady=10)

L2 = tk.Label(root, text='')
L2.pack(padx=10, pady=10)

# 綁定事件到 Label 上以實現拖曳
L1.bind("<Button-1>", start_move)
L1.bind("<B1-Motion>", do_move)

root.mainloop()
