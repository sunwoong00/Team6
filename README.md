# 위드미:
# Multimodal Input기반 지적장애인/경계선 지능인을 위한 안전도우미

<img src="https://drive.google.com/uc?export=view&id=12ogQey6rqwke_tgX9q2ydozusaihkGYa" alt="drawing" style="width:1000px;"/>

지적장애인과 경계선 지능인들은 일상생활에서 위험 상황에 처할 가능성이 높고, 이를 인지하거나 적절히 대처하기 어려운 경우가 많습니다. **"위드미"**는 멀티모달 입력(음성, 텍스트, 이미지 등)을 기반으로 사용자에게 상황에 맞는 안전 정보를 제공하고, 위험 상황을 예방하거나 신속히 대처할 수 있도록 지원하는 스마트 안전 도우미 서비스입니다.

---

### Repository 설명

##### Frontend
* React기반 

##### Backend
* FastAPI기반 

##### LLM

---

### 주요 기능

- 로그인
- 회원가입
- 

---

### 안전도우미 사용 방식

1. 레시피를 입력 받는다

2. 조리동작을 추출한다
    - EtriOpenAPI를 통해 동사(VV)를 분별, 이후 딕션너리를 통해 단순 동사인지 조리동작에 해당하는 동사인지 판단 → 조리동작을 기준으로 sequences 분리 <a href="https://github.com/iiVSX/lesik/tree/master/Backend#readme">
    <img src="https://img.shields.io/badge/백앤드 README-<COLOR>"
        style="height : auto; margin-left : 8px; margin-right : 8px;"/></a>
        
3. 레시피 구성 요소들을 추출한다
    - 개체명 인식을 통해 식재료, 용량, 첨가물, 온도, 시간을 추출한다
    - 학습시킨 KoELECTRA를 사용하여 개체명 인식을 진행하고 추가적으로 Rule-based을 통해 발견하지 못한 요소들을 딕셔너리를 통해 찾아낸다 <a href="https://github.com/iiVSX/lesik/blob/master/KoELECTRA/README.md">
    <img src="https://img.shields.io/badge/KoELECTRA README-<COLOR>"
        style="height : auto; margin-left : 8px; margin-right : 8px;"/></a>
        
4. 레시피 부가 요소 추출한다
    - Rule-Based를 통해 해당 조리 문장에 알맞은 조리도구를 찾아낸다 <a href="https://github.com/iiVSX/lesik/tree/master/Backend#readme">
    <img src="https://img.shields.io/badge/백앤드 README-<COLOR>"
        style="height : auto; margin-left : 8px; margin-right : 8px;"/></a>


### 개발자들  (ㄱ-ㄴ-ㄷ)

**김재민** - https://github.com/JMKim101

**방선웅** - https://github.com/sunwoong00

**안상현** - https://github.com/Ahnsanghyun-hi

**안종현** - https://github.com/aj0hnd

**유챤이** - https://github.com/qianyi-yu

**임동현** - https://github.com/hyunee0110


### 관련 링크

<a href="https://docs.google.com/presentation/d/1eMl0jOE0LA6ZvWR7yKkrVwtqXevlYt39/edit#slide=id.p1">
    <img src="https://img.shields.io/badge/발표자료 파워포인트-<COLOR>"
        style="height : auto; margin-left : 8px; margin-right : 8px;"/>
</a>


<a href="https://github.com/iiVSX/lesik/blob/master/KoELECTRA/README.md">
    <img src="https://img.shields.io/badge/KoELECTRA Readme-<COLOR>"
        style="height : auto; margin-left : 8px; margin-right : 8px;"/>
</a>


<a href="https://github.com/sunwoongskku/lesik/blob/master/Crawling/README.md">
    <img src="https://img.shields.io/badge/Crawling Readme-<COLOR>"
        style="height : auto; margin-left : 8px; margin-right : 8px;"/>
</a>


<a href="https://github.com/iiVSX/lesik/tree/master/Backend#readme">
    <img src="https://img.shields.io/badge/Backend Readme-<COLOR>"
        style="height : auto; margin-left : 8px; margin-right : 8px;"/>
</a>

<a href="https://whoami125.notion.site/AWS-EC2-4fc2808f27664eddba10483ccaa127f6">
    <img src="https://img.shields.io/badge/EC2 생성 및 보안 설정-<COLOR>"
        style="height : auto; margin-left : 8px; margin-right : 8px;"/>
</a>
