import { create } from "zustand"

type BreadcrumbState = {
  data: { name: string; url: string }[]
  // eslint-disable-next-line unused-imports/no-unused-vars
  setState: (data: { name: string; url: string }[]) => void
}

export const useBreadcrumbState = create<BreadcrumbState>((set) => ({
  data: [],
  setState: (data) => set({ data }),
}))
