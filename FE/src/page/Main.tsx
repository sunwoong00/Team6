import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Distance from "../component/Distance";
import Question from "../component/Question";
import ToggleButton from "../component/ToggleButton";
import CallingPopup from "../component/CallingPopup";
import "./Main.css";

function MainPage() {
    const [popupType, setPopupType] = useState<"calling" | null>(null); // 팝업 타입
    const [counter, setCounter] = useState(5); // 5초 카운트다운
    const [isCountingDown, setIsCountingDown] = useState(false); // 카운트다운 시작 여부
    const navigate = useNavigate();

    useEffect(() => {
        if (isCountingDown && counter > 0) {
            const interval = setInterval(() => {
                setCounter((prevCounter) => prevCounter - 1);
            }, 1000); // 1초마다 감소
            return () => clearInterval(interval); // 컴포넌트 언마운트 시 정리
        } else if (isCountingDown && counter === 0) {
            navigate("/call"); // 5초 후 CallPage로 이동
        }
    }, [isCountingDown, counter, navigate]);

    const handleQuestionClick = () => {
        console.log("Question clicked!");
        setPopupType("calling"); // CallingPopup 표시
        setIsCountingDown(true); // 카운트다운 시작
        setCounter(5); // 카운터 초기화
    };

    const handleCancelClick = () => {
        console.log("Cancel button clicked");
        setPopupType(null); // CallingPopup 닫기
        setIsCountingDown(false); // 카운트다운 중단
        navigate("/llm"); // LLMPage로 바로 이동
    };

    return (
        <div className="app-frame">
            <div className="main-page">
                <div className="top-section">
                    <div className="distance-container">
                        <Distance />
                    </div>
                    <div className="toggle-section">
                        <span className="time">23:30</span>
                        <ToggleButton />
                    </div>
                </div>
                <div className="question-section" onClick={handleQuestionClick}>
                    <Question />
                </div>

                {/* 팝업 렌더링 */}
                <CallingPopup onClick={handleCancelClick} />

                {/* 카운트다운 표시 */}
                {isCountingDown && popupType === "calling" && (
                    <div className="counter">
                        <p>Redirecting in {counter} seconds...</p>
                    </div>
                )}
            </div>
        </div>
    );
}

export default MainPage;
