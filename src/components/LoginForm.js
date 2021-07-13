import React, { useState } from "react";
import { Form, Input, Button } from "semantic-ui-react";
import { useHistory } from "react-router-dom";
import { backendService } from "../utils/paths";

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
            const account = { email, password };
            const response = await fetch(backendService.getLoginPath, {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(account),
            });

            if (response.ok) {
              console.log("response worked!");
              const data = await response.json();
              const status = data.status;

              setEmail("");
              setPassword("");
              if (status === 200) {
                history.push("/showTable");
              }
            }
          }}
        >
          login
        </Button>
      </Form.Field>
    </Form>
  );
};
