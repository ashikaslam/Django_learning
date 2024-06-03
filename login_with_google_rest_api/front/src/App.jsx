// src/App.jsx
import React from 'react';
import { GoogleLogin } from '@react-oauth/google';
import axios from 'axios';
import './index.css';
function App() {
  const responseMessage = (response) => {
    console.log('Login Success:', response);

    // Send the token to the backend
    sendTokenToBackend(response.tokenId);
  };

  const errorMessage = (error) => {
    console.log('Login Failed:', error);
  };

  const sendTokenToBackend = (tokenId) => {
    // Send a POST request to your backend with the token
    axios.post('http://127.0.0.1:8000/', { token: tokenId })
      .then(response => {
        console.log('Backend Response:', response.data);
      })
      .catch(error => {
        console.error('Error sending token to backend:', error);
      });
  };

  return (
    <div>
      <h2>React Google Login</h2>
      <br />
      <br />
      <GoogleLogin onSuccess={responseMessage} onError={errorMessage} />
    </div>
  );
}

export default App;
