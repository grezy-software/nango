"use client"

import { Icons } from "../icons"
import { Separator } from "../ui/separator"
import React from "react"

import { navLinks } from "@/config/links"

interface NavigationItem {
  name: string
  href: string
  icon?: (props: React.SVGProps<SVGSVGElement>) => JSX.Element
}

const navigation: {
  main: NavigationItem[]
  social: NavigationItem[]
} = {
  main: [
    { name: "About", href: "#" },
    { name: "Blog", href: "#" },
    { name: "Careers", href: "#" },
    { name: "Learn", href: "#" },
  ],
  social: [
    {
      name: "Email",
      href: "mailto:contact@grezy.org",
      icon: (props: React.SVGProps<SVGSVGElement>) => (
        <Icons.gmail className="size-6" />
      ),
    },
  ],
}

export default function Footer() {
  return (
    <footer className="container w-full">
      <Separator orientation="horizontal" />
      <div className="mx-auto w-full max-w-6xl px-4 py-12 sm:px-6 lg:px-8">
        <nav className="flex flex-wrap justify-center">
          {navLinks.map((item) => (
            <div key={item.path} className="px-5 py-2">
              <a
                href={item.path}
                className="text-muted-foreground hover:text-muted-foreground/80 text-sm"
              >
                {item.route}
              </a>
            </div>
          ))}
        </nav>
        <div className="mt-5 flex justify-center space-x-6">
          {navigation.social.map((item) => (
            <a
              key={item.name}
              href={item.href}
              className="text-muted-foreground hover:text-muted-foreground/80"
            >
              <span className="sr-only">{item.name}</span>
              {item.icon && <item.icon className="size-5" aria-hidden="true" />}
            </a>
          ))}
        </div>
        <div className="flex flex-col items-center justify-center">
          <p className="text-muted-foreground mt-6 text-center text-sm">
            &copy; {new Date().getFullYear()} This software was built by{" "}
            <span className="font-bold">Grezy Software</span>.
          </p>
        </div>
      </div>
    </footer>
  )
}
