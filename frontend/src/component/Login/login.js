import React, { useState } from "react";

import "./Login.styles.css";

export default function Login() {
  const [showPopUp, setShowPopUp] = useState(false);
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [permission,setPermission] =useState(false)

  const checkUserName = (inputEmail) => {
    if (!/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(inputEmail)) {
      setShowPopUp(true);
    }
  };
  const checkLogin = (userName, userPassword) => {
    if(userName==='testuser' && userPassword==='testpassword'){
        setPermission(true)
    }
  };

  //if permission is true, then router to dashboard
  return (
    <div className="login_box">
      <img
        src="https://www.nicepng.com/png/full/267-2670427_1-dbs-group-holdings-ltd-dbs-bank-logo.png"
        alt="logo"
      ></img>
      <p>User</p>
      <input
        type="text"
        onInput={(e) => {
          setUserName(e.target.value);
        }}
        placeholder={"Username"}
      ></input>
      {showPopUp && (
        <p className="validate_text">Please key in proper email address</p>
      )}

<p>Password</p>
      <input
        type="text"
        onInput={(e) => {
          setPassword(e.target.value);
        }}
        placeholder={"Password"}
      ></input>

<br/>
      <button
        className="login_button" onClick={
          () => {
            checkUserName(userName);
            checkLogin(userName,password)
          }
          
        }
        >Login!</button>
        <br/>
              <a href="#forgetPassword">Forget password?</a>
    </div>
  );
}
