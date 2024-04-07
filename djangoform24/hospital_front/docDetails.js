const loadTime = (id) => {
  fetch(
    `https://testing-8az5.onrender.com/doctor/availabletime/?doctor_id=${id}`
  )
    .then((res) => res.json())
    .then((data) => {
      data.forEach((item) => {
        const parent = document.getElementById("time_selection");
        const option = document.createElement("option");
        option.value = item.id;
        option.innerText = item.name;
        parent.appendChild(option);
      });
    });
};

const getparams = () => {
  const param = new URLSearchParams(window.location.search).get("doctorId");

  loadTime(param);
  fetch(`https://testing-8az5.onrender.com/doctor/list/${param}`)
    .then((res) => res.json())
    .then((data) => displayDetails(data));

  fetch(`https://testing-8az5.onrender.com/doctor/review/?doctor_id=${param}`)
    .then((res) => res.json())
    .then((data) => displayRVIEW(data));
};
getparams();

const displayDetails = (doctor) => {
  const parent = document.getElementById("doc-details");
  const div = document.createElement("div");
  div.classList.add("details");
  div.innerHTML = `
    
    <img src="${doctor.image}" alt="">
<h1>${doctor.full_name}</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Incidunt, repudiandae!</p>
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
take appointment
</button>
    `;
  parent.appendChild(div);
};

const displayRVIEW = (reviews) => {
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

const handleAppointment = () => {
  const doctor_id = new URLSearchParams(window.location.search).get("doctorId");

  const status = document.getElementsByName("availability");
  const selected = Array.from(status).find((button) => button.checked);
  const symptom = document.getElementById("syntrom").value;
  const time = document.getElementById("time_selection");
  const selectedTime = time.options[time.selectedIndex];

  const info = {
    appointment_type: selected.value,
    appointment_status: "Pending",
    time: selectedTime.value,
    symptom: symptom,
    cancel: false,
    patient: 1,
    doctor: doctor_id,
  };

  fetch("https://testing-8az5.onrender.com/appointment/", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(info),
  })
    .then((res) => res.json())

    .then((data) => {});

    window.location.href=`pdf.html?doctorId=6`;
};



////////////////////////


