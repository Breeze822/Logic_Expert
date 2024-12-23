# Logic Expert



python src/file_translation.py --model gemini --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/ExpI/ExpI_D/SUM_prompt_set.txt  --output_dir Exp/Gemini/ --prompt_type similar --neigh_num 20


python src/file_translation.py --model gemini --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/ExpI/ExpI_D/SUM_prompt_set.txt  --output_dir Exp/Gemini/ --prompt_type few --neigh_num 20


python src/file_translation.py --model gemini --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gemini/ --prompt_type roleplay --neigh_num 20


python src/file_translation.py --model gemini --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gemini/ --prompt_type roleplay --neigh_num 20

python src/file_translation.py --model  gpt-3.5-turbo --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gemini/ --prompt_type roleplay --neigh_num 20

python src/file_translation.py --model  gpt-3.5-turbo --file Dataset/Dataset_1.xlsx --prompt_path prompt_set/Role/mathematician_prompt.txt  --output_dir Exp/Gpt/ --prompt_type roleplay --neigh_num 20