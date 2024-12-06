from fastapi import FastAPI, HTTPException, Query, UploadFile, File
from pydantic import BaseModel, EmailStr
from firebase_admin import credentials, db
from dotenv import load_dotenv
import firebase_admin
import requests
import os

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
            'gps': None,
            'address': None,
            'stt_data': None,
            'slm_llm': None,
            'slm_data': None,
            'llm_data': None
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


'''
# /gps 엔드포인트
@app.post("/gps")
async def update_gps(data: GPSData):
    try:
        # Google Maps Reverse Geocoding API 호출
        geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "latlng": f"{data.latitude},{data.longitude}",
            "key": GOOGLE_MAPS_API_KEY
        }
        response = requests.get(geocode_url, params=params)
        response_data = response.json()

        if response.status_code != 200 or not response_data.get("results"):
            raise HTTPException(status_code=400, detail="Unable to fetch address from Google Maps API")

        # 주소 정보 추출
        address = response_data["results"][0]["formatted_address"]

        # Firebase Database에서 username에 해당하는 사용자 찾기
        ref = db.reference('users')
        users = ref.get()

        if not users:
            raise HTTPException(status_code=404, detail="No users found")

        for key, value in users.items():
            if value.get("username") == data.username:
                # 사용자 데이터 업데이트
                user_ref = ref.child(key)
                user_ref.update({
                    "latitude": data.latitude,
                    "longitude": data.longitude,
                    "address": address
                })
                return {
                    "message": f"Location updated for user {data.username}",
                    "latitude": data.latitude,
                    "longitude": data.longitude,
                    "address": address
                }

        # username이 없는 경우
        raise HTTPException(status_code=404, detail=f"User with username '{data.username}' not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating GPS: {str(e)}")
        '''


# /gps 엔드포인트
@app.post("/gps")
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
