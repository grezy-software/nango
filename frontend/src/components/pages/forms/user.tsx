"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useRouter } from "next/navigation"
import { useState } from "react"
import { toast } from "sonner"
import { z } from "zod"

import { BASE_LOGGED_IN_URL } from "@/lib/constants"
import { CreateUserSchema } from "@/lib/schemas/CreateUser"
import { useLoggedInState } from "@/lib/stores/loggedIn"
import { useUserState } from "@/lib/stores/user"
import { useFormAction } from "@/lib/use-form-action"

import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import InputSecret from "@/components/ui/input-secret"

import { createUser } from "@/actions/createUser"

export default function CreateUserForm() {
  const router = useRouter()
  const [showPassword, setShowPassword] = useState(false)
  const [showPasswordConfirm, setShowPasswordConfirm] = useState(false)
  const loggedIn = useLoggedInState()
  const user = useUserState()

  const form = useFormAction<z.infer<typeof CreateUserSchema>>({
    resolver: zodResolver(CreateUserSchema),
    reValidateMode: "onChange",
    defaultValues: {
      username: "",
      email: "",
      password: "",
      passwordConfirm: "",
    },
  })

  return (
    <Form {...form}>
      <form
        {...form.submitAction(
          async (data: z.infer<typeof CreateUserSchema>) => {
            if (data.password !== data.passwordConfirm) {
              toast.error(
                "Your passwords do not match, please make sure they are the same and retry.",
              )
              return
            }
            const response = await createUser(data)
            if (response.success) {
              loggedIn.setState(true)
              user.setState({ name: data.username, email: data.email })
              toast.success("Your account has been created successfully!")
              router.push(BASE_LOGGED_IN_URL)
            } else if (response.errors?.non_field_errors) {
              console.log("Errors:", response.errors?.non_field_errors)
              toast.error(
                `You got the following errors: ${response.errors?.non_field_errors.join(" ")}`,
              )
            } else {
              console.log("Errors:", response.errors)
              toast.error("An error has occurred, please try again...")
            }
          },
        )}
        className="w-full space-y-4 py-8"
      >
        <FormField
          control={form.control}
          name="username"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Username</FormLabel>
              <FormControl>
                <Input placeholder="Username" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="email"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Email</FormLabel>
              <FormControl>
                <Input placeholder="username@example.com" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="password"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Password</FormLabel>
              <FormControl>
                <InputSecret
                  field={field}
                  visible={showPassword}
                  setVisible={setShowPassword}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="passwordConfirm"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Confirm Password</FormLabel>
              <FormControl>
                <InputSecret
                  field={field}
                  visible={showPasswordConfirm}
                  setVisible={setShowPasswordConfirm}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button className="w-full" type="submit">
          Create
        </Button>
      </form>
    </Form>
  )
}
