import React from "react";
import { LoginForm } from "./components/LoginForm";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { ShowTableForm } from "./components/ShowTableForm";
import { TableNameForm } from "./components/TableNameForm";
import { home } from "./components/home";
import "./App.css";

function App() {
  return (
    <div className="App">
      <div className="navigation">
        <div>
          <a href="/home">Home</a>
        </div>
        <div>
          <a href="/login">LogIn</a>
        </div>
      </div>
      <Router>
        <Route exact path="/show-table" component={ShowTableForm} />
        <Route exact path="/login" component={LoginForm} />
        <Route exact path="/table-name" component={TableNameForm} />
        <Route exact path="/home" component={home} />
      </Router>
    </div>
  );
}

export default App;
