const token = localStorage.getItem("access_token");
if (!token) {
    window.location.href = `login.html`;
}

console.log(token);

const post_function = (event) => {
    event.preventDefault();

    // Check if token exists
    if (token) {
        // Extract form data
        const title = document.getElementById("title").value;
        const description = document.getElementById("description").value;
        const blood_need_time = document.getElementById("blood_need_time").value;
        const amount = document.getElementById("amount").value;
        const upazila = document.getElementById("upazila").value;
        const district = document.getElementById("district").value;
        const country = document.getElementById("country").value;
        const zip_code = document.getElementById("zip_code").value;
        const villageOrrad = document.getElementById("villageOrrad").value;
        const unionOrtown = document.getElementById("unionOrtown").value;
        const hospital_name = document.getElementById("hospital_name").value;
        const blood_grpup = document.querySelector('[name="blood_grpup"]').value;
        const image1 = document.getElementById("image1").files[0]; // Get the file object

        // Create FormData object
        const formData = new FormData();
        formData.append("title", title);
        formData.append("description", description);
        formData.append("blood_need_time", blood_need_time);
        formData.append("amount", amount);
        formData.append("upazila", upazila);
        formData.append("district", district);
        formData.append("country", country);
        formData.append("zip_code", zip_code);
        formData.append("villageOrrad", villageOrrad);
        formData.append("unionOrtown", unionOrtown);
        formData.append("hospital_name", hospital_name);
        formData.append("blood_grpup", blood_grpup);
        formData.append("image1", image1); // Append the image file

        // Make fetch request
        fetch("http://127.0.0.1:8000/post_object/post/", {
            method: "POST",
            headers: {
                Authorization: `Bearer ${token}`,
            },
            body: formData, // Pass FormData object as the body
        })
            .then((res) => {
                return res.json();
            })
            .then((data) => {
                // console.log('inside data ');
                // console.log(data);
                // if (data.status == 1) {
                //     console.log("hello inside");
                //     window.location.href = `otp.html?url=${data.activaton_url}`;
                // }
            })
            .catch((err) => {
                console.log('inside err ');
                console.log(err);
            });
    } else {
        window.location.href = `login.html`;
    }
    window.location.href=`post.html`;
};
