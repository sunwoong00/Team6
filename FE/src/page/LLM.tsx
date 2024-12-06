import React from "react";
import { useNavigate } from "react-router-dom";
import ChatBox from "../component/Chatbox";
import ICON from "../icon";
import "./LLM.css";

// Mock data for messages
const messages = [
    {
        message: 'I have a question about my order.',
        sender: 'User', // Add sender property
        isSender: true,
        avatar: ICON.userProfileIcon,
    },
    {
        message: "Okay, please provide me with your order number and I'll be happy to assist you.",
        sender: 'Support', // Add sender property
        isSender: false,
        avatar: ICON.userProfileIcon,
    },
];

function ChatBoxPage() {
    const navigate = useNavigate();

    const handleStartClick = () => {
        navigate("/logIn");
    };

    return (
        <div className="app-frame">
            <div className="llm-page">
                <ChatBox messages={messages} />
            </div>
        </div>
    );
}

export default ChatBoxPage;
