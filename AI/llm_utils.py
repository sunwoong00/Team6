import google.generativeai as genai
genai.configure(api_key="AIzaSyDTEl1c4xHY0VtPrPZptIvVZAFOulgcSxA")

def response_1_prompt(text):
    base_prompt_1 = '''
아래는 정리된 대화 내용입니다. 이 대화에서 대화자(특히 지적 장애인이나 경계선 지능 장애인)가 위험한 상황에 놓였는지 판단하고, 위험한 상황일 경우 이를 해결하기 위한 방법을 포함하여 요약해주세요. 결과는 딕셔너리 형식으로 작성해야 합니다.

위험이 없다고 판단될 경우:
{"위험": False, "요약": ""}

위험이 있다고 판단될 경우:
{"위험": True, "요약": "~~~~"}

다음은 예시입니다:

입력:
안녕하세요 오늘 날씨가 좋아요 어디 가시는 길이세요 그냥 산책 나왔어요 저도 비슷하게 걷고 있었어요

출력:
{"위험": False, "요약": ""}

입력:
아저씨가 계속 따라오고 있어요 뒤에 계속 걸어오고 있어요 너무 무서워요 어두운 골목이에요 그냥 집에 가려고 했는데 자꾸 말을 걸려고 해요

출력:
{"위험": True, "요약": "아저씨가 계속 따라오며 불안감을 느끼고 있습니다. 밝은 곳으로 이동하거나 가까운 가게나 사람이 많은 곳으로 가서 도움을 요청하세요. 주변에 도움을 줄 사람이 없다면 112에 신고하거나, 가까운 사람에게 연락을 시도하세요."}

입력:'''

    base_prompt_2 = '''


출력:
'''
    return base_prompt_1 + text + base_prompt_2


def llm_response(summary_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(response_1_prompt(summary_text))
    print(response.text)

# #위험상황 예시
# llm_response("길을 잃은 것 같아요 여기가 어디인지 모르겠어요 핸드폰 배터리도 거의 다 떨어졌어요 주변에 사람이 있나요 아니요 지나가던 사람이 도와준다고 하긴 했는데 계속 이상한 말을 하고 있어서 무서워요 가까운 가게나 사람들이 있는 곳으로 이동할 수 있나요 지금 너무 멀어서 갈 수 없어요")

# #위험상황이 아닌 예시
# llm_response("오늘 영화 보러 가기로 했는데 친구가 아직 안 와서 기다리고 있어요 얼마나 늦는다고 했나요 한 10분 정도 더 걸린대요 근처 카페에서 기다리고 있어요 음료 마시면서요 영화 시간은 언제인가요 20분 남았어요 친구 오면 바로 극장으로 갈 거예요")
