
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

    fetch('https://neighborhood-marketplace.onrender.com/auth/register/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(info),
    })
    .then((res) => res.json())
    .then((data) => {
        console.log('inside data');
        if (data.status === 1) {
                alert('Registration successful');
           window.location.href = `login.html`;
        }
        else{
            alert('Registration successful');
           window.location.href = `../index.html`;
        }
    })
    .catch((err) => {
        alert('Registration successful');
           window.location.href = `../index.html`;
        console.log('inside err');
        console.log(err);
    });
};

