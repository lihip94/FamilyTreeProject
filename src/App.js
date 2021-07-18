import React from "react";
import { LoginForm } from "./components/LoginForm";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { ShowTableForm } from "./components/ShowTableForm";
import { TableNameForm } from "./components/TableNameForm";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Router>
        <Route exact path="/showTable" component={ShowTableForm} />
        <Route exact path="/login" component={LoginForm} />
        <Route exact path="/table-name" component={TableNameForm} />
      </Router>
    </div>
  );
}

export default App;
