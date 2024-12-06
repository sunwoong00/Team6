import axios from 'axios';

export const getInfo = async () => {
    try {
        const response = await axios.get(`/get-info`);
        return response.data;
    } catch (error) {
        console.error('Error getting info', error);
        throw error;
    }
};

export const uploadStt = async (data: any) => {
    try {
        const response = await axios.post(`/upload-stt`, data);
        return response.data;
    } catch (error) {
        console.error('Error uploading stt', error);
        throw error;
    }
};

export const getLLMData = async () => {
    try {
        const response = await axios.get(`/get-llm-data`);
        return response.data;
    } catch (error) {
        console.error('Error getting LLM data', error);
        throw error;
    }
};

export const getLLMResponse = async () => {
    try {
        const response = await axios.get(`/get-llm-response2`);
        return response.data;
    } catch (error) {
        console.error('Error getting LLM response', error);
        throw error;
    }
};