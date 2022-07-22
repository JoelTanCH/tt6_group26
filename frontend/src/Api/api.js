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