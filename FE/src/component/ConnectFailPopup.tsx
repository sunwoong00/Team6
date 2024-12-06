import "./ConnectFailPopup.css";

function ConnectFailPopup(props: { onClick?: () => void }) {
    const stateText = "전화 연결에 실패했습니다.";
    const cancelText = "확인";

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

export default ConnectFailPopup;
