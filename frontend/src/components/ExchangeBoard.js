import {useState, useEffect} from 'react';
import { getCurrencies } from "../Api/api";
import { getConvertedAmount } from "../Api/api";
import {DebounceInput} from 'react-debounce-input';

export default function ExchangeBoard() {

    let [currencyList, setCurrencyList] = useState(['']);
    let [baseInput, setBaseInput] = useState(null);
    let [exchangeOnput, setExchangeOnput] = useState(0);
    let [baseBal, setBaseBal] = useState(0);
    let [exchangeBal, setExchangeBal] = useState(0);
    let [chosenExchange, setchosenExchange] = useState("")
    let [outputExchange, setOutputExchange] = useState("")
    let [timer, setTimer] = useState(null)

    //use effect used to load currencies initially when page renders
    useEffect(() => {

        console.log("Loading Currencies!");

        //declare data fetching async function
        const fetchData = async () => {
            const data = await getCurrencies();
            // if login success
            if (data.status === 200) {
                // update currency List 
                setCurrencyList(data.currencySymbols)
                console.log('currency list has been updated')
            }else {
                alert("something went wrong");
            }
        }
        //call the function 
        fetchData()
    }, [])


    async function handleOnExchange(){
        console.log("This will call an api call function");
    };

    async function handleOnBaseChange(event) {
        

        console.log("converting chosen currency amount!")
        // update state of baseinput
        setBaseInput(event.target.value);
        console.log(baseInput, chosenExchange, outputExchange)
        // get exchangeRate from API
        const data = await getConvertedAmount(chosenExchange, outputExchange, parseFloat(event.target.value));
        console.log(data)

        if (data.status === 200) {
            // update currency List 
            setExchangeOnput(data.convertedAmount.result.convertedAmount)
            console.log('Exchange output has been updated')
        }else {
            alert("something went wrong with currency exchange, ensure exchange rate to, from and amount are populated");
        }
    };

    function updateChosenExchange(event){
        console.log('updating chosen exchange!')
        setchosenExchange(event.target.value);
        console.log(event.target.value)
    }

    function updateOutputExchange(event){
        console.log('updating output exchange!')
        setOutputExchange(event.target.value);
        console.log(event.target.value)
    }

    return (
        <div className = "exchangeboard-box">
            <p className="exchangeboard-header">Wallet name</p>
            <div className = "exchangeboard-box">
                <p className = "exchange-text">Exchange</p>

                {/* This is for the base */}
                <div className="cur-data-box">
                    <div className="currency-select-left-box">
                        <select onChange = {updateChosenExchange} className="currency-select">
                            <option value="select">Select</option>
                            {currencyList.map(currency => <option value={currency.toLowerCase()}>{currency}</option>)}
                        </select>
                    </div>

                    <div className="currency-select-right-box">
                        <DebounceInput className="currency-input" type="number" debounceTimeout ={1000} onChange={(handleOnBaseChange)} value={baseInput}/>
                        <p className="currency-balance">{`Current Balance: ${baseBal}`}</p>
                    </div>
                </div>

                <p className='toLabel'>To</p>

                {/* This is for the exchanged */}
                <div className="cur-data-box">
                    <div className="currency-select-left-box">
                        <select onChange = {updateOutputExchange} className="currency-select">
                            <option value="select">Select</option>
                            {currencyList.map(currency => <option value={currency.toLowerCase()}>{currency}</option>)}
                        </select>
                    </div>

                    <div className="currency-select-right-box">
                        <input className="currency-input" type="number" value={exchangeOnput} disabled/>
                        <p className="currency-balance">{`Current Balance: ${baseBal}`}</p>
                    </div>
                </div>                

                <div className="exchange-btn" onClick={handleOnExchange}>Exchange</div>
            </div>
        </div>
    )
}