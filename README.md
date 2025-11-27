# Image-Coord-Extractor
A lightweight Python tool to extract bounding box coordinates (x1, y1, x2, y2) from images. Features continuous multi-region selection, visual feedback, and automatic coordinate calculation. 一个轻量级的图片坐标拾取工具。支持连续选取多个区域、可视化反馈以及自动计算矩形包围盒坐标，适用于 UI 自动化或计算机视觉数据标注。
# Image-Coord-Extractor (图片坐标拾取器)

一个基于 Python (Tkinter + Pillow) 的轻量级 GUI 工具，用于从截图中快速提取矩形区域的坐标。

主要用于 **RPA 自动化**（如 PyAutoGUI, Selenium）、**游戏脚本**编写或**计算机视觉**（Object Detection）的数据标注。

## ✨ 特性 (Features)

*   **连续多区域选取**：无需重启程序，点击满 4 个点自动记录一组数据，可立即开始下一组选取。
*   **可视化反馈**：
    *   点击时显示红色标记点和序号。
    *   区域确定后绘制绿色虚线框，避免重复选取。
*   **智能计算**：无需严格按照“左上-右下”顺序点击。只要点击矩形的四个角（或四条边），程序会自动通过 min/max 算法计算出标准的包围盒 `(x1, y1, x2, y2)`。
*   **格式兼容**：支持 `.png`, `.jpg`, `.jpeg`, `.bmp` 等常见图片格式。

## 🛠️ 依赖 (Dependencies)

本项目依赖 `Pillow` 库来处理图片。`tkinter` 通常包含在标准 Python 安装中。

```bash
pip install Pillow



##    使用方法 (Usage)
python sc.py

在弹出的文件对话框中选择一张图片（截图）。
选取坐标：
在目标区域点击 4 个点（通常为四个角：左上、右上、左下、右下）。
程序会自动计算该区域的坐标并输出到控制台。
图片上会显示绿色框标记该区域已完成。
继续选取：你可以直接继续点击下一组的 4 个点。
结束：关闭窗口即可退出程序。

输出示例 (Output Example)
控制台将按以下格式输出每一组的坐标：
=== 第 1 组区域完成 ===
x1 (Left)   : 100
y1 (Top)    : 200
x2 (Right)  : 350
y2 (Bottom) : 400
数据元组    : (100, 200, 350, 400)
---------------------------

=== 第 2 组区域完成 ===
x1 (Left)   : 500
y1 (Top)    : 100
x2 (Right)  : 600
y2 (Bottom) : 150
数据元组    : (500, 100, 600, 150)
---------------------------
x1, y1: 区域左上角坐标
x2, y2: 区域右下角坐标
