

const product_detail_fun = () => {
    const id = new URLSearchParams(window.location.search).get("id");

    const carouselInner = document.querySelector('.carousel-inner');
    fetch(`https://neighborhood-marketplace.onrender.com/products/RecentPost/?id=${id}`,
     {
        method: "GET",
        headers: { "content-type": "application/json" },
    })
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
    
            const element=data.post[0];
            const title = element.title;
            const description = element.description;
            const price = element.price;
            const id = element.id;
            const category = element.category;
            const condition = element.condition;
            const mobile_number = element.mobile_number;
            const email = element.email;
            const sell_availavle = element.sell_availavle;
            const image1 = element.product_picture;
            console.log(id);
            const parent = document.getElementById("container_product");
            const div = document.createElement("div");
            div.innerHTML=`
            
            <div class="card">
            <img src="${"https://neighborhood-marketplace.onrender.com/media/"+image1}" class="card-img-top" alt="Listing Title"   style="width: 100%; height: 450px;">
            <div class="card-body">
                <h5 class="card-title">${title}</h5>
                <p class="card-text">${description}</p>
                <p class="card-text"><strong>Price:</strong> $${price }</p>
                <p class="card-text"><strong>Category: ${category }</strong> Category Name</p>
                <p class="card-text"><strong>Condition: ${condition }</strong> New</p>
                <a href="contact_seller.html" class="btn btn-primary">Contact Seller</a>
            </div>
        </div>
            `;
            parent.appendChild(div);






            

        
        })
    
    .catch((err) => {
        console.log(err);
    });
};

product_detail_fun();
