"use client"

import { useState } from "react"

import { useLoggedInState } from "@/lib/stores/loggedIn"

import HeadingText from "@/components/headingText"
import SignInForm from "@/components/pages/forms/signIn"
import CreateUserForm from "@/components/pages/forms/user"
import { Button } from "@/components/ui/button"

export default function Login() {
  const loggedIn = useLoggedInState()
  const [loginMode, setLoginMode] = useState(true)

  return (
    <>
      <>
        {loginMode ? (
          <div>
            <div className="flex flex-col items-center space-y-2 pt-20 text-center">
              <HeadingText
                subtext={
                  "Please enter your credentials to access your account."
                }
              >
                Connect
              </HeadingText>
            </div>
            <SignInForm />
          </div>
        ) : (
          <div>
            <div className="flex flex-col items-center space-y-2 pt-20 text-center">
              <HeadingText
                subtext={
                  "Fill in your credentials so we can create your account."
                }
              >
                Create an account
              </HeadingText>
            </div>
            <CreateUserForm />
          </div>
        )}
      </>
      <div>
        {loggedIn.data ? (
          <></>
        ) : loginMode ? (
          <Button variant={"ghost"} onClick={() => setLoginMode(!loginMode)}>
            {"I don't have an account."}
          </Button>
        ) : (
          <Button variant={"ghost"} onClick={() => setLoginMode(!loginMode)}>
            {"I already have an account."}
          </Button>
        )}
      </div>
    </>
  )
}
