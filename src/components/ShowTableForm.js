import React, { useState, useEffect } from "react";
import { Persons } from "./Persons";
import { backendService } from "../utils/paths";

export const ShowTableForm = () => {
  const [persons, setPersons] = useState([]);

  useEffect(() => {
    let token = "";
    let tree_name = "";
    if (localStorage.getItem("authorized")) {
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
        setPersons(data.data);
      })
    );
  }, []);
  return <> {persons.length > 0 ? <Persons persons={persons} /> : null}</>;
};
