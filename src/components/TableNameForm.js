import React, { useState } from "react";
import { Form, Input, Button } from "semantic-ui-react";
import { useHistory } from "react-router-dom";

export const TableNameForm = () => {
  const [treeName, setTreeName] = useState("");
  localStorage.setItem("tree_name", "");
  let history = useHistory();
  function handleClick() {
    if (treeName) {
      localStorage.setItem("tree_name", treeName);
      history.push("/show-table");
    }
  }

  return (
    <Form>
      <Form.Field>
        <Input
          placeholder="family tree name"
          value={treeName}
          onChange={(e) => setTreeName(e.target.value)}
          type="treeName"
          id="treeName"
          name="treeName"
        />
      </Form.Field>
      <Form.Field>
        <Button onClick={handleClick}>get family information</Button>
      </Form.Field>
    </Form>
  );
};
