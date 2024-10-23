import { Bell, LucideProps } from "lucide-react"
import { ForwardRefExoticComponent, RefAttributes } from "react"
import { create } from "zustand"

const IconNameMapping = {
  Bell: Bell,
}

export type SideBarHeadOption = {
  title: string
  icon: keyof typeof IconNameMapping
  subtitle: string
}
export type SideBarHeadOptionWithReactIcon = {
  title: string
  iconName: keyof typeof IconNameMapping
  icon: ForwardRefExoticComponent<
    Omit<LucideProps, "ref"> & RefAttributes<SVGSVGElement>
  >
  subtitle: string
}

type SideBarHeadState = {
  data: SideBarHeadOption | undefined
  getState: () => SideBarHeadOptionWithReactIcon | undefined
  // eslint-disable-next-line unused-imports/no-unused-vars
  setState: (data: SideBarHeadOption) => void
}

export const useSideBarState = create<SideBarHeadState>((set) => ({
  data: undefined,
  getState: () => {
    const data = localStorage.getItem("sidebarState")
    if (data) {
      const parsed: SideBarHeadOption = JSON.parse(data)
      const icon = IconNameMapping[parsed.icon]
      return { ...parsed, icon: icon, iconName: parsed.icon }
    }
    return undefined
  },
  setState: (data) => {
    set({ data })
    localStorage.setItem("sidebarState", JSON.stringify(data))
  },
}))
