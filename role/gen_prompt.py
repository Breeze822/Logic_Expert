import pandas as pd

df = pd.read_excel('./Roles_least.xlsx')
with open('./empty_prompt.txt', 'r') as f:
    empty_prompt = f.read()

def gen_article(role):
    if role[0] == 'h':
        return 'an' if role[1].lower() in ['a', 'e', 'i', 'o', 'u'] else 'a'
    return 'an' if role[0].lower() in ['a', 'e', 'i', 'o', 'u'] else 'a'

prompts = []
# for _, row in df.iterrows():
#     role = row['role']
#     description = row['description']
#     article = gen_article(role)  
#     prompt = f"You are {article} {role} , {description} {empty_prompt}."
#     prompts.append(prompt)

# print(prompts)

for _, row in df.iterrows():
    role = row['role']
    description = row['description']
    article = gen_article(role)  
    prompt = f"You are {article} {role}, {description} {empty_prompt}."
    dic = {}
    dic["role"] = role
    dic["prompt"] = prompt
    prompts.append(dic)

# 将 prompts 转换为 DataFrame
prompts_df = pd.DataFrame(prompts)

# 保存为 Excel 文件
prompts_df.to_excel("prompts.xlsx", index=False)