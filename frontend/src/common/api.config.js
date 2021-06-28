import { CSRF_TOKEN } from "./csrf_token.js";

function requestConfig(data, method) {
  return {
    method: method || "GET",
    body: data ? JSON.stringify(data) : null,
    headers: {
      "content-type": "application/json",
      "X-CSRFTOKEN": CSRF_TOKEN,
    },
  };
}

export { requestConfig };
