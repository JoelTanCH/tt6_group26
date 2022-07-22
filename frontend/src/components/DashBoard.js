import React, {useState} from 'react';

export default function DashBoard() {
    let wallets = [
        {
          "id": 1,
          "user_id": 1,
          "name": "Multi-Currency Account"
        },
        {
          "id": 2,
          "user_id": 1,
          "name": "Travel Account"
        },
        {
          "id": 3,
          "user_id": 2,
          "name": "Trading Account"
        },
        {
          "id": 4,
          "user_id": 3,
          "name": "Multi-Currency Account"
        },
        {
          "id": 5,
          "user_id": 4,
          "name": "Trip to Japan"
        }
    ]

    let [wallet, setWallet] = useState("Select a Wallet")
    const handleWalletChange = (wallet) => {
        setWallet(wallet.target.value)
    }

    return (
    <div>
        {wallet}<br />
        <select onChange={handleWalletChange}> 
        <option value="Select a Wallet">Wallets</option>
        {wallets.map((wallet) => <option value={wallet.name}>{wallet.name}</option>)}
        </select>
    </div>
    )
}