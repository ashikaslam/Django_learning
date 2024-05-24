






const logout_fun = () => {
     const refresh_token = localStorage.getItem("refress");
     console.log(refresh_token);
    
    const info = {
        refresh_token
    };

     console.log(JSON.stringify(info));
    fetch('https://neighborhood-marketplace.onrender.com/auth/apiLogout/', {
        method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(info),  
    })
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
            
        })
            .catch((err) => {  
            });



           localStorage.clear();
            window.location.href=`html_templates/login.html`;
           
};


