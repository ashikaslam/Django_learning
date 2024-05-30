import React from "react";
import { useEffect } from "react";
import { useState } from "react";
const Hook_useEffect_apiFatch_async_awate = () => {
  const [myitem, setMyitem] = useState("");
  useEffect(() => {
    (async () => {
      let respoce = await fetch("https://jsonplaceholder.typicode.com/posts/");
      let data = await respoce.json();
      setMyitem(JSON.stringify(data));
    })();
  }, []);

  return (
    <div>
      <p>{myitem}</p>
    </div>
  );
};

export default Hook_useEffect_apiFatch_async_awate;
