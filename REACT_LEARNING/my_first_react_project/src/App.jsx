// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'

//import Demo from "./Demo";

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <h1>hello world</h1>
//     </>
//   )
// }

// export default App

//import React from 'react';



// import Header from "./components/Header";
// import Footer from "./components/Footer";
// import Hero from "./components/Hero";
// import ContactForm from "./components/ContactForm";
//import Short_hand_if_else from "./components/Short_hand_if_else";
//import Immediatedly_invoked_function from "./components/Immediatedly_invoked_function";
//import For_loop from "./components/For_loop";
//import Conditional_rendering from "./components/Conditional_rendering";
//import Props from "./components/Props";


// const my_map = {
// Name:"Aslam",
// Roll:"570963",
// Department:"Computer"

// }

// const btn_click=()=>{

// alert("hello world");
// };


const fomr_submit =(events)=>
{

  events.preventDefault();
  alert("hello inside the fun")

};


import Hook_use_ref from "./components/Hook_use_ref";




const App = () => {
  return (
    <div>
     
    <Hook_use_ref/>

    </div>
  );
};

export default App;