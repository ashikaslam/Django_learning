






  













  const psot_of_user_sell = () => {

    const access = localStorage.getItem("access");
    fetch('https://neighborhood-marketplace.onrender.com/products/my_post/', {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${access}`,
        },
       
    })
    .then(response => response.json())


    .then(data => {
        console.log(data);
        // Process the data and create cards
        const container = document.getElementById('post_container');
        const all_post = data.all_post;
        all_post.forEach(post => {
          // Create card elements using template literals for cleaner code
          const cardCol = document.createElement('div');
          cardCol.classList.add('col-md-3', 'mb-4');
    
          const cardHTML = `
            <div class="card">
              <img src="${"https://neighborhood-marketplace.onrender.com/media/"+post.product_picture}" class="card-img-top" alt="Post Image">
              <div class="card-body">
                <h5 class="card-title">${post.title}</h5>
                <a href="update_Post.html?id=${post.id}" class="btn btn-primary">Update</a>
                <button class="btn btn-danger btn-sm"    onclick="delete_reques(${post.id})"  >Delete</button>
              </div>
            </div>
          `;
    
          cardCol.innerHTML = cardHTML;
    
          // Append card to container
          container.appendChild(cardCol);
        });
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
}


psot_of_user_sell();


const delete_reques = (id) => {
  const access = localStorage.getItem("access");
  fetch(`https://neighborhood-marketplace.onrender.com/products/delete_my_post/?id=${id}`, {
      method: 'GET',
      headers: {
          Authorization: `Bearer ${access}`,
      },
  })
  .then(response => response.json())
  .then(data => {
      console.log(data);
      window.location.href = 'user_post.html';
     // window.location.href = 'user_post.html';
    })
    .catch(error => {
      window.location.href = 'user_post.html';
     // window.location.href = 'user_post.html';
      console.error('Error fetching data:', error);
    });
}
