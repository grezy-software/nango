"use client"

import { Link } from "next-view-transitions"
import { usePathname } from "next/navigation"

import { BASE_LOGGED_IN_URL } from "@/lib/constants"

export type TabType = {
  name: string
  href: string
  logo: React.ReactNode
  extra?: React.ReactNode
}

export default function SideBarTab({
  name,
  href,
  children,
}: {
  name: string
  href: string
  children: React.ReactNode
}) {
  const pathname = usePathname()

  return (
    <Link
      key={name}
      href={BASE_LOGGED_IN_URL + href}
      className={
        (pathname + "/" === BASE_LOGGED_IN_URL + href
          ? "bg-muted text-primary"
          : "text-muted-foreground") +
        " hover:text-primary flex items-center gap-3 rounded-lg px-3 py-2 transition-all"
      }
    >
      {children || null}
    </Link>
  )
}
