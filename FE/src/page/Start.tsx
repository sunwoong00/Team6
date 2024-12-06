import React from "react";
import { useNavigate } from "react-router-dom";
import Button from "../component/Button";
import ICON from "../icon";
import "./Start.css";

function StartPage() {
    const navigate = useNavigate();

    const handleStartClick = () => {
        navigate("/logIn");
    };

    return (
        <div className="app-frame">
            <div className="start-page">
                <div className="logo-container">
                    <ICON.logoIcon usecase="start" />
                </div>
                <div className="message">
                    위험을 예방하고 안전을 지키세요!
                </div>
                <Button onClick={handleStartClick}>지금 시작하기</Button>
            </div>
        </div>
    );
}

export default StartPage;
