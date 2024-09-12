import React from 'react';
import './Result.css';

const Result = ({ result }) => {
  return (
    <div className="result">
      <h2>PREDICTION:</h2>
      <p>{result}</p>
    </div>
  );
};

export default Result;
