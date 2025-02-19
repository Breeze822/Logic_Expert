import pandas as pd
import os
import concurrent.futures
import time
from prompt_speedup import *
# df = pd.read_excel('/home/xuyilongfei/project/logicExpert/role/Roles_least.xlsx')
df = pd.read_excel('./role/Roles_least.xlsx')
with open('./role/empty_prompt.txt', 'r', encoding='utf-8') as f:
    empty_prompt = f.read()

def gen_article(role):
    if role[0] == 'h':
        return 'an' if role[1].lower() in ['a', 'e', 'i', 'o', 'u'] else 'a'
    return 'an' if role[0].lower() in ['a', 'e', 'i', 'o', 'u'] else 'a'

prompts = []
for _, row in df.iterrows():
    role = row['role']
    description = row['description']
    article = gen_article(role)  
    prompt = f"You are {article} {role} , {description} {empty_prompt}."
    dic = {}
    dic["role"] = role
    dic["prompt"] = prompt
    prompts.append(dic)


def process_row(role,prompt_profix):
    filename = "/home/xuyilongfei/project/logicExpert/Dataset/Dataset_100_AP_2.xlsx"
    df = pd.read_excel(filename)
    data = []
    print("Start")
    print("=" * 50)
    ltl_exists = 'ltl' in df.columns
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        nl = row['en']  
        ltl = row['ltl'] if ltl_exists else None  
        final_prompt = (prompt_profix + "\nNatural Language: " 
                            + nl )
        # print(final_prompt)
        # print("Using Gemini")
        # response = gemini_answer(final_prompt)
        response = gpt_answer(final_prompt,"gpt-3.5-turbo")
        print(response)
        nl_translation = split_formula_to_get_final_LTL(response)
        if ltl_exists:
            truth_ltl = ltl.strip()
            final_res = nl_translation[0].replace(" ", "")
            final_res = final_res.replace("`", "")
            truth_ltl = truth_ltl.replace(" ", "")
            result = final_res == truth_ltl.replace(" ", "")
            reference = list(truth_ltl.replace(" ",""))  
            candidate = list(final_res)  
            
            eq = spot_equivalent(final_res, truth_ltl)
            
            score = sentence_bleu([reference], candidate, weights=(0.5,0.5,0,0))
            data.append([nl, final_res, truth_ltl.replace(" ", ""), result, score, eq])
            print(data[-1])
        else:
            data.append([nl, final_res])
    # Create new DataFrame to store results
    if ltl_exists:
        columns = ['NL', 'LTL', 'Truth_LTL', 'Result', 'BLEU', 'Equivalence']
    else:
        columns = ['NL', 'LTL']   
 
    result_df = pd.DataFrame(data, columns=columns)

    end_time = time.time()
    execution_time = end_time - start_time
    rounded_value = round(execution_time, 3)
    output_filedir_path = "/home/xuyilongfei/project/logicExpert/role/exp"
    if output_filedir_path != "":
        base_file_name = output_filedir_path + f"/{role}"
        # base_file_name = output_filedir_path + f"/syn_{engine}_{prompt_type}_infp"
        # base_file_name = output_filedir_path + f"/syn_{engine}_{prompt_type}_esfp"
        # base_file_name = output_filedir_path + f"/syn_{engine}_{prompt_type}_entj"


    else:    
        base_file_name = output_filedir_path + f"/default"
    
    # Check for existing file and increment the suffix number until an unused name is found
    counter = 1
    file_name = f"{base_file_name}_1.xlsx"  # start with _1
    while os.path.exists(file_name):  # if file exists, increment the counter and try a new file name
        counter += 1
        file_name = f"{base_file_name}_{counter}.xlsx"
    
    result_df.to_excel(file_name, index=False)

    # prompt_file_list = []
    # prompt_path = os.path.join(project_dir, 'prompt_set')
    # for prompt_file in os.listdir(prompt_path):
    #     if prompt_file.endswith(".txt"):
    #         filepath = os.path.join(prompt_path, prompt_file)
    #         prompt_file_list.append(filepath)

    
    print(f"The code execution is completed and it takes {execution_time} seconds in total.")
    print(f'Results for {role} method saved to {file_name}')
    
    

def process_dataframe_parallel(df):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(lambda prompt: process_row(prompt["role"], prompt["prompt"]), prompts)
    

process_dataframe_parallel(prompts)
