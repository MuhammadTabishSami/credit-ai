// // src/api/axiosInstance.js
// import axios from 'axios';

// const baseURL = process.env.REACT_APP_API_URL || (process.env.NODE_ENV === 'production'
//   ? 'http://35.178.138.99:8001/predictdata' // AWS endpoint
//   : 'http://localhost:8001/predictdata');       // Local development URL

// const axiosInstance = axios.create({
//   baseURL: baseURL,
//   timeout: 10000,  // optional timeout setting
//   headers: {
//     'Content-Type': 'application/json',
//   },
// });

// export default axiosInstance;

// src/api/axiosInstance.js
import axios from 'axios';

// Determine the base URL based on the environment variable and NODE_ENV
const baseURL = process.env.REACT_APP_API_URL || (process.env.NODE_ENV === 'production'
  ? 'http://35.178.138.99:8001' // AWS endpoint
  : 'http://localhost:8001');    // Local development URL

const axiosInstance = axios.create({
  baseURL: baseURL,
  timeout: 10000,  // Optional timeout setting
  headers: {
    'Content-Type': 'application/json',
  },
});

export default axiosInstance;
