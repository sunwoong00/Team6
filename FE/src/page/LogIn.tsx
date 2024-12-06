import React from "react";
import { useNavigate } from "react-router-dom";
import Button from "../component/Button";
import ICON from "../icon";
import InputBox from "../component/InputBox";
import "./LogIn.css";
import { login } from "../api/auth";

function LogInPage() {
    const navigate = useNavigate();

    const handleSignUpClick = () => {
        navigate("/SignUp"); // 회원가입 페이지로 이동
    };

    const handleLoginClick = async () => {
        try {
            const response = await login({ id: '', password: '', })
            console.log(response);
            navigate("/Main"); 
        } catch {
            console.log("Error login account")
        }
    };

    return (
        <div className="app-frame">
            <div className="login-page">
                <div className="login-container">
                    <div className="login-logo">
                        <ICON.logoIcon usecase="login" />
                    </div>
                    <h1 className="login-title">로그인</h1>
                    <div className="input-container">
                        <InputBox label="이메일" placeholder="이메일을 입력하세요" />
                        <InputBox label="비밀번호" placeholder="비밀번호를 입력하세요" type="password" />
                    </div>
                    <div className="link-container">
                        <a href="#" className="forgot-password">비밀번호를 잊으셨나요?</a>
                        <a onClick={handleSignUpClick} className="sign-up">회원가입</a>
                    </div>
                    <Button className="login-button" onClick={handleLoginClick}>
                        로그인
                    </Button>
                    <div className="social-login-container">
                        <span>Or Login with</span>
                        <div className="social-icons">
                            <ICON.facebookIcon />
                            <ICON.googleIcon />
                            <ICON.appleIcon />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default LogInPage;
