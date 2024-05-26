import { useRef } from "react";
const Hook_useRef_in_input_elements = () => {
  let first_name = useRef(null);
  let last_name = useRef(null);
  const show_name = () => {
    let fn = "unknwn";
    let ln = "unknwn";
    if (first_name.current) {
      fn = first_name.current.value;
    }
    if (last_name.current) {
      ln = last_name.current.value;
    }

    alert(fn + " " + ln);
  };

  return (
    <div>
      <input ref={first_name} type="text" placeholder="enter your first name" />
      <br />
      <input ref={last_name} type="text" placeholder="enter your last name" /> <br />
      <button  className="btn btn-primary"   onClick={show_name}>submit</button>
    </div>
  );
};

export default Hook_useRef_in_input_elements;


