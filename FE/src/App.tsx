import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import StartPage from "./page/Start";
import LogInPage from "./page/LogIn";

function App() {
    return (
        <Router>
            <Routes>
                {/* StartPage는 기본 경로("/") */}
                <Route path="/" element={<StartPage />} />
                {/* LoginPage는 "/logIn" 경로 */}
                <Route path="/LogIn" element={<LogInPage />} />
            </Routes>
        </Router>
    );
}

export default App;