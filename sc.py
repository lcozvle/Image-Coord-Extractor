from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def get_multi_region_coordinates():
    # 初始化隐藏的主窗口
    root = tk.Tk()
    root.withdraw()

    # 选择文件
    img_path = filedialog.askopenfilename(title="选择截图", filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not img_path:
        root.destroy()
        return

    # 打开图片
    try:
        pil_image = Image.open(img_path)
        width, height = pil_image.size
    except Exception as e:
        print(f"无法打开图片: {e}")
        root.destroy()
        return

    # 创建显示窗口
    window = tk.Toplevel()
    window.title("连续坐标拾取器 (每4点一组，关闭窗口结束)")
    window.attributes('-topmost', True) # 窗口置顶

    # 使用 Canvas 显示图片
    canvas = tk.Canvas(window, width=width, height=height, cursor="cross")
    canvas.pack()

    # 图片显示
    tk_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=tk_image, anchor=tk.NW)
    
    # --- 状态变量 ---
    # 使用列表存储当前正在进行的这一组的点
    current_points = [] 
    # 记录已经完成了多少组
    region_count = 0 

    def process_current_batch():
        """处理当前凑齐的4个点"""
        nonlocal region_count, current_points
        
        region_count += 1
        
        # 提取坐标
        x_values = [p[0] for p in current_points]
        y_values = [p[1] for p in current_points]

        # 计算包围盒 (x1, y1, x2, y2)
        x1, y1 = min(x_values), min(y_values)
        x2, y2 = max(x_values), max(y_values)

        # --- 控制台输出 ---
        print(f"\n=== 第 {region_count} 组区域完成 ===")
        print(f"x1 (Left)   : {x1}")
        print(f"y1 (Top)    : {y1}")
        print(f"x2 (Right)  : {x2}")
        print(f"y2 (Bottom) : {y2}")
        print(f"数据元组    : ({x1}, {y1}, {x2}, {y2})")
        print("---------------------------")

        # --- 视觉反馈 ---
        # 1. 画出最终确定的矩形框 (绿色，虚线)
        canvas.create_rectangle(x1, y1, x2, y2, outline='green', width=2, dash=(5, 2))
        # 2. 在框中间写上组号
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        canvas.create_text(center_x, center_y, text=f"Region {region_count}", fill='green', font=('Arial', 10, 'bold'))

        # --- 重置状态，准备下一组 ---
        current_points = []
        print(f"准备接收第 {region_count + 1} 组的坐标...")

    def on_click(event):
        """点击事件处理"""
        x, y = event.x, event.y
        
        # 记录点
        current_points.append((x, y))
        seq_num = len(current_points) # 当前组的第几个点 (1-4)
        
        # 画点和序号 (红色，临时标记)
        r = 4
        # tag用于标记这些临时的点，如果需要清除可以利用tag (这里保留轨迹)
        canvas.create_oval(x-r, y-r, x+r, y+r, fill='red', outline='red')
        canvas.create_text(x, y-15, text=str(seq_num), fill='red', font=('Arial', 10, 'bold'))

        print(f"  -> 第 {region_count + 1} 组 - 点 {seq_num}: ({x}, {y})")

        # 如果凑齐了4个点，进行结算
        if len(current_points) == 4:
            # 使用 after 稍微延迟一点点执行，让用户看到第4个点点下去的效果
            window.after(10, process_current_batch)

    # 绑定左键点击
    canvas.bind("<Button-1>", on_click)

    print("程序已启动。请按照：左上 -> 右上 -> 左下 -> 右下 的顺序（或者任意顺序）点击4个点。")
    print("每点击4次，程序将自动计算并输出该区域坐标，您可以接着选取下一个区域。")
    print("关闭窗口退出程序。")

    window.mainloop()

if __name__ == '__main__':
    get_multi_region_coordinates()