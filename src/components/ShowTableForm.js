import React from "react";
import { List, Header, Rating } from "semantic-ui-react";

export const persons = ({ persons }) => {
  return (
    <List>
      {persons.map((person) => {
        return (
          <List.Item key={person.id}>
            <Header>{person.name}</Header>
          </List.Item>
        );
      })}
    </List>
  );
};
