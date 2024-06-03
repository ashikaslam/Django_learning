// import axios from "axios";
// import { Navigate } from "react-router-dom";
// import { useState } from "react";
// import GoogleLogin from "react-google-login";
// import { gapi } from "gapi-script";
// import { useEffect } from "react";



 const Login = () => {
//   const clientId ="728972731870-s03ukp2jmfq21ipgseueu5jci4eltaus.apps.googleusercontent.com";

//   const onSuccess = async (res) => {
//     console.log("success:", res.accessToken);
//     const user = {
//       grant_type: "convert_token",
//       client_id: "arXawXbQQqP1KWOpEL6C2NNjPtJ4spQOA8JHeejy",
//       client_secret:
//         "p0P6OVxslDN8GSwZdOvfCxQLzjYjjWQfgi5VVmASu7hu7Ku3a3Nq0KNTzDkpbYhrFYJpLdifs97sb8zTvbrXLVK0GRCY8JvN0SmvJSOuGrpXSAjo3HCx2AfME2tCYG9K",
//       backend: "google-oauth2",
//       token: res.accessToken,
//     };

//     const { data } = await axios.post(
//       "http://localhost:8000/api-auth/convert-token/",
//       user,
//       {
//         headers: {
//           "Content-Type": "application/json",
//         },
//         withCredentials: true,
//       }
//     );

//     axios.defaults.headers.common[
//       "Authorization"
//     ] = `Bearer ${data["access_token"]}`;
//     localStorage.clear();
//     localStorage.setItem("access_token", data.access_token);
//     localStorage.setItem("refresh_token", data.refresh_token);
//     window.location.href = "/";
//   };

//   const onFailure = (err) => {
//     console.log("failed:", err);
//   };

  return (
    <div>
      <h1>hello</h1>
      
    </div>
  );
};

export default Login;
