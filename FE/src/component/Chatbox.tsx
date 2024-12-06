import React, { useState } from 'react';
import './Chatbox.css';
import ICON from '../icon/index';

interface ChatMessageProps {
  message: string;
  sender: string; // Keep this as required
  isSender: boolean;
  avatar: () => JSX.Element; // Avatar is a function returning a JSX element
}

const ChatMessage: React.FC<ChatMessageProps> = ({ message, sender, isSender, avatar }) => {
  return (
    <div className={`chat-message ${isSender ? 'chat-message--sender' : ''}`}>
      <div className="chat-avatar">
        <div className="avatar-background">
          {avatar()} 
        </div>
      </div>
      <div className="chat-content">
        <p className="chat-text">{message}</p>
      </div>
    </div>
  );
};

const ChatBox: React.FC = () => {
  const [inputValue, setInputValue] = useState('');
  const [messages, setMessages] = useState<ChatMessageProps[]>([]); // State for messages

  const handleSendMessage = () => {
    if (inputValue.trim()) {
      const newMessage = {
        message: inputValue,
        sender: 'User', 
        isSender: true,
        avatar: ICON.userProfileIcon,
      };
      setMessages([...messages, newMessage]); // Update messages state
      setInputValue(''); // Clear input after sending
    }
  };

  return (
    <div>
      <div className="flex">
        <ICON.logoIcon usecase='LLM' />
        <ICON.userIcon />
        <div className='meter'>3m</div>
      </div> 
      <div className="chat-box">
        <div className="chat-messages">
          {messages.map((message, index) => (
            <ChatMessage key={index} {...message} />
          ))}
        </div>
        <div className="input-wrapper">
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
            {ICON.arrowIcon()}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatBox;

// import React, { useState } from 'react';
// import './Chatbox.css';
// import ICON from '../icon/index';
// import Distance from './Distance';

// interface ChatMessageProps {
//   message: string;
//   sender: string; // Keep this as required
//   isSender: boolean;
//   avatar: () => JSX.Element; // Avatar is a function returning a JSX element
// }

// const ChatMessage: React.FC<ChatMessageProps> = ({ message, sender, isSender, avatar }) => {
//   return (
//     <div className={`chat-message ${isSender ? 'chat-message--sender' : ''}`}>
//       <div className="chat-avatar">
//         <div className="avatar-background">
//           {avatar()} 
//         </div>
//       </div>
//       <div className="chat-content">
//         <p className="chat-text">{message}</p>
//       </div>
//     </div>
//   );
// };

// interface ChatBoxProps {
//   messages: ChatMessageProps[];
// }

// const ChatBox: React.FC<ChatBoxProps> = ({ messages }) => {
//   const [message, setMessage] = useState('');
//   const [inputValue, setInputValue] = useState('');

//   const handleSendMessage = () => {
//     if (inputValue.trim()) {
//       console.log('Sending message:', inputValue);
//       setMessage(inputValue);
//       setInputValue(''); // Clear input after sending
//     }
//   };

//   return (
//     <div>
//         <div className="flex">
//             <ICON.logoIcon usecase='LLM' />
//             <ICON.userIcon />
//             <div className='meter'>3m</div>
//         </div> 
//         <div className="chat-box">
//             <div className="chat-messages">
//                 {messages.map((message, index) => (
//                 <ChatMessage key={index} {...message} />
//                 ))}
//             </div>
//             <div className="input-wrapper">
//                 <button
//                     className="record-button"
//                     // onClick={handleVoiceRecord}
//                     aria-label="Send message"
//                 >
//                     {ICON.arrowIcon()}
//                 </button>
//                 <input
//                     type="text"
//                     value={inputValue}
//                     onChange={(e) => setInputValue(e.target.value)}
//                     onKeyDown={(e) => e.key === 'Enter' && handleSendMessage()}
//                     className="input-box"
//                 />
//                 <button
//                     className="send-button"
//                     onClick={handleSendMessage}
//                     aria-label="Send message"
//                 >
//                     {ICON.arrowIcon()}
//                 </button>
//             </div>
//         </div>
//     </div>
    
//   );
// };

// export default ChatBox;

// // import React, { useState } from 'react';
// // import './Chatbox.css';
// // import ICON from '../icon/index';

// // interface ChatMessageProps {
// //   message: string;
// //   sender: string; // Keep this as required
// //   isSender: boolean;
// //   avatar: () => JSX.Element;
// // }

// // const ChatMessage: React.FC<ChatMessageProps> = ({ message, sender, isSender, avatar }) => {
// //   return (
// //     <div className={`chat-message ${isSender ? 'chat-message--sender' : ''}`}>
// //         <div className="chat-avatar">
// //             {avatar()}
// //         </div>
// //       <div className="chat-content">
// //         <p className="chat-text">{message}</p>
// //       </div>
// //     </div>
// //   );
// // };

// // interface ChatBoxProps {
// //   messages: ChatMessageProps[];
// // }

// // const ChatBox: React.FC<ChatBoxProps> = ({ messages }) => {
// //   const [inputValue, setInputValue] = useState('');

// //   const handleSendMessage = () => {
// //     if (inputValue.trim()) {
// //       console.log('Sending message:', inputValue);
// //       setInputValue(''); // Clear input after sending
// //     }
// //   };

// //   return (
// //     <div className="chat-box">
// //       <div className="chat-messages">
// //         {messages.map((message, index) => (
// //           <ChatMessage key={index} {...message} />
// //         ))}
// //       </div>
// //         <input
// //           type="text"
// //           value={inputValue}
// //           onChange={(e) => setInputValue(e.target.value)}
// //           onKeyDown={(e) => e.key === 'Enter' && handleSendMessage()}
// //           className="input-box"
// //         />
// //         <ICON.arrowIcon />
// //       </div>
// //   );
// // };

// // export default ChatBox;
