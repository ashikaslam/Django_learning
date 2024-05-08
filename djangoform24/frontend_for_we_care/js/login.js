


const login_function = (event) => {
    event.preventDefault();
    const  password = document.getElementById("login__password").value;
    const  user_name= document.getElementById("login__username").value;
    const info = {
        user_name,
        password 
   }
const final_url= "https://food-site-03s7.onrender.com/user_account/login/";
   console.log(final_url);

   fetch(final_url, {
     method: "POST",
     headers: { "content-type": "application/json" },
     body: JSON.stringify(info),
   })
   .then((res) =>{
     return res.json(); // Explicitly return res.json()
   } )
   .then(data => {
     
      console.log(data);
      if(data.status==1){

        
         if (data.access_token) {
           localStorage.setItem("access_token", data.access_token);
           window.location.href=`profile.html`;
           //document.write(data.access_token);
        //   localStorage.setItem("user_id", data.user_id);
          
        }


          
        }
    
   
     
    
    
 
 
 
    })
 
 
   .catch((err)=>{
     console.log('inside err ');
 
     console.log(err)
   });
 
 
 
 
 };