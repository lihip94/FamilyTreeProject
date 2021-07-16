import React, { useEffect, useState } from "react";
import { backendService } from "./utils/paths";
import { LoginForm } from "./components/LoginForm";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Persons } from "./Persons";
import "./App.css";

function App() {
  const [persons, setPersons] = useState([]);
  const token = localStorage.getItem("token");
  const tree_name = "Cohen";
  const userTreeInfo = { token, tree_name };
  useEffect(() => {
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
  return (
    <div className="App">
      <Router>
        <Route exact path="/login" component={LoginForm} />
      </Router>
      <Persons persons={persons} />
    </div>
  );
}

export default App;
