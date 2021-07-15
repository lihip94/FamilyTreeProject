import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import { postTreeTable } from "../requests/PostTreeTable";

const userToken = "df778ef2-2af4-475a-ba73-e1db707b075f";
const treeName = "Cohen";

export const ShowTable = async () => {
  const [authorized, setAuthorized] = useState(false);
  setAuthorized(localStorage.getItem("authorized"));
  if (!authorized) return <Redirect to="/login" />;
  const tree_data = await postTreeTable(userToken, treeName);
  if (tree_data.status === 200) {
    return <div>tree_data</div>;
  } else {
    setAuthorized(false);
    return <div>Hello user!</div>;
  }
};

// function ShowTable() {
//   const authorized = localStorage.getItem("authorized");

//   if (!authorized) return <Redirect to="/login" />;
//   console.log("11111111");
//   const tree_data = postTreeTable(userToken, treeName).then((response) => {
//     if (tree_data.status === 200) {
//       return <div>tree_data</div>;
//     }
//     return <div>Hello user!</div>;
//   });
// }

export default ShowTable;
