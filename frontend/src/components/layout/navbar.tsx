"use client"

import ThemeButton from "../themeButton"
import { useTheme } from "next-themes"
import { Link } from "next-view-transitions"
import Image from "next/image"
import { useEffect, useState } from "react"

import { navLinks } from "@/config/links"
import { ICON_DARK, ICON_LIGHT } from "@/config/nangoConf"

export default function Navbar() {
  const [navbar, setNavbar] = useState(false)
  const { theme } = useTheme()
  const handleClick = async () => {
    setNavbar(false)
  }

  useEffect(() => {
    if (navbar) {
      document.body.style.overflow = "hidden"
    } else {
      document.body.style.overflow = "auto"
    }
  }, [navbar])

  const navLinkPairs = []
  for (let i = 0; i < navLinks.length; i += 2) {
    navLinkPairs.push(navLinks.slice(i, i + 2))
  }

  return (
    <header className="container select-none">
      <nav className="justify-between md:flex md:items-center">
        <div>
          <div className="flex justify-between py-3 md:block md:py-5">
            <Link href="/" onClick={handleClick}>
              <Image
                src={theme === "dark" ? ICON_DARK : ICON_LIGHT}
                alt="Logo"
                width={100}
                height={100}
                className="cursor-pointer"
              />
            </Link>
            <div className="flex flex-row items-center gap-1 md:hidden">
              <ThemeButton />

              <button
                className="text-primary focus:border-primary rounded-md p-2 outline-none focus:border"
                aria-label="Hamburger Menu"
                onClick={() => setNavbar(!navbar)}
              >
                {navbar ? (
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="size-6"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fillRule="evenodd"
                      d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                      clipRule="evenodd"
                    />
                  </svg>
                ) : (
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="size-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    strokeWidth={2}
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M4 6h16M4 12h16M4 18h16"
                    />
                  </svg>
                )}
              </button>
            </div>
          </div>
        </div>
        <div className="flex flex-row items-center justify-between">
          <ThemeButton className="hidden md:flex" />
          <div
            className={`bg-background absolute z-10 m-auto rounded-md border p-4 md:static md:m-0 md:block md:border-none md:p-0 ${
              navbar ? "block" : "hidden"
            }`}
            style={navbar ? { width: "90%", left: "5%" } : {}}
          >
            <ul className="flex flex-col space-y-4 px-10 md:flex-row md:space-x-6 md:space-y-0">
              {navbar
                ? navLinkPairs.map((pair, index) => (
                    <li
                      key={index}
                      className="flex flex-row items-center justify-between"
                    >
                      {pair.map((link, idx) => (
                        <Link
                          key={idx}
                          className="text-sm hover:underline"
                          href={link.path}
                          onClick={handleClick}
                        >
                          {link.route}
                        </Link>
                      ))}
                    </li>
                  ))
                : navLinks.map((link) => (
                    <li key={link.route} className="">
                      <Link
                        className="text-sm hover:underline"
                        href={link.path}
                        onClick={handleClick}
                      >
                        {link.route}
                      </Link>
                    </li>
                  ))}
            </ul>
          </div>
        </div>
      </nav>
    </header>
  )
}
