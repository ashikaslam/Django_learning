
const handlenav = () => {
   
    const user_name= localStorage.getItem("user_name")
    if (user_name){

        document.getElementById("user_name_nav").innerText=user_name;
    }
}
handlenav  ();



async function checkLoginStatus(apiUrl, refreshUrl, accessToken, refreshToken) {
    async function makeRequest(token) {
        const response = await fetch(apiUrl, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        return response;
    }

    // Try to use the access token first
    let response = await makeRequest(accessToken);

    if (response.status === 401) {  // Unauthorized, token might be invalid or expired
        console.log("Access token invalid, trying to refresh token.");

        // Try to refresh the tokens
        const refreshResponse = await fetch(refreshUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ refresh: refreshToken })
        });

        if (refreshResponse.ok) {
            const data = await refreshResponse.json();
            const newAccessToken = data.access;
            const newRefreshToken = data.refresh;

            // Store the new tokens somewhere secure
            localStorage.setItem('access', newAccessToken);
            localStorage.setItem('refresh', newRefreshToken);

            // Retry the original request with the new access token
            response = await makeRequest(newAccessToken);

            if (response.ok) {
                return true;  // User is logged in
            }
        } else {
            console.log("Refresh token invalid or expired.");
        }
    } else if (response.ok) {
        return true;  // User is logged in
    }

    // If all attempts fail, prompt user to log in again
    return false;
}

// Example usage
const apiUrl = 'http://127.0.0.1:8000/auth/check_use_login/';
const refreshUrl = 'http://127.0.0.1:8000/token/refresh/';
const accessToken = localStorage.getItem('access');
const refreshToken = localStorage.getItem('refresh');

// checkLoginStatus(apiUrl, refreshUrl, accessToken, refreshToken).then(isLoggedIn => {
//     if (isLoggedIn) {
//         alert();
//         window.location.href = 'html_templates/user_profile.html';
//     } else {
//         window.location.href = 'html_templates/login.html';
//     }
// });

// Function to handle login check and redirection
function handleLoginCheck() {
    checkLoginStatus(apiUrl, refreshUrl, localStorage.getItem('access'), localStorage.getItem('refresh')).then(isLoggedIn => {
        if (isLoggedIn) {
            window.location.href = 'html_templates/user_profile.html';
        } else {
            window.location.href = 'html_templates/login.html';
        }
    });
}



function handleLoginCheck1() {
    checkLoginStatus(apiUrl, refreshUrl, localStorage.getItem('access'), localStorage.getItem('refresh')).then(isLoggedIn => {
        if (isLoggedIn) {
            window.location.href = 'html_templates/product_sel_post.html';
        } else {
            window.location.href = 'html_templates/login.html';
        }
    });
}



function handleLoginCheck2() {
    checkLoginStatus(apiUrl, refreshUrl, localStorage.getItem('access'), localStorage.getItem('refresh')).then(isLoggedIn => {
        if (isLoggedIn) {
            window.location.href = './user_profile.html';
        } else {
            window.location.href = './login.html';
        }
    });
}