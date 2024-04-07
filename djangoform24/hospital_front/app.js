
const loadServices = ()=>{
fetch("https://testing-8az5.onrender.com/services/")
  .then((res)=>res.json())
  .then((data)=>display_siervices(data))
  .catch((err)=>console.log(err));
};





const display_siervices = (serveces)=>{
    serveces.forEach(element => {
        const parent = document.getElementById("services-container");
        const  li = document.createElement("li");
        li.innerHTML=`
        <div class="card shadow h-100">
                <div class="ratio ratio-16x9">
                    <img src=${element.image} class="card-img-top" loading="lazy" alt="...">
                </div>
                <div class="card-body  p-3 p-xl-5">
                    <h3 class="card-title h5"> ${element.name}</h3>
                    <p class="card-text">${element.description}</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
            </div>
        
        `;
        parent.appendChild(li);




    });

};
loadServices();


const loadDoctors=(search)=>{
  document.getElementById("doctors-slider").innerHTML="";
  document.getElementById("loading_them").style.display="block";
  fetch(
    `https://testing-8az5.onrender.com/doctor/list/?search=${
      search ? search : ""
    }`
  )



  .then((res)=>res.json())
  .then((data)=>{


    if(data.results.length>0){
      document.getElementById("loading_them").style.display="none";
      document.getElementById("no_data").style.display="none";
      displayDoctors(data.results);
    }
    else{
      document.getElementById("loading_them").style.display="none";
      document.getElementById("no_data").style.display="block";
    }



  })
  .catch((err)=>console.log(err));
  

  
};
 
  
    
  












const displayDoctors = (allDoctors) => {
  allDoctors.forEach(single_doctor => {
     const parent = document.getElementById("doctors-slider");
     const div = document.createElement("div");
     div.classList.add("doc-card");
     div.innerHTML = `
       <img src=${single_doctor.image} alt="" style="height: 100px; width: 100px; border-radius: 50px;">
       <h1>${single_doctor.full_name}</h1>
       <h6>${single_doctor.designation[0]}</h6>
      
       
       ${single_doctor?.specialization.map(item => {
        return `<button>${item}</button>`;
      })}

       <h6>FEE is $${single_doctor.fee}</h6>
        
       <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur, aliquam.</p>
       <button> <a target="_blank" href="docDetails.html?doctorId=${single_doctor.id}"> details </a>   </button>
     `;
     parent.appendChild(div);
  });
 
};
loadDoctors();



const loadDegictions=()=>{
 
  fetch("https://testing-8az5.onrender.com/doctor/designation/")
  .then((res)=>res.json())
  .then((data)=>display_designation(data))
  .catch((err)=>console.log(err));
};

const display_designation=(arr)=>{

  arr.forEach(single_item => {


     const parent= document.getElementById("designaton_ber");
     const li = document.createElement("li");
     li.classList.add("dropdown-item");

     li.innerText = single_item.name;
     parent.appendChild(li);
});

};

loadDegictions();






////////////






const loadspesalizaton=()=>{
  
  fetch("https://testing-8az5.onrender.com/doctor/specialization/")
  .then((res)=>res.json())
  .then((data)=>display_spesalizaton(data))
  .catch((err)=>console.log(err));
};

const display_spesalizaton=(arr)=>{

  arr.forEach(single_item => {

     const parent= document.getElementById("specialization_ber");
     const li = document.createElement("li");
     li.classList.add("dropdown-item");

    // li.innerText = single_item.name;


     li.innerHTML=`
     <li onclick="loadDoctors(' ${single_item.name}')">  ${single_item.name}</li>
          `;
     parent.appendChild(li);
});

};

loadspesalizaton();





const handle_search=()=>{
  const our_value = document.getElementById("serarch_a_doc").value;
  loadDoctors(our_value);
};








const loadReview = () => {
  fetch("https://testing-8az5.onrender.com/doctor/review/")
    .then((res) => res.json())
    .then((data) => displayReview(data));
};




const displayReview = (reviews) => {
  reviews.forEach((review) => {
    const parent = document.getElementById("review-container");
    const div = document.createElement("div");
    div.classList.add("singel_reivew_card");
    div.innerHTML = `
        <img src="./images/clint1.jpg" alt="" />
            <h4>${review.reviewer}</h4>
            <p>
             ${review.body.slice(0, 100)}
            </p>
            <h6>${review.rating}</h6>
        `;
    parent.appendChild(div);
  });
};


loadReview();