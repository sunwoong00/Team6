import React, { ButtonHTMLAttributes } from 'react';
import './Button.css';

export type ButtonPreset = 'default' | 'primary';

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
    className?: string;
    preset?: ButtonPreset;
    children?: React.ReactNode; // Define children prop type
}

const Button: React.FC<ButtonProps> = ({
    className = '',
    onClick,
    preset = 'default',
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

export default Button;