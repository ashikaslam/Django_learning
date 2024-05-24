
const defautltprofile_data = () => {
const name = localStorage.getItem("user_name");
const email = localStorage.getItem("email");
const mobile_number = localStorage.getItem("mobile_number");

document.getElementById("email").value=email;
document.getElementById("phone").value=mobile_number;
document.getElementById("name").value=name;

}

defautltprofile_data();










const profile_upadate_data = (event) => {
    event.preventDefault();
    const access = localStorage.getItem("access");
    const formData = new FormData();
    formData.append('name', document.getElementById('name').value);
    formData.append('mobile_number', document.getElementById('phone').value);
    formData.append('email', document.getElementById('email').value);
    
    const profilePicture = document.getElementById('profile-picture').files[0];
    if (profilePicture) {
        formData.append('profile_picture', profilePicture);
    }

    fetch('https://neighborhood-marketplace.onrender.com/auth/profele_update/', {
        method: 'POST',
        headers: {
            Authorization: `Bearer ${access}`,
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 1) {

console.log(data);
            alert('Profile updated successfully!');



        } else {
            console.log(data);
            alert('Failed to update profile: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while updating the profile.');
    });
}
