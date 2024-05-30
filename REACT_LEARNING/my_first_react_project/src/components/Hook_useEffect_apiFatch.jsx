import React from "react";
import { useEffect } from "react";
import { useState } from "react";
const Hook_useEffect_apiFatch = () => {
  const [myitem, setMyitem] = useState("");
  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts/1")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok " + response.statusText);
        }
        return response.json(); // parses JSON response into native JavaScript objects
      })
      .then((data) => {
        console.log(data);
        setMyitem(JSON.stringify(data));
      })
      .catch((error) => {
        console.error(
          "There has been a problem with your fetch operation:",
          error
        );
      });
  }, []);

  return (
    <div>
      <p>{myitem}</p>
    </div>
  );
};

export default Hook_useEffect_apiFatch;
