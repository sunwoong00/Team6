import ollama
import google.generativeai as genai
genai.configure(api_key="AIzaSyDTEl1c4xHY0VtPrPZptIvVZAFOulgcSxA")

def response_prompt(text):
    base_prompt_1 = '''아래는 STT로 변환된 대화 내용입니다. 이 대화 내용을 정리하여 불필요한 내용(중복된 대화, 의미 없는 표현, 배경 소음 등)을 제거해주세요. 중요한 내용은 간결하게 표현해 주시고, 불필요한 반복이나 맥락 없는 문장은 삭제해주세요.

아래는 예시입니다:
입력:
안녕하세요 안녕하세요 음 오늘 날씨가 좋아요 어 맞아요 날씨가 정말 좋네요 그나저나 어디 가시는 길이세요 그냥 산책 나왔어요 아 네 저도 비슷하게 걷고 있었어요

출력:
안녕하세요 오늘 날씨가 좋아요 어디 가시는 길이세요 그냥 산책 나왔어요 저도 비슷하게 걷고 있었어요

입력:
저기 아저씨가 계속 따라오고 있어요 뭐라고요 누가 따라온다고요 뒤에 계속 걸어오고 있어요 너무 무서워요 어디 계세요 지금 안전한 곳인가요 아니요 어두운 골목이에요 어떡하죠 그냥 집에 가려고 했는데 자꾸 말을 걸려고 해요

출력:
아저씨가 계속 따라오고 있어요 뒤에 계속 걸어오고 있어요 너무 무서워요 어두운 골목이에요 그냥 집에 가려고 했는데 자꾸 말을 걸려고 해요

아래는 직접 출력해야되는 입력입니다.
입력:'''

    base_prompt_2 = '''출력:'''
    return base_prompt_1 + text + '\n\n' + base_prompt_2

# def slm_response(text):
#     stream = ollama.generate(model='llama3.2:1b', prompt=response_prompt(text))
#     print(stream['response'])
#     return stream['response']

def slm_response(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(response_prompt(text))
    #print(response.text)
    return response.text

# 위험상황 예시
# print(slm_response("길을 잃은 것 같아요 어... 여기가 어디인지 모르겠어요 아... 음 핸드폰 배터리도 거의 다 떨어졌어요 주변에 사람이 있나요 아니요 어... 지나가던 사람이 도와준다고 하긴 했는데 어... 어... 계속 이상한 말을 하고 있어서 무서워요 어 음... 가까운 가게나 사람들이 있는 곳으로 이동할 수 있나요 지금 너무 멀어서 어... 음... 갈 수 없어요"))