import axios from "axios";

const API_URL = "http://127.0.0.1:5000"; // Flask Backend URL

export const registerUser = async (username, password) => {
    try {
        const response = await axios.post(`${API_URL}/register`, { username, password });
        return response.data;
    } catch (error) {
        throw error.response?.data || "Registration failed";
    }
};

export const loginUser = async (username, password) => {
    try {
        const response = await axios.post(`${API_URL}/login`, { username, password });
        return response.data;
    } catch (error) {
        throw error.response?.data || "Login failed";
    }
};

export const fetchBooks = async (token) => {
    try {
        const response = await axios.get(`${API_URL}/books`, {
            headers: { Authorization: `Bearer ${token}` },
        });
        return response.data;
    } catch (error) {
        throw error.response?.data || "Failed to fetch books";
    }
};

export const addBook = async (token, bookData) => {
    try {
        const response = await axios.post(`${API_URL}/books`, bookData, {
            headers: { Authorization: `Bearer ${token}` },
        });
        return response.data;
    } catch (error) {
        throw error.response?.data || "Failed to add book";
    }
};

export const updateBook = async (token, bookId, bookData) => {
    try {
        const response = await axios.put(`${API_URL}/books/${bookId}`, bookData, {
            headers: { Authorization: `Bearer ${token}` },
        });
        return response.data;
    } catch (error) {
        throw error.response?.data || "Failed to update book";
    }
};

export const deleteBook = async (token, bookId) => {
    try {
        const response = await axios.delete(`${API_URL}/books/${bookId}`, {
            headers: { Authorization: `Bearer ${token}` },
        });
        return response.data;
    } catch (error) {
        throw error.response?.data || "Failed to delete book";
    }
};
//logout
export const logout = async (token) => {
    try {
      const response = await fetch('/api/logout', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
      });
  
      if (!response.ok) {
        throw new Error('logout not possible');
      }
  
      return await response.json();
    } catch (error) {
      throw new Error(error.message);
    }
  };
  