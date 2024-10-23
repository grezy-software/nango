import { PublicEnvScript } from "next-runtime-env"
import { ViewTransitions } from "next-view-transitions"
import { Inter as FontSans } from "next/font/google"

import { cn } from "@/lib/utils"

import { ICON_PATH, SITE_CONFIG } from "@/config/nangoConf"

import { ThemeProvider } from "@/components/themeProvider"
import { Toaster } from "@/components/ui/sonner"
import { TooltipProvider } from "@/components/ui/tooltip"

import "./globals.css"

const fontSans = FontSans({
  subsets: ["latin"],
  variable: "--font-sans",
})

export const metadata = {
  metadataBase: new URL(SITE_CONFIG.url.base),
  title: {
    default: SITE_CONFIG.name,
    template: `%s | ${SITE_CONFIG.name}`,
  },
  description: SITE_CONFIG.description,
  keywords: SITE_CONFIG.keywords,
  authors: [
    {
      name: SITE_CONFIG.author,
      url: SITE_CONFIG.url.author,
    },
  ],
  creator: SITE_CONFIG.author,
  openGraph: {
    type: "website",
    locale: "en_US",
    url: SITE_CONFIG.url.base,
    title: SITE_CONFIG.name,
    description: SITE_CONFIG.description,
    siteName: SITE_CONFIG.name,
    images: [
      {
        url: `/og-image.png`,
        width: 1200,
        height: 630,
        alt: SITE_CONFIG.name,
        type: "image/jpeg",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: SITE_CONFIG.name,
    description: SITE_CONFIG.description,
    images: [`/og-twitter.png`],
    creator: [""],
  },
  icons: {
    icon: ICON_PATH,
  },
}

export const viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "white" },
    { media: "(prefers-color-scheme: dark)", color: "black" },
  ],
}

interface RootLayoutProps {
  children: React.ReactNode
}

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <>
      <html lang="en" suppressHydrationWarning>
        <body
          className={cn(
            "bg-background min-h-screen font-sans antialiased",
            fontSans.variable,
          )}
        >
          <ThemeProvider attribute="class" defaultTheme="light" enableSystem>
            <TooltipProvider>
              <ViewTransitions>
                <PublicEnvScript />
                {children}
              </ViewTransitions>
            </TooltipProvider>
            <Toaster />
          </ThemeProvider>
        </body>
      </html>
    </>
  )
}
