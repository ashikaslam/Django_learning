

const handlereset_pass_1 = (event) => {
    event.preventDefault();
    // Extract form data
   
    const phone = document.getElementById('login_email').value;
    

    const info = {
        phone
    };

    console.log(JSON.stringify(info));

    fetch('http://127.0.0.1:8000/auth/reset_pass_pre/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(info),
    })
    .then((res) => res.json())
    .then((data) => {
        console.log('inside data');
        console.log(data);
        if (data.status === 1) {
            window.location.href=`../html_templates/otp.html?phone=${phone}`;
           // alert(data.message);



        } else {
            console.log('Login failed');
            alert('invalied data passed');
            // Display error message or handle as needed
        }
    })
    .catch((err) => {
        console.log('inside err');
        console.log(err);
    });
};







const handlereset_pass_2 = (event) => {
    event.preventDefault();
    // Extract form data
   
    const otp = document.getElementById('otp').value;
    const phone = new URLSearchParams(window.location.search).get("phone");

    const info = {
        otp,
        phone,
    };

    console.log(JSON.stringify(info));

    fetch('http://127.0.0.1:8000/auth/Confirm_otp_pass_change/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(info),
    })
    .then((res) => res.json())

    .then((data) => {
        console.log('inside data');
        console.log(data);


        if (data.status === 1) {
            window.location.href=`../html_templates/set_password.html?phone=${phone}`;
           


        } else {
            console.log('Login failed');
            alert('your otp is invaide or ist is expired');
            // Display error message or handle as needed
        }


    })
    .catch((err) => {
        console.log('inside err');
        console.log(err);
    });
};









const handlereset_pass_3 = (event) => {
    event.preventDefault();
    // Extract form data
   
    const new_pass = document.getElementById('new_password').value;
    const phone = new URLSearchParams(window.location.search).get("phone");

    const info = {
        new_pass,
        phone,
    };

    console.log(JSON.stringify(info));

    fetch('http://127.0.0.1:8000/auth/Final_password_set/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(info),
    })
    .then((res) => res.json())

    .then((data) => {
        console.log('inside data');
        console.log(data);


        if (data.status === 1) {
            alert('successfully changed your passord');
            window.location.href=`../html_templates/login.html`;

        } else {

            console.log('Login failed');
            alert('password reset failed try again');
            // Display error message or handle as needed
        }


    })
    .catch((err) => {
        console.log('inside err');
        console.log(err);
    });
};
