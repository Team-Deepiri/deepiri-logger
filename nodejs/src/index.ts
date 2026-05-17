import fs from "fs";
import path from "path";
import winston from "winston";
import { deepiriJsonFormat } from "./formatters";
import { requestLogger } from "./middleware";

export interface CreateLoggerOptions {
  logDir?: string;
  enableConsole?: boolean;
  level?: string;
}

export function createLogger(
  serviceName: string,
  version = "unknown",
  options: CreateLoggerOptions = {},
): winston.Logger {
  const level = options.level || process.env.LOG_LEVEL || "info";
  const logDir = options.logDir || process.env.LOG_DIR;
  const transports: winston.transport[] = [];

  if (logDir) {
    const resolvedLogDir = path.resolve(logDir);
    if (!fs.existsSync(resolvedLogDir)) {
      fs.mkdirSync(resolvedLogDir, { recursive: true });
    }

    transports.push(
      new winston.transports.File({
        filename: path.join(resolvedLogDir, "error.log"),
        level: "error",
        maxsize: 5242880,
        maxFiles: 5,
      }),
      new winston.transports.File({
        filename: path.join(resolvedLogDir, "combined.log"),
        maxsize: 5242880,
        maxFiles: 5,
      }),
    );
  }

  if (options.enableConsole !== false) {
    transports.push(new winston.transports.Console());
  }

  return winston.createLogger({
    level,
    format: winston.format.combine(deepiriJsonFormat(serviceName, version), winston.format.json()),
    defaultMeta: { service_name: serviceName, version },
    transports,
  });
}

export { requestLogger };
