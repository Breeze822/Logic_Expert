import spot
from Global import *
import time
def spot_equivalent (
    left : str,
    right : str
) -> bool:
    try:
        # 尝试将 left 转换为 spot.formula
        if not isinstance(left, spot.formula):
            left = spot.formula(left)

        # 尝试将 right 转换为 spot.formula
        if not isinstance(right, spot.formula):
            right = spot.formula(right)

        # 调用 Spot 的等价性检查函数
        ans = spot.are_equivalent(left, right)
        return ans
    except Exception as e:
        # 捕获所有异常并输出调试信息（可选）
        print(f"Error occurred in spot_equivalent: {e}")
        # 发生错误时返回 False
        return False

if __name__ == "__main__":
    prompt = "Every a is eventually followed by a e.   translate it to ltl"
    # try:
    response = Gemini_model.generate_content(prompt)
    ans = "G(a->Fe)"

    print(response.text)
    print("Equivalent" if spot_equivalent(response, ans) else "Not equivalent")
    # except Exception as e:
    #     print("Error! retry after for 30 seconds...")
    #     time.sleep(30)