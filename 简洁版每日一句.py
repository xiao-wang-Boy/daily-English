# daily_quick.py
# 超简洁版本 - 每次运行获取一句

import requests
from datetime import datetime

# ============== DeepSeek API配置 ==============
API_KEY = "xxxxx"  # 在这里填写你的API Key
API_URL = "https://api.deepseek.com/v1/chat/completions"


def get_sentence(topic="励志名言"):
    """获取一句英文句子及翻译"""
    prompt = f"请用英文生成一句关于'{topic}'的名言，并附上中文翻译。格式：英文|||中文"

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.8,
        "max_tokens": 300
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=20)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            if '|||' in content:
                en, zh = content.split('|||')
                return en.strip(), zh.strip()
    except:
        pass
    return None, None


def main():
    print("\n" + "=" * 50)
    print("🤖 每日一句英语")
    print("=" * 50)

    if not API_KEY:
        print("⚠️  请在代码中设置 API_KEY")
        return

    # 可以修改这里的主题
    topic = "人生哲理"   # 改成你想要的主题

    print(f"\n⏳ 正在获取 '{topic}' 主题句子...")
    en, zh = get_sentence(topic)

    if en and zh:
        print("\n" + "=" * 50)
        print(f"📝 {en}")
        print("-" * 50)
        print(f"📖 {zh}")
        print("=" * 50)
        print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("❌ 获取失败，请检查网络")


if __name__ == "__main__":
    main()
