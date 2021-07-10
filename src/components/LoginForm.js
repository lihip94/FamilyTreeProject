import React, { useState } from "react";
import { Form, Input, Button } from "semantic-ui-react";

export const LoginForm = ({ onNewMovie }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  return (
    <Form>
      <Form.Field>
        <Input
          placeholder="email address"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
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
            const account = { email: email, password: password };
            const response = await fetch("http://localhost:5000/login", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(account),
            });

            if (response.ok) {
              console.log("response worked!");
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
