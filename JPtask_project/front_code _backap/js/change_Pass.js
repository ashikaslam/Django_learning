






const change_passowrd = (event) => {
    event.preventDefault();

    const new_passowrd = document.getElementById("new_password").value;
    const current_passowrd = document.getElementById("current_password").value;
    const confirm_passowrd = document.getElementById("confirm_password").value;
  
    const info = {
        new_passowrd,current_passowrd,confirm_passowrd
  };
  




    const access = localStorage.getItem("access");
    fetch('http://127.0.0.1:8000/auth/chage_pass/', {
        method: 'POST',
        headers: {
            Authorization: `Bearer ${access}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify(info),
    })
        .then((res) => res.json())
        .then((data) => {
            console.log('inside data');
            console.log(data);
            if (data.status === 1) {
                alert('successfully changed passowrd');
                window.location.href = 'user_profile.html'; 
            }
            else{
                alert('operation faild');
            }
        })
        .catch((err) => {
            console.log('inside err');
            console.log(err);
            alert('operation faild');
        });


};