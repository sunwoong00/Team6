import React, { ButtonHTMLAttributes } from 'react';
import './Button.css';

<<<<<<< HEAD
export type ButtonPreset = 'default' | 'primary';
=======
export type ButtonPreset = 'default';
>>>>>>> fb5609c86054ee63336f74793e9d34692b6764d9

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
    className?: string;
    preset?: ButtonPreset;
<<<<<<< HEAD
    children?: React.ReactNode; // Define children prop type
=======
>>>>>>> fb5609c86054ee63336f74793e9d34692b6764d9
}

const Button: React.FC<ButtonProps> = ({
    className = '',
    onClick,
    preset = 'default',
<<<<<<< HEAD
    children = '로그인', 
}) => {
    return (
        <button 
            className={`button ${className}`} 
            onClick={onClick}
        >
            {children}
        </button>
    );
};
=======
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
>>>>>>> fb5609c86054ee63336f74793e9d34692b6764d9

export default Button;