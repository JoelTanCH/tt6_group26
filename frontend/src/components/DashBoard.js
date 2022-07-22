import React from 'react';
import Wallets from './Wallets.js';
import ExchangeRate from './ExchangeRate.js';
import ExchangeBoard from "./ExchangeBoard";

export default function DashBoard() {

    return (
    <div className = "dashboard-box">
        <div class="wallets"><Wallets /></div>
        <ExchangeBoard />
        <div class="exchange"><ExchangeRate /></div>
    </div>
    )
}