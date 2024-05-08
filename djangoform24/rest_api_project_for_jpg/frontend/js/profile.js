



const profile_data = () => {
    const token = localStorage.getItem("access_token");

    if (token){


       // fetch("https://food-site-03s7.onrender.com/user_account/my_profile/", {
        fetch("https://food-site-03s7.onrender.com/user_account/my_profile/", {
            method: "GET",
            headers: {
              Authorization: `Bearer ${token}`,
              "Content-Type": "application/json",
            },
          })
            .then((res) => res.json())
            .then((data) => {
              console.log(data);
             
             console.log(data);
             document.getElementById("inputFirstName").value=`${data.first_name}`
             document.getElementById("inputLastName").value=`${data.last_name}`
             document.getElementById("inputEmailAddress").value=`${data.email}`
             document.getElementById("inputPhone").value=`${data.mobile_number}`
             console.log(data.first_name);


            });




    }


   




  };



  profile_data();