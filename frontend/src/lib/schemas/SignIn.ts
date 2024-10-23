import { z } from "zod"

export const SignInSchema = z.object({
  password: z.string().min(8),
  email: z.string().email({
    message: "Invalid email address.",
  }),
})
