import { create } from "zustand"

type UserState = {
  data?: { name: string; email: string; avatar?: string }
  getState: () => { name: string; email: string; avatar?: string } | undefined
  // eslint-disable-next-line unused-imports/no-unused-vars
  setState: (data: { name: string; email: string; avatar?: string }) => void
}

export const useUserState = create<UserState>((set) => ({
  data: undefined,
  getState: () => {
    const data = localStorage.getItem("userData")
    if (data) {
      return JSON.parse(data)
    }
    return undefined
  },
  setState: (data) => {
    set({ data })
    localStorage.setItem("userData", JSON.stringify(data))
  },
}))
