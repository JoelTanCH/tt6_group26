import "./App.css";
import Login from "./component/Login/login";
//import Dashboard from "./component/dashboard/dashboard";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
// import Home from "./component/home/home";
// import Contact from "./component/contact/contact";
// import About from "./component/about/about";

function App() {
  return (
    <Login/>
    // <Router>
    //   <div>
    //     <h2>Welcome to React Router Tutorial</h2>

    //     <nav className="navbar navbar-expand-lg navbar-light bg-light">
    //       <ul className="navbar-nav mr-auto">
    //         <li>
    //           <Link to={"/"} className="nav-link">
    //             {" "}
    //             Home{" "}
    //           </Link>
    //         </li>

    //         <li>
    //           <Link to={"/contact"} className="nav-link">
    //             Contact
    //           </Link>
    //         </li>

    //         <li>
    //           <Link to={"/about"} className="nav-link">
    //             About
    //           </Link>
    //         </li>
    //       </ul>
    //     </nav>

    //     <hr />

    //     <Routes>
    //       <Route path="/" element={<Home />} />
    //       <Route path="/about" element={<About />} />
    //     </Routes>
    //   </div>
    // </Router>
  )
}

export default App;
