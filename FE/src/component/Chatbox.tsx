import React, { useState } from 'react';
import './Chatbox.css';
import ICON from '../icon/index'

interface ChatMessageProps {
  message: string;
  sender: string;
  isSender: boolean;
  avatar: string;
}

const ChatMessage: React.FC<ChatMessageProps> = ({ message, sender, isSender, avatar }) => {
  return (
    <div className={`chat-message ${isSender ? 'chat-message--sender' : ''}`}>
      <img src={avatar} alt={sender} className="chat-avatar" />
      <div className="chat-content">
        <p className="chat-text">{message}</p>
      </div>
    </div>
  );
};

interface ChatBoxProps {
  messages: ChatMessageProps[];
}

const ChatBox: React.FC<ChatBoxProps> = ({ messages }) => {
  const [inputValue, setInputValue] = useState('');

  const handleSendMessage = () => {
    if (inputValue.trim()) {
      console.log('Sending message:', inputValue);
      setInputValue(''); // Clear input after sending
    }
  };

  return (
    <div className="chat-box">
      <div className="chat-messages">
        {messages.map((message, index) => (
          <ChatMessage key={index} {...message} />
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSendMessage()}
          className="input-box"
        />
        <button 
          className="send-button" 
          onClick={handleSendMessage}
          aria-label="Send message"
        >
            {/* <img className="icon">{ICON.arrowIcon()}</img> */}
        </button>
      </div>
    </div>
  );
};

export default ChatBox;
