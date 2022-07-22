import React, { useState, useContext } from "react";
import { login } from "../Api/api";
import { useNavigate } from "react-router-dom";
import AuthContext from "../context/AuthContext";

export default function Login() {
  let {auth, setAuth} = useContext(AuthContext);
  const [showPopUp, setShowPopUp] = useState(false);
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [permission,setPermission] =useState(false)

  // const checkUserName = (inputEmail) => {
  //   if (!/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(inputEmail)) {
  //     setShowPopUp(true);
  //   }
  // };
  const checkLogin = (userName, userPassword) => {
    if(userName==='testuser' && userPassword==='testpassword'){
        setPermission(true)
        navigate("/home");
    }
  };

  async function handleLogin(user, pass) {
    let res = await login(user, pass);
    // if login success
    if (res.status === 200) {
      // storing data to session storage
      sessionStorage.setItem('jwt', res.accessToken.token);
      // set global data such as authenticated to true
      console.log(res.accessToken.token);
      setAuth(true);
      navigate("/home");
      
    }  else {
      alert("Incorrect username/password");
    }
  }
  const navigate = useNavigate();

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
        <p className="validate_text">Please input email.</p>
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
            checkLogin(userName,password);
            handleLogin(userName, password);
            console.log(userName, password)
          }
          
        }
        >Login!</button>
        <br/>
              <a href="#forgetPassword">Forget password?</a>
    </div>
  );
}
