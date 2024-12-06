# 위드미:<br/> Multimodal Input기반 지적장애인/경계선 지능인을 위한 안전도우미


![image](https://github.com/user-attachments/assets/86da15ab-f193-4dc8-a3ad-3c2ce7a43237)

지적장애인과 경계선 지능인들은 일상생활에서 위험 상황에 처할 가능성이 높고, 이를 인지하거나 적절히 대처하기 어려운 경우가 많습니다. "위드미"는 멀티모달 입력(음성, 텍스트, 이미지 등)을 기반으로 사용자에게 상황에 맞는 안전 정보를 제공하고, 위험 상황을 예방하거나 신속히 대처할 수 있도록 지원하는 스마트 안전 도우미 서비스입니다.

---

### Repository 설명

##### Frontend
* React기반 안전도우미 frontend 코드

##### Backend
* FastAPI기반 안전도우미 backend 코드
* firebase기반 데이터베이스 구축

##### LM
* slm과 llm의 조합으로 효율적인 사용
* RAG를 통한 최신 정보 업데이트 가능

<img width="716" alt="image" src="https://github.com/user-attachments/assets/187a2207-d650-40bc-b882-e83fe46d43d5">

---

### 주요 기능

- 로그인
- 회원가입
- 실시간 gps 기능
- 주변 음성 분석
- SLM 기반 text 요약
- LLM 기반 위험 상황 분석
- LLLM 기반 위험 상황 해결법 제시

---

### 안전도우미 사용 방식

1. 사용자와 보호자가 gps 거리상으로 멀리 떨어졌을 때 작동한다.

2. 사용자 주변 음성을 실시간으로 분석
    - 버튼을 누른 경우 80초 동안 주변 소리 분석 시작
        
3. 주변 소리를 stt를 통해 text로 변환 후 SLM 기반으로 요약

4. 요약한 내용에 대해서 LLM을 통한 위험 상황 분석

5. 위험 상황 발생시 보호자에게 연락

6. 보호자에게 연락되지 않을 경우 LLM이 직접 해결법을 만들어서 제시
   


### 개발자들  (ㄱ-ㄴ-ㄷ)

**김재민** - https://github.com/JMKim101

**방선웅** - https://github.com/sunwoong00

**안상현** - https://github.com/Ahnsanghyun-hi

**안종현** - https://github.com/aj0hnd

**유챤이** - https://github.com/qianyi-yu

**임동현** - https://github.com/hyunee0110

