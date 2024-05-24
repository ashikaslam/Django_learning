import { useRef } from "react";

const Hook_use_ref = () => {
   const my_variable = useRef(null);

   const change = () => {
      if (my_variable.current) {
         my_variable.current.innerText = "hello world";
      }
   };

   return (
       <div>
           <h2 ref={my_variable}>Initial text</h2>
           <button onClick={change}>Change</button>
       </div>
   );
};

export default Hook_use_ref;
