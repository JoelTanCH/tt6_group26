import React, {useContext} from "react";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Navigate
} from 'react-router-dom';
import AuthContext from "../context/AuthContext";
import Login from "../components/login";
import DashBoard from "../components/DashBoard";

const ProtectedRoute = ({auth, redirectPath = "/", children}) => {
    if (!auth) {
        return <Navigate to={redirectPath} replace/>
    }

    return children;
}


export default function Main() {

    let {auth} = useContext(AuthContext);

    return(
        <div className="mainpage-container">
            <Router>
                <Routes>

                    <Route 
                        path="/home"
                        element={
                            <ProtectedRoute auth={auth}>
                                <DashBoard />
                            </ProtectedRoute>
                        }
                    />
                    
                    <Route path="/" element={<Login />}></Route>
                </Routes>
            </Router>
        </div>
    )
}