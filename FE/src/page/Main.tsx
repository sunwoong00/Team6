import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Distance from "../component/Distance";
import Question from "../component/Question";
import ToggleButton from "../component/ToggleButton";
import CallingPopup from "../component/CallingPopup";
import ConnectFailPopup from "../component/ConnectFailPopup";
import "./Main.css";

function MainPage() {
    const [popupType, setPopupType] = useState<"calling" | "failed" | null>(null); // 팝업 타입
    const navigate = useNavigate();
    const [timeoutId, setTimeoutId] = useState<NodeJS.Timeout | null>(null); // 타이머 ID 저장

    useEffect(() => {
        console.log("Popup type updated:", popupType);

        if (popupType === "calling") {
            // "calling" 상태에서 10초 후 CallPage로 이동
            const id = setTimeout(() => {
                console.log("10 seconds elapsed, navigating to CallPage...");
                navigate("/call");
            }, 10000);
            setTimeoutId(id);
        }

        return () => {
            // 컴포넌트 언마운트 시 타이머 정리
            if (timeoutId) {
                clearTimeout(timeoutId);
                console.log("Timeout cleared");
            }
        };
    }, [popupType, navigate, timeoutId]);

    const handleQuestionClick = () => {
        console.log("Question clicked!");
        setPopupType("calling"); // CallingPopup 표시
    };

    const handleCancelClick = () => {
        console.log("Cancel button clicked");
        if (timeoutId) {
            clearTimeout(timeoutId); // 타이머 취소
            console.log("Timeout cleared");
        }
        setPopupType("failed"); // ConnectFailPopup으로 전환
    };

    const handleConfirmClick = () => {
        console.log("Confirm button clicked");
        navigate("/llm"); // LLMPage로 이동
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
                {popupType === "calling" && (
                    <CallingPopup onClick={handleCancelClick} />
                )}
                {popupType === "failed" && (
                    <ConnectFailPopup onClick={handleConfirmClick} />
                )}
            </div>
        </div>
    );
}

export default MainPage;
