import "./CheckPopup.css";

function CheckPopup(props: { onClick?: () => void }) {
    const stateText = "전화 연결에 실패했습니다.";
    const cancelText_1 = "예";
    const cancelText_2 = "아니오";

    return (
    <div className="popup-container">
        <div className="popup">
            <div className="text">
                <div className="textSt">{stateText}</div>
            </div>
            <div className="button-group">
                <div className="cancel" onClick={props.onClick}>
                    {cancelText_1}
                </div>
                <div className="cancel" onClick={props.onClick}>
                    {cancelText_2}
                </div>
            </div>
        </div>
    </div>
    );
}

export default CheckPopup;
