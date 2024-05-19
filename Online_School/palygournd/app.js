

  
  
function submitComment() { 
const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MTAxMzEyLCJpYXQiOjE3MTYwNDEzMTIsImp0aSI6IjU2NTc0MjUyZTEwYzRhNTE5MTNlMDZhMjk0MDFmZmNlIiwidXNlcl9pZCI6Mn0.dyZEsxEW16I7pH0ZvzamGEabtIB1q1lgmyZMYU7ltf0" ;
    fetch(`http://127.0.0.1:8000/auth/logout/`, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
       
      },
     
    })
      .then((res) => {
        return res.json(); // Explicitly return res.json()
      })
      .then((data) => {
        console.log(data);
      })
      .catch((err) => {
        console.log(err);
      });
  
  
     
  }
  
  
submitComment();
  
  