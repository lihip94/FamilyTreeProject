import React, { useEffect } from "react";
import { backendService } from "./utils/paths";
import { LoginForm } from "./components/LoginForm";
import { BrowserRouter as Router, Route } from "react-router-dom";
import ShowTable from "./components/ShowTableForm";
import "./App.css";

function App() {
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
        console.log(data);
      })
    );
  }, []);
  return (
    <div className="App">
      <Router>
        <Route exact path="/login" component={LoginForm} />
        <Route exact path="/showTable" component={ShowTable} />
      </Router>
    </div>
  );
}

export default App;
