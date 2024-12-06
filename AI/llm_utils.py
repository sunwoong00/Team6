import google.generativeai as genai
genai.configure(api_key="AIzaSyDTEl1c4xHY0VtPrPZptIvVZAFOulgcSxA")
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class RetrievalEngine:
    def __init__(self, demo_data_path: str):
        self.naturalFormat = True
        with open(demo_data_path, 'r', encoding='utf-8') as f:
            self.demo_set = json.load(f)
        self.sentence_embedder = SentenceTransformer("all-MiniLM-L12-v2")

    def single_retrieval(self, query, category=None):
        query_emb = self.sentence_embedder.encode([query])
        best_item = None
        best_dist = float('inf')
        
        # Loop through each category in the JSON file
        for cat, items in self.demo_set.items():
            if category and cat != category:
                continue  # Skip categories that don't match the specified category
            
            for item in items:
                # Combine fields into a single text to represent the item
                if cat == "뉴스":
                    item_text = f"{item['title']} on {item['date']}"
                
                item_emb = self.sentence_embedder.encode([item_text])
                dist = 1 - cosine_similarity(query_emb, item_emb)[0][0]
                
                # Keep track of the best match
                if dist < best_dist:
                    best_dist = dist
                    best_item = (cat, item)  # Store both category and item for context
        
        return best_item  # Return the best matching item

    def search_demo(self, query, category=None):
        result_text = ''
        best_item = self.single_retrieval(query, category=category)

        if best_item:
            cat, item = best_item
            if cat == "뉴스":
                result_text = f"뉴스: {item['title']} on {item['date']} on {item['description']}"
        
        return result_text

def response_1_prompt(text, raginput):
    base_prompt_1 = '''
아래는 정리된 대화 내용입니다. 이 대화에서 대화자(특히 지적 장애인이나 경계선 지능 장애인)가 위험한 상황에 놓였는지 판단하고, 위험한 상황일 경우 이를 해결하기 위한 방법을 포함하여 요약해주세요. 결과는 딕셔너리 형식으로 작성해야 합니다.

위험이 없다고 판단될 경우:
F

위험이 있다고 판단될 경우:
T
~~~~

해당 출력 구조를 무조건 지켜서 일반 텍스트로 출력해줘.
LLM 응답에서 코드 블록을 사용하지 말고 일반 텍스트로 답변해 주세요.

다음은 예시입니다:

입력:
안녕하세요 오늘 날씨가 좋아요 어디 가시는 길이세요 그냥 산책 나왔어요 저도 비슷하게 걷고 있었어요

출력:
F

입력:
아저씨가 계속 따라오고 있어요 뒤에 계속 걸어오고 있어요 너무 무서워요 어두운 골목이에요 그냥 집에 가려고 했는데 자꾸 말을 걸려고 해요

출력:
T
아저씨가 계속 따라오며 불안감을 느끼고 있습니다. 밝은 곳으로 이동하거나 가까운 가게나 사람이 많은 곳으로 가서 도움을 요청하세요. 주변에 도움을 줄 사람이 없다면 112에 신고하거나, 가까운 사람에게 연락을 시도하세요.

아래는 실시간 입력과 관련될 수도 있는 실시간 예시입니다.
해당 예시를 통해 위험여부가 추가로 있는지 확인해주세요.

다음은 예시입니다:

Rag: [뉴스: 서울 도심, 주말마다 대규모 집회로 시민 불편 on 2024-11-08 on 서울 광화문 일대에서는 주말마다 대규모 집회와 시위가 지속적으로 열려 시민들의 불편이 가중되고 있습니다.]
입력: 광화문 쪽으로 가고 있는데 사람이 엄청 많네. 뭐 하는 건지 알아? 그냥 주말이라 그런 거 아닐까? 그런데 소리도 크고 조금 무서운 느낌이 드는 것 같아. 에이, 별일 없겠지. 그냥 지나가자. 그래, 별거 아니겠지. 빨리 가면 문제 없을 거야.
출력:
T
광화문에서 대규모 집회로 인해 혼잡하고 불안감을 느낄 수 있지만, 위험을 인지하지 못하고 계속 이동하려고 하고 있습니다. 상황이 안전하지 않을 수 있으니 혼잡 지역을 피하거나 신중히 행동하세요.

여기서부턴 실제 입력입니다.

Rag: '''
    base_prompt_2 = '''
입력:'''

    base_prompt_3 = '''


출력:
'''
    return base_prompt_1 + raginput + base_prompt_2 +  text + base_prompt_3


def response_2_prompt(text):
    base_prompt_1 = '''당신이 지금 겪고 있는 상황에 대해 도와줄게요. 아래의 질문에 답을 해주세요. 나는 안전을 가장 중요하게 생각하며, 어떤 경우든 위험할 수 있는 상황이라면 당신에게 행동을 권하지 않고 대기하라고 할 거예요. 하지만, 위험하지 않은 질문이라면 선택이나 결정을 도와줄게요.

지금 하고 싶은 일이 무엇인지, 또는 결정하기 어려운 일이 무엇인지 간단히 설명해 주세요.
만약, 그 일이 위험과 관련되었다면, (예: 길 건너기, 화기 다루기 등) 바로 행동하지 말고, 도움이 올 때까지 대기하세요. 이럴 때는 주변에 도움을 요청하거나, 보호자 또는 신뢰할 수 있는 사람에게 전화하세요.
만약 그 일이 일상적인 선택과 관련된 거라면, 내가 필요한 정보를 알려드릴게요. 예를 들어, 어떤 음료를 마실지, 어떤 물건을 선택할지 고민이 된다면, 각 선택의 장점과 단점을 간단히 설명해 줄게요.

답변 형식은 아래와 같이 지켜주세요.
해당 출력 구조를 무조건 지켜서 일반 텍스트로 출력해줘.
LLM 응답에서 코드 블록을 사용하지 말고 일반 텍스트로 답변해 주세요.

예시 질문 1: "횡단보도가 파란불인데 차가 오고 있어요. 어떻게 해야 하나요?"
답변: 차가 보인다면, 길을 건너지 말고 안전한 장소에서 보호자에게 전화하세요. 절대로 혼자 판단하지 말고, 대기하세요.

예시 질문 2: "음료수 두 개 중 뭘 마실지 모르겠어요. 한 개는 주스이고, 다른 한 개는 탄산음료예요."
답변: 주스는 건강에 더 좋을 수 있고, 탄산음료는 시원하고 청량한 느낌을 줄 거예요. 당신이 원하는 기분에 따라 선택하면 좋겠어요!

어떤 경우든, 나와 함께라면 당신은 안전하고, 올바른 선택을 할 수 있을 거예요. 그럼, 지금 하고 싶은 일에 대해 말해주세요.
질문: '''

    base_prompt_2 = '''답변:'''

    return base_prompt_1 + text + '\n' + base_prompt_2

def rag_response_1(summary_text):
    engine = RetrievalEngine(demo_data_path='/home/sunwoong89/skku/RE:ALThon/Team6/AI/new_infor.json')
    query = summary_text
    result = engine.search_demo(query, category="뉴스")
    return result



def llm_response_1(summary_text):
    # print("$$$$$$$$$$$$$$$$$$$$")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(response_1_prompt(summary_text, rag_response_1(summary_text)))
    # filtered_lines = [line for line in response.text.splitlines() if "```" not in line]
    # print(filtered_lines[0])
    return response.text


def llm_response_2(summary_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(response_2_prompt(summary_text))
    # print(response.text)
    # filtered_lines = [line for line in response.text.splitlines() if "`" not in line]
    # print(filtered_lines[0])
    return response.text

# #위험상황 예시
# llm_response("길을 잃은 것 같아요 여기가 어디인지 모르겠어요 핸드폰 배터리도 거의 다 떨어졌어요 주변에 사람이 있나요 아니요 지나가던 사람이 도와준다고 하긴 했는데 계속 이상한 말을 하고 있어서 무서워요 가까운 가게나 사람들이 있는 곳으로 이동할 수 있나요 지금 너무 멀어서 갈 수 없어요")

# #위험상황이 아닌 예시
# llm_response("오늘 영화 보러 가기로 했는데 친구가 아직 안 와서 기다리고 있어요 얼마나 늦는다고 했나요 한 10분 정도 더 걸린대요 근처 카페에서 기다리고 있어요 음료 마시면서요 영화 시간은 언제인가요 20분 남았어요 친구 오면 바로 극장으로 갈 거예요")

# #위험상황 예시 rag 사용
# print(rag_response_1("광화문"))