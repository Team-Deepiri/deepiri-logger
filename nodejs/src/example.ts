import { createLogger } from "./index";
import { scrubPii } from "./formatters";

const logger = createLogger("diri-cyrex", "0.0.1");

logger.info("User signup", {
  email: "bob@example.com",
  api_key: "AKIAIOSFODNN7EXAMPLE",
  authorization: "Bearer abcdefghijklmnopqrstuvwxyz",
});

console.log('masked:', JSON.stringify(scrubPii({
  email: "bob@example.com",
  api_key: "AKIAIOSFODNN7EXAMPLE",
  authorization: "Bearer abcdefghijklmnopqrstuvwxyz",
})));
