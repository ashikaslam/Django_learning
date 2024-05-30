import React, { useEffect } from "react";

const Hook_useEffect = () => {
  useEffect(() => {
    console.log("Hello");
  }, [10]);

  return <div></div>;
};

export default Hook_useEffect;
