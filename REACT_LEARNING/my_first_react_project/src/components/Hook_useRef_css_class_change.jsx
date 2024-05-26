import { useRef } from "react";





import React from 'react';

const Hook_useRef_css_class_change = () => {
    let my_button  = useRef(null);
    const change=()=>{
        if(my_button.current){
            alert('hello');

            
            my_button.current.classList.remove('btn', 'btn-primary');
            my_button.current.classList.add('btn', 'btn-danger');
          
        }
    };

    return (
        <div>
            <button type="submit" className='btn btn-primary'  ref={my_button} onClick={change}>submit</button>
        </div>
    );
};

export default Hook_useRef_css_class_change;