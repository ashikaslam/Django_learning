




const handleRegistration = (evevt) => {
    evevt.preventDefault();
   


  username = get_value("username");
  first_name= get_value("first_name");
  last_name = get_value("last_name");
  password = get_value("password");
  confirm_password = get_value("confirm_password");
  email = get_value("email");

const info = {
    username,
    first_name,
    last_name,
    email,
    password,
    confirm_password,
  }




if(confirm_password===password){
    document.getElementById("error-for-pass").innerText="";

    if (/^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/.test(password))
      {

        fetch("https://testing-8az5.onrender.com/patient/register/", {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify(info),
        })
          .then((res) => res.json())
          .then((data) => console.log(data))
          .catch((err)=>console.log(err));
      } 
      
      
      
      else {
        document.getElementById("error-for-pass").innerText =
          "pass must contain eight characters, at least one letter, one number and one special character:";
      }
console.log(JSON.stringify(info));

}

else{document.getElementById("error-for-pass").innerText="both pass fields not matched";}


};










get_value = (id)=>{

const data = document.getElementById(id).value;
return data;

};





const handleLogin = (event) => {
    event.preventDefault();
    const username = get_value("login-username");
    const password = get_value("login-password");
    console.log(username, password);
    if ((username, password)) {
      fetch("https://testing-8az5.onrender.com/patient/login/", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ username, password }),
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
  
          if (data.token && data.user_id) {
            localStorage.setItem("token", data.token);
            localStorage.setItem("user_id", data.user_id);
            window.location.href = "index.html";
          }
        });
    }
  };