import React, { ButtonHTMLAttributes } from 'react';
import './Button.css';

export type ButtonPreset = 'default';

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
    className?: string;
    preset?: ButtonPreset;
}

const Button: React.FC<ButtonProps> = ({
    className = '',
    onClick,
    preset = 'default',
    children,
}) => {
    const presetStyles = {
        default: {
            background: '#5DB075',
            text: 'preset-text-default',
            border: 'preset-border-default',
        }
    }

    const {
        background: presetBackground,
        text: presetText,
        border: presetBorder,
    } = presetStyles[preset]

    return (
        <button 
            className={`button ${presetText} ${presetBorder} ${className}`}
            onClick={onClick}
            style={{ backgroundColor: presetBackground }}
        >
           <div className="button-content">{children}</div>
        </button>
    )
}

export default Button;