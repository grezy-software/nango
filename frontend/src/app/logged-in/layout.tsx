import { SITE_CONFIG } from "@/config/nangoConf"

import { SidebarProvider } from "@/components/ui/sidebar"

import AppSideBar from "./sidebar"

export const metadata = {
  title: `${SITE_CONFIG.name} | Logged In`,
}
export default function LoggedIn({ children }: { children: React.ReactNode }) {
  return (
    <>
      <SidebarProvider>
        <AppSideBar />
      </SidebarProvider>
      <main>{children}</main>
    </>
  )
}
