import React, { useState } from "react";
import { Form, Input, Button } from "semantic-ui-react";
import { useHistory } from "react-router-dom";

export const LoginForm = ({ onNewMovie }) => {
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
            const account = { email, password };
            const response = await fetch("/login", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(account),
            });

            if (response.ok) {
              console.log("response worked!");
              console.log(response.json().then((data) => console.log(data)));
              setEmail("");
              setPassword("");
              history.push("/showTable");
            }
          }}
        >
          login
        </Button>
      </Form.Field>
    </Form>
  );
};
