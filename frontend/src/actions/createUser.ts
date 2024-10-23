"use client"

import { z } from "zod"

import { CreateUserSchema } from "@/lib/schemas/CreateUser"

import signIn from "./signIn"
import axiosInstance from "@/api/axios"
import { ServerActionResponse } from "@/types/form"

export async function createUser(
  data: z.infer<typeof CreateUserSchema>,
): Promise<ServerActionResponse<z.infer<typeof CreateUserSchema>, null>> {
  const validatedData = CreateUserSchema.safeParse({
    username: data.username,
    email: data.email,
    password: data.password,
    passwordConfirm: data.passwordConfirm,
  })

  if (!validatedData.success) {
    return {
      success: false,
      errors: validatedData.error.flatten().fieldErrors,
    }
  }
  const user = await axiosInstance.post("/api/user/", validatedData.data)
  if (user.status !== 201) {
    console.log("user create error", user)
    return {
      success: false,
      errors: user.data,
    }
  }
  const res = await signIn({
    email: validatedData.data.email,
    password: validatedData.data.password,
  })
  if (!res.success) {
    console.log("sign in error", res)
    return {
      success: false,
    }
  }

  return {
    success: true,
  }
}
