import "./StopPopup.css";

function StopPopup(props: { onClick?: () => void }) {
    const stateText = "1분간 녹음을 중단합니다.";
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

export default StopPopup;
