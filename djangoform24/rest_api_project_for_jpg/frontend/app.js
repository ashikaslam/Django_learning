// const handleRegistration = (event) => {
//   event.preventDefault();
  
//   var logindata = {
//     "user_name": "017",
//     "password": "123"
//   };

//   fetch("http://127.0.0.1:8000/user_account/login/", {
//     method: "POST",
//     headers: { "content-type": "application/json" },
//     body: JSON.stringify(logindata),
//   })
//   .then((res) => {
//     console.log('inside res of login');
//     return res.json(); // Explicitly return res.json()
//   })
//   .then(data => {
//     console.log('inside data of login');
//     console.log(data);

//   })
//   .catch((err) => {
//     console.log('inside err login');
//     console.log(err);
//   });
// };














const handleRegistration = (event) => {
  event.preventDefault();
    // Extract form data
    
     const first_name = document.getElementById("first_name").value;
     const last_name = document.getElementById("last_name").value;
     const birth_day = document.getElementById("birthday").value;
     const mobile_number = document.getElementById("phone").value;
     const email = document.getElementById("email").value;
     const password = document.getElementById("password").value;
     const confirm_password = document.getElementById("confirm_password").value;
     const gender1 = document.getElementById("gender1").checked; // Boolean value for gender1
     const gender2 = document.getElementById("gender2").checked; // Boolean value for gender2
     const blood_grpup = document.querySelector('[name="subject"]').value;
     var gender="male";
     if (gender2==true){
        gender="female"
     }


     const info = {
        mobile_number,
        first_name,
        last_name,
        email,
        password,
        confirm_password,
        blood_grpup,
        gender,
      }
   console.log(JSON.stringify(info));

    fetch("http://127.0.0.1:8000/user_account/register/", {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify(info),
        })
          .then((res) =>{

            return res.json(); // Explicitly return res.json()
          

          } )
          
          .then(data => {
            
            console.log('inside data ');
           // console.log(data);
           // console.log(data.status)
            if (data.status==1){
              console.log("helllo inside")
              window.location.href=`otp.html?url=${data.activaton_url}`;
            }
           
           
 
 
 
           })


          .catch((err)=>{
            console.log('inside err ');

            console.log(err)
          });
          


 };





 const handlelogOut = (event) => {
  const token = localStorage.getItem("access_token");
  event.preventDefault();
  if (token){
    localStorage.removeItem("access_token");

  }
  window.location.href=`index.html`;   
     
     
   
};






const home_content = () => {
  const parent = document.getElementById("all_content");
    fetch("http://127.0.0.1:8000/post_object/home/", {
          method: "GET",
          headers: { "content-type": "application/json" },
         
        })

          .then((res) =>{

            return res.json(); // Explicitly return res.json()
          } )
          
          .then(data => {
            
          console.log(data);
          const all_post = data.all_post;
          data.all_post.forEach(element => {

         // here element is single post
          const amount= element.amount;
          const  apply_availavle = element.apply_availavle;
          const at_leas_5_people_managed =element.at_leas_5_people_managed;
          const blood_grpup=element.blood_grpup;
          const blood_need_time=element.blood_need_time;
          const country=element.country;
          const description=element.description;
          const  district= element.district;
          const  donate_done=element. donate_done;
          const  hospital_name= element.hospital_name;
          const  id = element.id;
          const image1 = element.image1;
          const impage2= element.impage2;
          const post_time= element.post_time;
          const post_update_time= element.post_update_time;
          const  title= element.title;
          const  unionOrtown= element. unionOrtown;
          const  upazila= element. upazila;
          const   user_id= element.  user_id;
          const   villageOrrad= element.  villageOrrad;
          const  zip_code= element. zip_code;

         
          const div = document.createElement("div");
          div.innerHTML=`
          
          
          <div class="ratio ratio-16x9">
          <img src="${"http://127.0.0.1:8000/media/"+image1}" class="card-img-top" loading="lazy" alt="...">
      </div>
      <div class="card-body p-3 p-xl-5">
          <h3 class="card-title h5" id="title">${title}</h3>
          <p class="card-text" id="time">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <p class="card-text" id="address">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <a href="#" class="btn btn-primary">details</a>
      </div>

          
          `;
          parent.appendChild(div);

          
          
          
          });

          })
          .catch((err)=>{ });
 };

 home_content();



