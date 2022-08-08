import {useState} from 'react';



export default function ExchangeBoard() {

    let [currencyList, setCurrencyList] = useState(['SGD']);
    let [baseInput, setBaseInput] = useState(0);
    let [exchangeInput, setExchangeInput] = useState(0);
    let [baseBal, setBaseBal] = useState(0);
    let [exchangeBal, setExchangeBal] = useState(0);

    async function handleOnExchange(){
        console.log("This will call an api call function");
    };

    async function handleOnBaseChange(event) {
        // update state of baseinput
        setBaseInput(event.target.value);

        // get exchangeRate from API

        // generate exchangeInput and setstate based on the rate (api will return ammount)

    };
    

    return (
        <div className = "exchangeboard-box">
            <p className="exchangeboard-header">Wallet name</p>
            <div className = "exchangeboard-box">
                <p className = "exchange-text">Exchange</p>

                {/* This is for the base */}
                <div className="cur-data-box">
                    <div className="currency-select-left-box">
                        <select className="currency-select">
                            <option value="select">Select</option>
                            {currencyList.map(currency => <option value={currency.toLowerCase()}>{currency}</option>)}
                        </select>
                    </div>

                    <div className="currency-select-right-box">
                        <input className="currency-input" type="number" onChange={(handleOnBaseChange)} value={baseInput}/>
                        <p className="currency-balance">{`Current Balance: ${baseBal}`}</p>
                    </div>
                </div>

                <p className='toLabel'>To</p>

                {/* This is for the exchanged */}
                <div className="cur-data-box">
                    <div className="currency-select-left-box">
                        <select className="currency-select">
                            <option value="select">Select</option>
                            {currencyList.map(currency => <option value={currency.toLowerCase()}>{currency}</option>)}
                        </select>
                    </div>

                    <div className="currency-select-right-box">
                        <input className="currency-input" type="number" value={exchangeInput} disabled/>
                        <p className="currency-balance">{`Current Balance: ${baseBal}`}</p>
                    </div>
                </div>                

                <div className="exchange-btn" onClick={handleOnExchange}>Exchange</div>
            </div>
        </div>
    )
}