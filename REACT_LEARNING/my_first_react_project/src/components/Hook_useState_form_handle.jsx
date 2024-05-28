import React, { useState } from "react";

const Hook_useState_form_handle = () => {
  let [form_obj, set_form_obj] = useState({
    fName: "",
    lName: "",
    city: "",
    gender: "Male",
  });
  const inputOnChange = (property, value) => {
    set_form_obj((preObj) => ({
      ...preObj,
      [property]: value,
    }));
  };
  const formSubmit = (e) => {
    e.preventDefault(); /// what wrong with this line?
    console.log(form_obj);
   
  };

  return (
    <div>
      <form onSubmit={formSubmit}>
        <input
          onChange={(e) => {
            inputOnChange("fName", e.target.value);
          }}
          type="text"
          placeholder="First Name"
          value={form_obj.fName}
        />
        <br />
        <input
          onChange={(e) => {
            inputOnChange("lName", e.target.value);
          }}
          type="text"
          placeholder="Last Name"
          value={form_obj.lName}
        />
        <br />
        <select
          onChange={(e) => {
            inputOnChange("city", e.target.value);
          }}
          value={form_obj.city}
        >
          <option value="">Choose Chity</option>
          <option value="Dhaka">Dhaka</option>
          <option value="Khulna">Khulna</option>
          <option value="Borishal">Borishal</option>
        </select>
        <br />
        <input
          type="radio"
          name="gender"
          checked={form_obj.gender === "Male"}
          onChange={() => {
            inputOnChange("gender", "Male");
          }}
        />
        Male
        <input
          type="radio"
          name="gender"
          checked={form_obj.gender === "Female"}
          onChange={() => {
            inputOnChange("gender", "Female");
          }}
        />
        Feale
        <br />
        <button type="submit">submit</button>
      </form>
    </div>
  );
};

export default Hook_useState_form_handle;
