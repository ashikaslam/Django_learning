import React, { useState } from "react";

const Hook_useState_handle_object = () => {
  const [myObject, setMyObject] = useState({
    key1: 10,
    key2: 20,
    key3: 30,
  });

  const change = () => {
    alert();
    // Use setMyObject to update the state with a new object
    setMyObject({ ...myObject, key1: 40 });
  };

  return (
    <div>
      <h3>{myObject.key1}</h3>
      <button onClick={change}>click</button>
    </div>
  );
};

export default Hook_useState_handle_object;
