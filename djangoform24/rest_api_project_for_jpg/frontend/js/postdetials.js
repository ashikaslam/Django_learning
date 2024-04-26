

// const single_post= () => {

//     const id = new URLSearchParams(window.location.search).get("id");
//     fetch("http://127.0.0.1:8000/post_object/home/", {
//       method: "GET",
//       headers: { "content-type": "application/json" },
     
//     })

//         .then((res) =>{
//           return res.json(); // Explicitly return res.json()
//         } )
        
//         .then(data => {
          
//         const element=data.post;
//        // here element is single post
//         const amount= element.amount;
//         const  apply_availavle = element.apply_availavle;
//         const at_leas_5_people_managed =element.at_leas_5_people_managed;
//         const blood_grpup=element.blood_grpup;
//         const blood_need_time=element.blood_need_time;
//         const country=element.country;
//         const description=element.description;
//         const  district= element.district;
//         const  donate_done=element. donate_done;
//         const  hospital_name= element.hospital_name;
//         const  id = element.id;
//         const image1 = element.image1;
//         const impage2= element.impage2;
//         const post_time= element.post_time;
//         const post_update_time= element.post_update_time;
//         const  title= element.title;
//         const  unionOrtown= element. unionOrtown;
//         const  upazila= element. upazila;
//         const   user_id= element.  user_id;
//         const   villageOrrad= element.  villageOrrad;
//         const  zip_code= element. zip_code;
//         console.log(data);

       

        
        
        
       

//         })


//         .catch((err)=>{

//           console.log("insise err")
//          });





  
  
//   };


//   single_post ();


















const post_del = () => {
  fetch("http://127.0.0.1:8000/post_object/home?id=5", {
  method: "GET",
  headers: { "content-type": "application/json" },
})
          .then((res) =>{

            return res.json(); // Explicitly return res.json()
          } )
          
          .then(data => {
            
          console.log(data);
          
          
          
          
        

          })
          .catch((err)=>{ 
            console.log(err)
          });
 };




 post_del();