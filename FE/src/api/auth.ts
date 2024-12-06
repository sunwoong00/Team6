import axios from 'axios';

export const login = async (data: any) => {
    try {
        const response = await axios.post(`/login`, data);
        return response.data;
    } catch (error) {
        console.error('Error posting login:', error);
        throw error;
    }
};

export const register = async (data: any) => {
    try {
        const response = await axios.post(`/register`, data);
        return response.data;
    } catch (error) {
        console.error('Error posting register:', error);
        throw error;
    }
};