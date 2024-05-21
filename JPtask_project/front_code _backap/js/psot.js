




const psot_for_sell = (event) => {
    event.preventDefault();
    const access = localStorage.getItem("access");
    
// Collect form data
const formData = new FormData();
formData.append('title', document.getElementById('title').value);
formData.append('description', document.getElementById('description').value);
formData.append('price', document.getElementById('price').value);
formData.append('category', document.getElementById('category').value);
formData.append('condition', document.getElementById('condition').value);
formData.append('email', document.getElementById('email').value);
formData.append('mobile_number', document.getElementById('mobile_number').value);

const productPicture = document.getElementById('product_picture').files[0];
if (productPicture) {
    formData.append('product_picture', productPicture);
}







    fetch('http://127.0.0.1:8000/products/create_sell_post/', {
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
            alert(' successfully! psoted');
            window.location.href = '../index.html';


        } else {
            console.log(data);
            alert('Failed to post: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while posting.');
    });
}
