import React, { useState } from "react";
import { Form, Input, Button } from "semantic-ui-react";
import { useHistory } from "react-router-dom";
import { getLogin } from "../requests/PostLogin";

export let token = "";
export const LoginForm = () => {
  localStorage.setItem("authorized", false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  let history = useHistory();

  return (
    <div>
      <div>
        <header>
          <b>Log in to continue to Shorashim</b>
        </header>
      </div>
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
              if (!email || !password) {
                setEmail("");
                setPassword("");
                localStorage.setItem("authorized", false);
              } else {
                const userResponse = await getLogin(email, password);
                console.log(userResponse.status);
                if (userResponse.status === 200) {
                  if (userResponse.data) {
                    console.log(userResponse);
                    token = userResponse.data.token;
                    localStorage.setItem("authorized", true);
                    localStorage.setItem("token", token);
                    history.push({
                      pathname: "/table-name",
                    });
                  }
                } else {
                  setEmail("");
                  setPassword("");
                  localStorage.setItem("authorized", false);
                }
              }
            }}
          >
            login
          </Button>
        </Form.Field>
      </Form>
    </div>
  );
};
