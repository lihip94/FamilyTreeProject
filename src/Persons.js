import React from "react";
// import { List, Header } from "semantic-ui-react";

export const Persons = ({ persons }) => {
  return (
    <div>{persons.length}</div>
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
