import React from 'react';
import Menu from "./Menu";
import { useParams } from 'react-router-dom';
const product_page = () => {
    let {id} = useParams();
    return (
        <div>
              <Menu/>
           <h1>this is products  {id }</h1> 
        </div>
    );
};

export default product_page;