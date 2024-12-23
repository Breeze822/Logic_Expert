# import google.generativeai as genai
# import os
# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "http://127.0.0.1:7890"
# genai.configure(api_key="AIzaSyDzIx4cJGqoaFmg43kagPzoeZ3Y00-DDag")
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Explain how AI works")
# print(response.text)



import requests

# 测试 Gemini API 的基础 GET 请求
url = "https://api.gemini.com/v1/symbols"
try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        print("Gemini API 连接成功！")
        print("返回的数据：", response.json())
    else:
        print(f"Gemini API 请求失败，状态码：{response.status_code}")
except requests.exceptions.RequestException as e:
    print("连接错误：", e)
