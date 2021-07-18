import React from "react";
import { LoginForm } from "./components/LoginForm";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { ShowTableForm } from "./components/ShowTableForm";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Router>
        <Route exact path="/showTable" component={ShowTableForm} />
        <Route exact path="/login" component={LoginForm} />
      </Router>
    </div>
  );
}

export default App;
