"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useRouter } from "next/navigation"
import { useState } from "react"
import { toast } from "sonner"
import { z } from "zod"

import { BASE_LOGGED_IN_URL } from "@/lib/constants"
import { SignInSchema } from "@/lib/schemas/SignIn"
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

import getUserInfo from "@/actions/getUserInfo"
import signIn from "@/actions/signIn"

export default function SignInForm() {
  const router = useRouter()
  const [showPassword, setShowPassword] = useState(false)
  const loggedIn = useLoggedInState()
  const user = useUserState()
  const form = useFormAction<z.infer<typeof SignInSchema>>({
    resolver: zodResolver(SignInSchema),
    reValidateMode: "onChange",
    defaultValues: {
      email: "",
      password: "",
    },
  })

  return (
    <Form {...form}>
      <form
        {...form.submitAction(async (data: z.infer<typeof SignInSchema>) => {
          const response = await signIn(data)
          console.log(response)
          if (response.success) {
            const userInfo = await getUserInfo()
            loggedIn.setState(true)
            user.setState({ name: userInfo.username, email: userInfo.email })
            toast.success("Login successful!")
          } else {
            toast.error("An error has occurred, please try again...")
          }
          router.push(BASE_LOGGED_IN_URL + "/")
        })}
        className="w-full space-y-4 py-8"
      >
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
        <Button className="w-full" type="submit">
          Log In
        </Button>
      </form>
    </Form>
  )
}
