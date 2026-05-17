import { deepiriJsonFormat } from "./formatters";

const info: Record<string, any> = {
  message: "User signup",
  level: "info",
  email: "bob@example.com",
  api_key: "AKIAIOSFODNN7EXAMPLE",
  authorization: "Bearer abcdefghijklmnopqrstuvwxyz",
};

const format = deepiriJsonFormat("diri-cyrex", "0.0.1");
// `format` is a winston Format object with a `transform` function
const formatted = (format as any).transform({ ...info });
console.log(JSON.stringify(formatted));
