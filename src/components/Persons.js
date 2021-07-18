import React from "react";
//import { List, Header } from "semantic-ui-react";
import "./persons.css";

export const Persons = ({ persons }) => {
  console.log(persons);
  return (
    <div>
      {persons.map((person) => {
        return (
          <div className="person-container">
            <div>{person.first_name}</div>
            <div>{person.last_name}</div>
          </div>
        );
      })}
    </div>
    // <List>
    //   {persons.map((person) => {
    //     return (
    //       <List.Item key={person.first_name}>
    //         <Header>{person.first_nam}</Header>
    //       </List.Item>
    //     );
    //   })}
    // </List>
  );
};
