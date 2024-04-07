const handlepdf = () => {


    const doctor_id = new URLSearchParams(window.location.search).get("doctorId");
  
    fetch(`https://testing-8az5.onrender.com/doctor/list/${doctor_id}`)
      .then((res) => res.json())
  
      .then((data) => {
        fetch(`https://testing-8az5.onrender.com/users/6`)
          .then((res) => res.json())
  
          .then((pdata) => {
            const all_data = [data, pdata];
            console.log(all_data);
            
            const parent = document.getElementById("pdf-container");
            const div = document.createElement("div");
          
            div.innerHTML = `
  
  
  
  <div class="patient">
  <h2 >${all_data[1].username}</h2>
  <h2 >${all_data[1].first_name} ${all_data[1].last_name} </h2>
  <h2 >${all_data[1].email}</h2>
  
  </div>
  
  
  <div class="doctor">
  
  <img class="w-25"  src="${data.image}"/>
  <h2 class="doc-name">${data.full_name}</h2>
  
  
  
  </div>
  
  
  
  
  `;
  parent.appendChild(div);     
          });
      });
  };
  
  handlepdf();
  
  





  const donwloadPdf = () => {
    const element = document.getElementById("pdf-container");
  
    // Define the options for html2pdf
    const options = {
      margin: 10,
      filename: "appt.pdf",
      image: { type: "jpeg", quality: 0.98 },
      html2canvas: { scale: 2 },
      jsPDF: { unit: "mm", format: "a4", orientation: "portrait" },
    };
  
    // Use html2pdf to generate and download the PDF
      html2pdf(element, options);
      
  };
  ///////////////////////////////