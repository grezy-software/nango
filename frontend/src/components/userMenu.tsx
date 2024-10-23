"use client"

import { User } from "lucide-react"
import { useRouter } from "next/navigation"
import { useEffect, useState } from "react"

import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

import signOut from "@/actions/signOut"
import axiosInstance from "@/api/axios"

export default function UserMenu(): JSX.Element {
  const [user, setUser] = useState<{ username?: string }>({})
  const router = useRouter()
  useEffect(() => {
    async function fetchData() {
      const response = await axiosInstance.get("/api/user")
      if (response) {
        setUser(response.data)
      }
    }
    fetchData()
  }, [])
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="secondary" size="icon" className="rounded-full">
          <Avatar className="border-2">
            <AvatarImage></AvatarImage>
            <AvatarFallback>
              {user.username && user.username[0] ? (
                user.username[0].toUpperCase()
              ) : (
                <User />
              )}
            </AvatarFallback>
          </Avatar>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <DropdownMenuLabel>My Account</DropdownMenuLabel>
        <DropdownMenuSeparator />
        {/* <DropdownMenuItem>Settings</DropdownMenuItem> */}
        {/* <DropdownMenuItem>Support</DropdownMenuItem> */}
        {/* <DropdownMenuSeparator /> */}
        <DropdownMenuItem
          onClick={async () => {
            await signOut()
            router.push("/")
          }}
        >
          Logout
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
