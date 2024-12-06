import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import StartPage from "./page/Start";
import LogInPage from "./page/LogIn";
import SignUpPage from "./page/SignUp";
import MainPage from "./page/Main";
import CallPage from "./page/Call";
import ChatBoxPage from './page/LLM'

function App() {
    return (
        <Router>
            <Routes>
                {/* StartPage는 기본 경로("/") */}
                <Route path="/" element={<StartPage />} />
                {/* LoginPage는 "/logIn" 경로 */}
                <Route path="/LogIn" element={<LogInPage />} />
                <Route path="/SignUp" element={<SignUpPage />} />
                <Route path="/Main" element={<MainPage />} />
                <Route path="/Call" element={<CallPage />} />
                <Route path="/ChatBox" element={<ChatBoxPage />}></Route>
            </Routes>
        </Router>
    );
}

export default App;
