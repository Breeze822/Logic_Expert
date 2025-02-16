import pandas as pd
import matplotlib.pyplot as plt

def compare_equivalence(file_paths_groups, group_labels, file_labels):
    """
    对比多个文件组中 Equivalence 列中 True 的比例。

    参数:
    - file_paths_groups: 包含多个文件路径列表的列表，每个子列表对应一个组
    - group_labels: 每个文件组的标签列表，用于显示在图表中
    - file_labels: 每个组内文件的标签列表
    """
    if len(file_paths_groups) != len(group_labels):
        raise ValueError("文件组和组标签数量必须一致！")

    num_groups = len(file_paths_groups)
    num_files_per_group = len(file_paths_groups[0])
    true_ratios = []

    for file_paths in file_paths_groups:
        group_ratios = []
        for file_path in file_paths:
            # 读取 Excel 文件
            data = pd.read_excel(file_path)

            # 确保 Equivalence 列是字符串类型
            data['Equivalence'] = data['Equivalence'].astype(str)

            # 统计 True 的数量和比例
            total_rows = len(data)
            true_count = data['Equivalence'].str.lower().value_counts().get('true', 0)
            true_ratio = true_count / total_rows if total_rows > 0 else 0

            group_ratios.append(true_ratio)
        true_ratios.append(group_ratios)

    # 可视化比较
    x = range(len(file_labels))
    bar_width = 0.2
    plt.figure(figsize=(10, 6))

    for i, (group_ratios, group_label) in enumerate(zip(true_ratios, group_labels)):
        offset = i * bar_width
        bars = plt.bar([pos + offset for pos in x], group_ratios, bar_width, label=group_label)

        # 在柱形图上显示比例
        for bar, ratio in zip(bars, group_ratios):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{ratio:.1%}', ha='center', va='bottom', fontsize=8)

    plt.xticks([pos + bar_width for pos in x], file_labels, rotation=45)
    plt.xlabel('Files')
    plt.ylabel('Proportion of True')
    plt.title('Comparison of True Proportion Across File Groups')
    plt.legend()
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.show()

    # 打印比例
    for group_label, group_ratios in zip(group_labels, true_ratios):
        print(f"Group {group_label}:")
        for file_label, ratio in zip(file_labels, group_ratios):
            print(f"  {file_label}: {ratio:.2%}")

# 使用示例
file_paths_groups = [['Exp/Gpt4o/syn_gpt4o_roleplay_intj_207.928_neigh=20_1.xlsx', 'Exp/Gpt4o/syn_gpt4o_roleplay_esfp_212.006_neigh=20_1.xlsx', 'Exp/Gpt4o/syn_gpt4o_roleplay_empty331.072_neigh=20_1.xlsx'], 
              ['Exp/Gpt/syn_gpt-3.5-turbo_roleplay_intj_43.492_neigh=20_1.xlsx', 'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_esfp_38.145_neigh=20_1.xlsx', 'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty53.0_neigh=20_1.xlsx'],
               ['Exp/Gemini/syn_gemini_roleplay_intj_191.289_neigh=20_1.xlsx', 'Exp/Gemini/syn_gemini_roleplay_esfp_207.595_neigh=20_1.xlsx', 'Exp/Gemini/syn_gemini_roleplay_empty288.435_neigh=20_1.xlsx'] ] # gpt4o

group_labels = ['gpt4o', 'gpt3.5', 'gemini']   # 替换为实际组名称
file_labels = ['intj', 'esfp', 'empty']   # 替换为实际文件名称
compare_equivalence(file_paths_groups, group_labels, file_labels)
