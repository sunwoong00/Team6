import "./popup.css";

function Popup(props: { onClick?: () => void }) {
    const stateText = "보호자에게\n전화 연결 중입니다...";
    const cancelText = "연결 취소하기";

    return (
    <div className="popup-container">
        <div className="popup">
            <div className="text">
                <div className="textSt">{stateText}</div>
            </div>
            <div className="cancel" onClick={props.onClick}>
                {cancelText}
            </div>
        </div>
    </div>
    );
}

export default Popup;
