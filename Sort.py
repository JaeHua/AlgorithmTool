import time
import global_vals
class SortingAlgorithms:
    @staticmethod
    def bubble_sort(input_data):
        # 将输入数据转换为列表
        data_list = [int(x) for x in input_data.split()]  # 使用列表推导式将字符串转换为整数列表
        n = len(data_list)
        comparisons = 0  # 记录比较次数
        start_time = time.time()  # 记录开始时间
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                comparisons += 1
                if data_list[j] > data_list[j + 1]:
                    data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
        end_time = time.time()  # 记录结束时间
        elapsed_time = (end_time - start_time) * 1000  # 将时间单位更改为毫秒
        # 将排序后的列表转换回字符串，并添加空格间隙
        output_data = " ".join(map(str, data_list))

        # 构造额外输出信息
        global_vals.extra_output = f"比较次数: {comparisons}\n所用时间: {elapsed_time} 毫秒"
        # 将排序结果和额外输出信息拼接

        return output_data


    def quick_sort(arr):
       pass
    @staticmethod
    def merge_sort(input_data):
      pass