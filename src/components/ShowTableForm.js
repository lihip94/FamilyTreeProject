import React from "react";
import { Redirect } from "react-router-dom";
// import { List, Header, Rating } from "semantic-ui-react";

// export const persons = ({ persons }) => {
//   return (
//     <List>
//       {persons.map((person) => {
//         return (
//           <List.Item key={person.id}>
//             <Header>{person.name}</Header>
//           </List.Item>
//         );
//       })}
//     </List>
//   );
// };

function ShowTable({ authorized }) {
  if (!authorized) return <Redirect to="/login" />;
  else return <div>Hello user!</div>;
}

export default ShowTable;
