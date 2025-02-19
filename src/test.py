import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties  
  
font = FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', size=16) 

# for i in a:
#     print(i)
# plt.rcParams['font.family'] = 'fonts-wqy-zenhei' # 或者使用你系统中的其他中文字体，如 'Microsoft YaHei'

# # 设置负号正常显示
# rcParams['axes.unicode_minus'] = False

def compare_equivalence(file_paths_groups, group_labels, file_labels):
    """
    对比多个文件组中 Equivalence 列中 True 的比例。

    参数:
    - file_paths_groups: 包含多个文件路径列表的列表，每个子列表对应一个来源（如 gpt4o、gpt3.5、gemini）
    - group_labels: 每组内的分组标签列表（如 intj、esfp、empty、...）
    - file_labels: 每个文件来源的标签
    """
    if len(file_paths_groups) != len(file_labels):
        raise ValueError("文件组数量与文件标签数量必须一致！")

    num_groups = len(file_paths_groups)
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
    x = range(len(group_labels))
    bar_width = 0.15  # 缩小宽度以容纳更多条形
    plt.figure(figsize=(12, 6))  # 调整图大小

    for i, (group_ratios, file_label) in enumerate(zip(true_ratios, file_labels)):
        offset = i * bar_width
        bars = plt.bar([pos + offset for pos in x], group_ratios, bar_width, label=file_label)

        # 在柱形图上显示比例
        for bar, ratio in zip(bars, group_ratios):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{ratio:.1%}', ha='center', va='bottom', fontsize=8)

    plt.xticks([pos + bar_width * (len(file_labels) / 2) for pos in x], group_labels, fontproperties=font)
    # plt.xticks([pos + bar_width * (len(file_labels) / 2) for pos in x], group_labels, rotation=45, fontproperties=font)
    plt.xlabel('角色', fontproperties=font)
    plt.ylabel('正确率', fontproperties=font)
    # plt.title('Comparison of True Proportion Across Sources')
    plt.legend()
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.show()

    # 打印比例
    for file_label, group_ratios in zip(file_labels, true_ratios):
        print(f"Source {file_label}:")
        for group_label, ratio in zip(group_labels, group_ratios):
            print(f"  {group_label}: {ratio:.2%}")

# 使用示例
file_paths_groups = [
    [
        'Exp/AP/Gpt4o/syn_gpt4o_roleplay_intj_1.xlsx',
        'Exp/AP/Gpt4o/syn_gpt4o_roleplay_esfp_1.xlsx',
        'Exp/AP/Gpt4o/syn_gpt4o_roleplay_infp_1.xlsx',
        'Exp/AP/Gpt4o/syn_gpt4o_roleplay_entj_1.xlsx',
        'Exp/AP/Gpt4o/syn_gpt4o_roleplay_empty_1.xlsx'
    ],
    [
        'Exp/AP/Gpt/syn_gpt-3.5-turbo_roleplay_intj_1.xlsx',
        'Exp/AP/Gpt/syn_gpt-3.5-turbo_roleplay_esfp_1.xlsx',
        'Exp/AP/Gpt/syn_gpt-3.5-turbo_roleplay_infp_1.xlsx',
        'Exp/AP/Gpt/syn_gpt-3.5-turbo_roleplay_entj_1.xlsx',
        'Exp/AP/Gpt/syn_gpt-3.5-turbo_roleplay_empty_1.xlsx'
    ],
    [
        'Exp/AP/Gemini/syn_gemini_roleplay_intj_1.xlsx',
        'Exp/AP/Gemini/syn_gemini_roleplay_esfp_1.xlsx',
        'Exp/AP/Gemini/syn_gemini_roleplay_infp_1.xlsx',
        'Exp/AP/Gemini/syn_gemini_roleplay_entj_1.xlsx',
        'Exp/AP/Gemini/syn_gemini_roleplay_empty_1.xlsx',
        # 'Exp/AP/Gemini/syn_gemini_roleplay_empty_1.xlsx',
        # 'Exp/AP/Gemini/syn_gemini_roleplay_empty_1.xlsx',
        # 'Exp/AP/Gemini/syn_gemini_roleplay_empty_1.xlsx',
        # 'Exp/AP/Gemini/syn_gemini_roleplay_empty_1.xlsx'


    ]
]

# file_paths_groups = [
#     [
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_1.xlsx',
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_2.xlsx',
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_3.xlsx',
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_1.xlsx',
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_1.xlsx'
#     ],
#     [
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_1.xlsx',
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_2.xlsx',
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_3.xlsx',
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_1.xlsx',
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_1.xlsx'
#     ],
#     [
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_1.xlsx',
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_2.xlsx',
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_3.xlsx',
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_1.xlsx',
#         'Exp/Gpt/syn_gpt-3.5-turbo_roleplay_empty_1.xlsx'
#     ]
# ]

group_labels = ['逻辑学家', '形式化专家', 'NLP专家', 'LTL专家', '无角色']  # 替换为分组名称
file_labels = ['gpt4o', 'gpt3.5', 'gemini']  # 替换为文件来源名称
compare_equivalence(file_paths_groups, group_labels, file_labels)
