"use client"

import { Moon, Sun } from "lucide-react"
import { useTheme } from "next-themes"

import { cn } from "@/lib/utils"

import { Button } from "@/components/ui/button"

export default function ThemeButton({
  className = "",
}: {
  className?: string
}): JSX.Element {
  const { theme, setTheme } = useTheme()

  return (
    <Button
      variant="ghost"
      size="icon"
      onClick={() => {
        if (theme === "dark") {
          setTheme("light")
        } else {
          setTheme("dark")
        }
      }}
      className={cn(className, "bg-background")}
    >
      <Sun className="size-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
      <Moon className="absolute size-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
    </Button>
  )
}
