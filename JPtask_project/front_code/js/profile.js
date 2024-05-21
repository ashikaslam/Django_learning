
const handle_profile_see_final = () => {
    const access = localStorage.getItem("access");
    fetch('http://127.0.0.1:8000/auth/profele_data/', {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${access}`,
        },
    })
        .then((res) => res.json())
        .then((data) => {
            console.log('inside data');
            console.log(data);
            if (data.status === 1) {
                
                document.getElementById("user_name").innerText=data.user_name;
                document.getElementById("user_email").innerText=data.email;
                document.getElementById("user_phone").innerText=data.phone_number;
                document.getElementById('profile-picture').src = data.profile_picture;
                
            }
        })


};

handle_profile_see_final();