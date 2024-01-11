import tkinter as tk
import time
import global_vals
from Sort import SortingAlgorithms
from tkinter import messagebox
 # 调整窗口大小
algorithm_descriptions = {
    "冒泡排序": "冒泡排序是一种简单的排序算法...",
    "快速排序": "快速排序是一种常用的排序算法...",
    "归并排序": "归并排序是一种分治思想的排序算法...",
    "线性搜索": "线性搜索是一种简单的搜索算法...",
    "二分搜索": "二分搜索是一种高效的搜索算法...",
    "哈希搜索": "哈希搜索是一种基于哈希表的搜索算法...",
    "字符串匹配": "字符串匹配是一种常见的字符串操作算法...",
    "字符串反转": "字符串反转是将字符串倒序排列的算法...",
    "字符串拼接": "字符串拼接是将多个字符串连接起来的算法..."
}
# 示例算法函数
def algorithm_1(input_data):
    # 在此处添加算法逻辑
    output_data = input_data + " processed by algorithm 1"
    return output_data

def algorithm_2(input_data):
    # 在此处添加算法逻辑
    output_data = input_data + " processed by algorithm 2"
    return output_data



def search_algorithm(input_data):
    # 在此处添加搜索算法逻辑
    output_data = "Search algorithm applied to: " + input_data
    return output_data

def string_algorithm(input_data):
    # 在此处添加字符串算法逻辑
    output_data = "String algorithm applied to: " + input_data
    return output_data

# 更新第二个下拉菜单的选项
def update_algorithm_menu(*args):
    selected_category = algorithm_category_dropdown.get()  # 获取选择的算法类别

    # 根据选择的类别更新第二个下拉菜单的选项
    if selected_category == "排序":
        algorithm_menu['menu'].delete(0, 'end')  # 清空现有选项
        algorithm_dropdown.set("选择排序算法")  # 默认提示文本
        sorting_algorithms = ["冒泡排序", "快速排序", "归并排序"]
        for algo in sorting_algorithms:
            algorithm_menu['menu'].add_command(label=algo, command=tk._setit(algorithm_dropdown, algo))
    elif selected_category == "搜索":
        algorithm_menu['menu'].delete(0, 'end')  # 清空现有选项
        algorithm_dropdown.set("选择搜索算法")  # 默认提示文本
        search_algorithms = ["线性搜索", "二分搜索", "哈希搜索"]
        for algo in search_algorithms:
            algorithm_menu['menu'].add_command(label=algo, command=tk._setit(algorithm_dropdown, algo))
    elif selected_category == "字符串算法":
        algorithm_menu['menu'].delete(0, 'end')  # 清空现有选项
        algorithm_dropdown.set("选择字符串算法")  # 默认提示文本
        string_algorithms = ["字符串匹配", "字符串反转", "字符串拼接"]
        for algo in string_algorithms:
            algorithm_menu['menu'].add_command(label=algo, command=tk._setit(algorithm_dropdown, algo))

# 执行按钮点击事件
def execute_algorithm():
    # global extra_output
    input_data = input_entry.get(1.0,tk.END)  # 获取输入框中的数据
    selected_algorithm = algorithm_dropdown.get()  # 获取选择的算法

    # 根据选择的算法调用相应函数
    if selected_algorithm == "冒泡排序":
        output_data = SortingAlgorithms.bubble_sort(input_data)
    elif selected_algorithm == "快速排序":
        output_data = SortingAlgorithms.quick_sort(input_data)
    elif selected_algorithm == "归并排序":
        output_data = SortingAlgorithms.merge_sort(input_data)
    elif selected_algorithm == "线性搜索":
        output_data = search_algorithm(input_data)
    elif selected_algorithm == "二分搜索":
        output_data = search_algorithm(input_data)
    elif selected_algorithm == "哈希搜索":
        output_data = search_algorithm(input_data)
    elif selected_algorithm == "字符串匹配":
        output_data = string_algorithm(input_data)
    elif selected_algorithm == "字符串反转":
        output_data = string_algorithm(input_data)
    elif selected_algorithm == "字符串拼接":
        output_data = string_algorithm(input_data)
    else:
        output_data = "No algorithm selected."

    output_text.delete("1.0", tk.END)  # 清空输出框中的内容
    output_text.insert(tk.END, output_data)  # 在输出框中显示结果
    output_text.insert(tk.END, "\n")  # 添加换行符
    output_text.insert(tk.END, global_vals.extra_output)  # 在输出框中显示额外输出信息
def clear_output():
    input_entry.delete(0, tk.END)  # 清空输入框中的内容
    output_text.delete("1.0", tk.END)  # 清空输出框中的内容
    # description_text.delete("1.0",tk.END)

# 创建主窗口
window = tk.Tk()
window.title("算法工具1.0")
window.geometry("600x700")  # 调整窗口大小
# 算法类别选择下拉菜单和标签
category_label = tk.Label(window, text="选择算法类别:")
category_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
algorithm_categories = ["排序", "搜索", "字符串算法"]  # 可选择的算法类别
algorithm_category_dropdown = tk.StringVar(window)
algorithm_category_dropdown.set("选择算法类别")  # 默认提示文本
algorithm_category_dropdown.trace("w", update_algorithm_menu)  # 监听选择的类别变化
algorithm_category_menu = tk.OptionMenu(window, algorithm_category_dropdown, *algorithm_categories)
algorithm_category_menu.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# 算法选择下拉菜单和标签
algorithm_label = tk.Label(window, text="选择算法:")
algorithm_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
algorithm_dropdown = tk.StringVar(window)
algorithm_dropdown.set("选择排序算法")  # 默认提示文本
algorithm_menu = tk.OptionMenu(window, algorithm_dropdown, "选择排序算法")
algorithm_menu.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

# 输入框和标签
input_label = tk.Label(window, text="输入:")
input_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
input_entry = tk.Text(window,height=5, width=40)  # 调整输入框的宽度
input_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)  # 跨越两列

# 输出框和标签
output_label = tk.Label(window, text="输出:")
output_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
output_text = tk.Text(window, height=10, width=40)  # 调整输出框的宽度
output_text.grid(row=3, column=1, columnspan=2, padx=10, pady=10)  # 跨越两列
# 执行按钮
execute_button = tk.Button(window, text="执行", command=execute_algorithm, width=20)  # 调整按钮的宽度
execute_button.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W+tk.E)  # 水平居中
# 清除按钮
clear_button = tk.Button(window, text="清除", command=clear_output, width=20)  # 调整按钮的宽度
clear_button.grid(row=4, column=2, padx=10, pady=10, sticky=tk.W+tk.E)  # 水平居中

window.mainloop()