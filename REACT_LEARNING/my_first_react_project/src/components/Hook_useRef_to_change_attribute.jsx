import { useRef } from "react";

const Hook_useRef_to_change_attribute = () => {
  const my_image = useRef(null);

  const change = () => {
    if (my_image.current) {
        my_image.current.src = "https://loremflickr.com/640/360";
        my_image.current.setAttribute('width','100%')
    }
  };

  return (
    <div>
      <img ref={my_image} src="https://placehold.co/600x400" alt="image" />
      <button onClick={change}>Change Image</button>
    </div>
  );A
};

export default Hook_useRef_to_change_attribute;
