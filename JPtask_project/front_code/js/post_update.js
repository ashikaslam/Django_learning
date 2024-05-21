





const product_detail_fun = () => {
    const id = new URLSearchParams(window.location.search).get("id");

    fetch(`http://127.0.0.1:8000/products/RecentPost/?id=${id}`, {
        method: "GET",
        headers: { "content-type": "application/json" },
    })
    .then((res) => res.json())
    .then((data) => {
        console.log(data);

        if (data.post && data.post.length > 0) {
            const element = data.post[0];
            document.getElementById('title').value = element.title;
            document.getElementById('description').value = element.description;
            document.getElementById('price').value = element.price;
            document.getElementById('category').value = element.category;
            document.getElementById('condition').value = element.condition;
            document.getElementById('mobile_number').value = element.mobile_number;
            document.getElementById('email').value = element.email;
            
        }
    })
    .catch((err) => {
        console.log(err);
    });
};



product_detail_fun();








const post_upadate_data = (event) => {



    event.preventDefault();
    const access = localStorage.getItem("access");
    const id = new URLSearchParams(window.location.search).get("id");


    const formData = new FormData();
    formData.append('title', document.getElementById('title').value);
    formData.append('description', document.getElementById('description').value);
    formData.append('price', document.getElementById('price').value);
    formData.append('category', document.getElementById('category').value);
    formData.append('condition', document.getElementById('condition').value);
    formData.append('mobile_number', document.getElementById('mobile_number').value);
    formData.append('email', document.getElementById('email').value);
    
    const productPicture = document.getElementById('product_picture').files[0];
    if (productPicture) {
        formData.append('product_picture', productPicture);
    }




    fetch(`http://127.0.0.1:8000/products/update_sell_post/?id=${id}`, {
        method: 'POST',
        headers: {
            Authorization: `Bearer ${access}`,
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
      

console.log(data);

           
window.location.href = 'user_post.html';


       
    })
    .catch(error => {
        console.error('Error:', error);
        window.location.href = 'user_post.html';
    });


   
}

