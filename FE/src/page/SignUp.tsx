import React, {useState} from "react";
import { useNavigate } from "react-router-dom";
import Button from "../component/Button";
import ICON from "../icon";
import InputBox from "../component/InputBox";
import "./SignUp.css";
import { register } from "../api/auth";

function SignUpPage() {
    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [isProtector, setIsProtector] = useState(false);
    const [agreeToGPS, setAgreeToGPS] = useState(false);

    const handleSignUpClick = async () => {

        if (!username || !email || !password) {
            alert("모든 필드를 입력해 주세요.");
            return;
        }

        if (!agreeToGPS) {
            alert("GPS 정보 수집 및 사용 약관에 동의해야 합니다.");
            return;
        }

        try {
            const response = await register({ 
                username: username,
                email: email, 
                password: password, 
                user_protecter: !isProtector})
            console.log(response);
            navigate("/LogIn"); 
        } catch {
            console.log("Error register account")
        }
    };

    return (
        <div className="app-frame">
            <div className="sign-up-page">
                <div className="sign-up-logo">
                    <ICON.logoIcon usecase="signup" />
                </div>
                <h1 className="sign-up-title">회원가입</h1>
                <div className="input-container">
                    <InputBox label="이름" placeholder="이름" onChange={(e) => setUsername(e.target.value)}/>
                    <InputBox label="이메일" placeholder="이메일" onChange={(e) => setEmail(e.target.value)}/>
                    <InputBox label="비밀번호" placeholder="비밀번호" type="password" onChange={(e) => setPassword(e.target.value)}/>
                </div>
                <div className="agreement-container">
                    <label className="checkbox-container">
                        <input type="checkbox" className="checkbox" checked={isProtector}
                        onChange={() => setIsProtector(!isProtector)}/>
                        <span className="label-text">저는 <b>보호자</b>입니다.</span>
                    </label>
                    <label className="checkbox-container">
                        <input type="checkbox" className="checkbox" checked={agreeToGPS}
                        onChange={() => setAgreeToGPS(!agreeToGPS)}/>
                        <span className="label-text">
                            <b>GPS 정보 수집</b> 및 사용 약관에 동의합니다.
                        </span>
                    </label>
                </div>
                <Button className="sign-up-button" onClick={handleSignUpClick}>
                    회원가입
                </Button>
                <div className="login-link-container">
                    이미 계정이 있습니까?{" "}
                    <a href="#" className="login-link" onClick={handleSignUpClick}>
                        로그인
                    </a>
                </div>
            </div>
        </div>
    );
}

export default SignUpPage;
