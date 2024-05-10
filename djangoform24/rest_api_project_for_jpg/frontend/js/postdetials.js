

const single_post= () => {

    const id = new URLSearchParams(window.location.search).get("id");
    fetch(`https://food-site-03s7.onrender.com/post_object/home/?id=${id}`, {
      method: "GET",
      headers: { "content-type": "application/json" },
     
    })

        .then((res) =>{
          return res.json(); // Explicitly return res.json()
        } )
        
        .then(data => {
          
        const element=data.post[0];
        console.log(element);
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
      
       


  
        const parent = document.getElementById("post_container");
         const div = document.createElement("div");
        div.innerHTML=`   
        
        
        <h2>title</h2>
            <p>${title}</p>
          
            
            
           
            <p><strong>Blood Group:${blood_grpup}</strong> </p>
            <p><strong>Amount:</strong> ${amount} bag</p>
            <p><strong>Post Time:${post_time}</strong> </p>
           
            <p><strong>Blood Needed Time:${blood_need_time}</strong> </p>
           
           
          
            
        </div>
        <div class="post-address">
            <h3>Hospital Address</h3>
            <p><strong>Country:${country} </strong> </p>
            <p><strong>District:${district} </strong></p>
            <p><strong>Upazila:${upazila} </strong> </p>
            <p><strong>Union/Town:${unionOrtown} </strong></p>
            <p><strong>Village/Road: ${villageOrrad}</strong> </p>
            <p><strong>Zip Code: ${ zip_code}</strong> </p>
            <p><strong>Hospital Name:${ hospital_name} </strong> </p>
        </div>
    </br>
    <a href="#" class="btn btn-primary">applly to help</a>
        
        `;
       parent.appendChild(div);

        




        
     










       

        })





        .catch((err)=>{

          console.log("insise err of post deltials")
         });





  
  
  };


  single_post ();


















// const post_del = () => {
//   //fetch("http://127.0.0.1:8000/post_object/home?id=1", {
//   fetch("https://food-site-03s7.onrender.com/post_object/home/?id=1", {
//   method: "GET",
//   headers: { "content-type": "application/json" },
// })
//           .then((res) =>{

//             return res.json(); // Explicitly return res.json()
//           } )
          
//           .then(data => {
            
//           console.log(data);
          
          
          
          
        

//           })
//           .catch((err)=>{ 
//             console.log(err)
//           });
//  };




//  post_del();





const all_coments= () => {
const id = new URLSearchParams(window.location.search).get("id");

  //fetch(`https://food-site-03s7.onrender.com/post_object/home/?id=${id}`, {
//fetch(`http://127.0.0.1:8000/post_object/get_coment_for_a_post/?id=${id}`, {
fetch(`https://food-site-03s7.onrender.com/post_object/get_coment_for_a_post/?id=${id}`, {
  method: "GET",
  headers: { "content-type": "application/json" },
 
})

    .then((res) =>{
      return res.json(); // Explicitly return res.json()
    } )
    
    .then(data => {

    const parent = document.getElementById("coment_holder");


 var coment_list = data.all_the_coment
 //console.log(coment_list);

 coment_list.forEach(single_coment => {
  console.log(single_coment);

   const div = document.createElement("div");

       div.innerHTML=`
      

       <div id="single_coment">

 <p>user name:${single_coment.user_name} </p>

 <p>time:${single_coment.time}</p>

 <p>text:${single_coment.coment_text} </p>
 <br> <br>
      
       `;


       parent.appendChild(div);
    });



    })



    .catch((err)=>{

      console.log("insise err of post comts  ");
      console.log(err);
     });



}


all_coments () ;