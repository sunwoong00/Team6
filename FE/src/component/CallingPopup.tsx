import "./CallingPopup.css";

interface CallingPopupProps {
    onClick?: () => void; // Optional click handler
}

function CallingPopup({ onClick }: CallingPopupProps) {
    const stateText = "보호자에게\n전화 연결 중입니다...";
    const cancelText = "연결 취소하기";

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

export default CallingPopup;
