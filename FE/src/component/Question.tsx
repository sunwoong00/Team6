import './Question.css';
import ICON from '../icon';
import { useNavigate } from "react-router-dom";

function Question() {

    const navigate = useNavigate();

    const handleMainClick = () => {
        navigate("/Call"); // 회원가입 버튼 클릭 시 "/main" 페이지로 이동
    };
    return (
        <div className="question-container" onClick={handleMainClick}>
                <ICON.questionIcon />
        </div>
    );
}

export default Question;
