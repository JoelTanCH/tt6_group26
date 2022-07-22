import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from './components/login'
import DashBoard from "./components/DashBoard";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route exact path="/" element={<Login/>}></Route>
          <Route path='/home' element={<DashBoard/>}></Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
