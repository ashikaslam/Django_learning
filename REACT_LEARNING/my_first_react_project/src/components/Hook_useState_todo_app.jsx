import React, { useState } from "react";

const Hook_useState_todo_app = () => {
  const [myObject, setMyObject] = useState([]);
  const [myitem, setMyitem] = useState("");

  const add = () => {
    // The line myitem.trim() is used to remove any leading and trailing
    // whitespace from the string stored in the myitem state.
    // Here's a detailed explanation of what it does and why it's used:

    if (myitem.trim()) {
      setMyObject([...myObject, myitem]);
      setMyitem(""); // Clear the input field after adding
    }
  };

  const remove_Itme = (ind) => {
    myObject.splice(ind, 1);
    setMyObject([...myObject]);
  };

  return (
    <div>
      <p>{myObject.length}</p>
      <br />
      <input
        type="text"
        placeholder="add an item"
        value={myitem}
        onChange={(e) => setMyitem(e.target.value)}
      />
      <button onClick={add}>add</button>
      <ul>
        {myObject.map((item, index) => (
          <li key={index}>
            {item}
            <button onClick={() => remove_Itme(index)}>remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Hook_useState_todo_app;
