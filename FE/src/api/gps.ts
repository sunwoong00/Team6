import axios from 'axios';

export const updateGps = async (data: any) => {
    try {
        const response = await axios.post(`/update-gps`, data);
        return response.data;
    } catch (error) {
        console.error('Error update gps', error);
        throw error;
    }
};