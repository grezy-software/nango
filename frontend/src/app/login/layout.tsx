import { SITE_CONFIG } from "@/config/nangoConf"

import Navbar from "@/components/layout/navbar"

export const metadata = {
  title: `${SITE_CONFIG.name} | Login`,
}

export default function Login({ children }: { children: React.ReactNode }) {
  return (
    <>
      <Navbar />
      <main className="container flex flex-col items-center py-8">
        {children}
      </main>
    </>
  )
}
