import { z } from "zod"

export const CreateUserSchema = z.object({
  username: z
    .string()
    .regex(
      RegExp("^[a-zA-Z0-9_.-]*$"),
      "Please use a username that only contains numbers and letters (no spaces).",
    ),
  password: z.string().min(8),
  passwordConfirm: z.string().min(8),
  email: z.string().email({
    message: "Invalid email address.",
  }),
})
