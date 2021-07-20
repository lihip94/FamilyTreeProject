import React from "react";
//import { List, Header } from "semantic-ui-react";
import "./persons.css";

export const Persons = ({ persons }) => {
  console.log(persons);
  return (
    <div>
      <div className="person-container">
        <table class="center">
          <tr>
            <td>
              <b>first name</b>
            </td>
            <td>
              <b>last name</b>
            </td>
            <td>
              <b>gender</b>
            </td>
          </tr>
        </table>
      </div>
      {persons.map((person) => {
        return (
          <div className="person-container">
            <table class="center">
              <tr>
                <td>{person.first_name}</td>
                <td>{person.last_name}</td>
                <td>{person.gender}</td>
              </tr>
            </table>
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
