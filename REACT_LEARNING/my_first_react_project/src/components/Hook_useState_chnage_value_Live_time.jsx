import React, { useState } from "react";

const Hook_useState_chnage_value_Live_time = () => {
  let [number, setNumber] = useState(20);

  const setNumberValue = () => {
    setNumber(number + 1);
  };

  return (
    <div>
      <h2>{number}</h2>
      <button onClick={setNumberValue}>click</button>
    </div>
  );
};

export default Hook_useState_chnage_value_Live_time;
