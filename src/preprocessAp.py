import re
def extract_atomic_propositions(ltl):
    """
    使用栈解析 LTL 公式，提取原子命题，确保区分逻辑操作符和原子命题。
    :param ltl: 输入的 LTL 公式
    :return: 原子命题集合
    """
    operators = {"G", "F", "X", "U", "|", "&", "->", "<->", "!"}
    stack = []
    atomic_props = set()
    current_token = ""
    
    i = 0
    while i < len(ltl):
        char = ltl[i]
        
        if char in {"(", ")"}:
            # 碰到括号，可能是开始或结束一个嵌套
            if current_token.strip() and current_token.strip() not in operators:
                atomic_props.add(current_token.strip())
            current_token = ""
            
            if char == "(":
                stack.append(char)
            elif char == ")":
                if stack:
                    stack.pop()
        
        elif char in {" ", "\t"}:
            # 空格分割完成一个可能的 token
            if current_token.strip() and current_token.strip() not in operators:
                atomic_props.add(current_token.strip())
            current_token = ""
        
        elif char in "|&":
            # 单字符双目操作符
            if current_token.strip() and current_token.strip() not in operators:
                atomic_props.add(current_token.strip())
            current_token = ""
        
        elif ltl[i:i+2] in {"->", "<-"}:
            # 双字符双目操作符
            if current_token.strip() and current_token.strip() not in operators:
                atomic_props.add(current_token.strip())
            current_token = ""
            i += 1  # 跳过下一个字符
        
        elif char.isalnum() or char == "_":
            # 构造可能的原子命题
            current_token += char
        
        else:
            # 其他字符（如逻辑运算符等）
            if current_token.strip() and current_token.strip() not in operators:
                atomic_props.add(current_token.strip())
            current_token = ""
        
        i += 1
    
    # 检查最后一个 token
    if current_token.strip() and current_token.strip() not in operators:
        atomic_props.add(current_token.strip())
    
    return atomic_props


def replace_nl_and_ltl(nl, ltl):
    """
    将 LTL 和对应的 NL 描述中的原子命题替换为 AP1, AP2, ...
    :param nl: 自然语言描述
    :param ltl: LTL 公式
    :return: 替换后的 NL 和 LTL
    """
    # 提取 LTL 中的原子命题
    atomic_propositions = list(extract_atomic_propositions(ltl))
    
    # 创建原子命题到 AP 的映射
    ap_mapping = {ap: f"AP{i + 1}" for i, ap in enumerate(atomic_propositions)}
    
    # 替换 LTL 中的原子命题
    replaced_ltl = ltl
    for ap, ap_code in ap_mapping.items():
        # 确保精确匹配原子命题
        replaced_ltl = re.sub(rf"\b{re.escape(ap)}\b", ap_code, replaced_ltl)
    
    # 替换 NL 中的原子命题
    replaced_nl = nl
    for ap, ap_code in ap_mapping.items():
        # 先查找完全匹配的原子命题
        if ap in replaced_nl:
            replaced_nl = replaced_nl.replace(ap, ap_code)
        else:
            # 再查找空格替换后的版本
            ap_with_spaces = ap.replace("_", " ")
            if ap_with_spaces in replaced_nl:
                replaced_nl = replaced_nl.replace(ap_with_spaces, ap_code)
    
    return replaced_nl, replaced_ltl


# 输入示例
nl_list = [
    "a bridge closes involves that whenever a train has been launched then in the future the semaphore is yellow",
    "when FkXcmihRktQmk then every time V_xIUgDchXP then it is going to happen that TDXFQVE afterwards"
]

ltl_list = [
    "G(( bridge_closes ) -> G(( train_has_been_launched ) -> F( semaphore_is_yellow )))",
    "G(( FkXcmihRktQmk ) -> G(( V_xIUgDchXP ) -> F( TDXFQVE )))"
]

# 执行替换
for i, (nl, ltl) in enumerate(zip(nl_list, ltl_list)):
    replaced_nl, replaced_ltl = replace_nl_and_ltl(nl, ltl)
    print(f"Example {i + 1}:")
    print(f"Original NL: {nl}")
    print(f"Replaced NL: {replaced_nl}")
    print(f"Original LTL: {ltl}")
    print(f"Replaced LTL: {replaced_ltl}")
    print("-" * 50)
