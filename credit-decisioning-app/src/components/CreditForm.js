import React, { useState } from 'react';
import './CreditForm.css';
import axios from 'axios';

function CreditForm({ setResult }) {
  const [formData, setFormData] = useState({
    debt_settlement_flag: '',
    sub_grade: '',
    grade: '',
    term: '',
    last_fico_range_high: '',
    last_fico_range_low: '',
    collection_recovery_fee: '',
    total_pymnt_inv: '',
    int_rate: '',
    fico_range_high: ''
  });

  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent the default form submission

    // Convert string values to appropriate types before sending
    const dataToSend = {
      ...formData,
      last_fico_range_high: parseFloat(formData.last_fico_range_high),
      last_fico_range_low: parseFloat(formData.last_fico_range_low),
      collection_recovery_fee: parseFloat(formData.collection_recovery_fee),
      total_pymnt_inv: parseFloat(formData.total_pymnt_inv),
      int_rate: parseFloat(formData.int_rate),
      fico_range_high: parseFloat(formData.fico_range_high)
    };

    try {
      const response = await axios.post('http://localhost:8001/predictdata', dataToSend, {
        headers: {
          'Content-Type': 'application/json'
        }
      });

      setResult(response.data.result);
      setError(null); // Clear any previous error
    } catch (error) {
      console.error('Error making prediction request:', error);
      setError('There was a problem submitting your request. Please try again.');
    }
  };

  return (
    <div className="credit-form-container">
      <h1 className="form-title">Let's Check Your Credit Worthiness!</h1>
      {error && <div className="error-message">{error}</div>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label className="form-label">Debt Settlement Flag</label>
          <select className="form-control" name="debt_settlement_flag" onChange={handleChange} required>
            <option value="">Select an option</option>
            <option value="N">No</option>
            <option value="Y">Yes</option>
          </select>
        </div>

        <div className="form-group">
          <label className="form-label">Sub Grade</label>
          <select className="form-control" name="sub_grade" onChange={handleChange} required>
            <option value="">Select an option</option>
            <option value="C3">C3</option>
            <option value="B5">B5</option>
            <option value="C5">C5</option>
            <option value="C1">C1</option>
            <option value="A2">A2</option>
            <option value="B3">B3</option>
            <option value="E4">E4</option>
            <option value="D2">D2</option>
            <option value="E5">E5</option>
            <option value="D1">D1</option>
            <option value="C2">C2</option>
            <option value="A1">A1</option>
            <option value="D4">D4</option>
            <option value="A4">A4</option>
            <option value="E2">E2</option>
            <option value="B2">B2</option>
            <option value="A5">A5</option>
            <option value="B4">B4</option>
            <option value="D5">D5</option>
            <option value="B1">B1</option>
            <option value="E3">E3</option>
            <option value="A3">A3</option>
            <option value="E1">E1</option>
            <option value="D3">D3</option>
            <option value="C4">C4</option>
            <option value="F4">F4</option>
            <option value="F5">F5</option>
            <option value="G1">G1</option>
            <option value="G5">G5</option>
            <option value="F1">F1</option>
            <option value="F2">F2</option>
            <option value="G2">G2</option>
            <option value="G4">G4</option>
            <option value="F3">F3</option>
            <option value="G3">G3</option>
          </select>
        </div>

        <div className="form-group">
          <label className="form-label">Grade</label>
          <select className="form-control" name="grade" onChange={handleChange} required>
            <option value="">Select an option</option>
            <option value="G">G</option>
            <option value="F">F</option>
            <option value="E">E</option>
            <option value="D">D</option>
            <option value="C">C</option>
            <option value="B">B</option>
            <option value="A">A</option>
          </select>
        </div>

        <div className="form-group">
          <label className="form-label">Term</label>
          <select className="form-control" name="term" onChange={handleChange} required>
            <option value="">Select an option</option>
            <option value="36 months">36 months</option>
            <option value="60 months">60 months</option>
          </select>
        </div>

        <div className="form-group">
          <label className="form-label">Last FICO Range High</label>
          <input className="form-control placeholder-input" type="number" name="last_fico_range_high" onChange={handleChange} placeholder="Enter last FICO range high" />
        </div>

        <div className="form-group">
          <label className="form-label">Last FICO Range Low</label>
          <input className="form-control placeholder-input" type="number" name="last_fico_range_low" onChange={handleChange} placeholder="Enter last FICO range low" />
        </div>

        <div className="form-group">
          <label className="form-label">Collection Recovery Fee</label>
          <input className="form-control placeholder-input" type="number" name="collection_recovery_fee" onChange={handleChange} step="0.01" placeholder="Enter collection recovery fee" />
        </div>

        <div className="form-group">
          <label className="form-label">Total Payment Involved</label>
          <input className="form-control placeholder-input" type="number" name="total_pymnt_inv" onChange={handleChange} step="0.01" placeholder="Enter total payment involved" />
        </div>

        <div className="form-group">
          <label className="form-label">Interest Rate</label>
          <input className="form-control placeholder-input" type="number" name="int_rate" onChange={handleChange} step="0.01" placeholder="Enter interest rate" />
        </div>

        <div className="form-group">
          <label className="form-label">FICO Range High</label>
          <input className="form-control placeholder-input" type="number" name="fico_range_high" onChange={handleChange} placeholder="Enter FICO range high" />
        </div>

        <div className="form-group">
          <input className="btn btn-primary predict-button" type="submit" value="PREDICT" />
        </div>
      </form>
    </div>
  );
}

export default CreditForm;


////////////////////////////////////////////////
////////////////////////////////////////////////
////////////////////////////////////////////////

// import React, { useState } from 'react';
// import './CreditForm.css';
// import axiosInstance from '../api/axiosInstance';  // Import the dynamic axios instance

// function CreditForm({ setResult }) {
//   const [formData, setFormData] = useState({
//     debt_settlement_flag: '',
//     sub_grade: '',
//     grade: '',
//     term: '',
//     last_fico_range_high: '',
//     last_fico_range_low: '',
//     collection_recovery_fee: '',
//     total_pymnt_inv: '',
//     int_rate: '',
//     fico_range_high: ''
//   });

//   const [error, setError] = useState(null);

//   const handleChange = (e) => {
//     const { name, value } = e.target;
//     setFormData({ ...formData, [name]: value });
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault(); // Prevent the default form submission

//     // Convert string values to appropriate types before sending
//     const dataToSend = {
//       ...formData,
//       last_fico_range_high: parseFloat(formData.last_fico_range_high),
//       last_fico_range_low: parseFloat(formData.last_fico_range_low),
//       collection_recovery_fee: parseFloat(formData.collection_recovery_fee),
//       total_pymnt_inv: parseFloat(formData.total_pymnt_inv),
//       int_rate: parseFloat(formData.int_rate),
//       fico_range_high: parseFloat(formData.fico_range_high)
//     };

//     try {
//       const response = await axiosInstance.post('/predictdata', dataToSend, {
//         headers: {
//           'Content-Type': 'application/json'
//         }
//       });

//       setResult(response.data.result);
//       setError(null); // Clear any previous error
//     } catch (error) {
//       console.error('Error making prediction request:', error);
//       setError('There was a problem submitting your request. Please try again.');
//     }
//   };

//   return (
//     <div className="credit-form-container">
//       <h1 className="form-title">Let's Check Your Credit Worthiness!</h1>
//       {error && <div className="error-message">{error}</div>}
//       <form onSubmit={handleSubmit}>
//         <div className="form-group">
//           <label className="form-label">Debt Settlement Flag</label>
//           <select className="form-control" name="debt_settlement_flag" onChange={handleChange} required>
//             <option value="">Select an option</option>
//             <option value="N">No</option>
//             <option value="Y">Yes</option>
//           </select>
//         </div>

//         <div className="form-group">
//           <label className="form-label">Sub Grade</label>
//           <select className="form-control" name="sub_grade" onChange={handleChange} required>
//             <option value="">Select an option</option>
//             <option value="C3">C3</option>
//             <option value="B5">B5</option>
//             <option value="C5">C5</option>
//             <option value="C1">C1</option>
//             <option value="A2">A2</option>
//             <option value="B3">B3</option>
//             <option value="E4">E4</option>
//             <option value="D2">D2</option>
//             <option value="E5">E5</option>
//             <option value="D1">D1</option>
//             <option value="C2">C2</option>
//             <option value="A1">A1</option>
//             <option value="D4">D4</option>
//             <option value="A4">A4</option>
//             <option value="E2">E2</option>
//             <option value="B2">B2</option>
//             <option value="A5">A5</option>
//             <option value="B4">B4</option>
//             <option value="D5">D5</option>
//             <option value="B1">B1</option>
//             <option value="E3">E3</option>
//             <option value="A3">A3</option>
//             <option value="E1">E1</option>
//             <option value="D3">D3</option>
//             <option value="C4">C4</option>
//             <option value="F4">F4</option>
//             <option value="F5">F5</option>
//             <option value="G1">G1</option>
//             <option value="G5">G5</option>
//             <option value="F1">F1</option>
//             <option value="F2">F2</option>
//             <option value="G2">G2</option>
//             <option value="G4">G4</option>
//             <option value="F3">F3</option>
//             <option value="G3">G3</option>
//           </select>
//         </div>

//         <div className="form-group">
//           <label className="form-label">Grade</label>
//           <select className="form-control" name="grade" onChange={handleChange} required>
//             <option value="">Select an option</option>
//             <option value="G">G</option>
//             <option value="F">F</option>
//             <option value="E">E</option>
//             <option value="D">D</option>
//             <option value="C">C</option>
//             <option value="B">B</option>
//             <option value="A">A</option>
//           </select>
//         </div>

//         <div className="form-group">
//           <label className="form-label">Term</label>
//           <select className="form-control" name="term" onChange={handleChange} required>
//             <option value="">Select an option</option>
//             <option value="36 months">36 months</option>
//             <option value="60 months">60 months</option>
//           </select>
//         </div>

//         <div className="form-group">
//           <label className="form-label">Last FICO Range High</label>
//           <input className="form-control placeholder-input" type="number" name="last_fico_range_high" onChange={handleChange} placeholder="Enter last FICO range high" />
//         </div>

//         <div className="form-group">
//           <label className="form-label">Last FICO Range Low</label>
//           <input className="form-control placeholder-input" type="number" name="last_fico_range_low" onChange={handleChange} placeholder="Enter last FICO range low" />
//         </div>

//         <div className="form-group">
//           <label className="form-label">Collection Recovery Fee</label>
//           <input className="form-control placeholder-input" type="number" name="collection_recovery_fee" onChange={handleChange} step="0.01" placeholder="Enter collection recovery fee" />
//         </div>

//         <div className="form-group">
//           <label className="form-label">Total Payment Involved</label>
//           <input className="form-control placeholder-input" type="number" name="total_pymnt_inv" onChange={handleChange} step="0.01" placeholder="Enter total payment involved" />
//         </div>

//         <div className="form-group">
//           <label className="form-label">Interest Rate</label>
//           <input className="form-control placeholder-input" type="number" name="int_rate" onChange={handleChange} step="0.01" placeholder="Enter interest rate" />
//         </div>

//         <div className="form-group">
//           <label className="form-label">FICO Range High</label>
//           <input className="form-control placeholder-input" type="number" name="fico_range_high" onChange={handleChange} placeholder="Enter FICO range high" />
//         </div>

//         <div className="form-group">
//           <input className="btn btn-primary predict-button" type="submit" value="PREDICT" />
//         </div>
//       </form>
//     </div>
//   );
// }

// export default CreditForm;









