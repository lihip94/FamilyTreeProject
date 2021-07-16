import { backendService } from "../utils/paths";

export async function getLogin(email, password) {
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
    const userResponse = await response.json();
    return userResponse;
  } else {
    return 400;
  }
}
