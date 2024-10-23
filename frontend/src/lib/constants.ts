import { env } from "next-runtime-env"

export const BASE_LOGGED_IN_URL = "/logged-in"
export const BASE_API_URL =
  process.env.NODE_ENV === "production"
    ? env("NEXT_PUBLIC_BACKEND_URL")
    : "http://localhost:8000/"
