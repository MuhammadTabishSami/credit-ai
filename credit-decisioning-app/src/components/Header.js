
import React from 'react';
import './Header.css';
import logo from '../assets/credit_aii.png';

const Header = () => {
  return (
    <header className="header">
      <img src={logo} alt="AI Credit Logo" className="header-logo" />
      <hr className="header-divider" />
    </header>
  );
}

export default Header;


