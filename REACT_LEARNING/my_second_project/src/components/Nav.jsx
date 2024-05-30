import React from "react";
import logo from "../assets/images/logo-bg.png";
const Nav = () => {
  return (
    <div>

<nav className="nav">
      <ul>
        <li>
          <a href="index.html" className="brand">
           <img src={logo} alt="Learn with Sumit Logo" />
            <h3>Learn with Sumit</h3>
          </a>
        </li>
      </ul>
      <div className="account">
        <span className="material-icons-outlined" title="Account">
          account_circle
        </span>
        <a href="signup.html">Signup</a>
       
      </div>
    </nav>

    </div>
  );
};

export default Nav;
