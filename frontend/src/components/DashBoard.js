import React from 'react';
import Wallets from './Wallets.js';
import ExchangeRate from './ExchangeRate.js';
import ExchangeBoard from "./ExchangeBoard";

export default function DashBoard() {

    return (
    <div className = "dashboard-box">
        <div className='dashboard-left'>
            <div className="wallets"><Wallets /></div>
        </div>
        <div className='dashboard-right'>
            <ExchangeBoard />
            <div className="exchange"><ExchangeRate /></div>
        </div>
    </div>
    )
}