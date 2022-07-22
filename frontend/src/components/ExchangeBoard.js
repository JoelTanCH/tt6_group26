
export default function ExchangeBoard() {

    function CurDatabox() {
        return(
            <div className="cur-data-box">
                <div className="currency-select-left-box">
                    <select className="currency-select"></select>
                </div>

                <div className="currency-select-right-box">
                    <input className="currency-input" type="number" placeholder="0" />
                    <p className="currency-balance">Current Balance:</p>
                </div>
            </div>
        )
    }

    return (
        <div className = "exchangeboard-box">
            <p className="exchangeboard-header">Wallet name</p>
            <div className = "exchangeboard-box">
                <p className = "exchange-text">Exchange</p>
                <CurDatabox />
                <CurDatabox />
            </div>
        </div>
    )
}