



import React from 'react';
import { useRef } from "react";
const Hook_useRef_change_mutibale_data_behind_the_sence = () => {
    let my_number = useRef(20);
    const change=()=>{
        my_number.current++;
        console.log("hello",my_number.current);
    };
    return (
        <div>
            <button  onClick={change}>click</button>
        </div>
    );
};

export default Hook_useRef_change_mutibale_data_behind_the_sence;