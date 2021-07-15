import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import { PostTreeTable } from "../requests/PostTreeTable";

// const userToken = "df778ef2-2af4-475a-ba73-e1db707b075f";
const treeName = "Cohen";

export function ShowTable() {
  const [authorized, setAuthorized] = useState(false);
  const [userToken, setUserToken] = useState("");
  setAuthorized(localStorage.getItem("authorized"));
  setUserToken(localStorage.getItem("token"));
  if (!authorized) return <Redirect to="/login" />;
  const tree_data = PostTreeTable(userToken, treeName);
  console.log(tree_data);
  if (tree_data.status === 200) {
    return <div>tree_data</div>;
  } else {
    setAuthorized(false);
    return <div>Hello user!</div>;
  }
}

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
