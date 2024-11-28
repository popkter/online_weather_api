from openai import OpenAI

from function_call import FUNCTION_CALL_TOOLS

CHAT_API_KEY = ""

CLIENT = OpenAI(api_key=CHAT_API_KEY, base_url="https://api.deepseek.com")

# 发送消息
def send_messages(messages):
    response = CLIENT.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=FUNCTION_CALL_TOOLS
    )
    return response.choices[0].message

# 流式响应
def stream_response(messages):
    return CLIENT.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=True
    )