import React, { useState } from "react";
import { Form, Input, Button } from "semantic-ui-react";
import { useHistory } from "react-router-dom";
import { getLogin } from "../requests/GetLogin";

export const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  let history = useHistory();

  return (
    <Form>
      <Form.Field>
        <Input
          placeholder="email address"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          type="email"
          id="email"
          name="email"
        />
      </Form.Field>
      <Form.Field>
        <Input
          type="password"
          placeholder="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </Form.Field>
      <Form.Field>
        <Button
          onClick={async () => {
            const status = await getLogin(email, password);
            if (status === 200) {
              history.push("/showTable");
            } else {
              setEmail("");
              setPassword("");
            }
          }}
        >
          login
        </Button>
      </Form.Field>
    </Form>
  );
};
