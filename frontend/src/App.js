import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from './components/login'
import DashBoard from "./components/DashBoard";
import {AuthProvider} from "./context/AuthContext";
import Main from './screens/Main';

function App() {
  return (
    <AuthProvider>
      <div className="App">
        <Main />
      </div>
    </AuthProvider>
  );
}

export default App;
