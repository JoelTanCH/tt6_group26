import axios from 'axios';

const API=axios.create({
    baseURL:"http://127.0.0.1:5000",
    headers: {
        "Content-Type": "application/json",
    },
});

export async function login(user, pass) {
    let authData = {username: user,
                    password: pass};

    try{
        const res = await API.post('/login', {}, {
            auth: authData
        })
        return {
            status: res.status,
            accessToken: res.data
        }
    } catch(err) {
        return {status: err.response.status};
    }
}

export async function getCurrencies() {
    try{
        const res = await API.get('/get_currencies_available', {}, {})
        return {
            status: res.status,
            currencySymbols: res.data.currency_symbols
        }
    } catch(err) {
        return {status: err.response.status};
    }
}