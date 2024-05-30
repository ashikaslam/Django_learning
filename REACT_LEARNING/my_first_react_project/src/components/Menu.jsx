


import React from "react";
import { NavLink } from "react-router-dom";
const Menu = () => {
  return (
    <div>
      <ul>
        <li>
          <NavLink className={({isActive,isPending})=>isActive?"is_active":"is_not_active"   }   to="/">home</NavLink>
        </li>
        <li>
          <NavLink  className={({isActive,isPending})=>isActive?"is_active":"is_not_active"   }   to="/products/10">porduct</NavLink>
        </li>
      </ul>
    </div>
  );
};

export default Menu;
