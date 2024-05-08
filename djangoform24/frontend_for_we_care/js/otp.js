


const opt_confirm = (event) => {
   event.preventDefault();
   const  num1= document.getElementById("first").value;
   const  num2= document.getElementById("second").value;
   const  num3= document.getElementById("third").value;
   const  num4= document.getElementById("fourth").value;
   const  num5= document.getElementById("fifth").value;
   const  num6= document.getElementById("sixth").value;

   otp=num1+num2+num3+num4+num5+num6

   const info = {
    otp
  }


  const param = new URLSearchParams(window.location.search).get("url");
  const email = new URLSearchParams(window.location.search).get("email");
  
const final_url = param+"&email="+email;
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
    
    if(data.status==1){

    const login_url = data.login_url
    console.log(login_url);
    window.location.href=`login.html?login_url=${login_url}`;
      
    }
   
  
    
   
   



   })


  .catch((err)=>{
    console.log('inside err ');

    console.log(err)
  });




};