import "./ConnectFailPopup.css";

interface ConnectFailPopupProps {
    onClick?: () => void; // Optional click handler
}

function ConnectFailPopup({ onClick }: ConnectFailPopupProps) {
    const stateText = "전화 연결에 실패했습니다.";
    const cancelText = "확인";

    return (
        <div className="popup-container">
            <div className="popup">
                <div className="text">
                    <div className="textSt">{stateText}</div>
                </div>
                <div
                    className="cancel"
                    onClick={() => {
                        if (onClick) {
                            onClick(); // Call the passed onClick handler
                        }
                    }}
                >
                    {cancelText}
                </div>
            </div>
        </div>
    );
}

export default ConnectFailPopup;
