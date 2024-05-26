import React from "react";
import { useRef } from "react";
const Hook_useRef_caching_expensive_computations = () => {
  let api_data = useRef(null);
  let my_P_tag = useRef(null);
  const call_api = async () => {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts");
    api_data.current = await response.json();
  };
  const show = () => {
    my_P_tag.current.innerText = JSON.stringify(api_data);
    console.log(JSON.stringify(api_data));
  };

  return (
    <div>
      <button onClick={call_api}>call_api</button>
      <br />
      <button onClick={show}>show</button>
      <br />
      <p ref={my_P_tag}></p>
    </div>
  );
};

export default Hook_useRef_caching_expensive_computations;
