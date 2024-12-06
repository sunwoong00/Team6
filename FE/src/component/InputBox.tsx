import React, { InputHTMLAttributes } from 'react';
import './InputBox.css';

export type InputBoxPreset = 'default' | 'primary';

interface InputBoxProps extends InputHTMLAttributes<HTMLButtonElement> {
    className?: string;
    label: string;
    placeholder?: string;
}

const Button: React.FC<InputBoxProps> = ({
    className = '',
    label, //이름 & 비밀번호
    placeholder, 
}) => {
    return (
        <div className='input-container'>
            {/* change to label later */}
            <span className='title'>{label}</span> 
        <input
            className={`input-box ${className}`} 
            type="text"
            placeholder={placeholder}
        >
        </input>
        </div>
    );
};

export default Button;