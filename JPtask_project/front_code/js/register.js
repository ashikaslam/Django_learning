
const handleRegistration = (event) => {
    event.preventDefault();
    // Extract form data
    const name = document.getElementById('id_name').value;
    const email = document.getElementById('id_email').value;
    const mobile_number = document.getElementById('id_mobile_number').value;
    const password = document.getElementById('id_password').value;

    const info = {
        name,
        email,
        mobile_number,
        password
    };
    console.log(JSON.stringify(info));

    fetch('http://127.0.0.1:8000/auth/register/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(info),
    })
    .then((res) => res.json())
    .then((data) => {
        console.log('inside data');
        if (data.status === 1) {
            console.log('Registration successful');
           // window.location.href = `otp.html?url=${data.activation_url}`;
        }
    })
    .catch((err) => {
        console.log('inside err');
        console.log(err);
    });
};

