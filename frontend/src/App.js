import logo from './logo.svg';
import './App.css';
import React from 'react';
import Login from './components/login'
import DashBoard from "./components/DashBoard";

function App() {
  return (
    <div className="App">
      <header className="App-header">
      </header>
      <Login/>
      <DashBoard />
    </div>
  );
}

export default App;
