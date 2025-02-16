# Logic Expert

python src/file_translation.py --model gemini --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/ExpI/ExpI_S/static_prompt.txt  --output_dir Exp/ExpI/Gemini_S/ --prompt_type similar --neigh_num 20 

python src/file_translation.py --model gemini --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/ExpI/ExpI_D/SUM_prompt_set.txt  --output_dir Exp/Gemini/ --prompt_type similar --neigh_num 20


python src/file_translation.py --model gemini --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/ExpI/ExpI_D/SUM_prompt_set.txt  --output_dir Exp/Gemini/ --prompt_type few --neigh_num 20


python src/file_translation.py --model gemini --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gemini/ --prompt_type roleplay --neigh_num 20


python src/file_translation.py --model gemini --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gemini/ --prompt_type roleplay --neigh_num 20

python src/file_translation.py --model gpt-3.5-turbo --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gpt/ --prompt_type roleplay --neigh_num 20

python src/file_translation.py --model gpt4o --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gpt4o/ --prompt_type roleplay --neigh_num 20

##
python src/file_translation.py --model gpt4o --file Dataset/Dataset_100.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gpt4o/ --prompt_type roleplay --neigh_num 20

python src/file_translation.py --model gpt-3.5-turbo --file Dataset/Dataset_100.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gpt/ --prompt_type roleplay --neigh_num 20

python src/file_translation.py --model gemini --file Dataset/Dataset_100.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gemini/ --prompt_type roleplay --neigh_num 20



##
python src/file_translation.py --model gemini --file Dataset/Dataset_100_2.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gemini/ --prompt_type roleplay --neigh_num 20

python src/file_translation.py --model gpt-3.5-turbo --file Dataset/Dataset_100_2.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gpt/ --prompt_type roleplay --neigh_num 20

python src/file_translation.py --model gemini --file Dataset/Dataset_100_2.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gemini/ --prompt_type roleplay --neigh_num 20

### ap
python src/file_translation.py --model gemini --file Dataset/Dataset_100_AP_2.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/AP/Gemini/ --prompt_type roleplay --neigh_num 20

python src/file_translation.py --model gpt-3.5-turbo --file Dataset/Dataset_100_AP_2.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/AP/Gpt/ --prompt_type roleplay --neigh_num 20

python src/file_translation.py --model gpt4o --file Dataset/Dataset_100_AP_2.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/AP/Gpt4o/ --prompt_type roleplay --neigh_num 20