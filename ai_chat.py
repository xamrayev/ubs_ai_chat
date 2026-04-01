from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

def ai_chat(savol:str):
    completion = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
        "role": "user",
        "content": f"{savol}"
        }
    ]
    )
    return completion.choices[0].message.content

# savol = "C++ tilini o'rganish kerakmi?"
# print(ai_chat(savol))