from fastapi import FastAPI, HTTPException, Query, UploadFile, File
from pydantic import BaseModel, EmailStr
from firebase_admin import credentials, db
from dotenv import load_dotenv
import firebase_admin
import requests
import sys, os, logging
import json

sys.path.append(os.path.abspath("../AI"))
from llm_utils import llm_response_1, llm_response_2
from slm_utils import slm_response

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# FastAPI 앱 초기화
app = FastAPI()

# Firebase 초기화
cred = credentials.Certificate("team6-8924e-firebase-adminsdk-vdshl-543124bd12.json")  # Firebase JSON 키 파일 경로
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://team6-8924e-default-rtdb.firebaseio.com/'  # Firebase Realtime Database URL
})

# .env 파일 로드
load_dotenv()

# API 키 가져오기
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

if not GOOGLE_MAPS_API_KEY:
    raise ValueError("Google Maps API Key is not set in the .env file")

# Pydantic 모델
class Login(BaseModel):
    id: EmailStr
    password: str

class RegisterData(BaseModel):
    username: str
    id: EmailStr
    password: str
    user_protector: bool

'''class GPSData(BaseModel):
    username: str
    latitude: float
    longitude: float'''

class GPS(BaseModel):
    username: str
    latitude: float
    longitude: float


# /login 엔드포인트
@app.post("/login")
async def login(data: Login):
    try:
        # Firebase Database 참조
        ref = db.reference('users')
        users = ref.get()  # 모든 사용자 데이터 가져오기

        # id와 password가 일치하는 사용자 찾기
        for key, value in users.items():
            if value.get('id') == data.id and value.get('password') == data.password:
                return {"message": "Login successful", "username": value.get('username')}

        # 사용자 찾지 못한 경우
        raise HTTPException(status_code=401, detail="Invalid email or password")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during login: {str(e)}")
    

# /register 엔드포인트
@app.post("/register")
async def register(data: RegisterData):
    try:
        # Firebase Database에 데이터 저장
        ref = db.reference('users')  # 'users'라는 노드에 데이터 저장
        ref.push({
            'username': data.username,
            'id': data.id,
            'password': data.password,
            'user_protector': data.user_protector,
            'latitude': 0,
            'longitude' : 0,
            'stt_data': '',
            'slm_data': '',
            'llm_data': {
                'new': False,
                'reply': ''
            }
        })
        return {"message": "User saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving user: {str(e)}")


# /get_info 엔드포인트
@app.get("/get-info")
async def get_info(username: str = Query(..., description="The username to search for")):
    try:
        # Firebase Database 참조
        ref = db.reference('users')
        users = ref.get()  # 모든 사용자 데이터 가져오기

        # Firebase에 데이터가 없는 경우 처리
        if not users:
            raise HTTPException(status_code=404, detail="No users found")

        # username에 해당하는 사용자 찾기
        for key, value in users.items():
            if value.get("username") == username:
                return {"user": value}

        # username이 없는 경우
        raise HTTPException(status_code=404, detail=f"User with username '{username}' not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching user info: {str(e)}")


@app.post("/upload-stt")
async def upload_stt(username: str, input_text: str):
    try:
        # Firebase Database 참조
        ref = db.reference('users')
        users = ref.get()  # 모든 사용자 데이터 가져오기

        # Firebase에 데이터가 없는 경우 처리
        if not users or not isinstance(users, dict):
            raise HTTPException(status_code=404, detail="No users found")

        # username에 해당하는 사용자 찾기
        for key, value in users.items():
            if not isinstance(value, dict):  # value가 dict가 아니면 건너뛰기
                continue

            if value.get("username") == username:
                # 현재 stt_data 가져오기
                stt_data = value.get("stt_data", "")
                updated_stt_data = stt_data + input_text  # 기존 데이터에 입력 텍스트 추가

                # stt_data 업데이트
                user_ref = ref.child(key)
                if len(updated_stt_data) > 350:  # 길이가 350자를 초과하면 처리
                    # SLM 함수 호출
                    summary_response = slm_response(updated_stt_data)

                    '''# 반환 값이 딕셔너리인지 확인
                    if not isinstance(summary_response, dict):
                        raise HTTPException(status_code=500, detail="SLM response is not a valid dictionary")

                    summary = summary_response.get("요약")'''
                    summary = summary_response
                    if not summary:
                        raise HTTPException(status_code=400, detail="SLM response does not contain '요약'.")

                    # SLM 요약 데이터를 기반으로 LLM 함수 호출
                    llm_response = llm_response_1(summary)

                    '''# 반환 값이 딕셔너리인지 확인
                    if not isinstance(llm_response, dict):
                        raise HTTPException(status_code=500, detail="LLM response is not a valid dictionary")'''

                    # print(type(llm_response))

                    # is_risky = llm_response.get("위험", False)

                    print(llm_response)

                    # if isinstance(llm_response, str):
                    #     try:
                    #         llm_response = json.loads(llm_response)  # JSON 문자열을 Python dict로 변환
                    #     except json.JSONDecodeError as e:
                    #         print(f"JSON 변환 오류: {e}")
                    #         llm_response = {}  # 변환 실패 시 기본값 설정

                    # 이제 dict로 동작
                    # print(type(llm_response))  # <class 'dict'>
                    # llm_response = list(llm_response)
                    is_risky = llm_response[0]

                    
                    # print(is_risky)
                    

                    if is_risky=='T':
                        # "위험"이 True인 경우 "reply" 및 "new" 업데이트
                        reply = llm_response.split("\n")[1]
                        print("reply: " + reply)
                        llm_data = value.get("llm_data", {})
                        user_ref.update({
                            "llm_data": {
                                # **llm_data,  # 기존 llm_data 유지
                                "reply": reply,
                                "new": True
                            }
                        })
                        user_ref.update({"stt_data": ""})  # stt_data 초기화
                        return {
                            "message": "LLM response indicates risk. Reply stored in llm_data.",
                            "reply": reply
                        }

                    # "위험"이 False인 경우 업데이트만 수행
                    user_ref.update({
                        "slm_data": summary,
                        "stt_data": ""  # stt_data 초기화
                    })
                    return {
                        "message": "SLM and LLM responses processed successfully",
                        "summary": summary,
                        "stt_data": ""
                    }

                else:
                    # 길이가 350자 이하인 경우 업데이트만 수행
                    user_ref.update({
                        "stt_data": updated_stt_data
                    })
                    return {"message": "STT data updated successfully", "stt_data": updated_stt_data}

        # username이 없는 경우
        raise HTTPException(status_code=404, detail=f"User with username '{username}' not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading STT data: {str(e)}")


# /gps 엔드포인트
@app.post("/update_gps")
async def update_gps(data: GPS):
    try:
        # Firebase Database 참조
        ref = db.reference('users')
        users = ref.get()  # 모든 사용자 데이터 가져오기

        if not users:
            raise HTTPException(status_code=404, detail="No users found")

        # username에 해당하는 사용자 찾기 및 업데이트
        for key, value in users.items():
            if value.get("username") == data.username:
                user_ref = ref.child(key)
                user_ref.update({
                    "latitude": data.latitude,
                    "longitude": data.longitude
                })
                return {
                    "message": f"Location updated for user {data.username}",
                    "latitude": data.latitude,
                    "longitude": data.longitude
                }

        # username이 없는 경우
        raise HTTPException(status_code=404, detail=f"User with username '{data.username}' not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating GPS: {str(e)}")


@app.post("/get-llm-data")
async def get_llm_data(username: str):
    try:
        # Firebase Database 참조
        ref = db.reference('users')
        users = ref.get()  # 모든 사용자 데이터 가져오기

        if not users:
            raise HTTPException(status_code=404, detail="No users found")

        # username에 해당하는 사용자 찾기
        for key, value in users.items():
            if value.get("username") == username:
                llm_data = value.get("llm_data", {})
                if llm_data.get("new") == True:  # Boolean True 확인
                    # 'reply' 값 저장 후 업데이트
                    reply = llm_data.get("reply", "")
                    user_ref = ref.child(key)
                    user_ref.update({
                        "llm_data": {
                            **llm_data,  # 기존 llm_data 유지
                            "new": False,  # 'new' 값을 Boolean False로 변경
                            "reply": ""  # 'reply' 값을 빈 문자열로 변경
                        }
                    })
                    return {"reply": reply}

                # 'new' 값이 False인 경우 아무 작업 안 함
                return {"message": "No new data to process"}

        # username이 없는 경우
        raise HTTPException(status_code=404, detail=f"User with username '{username}' not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching llm data: {str(e)}")


@app.post("/get-llm-response2")
async def get_llm_response2(input_text: str):
    try:
        # ../AI/llm_utils.py에 정의된 LLM 함수 호출
        response = llm_response_2(input_text)
        # if isinstance(response, str):
        #     try:
        #         response = json.loads(response)  # JSON 문자열을 Python dict로 변환
        #     except json.JSONDecodeError as e:
        #         print(f"JSON 변환 오류: {e}")
        #         response = {}

        # JSON 응답에서 "요약" 키 추출
        summary = response
        if not summary:
            raise HTTPException(status_code=400, detail="Response does not contain '요약'.")

        # 요약 내용 반환
        return {"summary": summary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing input: {str(e)}")