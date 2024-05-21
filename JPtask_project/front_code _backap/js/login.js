

const handleLogin = (event) => {
  event.preventDefault();
  // Extract form data
  const user_name = document.getElementById("login_email").value;
  const password = document.getElementById("login_password").value;

  const info = {
    user_name,
    password,
};

  console.log(JSON.stringify(info));

  fetch("http://127.0.0.1:8000/auth/login/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(info),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log("inside data");
      console.log(data);
      if (data.status === 1) {
        console.log("Login successful");
        // Redirect to dashboard or any other page
        localStorage.setItem("user_id", data.user_id);
        localStorage.setItem("refresh", data.refresh);
        localStorage.setItem("access", data.access);
        localStorage.setItem("email", data.email);
        localStorage.setItem("user_name", data.user_name);
        localStorage.setItem("mobile_number", data.mobile_number);
        window.location.href = `../index.html`;
      } else {
        console.log("Login failed");
        alert("Login failed");
        // Display error message or handle as needed
      }
    })
    .catch((err) => {
      console.log("inside err");
      console.log(err);
    });
};
