


// const check_login  = () =>  {
   
    
//     const usr_id = localStorage.getItem("user_id");
//     const refress = localStorage.getItem("refress");
//     const access = localStorage.getItem("access");
//     if (!user_id || !refress || !access){
//         return false;
//     }
//     console.log(access);
//     const info = {
//         refress
//     };

//     console.log(JSON.stringify(info));

//     fetch('http://127.0.0.1:8000/auth/check_use_login/', {
//         method: 'GET',
//         headers: {
//             Authorization: `Bearer ${access}`,
//         },
        
//     })
//     .then((res) => res.json())
//     .then((data) => {
//         console.log('inside data');
//         console.log(data);
//         if (data.status === 1 && data.user_id==usr_id) {
//             console.log(data);
//             return true;
            

//         } else {
           
//             /////////////////////////////






//             fetch('http://127.0.0.1:8000/auth/check_use_login/', {
//                 method: 'POST',
//                 headers: { 'Content-Type': 'application/json' },
//                 body: JSON.stringify(info),
                
//             })
//             .then((res) => res.json())
//             .then((data) => {
//                 console.log('inside data');
//                 console.log(data);

                
//                 if (data.access  && data.refress) {




//                     localStorage.setItem('refress', data.refress);
//                     localStorage.setItem("access", data.access);

            
//                     console.log(data);
//                     return true;
                    
        
//                 }
                
//                 else {
                   
//         return false
//                 }
//             })
//             .catch((err) => {
//                 console.log('inside err');
//                 console.log(err);
//             });









// //////////////////////////////

//         }
//     })
//     .catch((err) => {
//         console.log('inside err');
//         console.log(err);
//     });








//     return false
// };




// export const  a = 100;