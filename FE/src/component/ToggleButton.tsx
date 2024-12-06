import React, { useState } from "react";
import "./ToggleButton.css";

function ToggleButton() {
  const [isActive, setIsActive] = useState(false);

  const handleClick = () => {
    setIsActive(!isActive); // 상태를 반전
  };

  return (
    <div
      className={`toggle-button ${isActive ? "active" : ""}`}
      onClick={handleClick}
    >
      <div className={`circle ${isActive ? "active-circle" : ""}`}></div>
    </div>
  );
}

export default ToggleButton;
