const home_content = () => {
    const carouselInner = document.querySelector('.carousel-inner');
    
    fetch("http://127.0.0.1:8000/products/RecentPost/", {
        method: "GET",
        headers: { "content-type": "application/json" },
    })
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
        const all_post = data.all_post;

        all_post.forEach((element, index) => {
            const title = element.title;
            const description = element.description;
            const price = element.price;
            const id = element.id;
            const image1 = element.product_picture;
            console.log(id);

            // Create a new div element for each carousel item
            const carouselItem = document.createElement('div');
            carouselItem.classList.add('carousel-item');
            if (index === 0) {
                carouselItem.classList.add('active');
            }
            carouselItem.style.backgroundImage = `url('${"http://127.0.0.1:8000/media/"+image1}')`;
            carouselItem.style.backgroundSize = 'cover';

            carouselItem.innerHTML = `
                <div class="carousel-caption d-none d-md-block">
                    <h5>${title}</h5>
                    <p><h3>${price}$</h3></p>
                    <a href="html_templates/product_detail.html?id=${id}" class="btn btn-primary">View Details</a>
                </div>
            `;

            carouselInner.appendChild(carouselItem);
            console.log(element,index);
        });
    })
    .catch((err) => {
        console.log(err);
    });
};

home_content();
