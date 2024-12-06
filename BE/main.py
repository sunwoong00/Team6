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
class Login(BaseModel):
    id: EmailStr
    password: str

class RegisterData(BaseModel):
    username: str
    id: EmailStr
    password: str
    user_protector: bool

class GPS(BaseModel):
    username: str


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
            'gps': None,
            'stt_data': None,
            'slm_llm': None,
            'slm_data': None,
            'llm_data': None
        })
        return {"message": "User saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving user: {str(e)}")


'''
# /gps 엔드포인트
@app.post("/gps")
'''