from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import firebase_admin
from firebase_admin import credentials, db

# FastAPI 앱 초기화
app = FastAPI()

# Firebase 초기화
cred = credentials.Certificate("team6-8924e-firebase-adminsdk-vdshl-543124bd12.json")  # Firebase JSON 키 파일 경로
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://team6-8924e-default-rtdb.firebaseio.com/'  # Firebase Realtime Database URL
})

# Pydantic 모델
class LoginData(BaseModel):
    username: str
    password: str
    id: EmailStr
    user_protector: bool

# /login 엔드포인트
@app.post("/login")
async def login(data: LoginData):
    try:
        # Firebase Database에 데이터 저장
        ref = db.reference('users')  # 'users'라는 노드에 데이터 저장
        ref.push({
            'username': data.username,
            'id': data.id,
            'password': data.password,
            'user_protector': data.user_protector,
            'gps': None,
            'stt_data': None,
            'slm_llm': None,
            'slm_data': None,
            'llm_data': None
        })
        return {"message": "User saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving user: {str(e)}")