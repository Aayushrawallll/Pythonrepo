// removal of auth.token
import Router from 'next/router';

export const logout = () => {
  localStorage.removeItem('token'); // Remove the token from local storage
  Router.push('/login'); // Redirect to the login page
};
