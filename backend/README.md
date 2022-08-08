# APIs

Documentation of backend API routes

## Description

An in-depth description of the arguments required for the api routes and what they will return

### API routes
* @get "/users"
takes in nothing\
returns
```
{
  "1": {
    "user": "Jacky",
    "username": "user101"
  },
  "2": {
    "user": "Jane",
    "username": "user102"
  },
  "3": {
    "user": "Tom",
    "username": "user103"
  },
  "4": {
    "user": "Helen",
    "username": "user104"
  },
  "5": {
    "user": "Mark",
    "username": "user105"
  }
}
```
* @post "/login"
takes in a form with "username" and "password"\
returns a jwt token which will be used to verify the user for every subsequent request
```
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidXNlcjEwMSIsImV4cCI6MTY1ODQ4NTE3OH0.9dlXWJSDiA_hi0xnHHCNkWTpop9YNHLYdpLlpEcsrQM"
}
```
* for all subsequent requests, only the jwt token is required to verify a user

* @get "/get_currencies_available"
returns
```

```

