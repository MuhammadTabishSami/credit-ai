// import axios from 'axios';
import React, { useState } from 'react';

import './App.css';
import Header from './components/Header';
import Result from './components/Result'; 
import heroVideo from './assets/hero-video.mp4';
import CreditForm from './components/CreditForm';
import workflowimage from './assets/credit_workflow.png';

function App() {
  const [result, setResult] = useState(null);
  
  return (
    <div className="App">
      <Header />
      <div className="hero">
        <video className="hero-video" autoPlay muted loop>
          <source src={heroVideo} type="video/mp4" />
        </video>
        <div className="bubbles-container">
          <div className="bubble small"></div>
          <div className="bubble medium"></div>
          <div className="bubble large"></div>
          <div className="bubble small"></div>
          <div className="bubble medium"></div>
          <div className="bubble large"></div>
        </div>
        <div class="hero-heading">
        <span class="typing">CREDIT <span class="highlighted">AI</span></span>
  </div>
        <p className="hero-subtext">Check your creditworthiness effortlessly!</p>
      </div>
      <div className="container">
        <div className="column image-upload-column">
          <img src={workflowimage} alt="Uploaded" className="uploaded-image" />
        </div>
        <div className="column form-column">
          <CreditForm setResult={setResult} />
        </div>
      </div>
      <div className="prediction-section">
        <Result result={result} />
      </div>
    </div>
  );
}

export default App;
