/* eslint-disable */

import axios from 'axios';

// this base url will be change based on
// if you need to point to production.

const BASE_URL = 'http://localhost:8000';
const ACCESS_TOKEN = 'access_token';
const REFRESH_TOKEN = 'refresh_token';

const tokenRequest = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    accept: 'application/json',
  },
});

const registerUser = (username, password, password2, firstName, lastName, email) => {
  const registerBody = {
    username, password, password2, email, first_name: firstName, last_name: lastName
  } 

  // console.log('Register User Body: ', registerBody)

  return tokenRequest.post('/api/register', registerBody)
  .then((response) => {
    console.log('registerUser: ', response.user)
    return Promise.resolve(response.user)
  })
  .catch((err) => {
    console.log(err);
    return Promise.reject(err);
  });
};

const loginUser = (username, password) => {
  const loginBody = { username, password };
  return tokenRequest.post('/api/token/both/', loginBody)
    .then((response) => {
      window.localStorage.setItem(ACCESS_TOKEN, response.data.access);
      window.localStorage.setItem(REFRESH_TOKEN, response.data.refresh);
      return Promise.resolve(response.data);
    }).catch((error) => {
      console.log(error);
      return Promise.reject(error);
    });
};

const refreshToken = () => {
  const refreshBody = { refresh: window.localStorage.getItem(REFRESH_TOKEN) };
  return tokenRequest.post('/api/token/access/', refreshBody)
    .then((response) => {
      window.localStorage.setItem(ACCESS_TOKEN, response.data.access);
      return Promise.resolve(response.data);
    }).catch((error) => Promise.reject(error));
};

const isCorrectRefreshError = (status) => status === 401;


const authRequest = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    Authorization: `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`,
    'Content-Type': 'application/json',
  },
});

const logoutUser = () => {
  window.localStorage.removeItem(ACCESS_TOKEN);
  window.localStorage.removeItem(REFRESH_TOKEN);
  authRequest.defaults.headers.Authorization = '';
};

const errorInterceptor = (error) => {
  const originalRequest = error.config;
  const { status } = error.response;
  if (isCorrectRefreshError(status)) {
    return refreshToken().then(() => {
      const headerAuthorization = `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`;
      authRequest.defaults.headers.Authorization = headerAuthorization;
      originalRequest.headers.Authorization = headerAuthorization;
      return authRequest(originalRequest);
    }).catch((tokenRefreshError) => {
      // if token refresh fails, logout the user to avoid potential security risks.
      logoutUser();
      return Promise.reject(tokenRefreshError);
    });
  }
  return Promise.reject(error);
};

authRequest.interceptors.response.use(
  (response) => response, // this is for all successful requests.
  (error) => errorInterceptor(error), // handle the request
);

export {
  tokenRequest, loginUser, logoutUser, refreshToken, authRequest,registerUser,    
  errorInterceptor, BASE_URL, ACCESS_TOKEN, REFRESH_TOKEN,
};
