import re
import pandas as pd
import os
def extract_atomic_propositions_ordered(ltl):
    """
    从 LTL 公式中提取原子命题，保持它们在公式中的出现顺序。
    :param ltl: 输入的 LTL 公式
    :return: 按照出现顺序的原子命题列表
    """
    operators = {"G", "F", "X", "U", "|", "&", "->", "<->", "!"}
    stack = []
    atomic_props = []
    current_token = ""
    
    i = 0
    while i < len(ltl):
        char = ltl[i]
        
        if char in {"(", ")"}:
            if current_token.strip() and current_token.strip() not in operators:
                if current_token.strip() not in atomic_props:
                    atomic_props.append(current_token.strip())
            current_token = ""
            
            if char == "(":
                stack.append(char)
            elif char == ")":
                if stack:
                    stack.pop()
        
        elif char in {" ", "\t"}:
            if current_token.strip() and current_token.strip() not in operators:
                if current_token.strip() not in atomic_props:
                    atomic_props.append(current_token.strip())
            current_token = ""
        
        elif char in "|&":
            if current_token.strip() and current_token.strip() not in operators:
                if current_token.strip() not in atomic_props:
                    atomic_props.append(current_token.strip())
            current_token = ""
        
        elif ltl[i:i+2] in {"->", "<-"}:
            if current_token.strip() and current_token.strip() not in operators:
                if current_token.strip() not in atomic_props:
                    atomic_props.append(current_token.strip())
            current_token = ""
            i += 1
        
        elif char.isalnum() or char == "_":
            current_token += char
        
        else:
            if current_token.strip() and current_token.strip() not in operators:
                if current_token.strip() not in atomic_props:
                    atomic_props.append(current_token.strip())
            current_token = ""
        
        i += 1
    
    if current_token.strip() and current_token.strip() not in operators:
        if current_token.strip() not in atomic_props:
            atomic_props.append(current_token.strip())
    
    return atomic_props


def replace_nl_and_ltl_consistently(nl, ltl):
    """
    按出现顺序替换 LTL 和 NL 中的原子命题，确保 AP 编号一致。
    :param nl: 自然语言描述
    :param ltl: LTL 公式
    :return: 替换后的 NL 和 LTL
    """
    # 提取原子命题按顺序
    atomic_propositions = extract_atomic_propositions_ordered(ltl)
    
    # 创建原子命题到 AP 的映射
    ap_mapping = {ap: f"AP{i + 1}" for i, ap in enumerate(atomic_propositions)}
    
    # 替换 LTL 中的原子命题
    replaced_ltl = ltl
    for ap, ap_code in ap_mapping.items():
        replaced_ltl = re.sub(rf"\b{re.escape(ap)}\b", ap_code, replaced_ltl)
    
    # 替换 NL 中的原子命题
    replaced_nl = nl
    for ap, ap_code in ap_mapping.items():
        if ap in replaced_nl:
            replaced_nl = replaced_nl.replace(ap, ap_code)
        else:
            ap_with_spaces = ap.replace("_", " ")
            if ap_with_spaces in replaced_nl:
                replaced_nl = replaced_nl.replace(ap_with_spaces, ap_code)
    
    return replaced_nl, replaced_ltl


# # 执行替换
# for i, (nl, ltl) in enumerate(zip(nl_list, ltl_list)):
#     replaced_nl, replaced_ltl = replace_nl_and_ltl_consistently(nl, ltl)
#     print(f"Example {i + 1}:")
#     print(f"Original NL: {nl}")
#     print(f"Replaced NL: {replaced_nl}")
#     print(f"Original LTL: {ltl}")
#     print(f"Replaced LTL: {replaced_ltl}")
#     print("-" * 50)


file_name = "Dateset_100.xlsx"
file_path = os.path.join(os.path.dirname(__file__), "../Dataset", file_name)
file_path = "/home/xuyilongfei/project/logicExpert/Dataset/Dataset_100.xlsx"
df = pd.read_excel(file_path)

# Process each row in the DataFrame
processed_data = []
for index, row in df.iterrows():
    original_nl = row['en']
    original_ltl = row['ltl']
    
    replaced_nl, replaced_ltl = replace_nl_and_ltl_consistently(original_nl, original_ltl)
    processed_data.append({'en': replaced_nl, 'ltl': replaced_ltl})

# Create a new DataFrame with processed data
processed_df = pd.DataFrame(processed_data)

# Save the new DataFrame to a file with "preprocessed_" prefix
output_path = file_path.replace(file_path.split("/")[-1], f"preprocess2_{file_path.split('/')[-1]}")
processed_df.to_excel(output_path, index=False)

print(f"Processed file saved to {output_path}")