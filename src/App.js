import React from "react";
import { LoginForm } from "./components/LoginForm";
import { BrowserRouter as Router, Route } from "react-router-dom";
import ShowTable from "./components/ShowTableForm";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Router>
        <Route exact path="/login" component={LoginForm} />
        <Route
          exact
          path="/showTable"
          component={() => <ShowTable authorized={true} />}
        />
      </Router>
    </div>
  );
}

export default App;
