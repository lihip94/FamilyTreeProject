import React, { useState, useEffect } from "react";
import { Persons } from "./Persons";
import { backendService } from "../utils/paths";

export const ShowTableForm = () => {
  console.log("hello");
  const [persons, setPersons] = useState([]);

  useEffect(() => {
    let token = "";
    let tree_name = "";
    if (localStorage.getItem("authorized")) {
      console.log("#################");
      console.log(localStorage.getItem("authorized"));
      console.log(localStorage.getItem("token"));
      console.log(localStorage.getItem("tree_name"));
      token = localStorage.getItem("token");
      tree_name = localStorage.getItem("tree_name");
    }
    const userTreeInfo = { token, tree_name };
    fetch(backendService.getTreeInformation, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userTreeInfo),
    }).then((response) =>
      response.json().then((data) => {
        console.log(typeof data.data);
        console.log(data.data);
        setPersons(data.data);
      })
    );
  }, []);
  return <> {persons.length > 0 ? <Persons persons={persons} /> : null}</>;
};
