import React from "react";
import CallingOption from "../component/CallingOption";
import "./Call.css";

function CallPage() {

    const safer = "보호자";
    const phoneNum = "010-1234-5678";

    return (
        <div className="app-frame">
            <div className="call-page">
                <div className="call-header">
                    <h1 className="call-title">{safer}</h1>
                    <p className="call-number">{phoneNum}</p>
                </div>
                <div className="call-options">
                    <CallingOption />
                </div>
            </div>
        </div>
    );
}

export default CallPage;
