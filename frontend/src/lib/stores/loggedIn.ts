import { create } from "zustand"

type LoggedInState = {
  data: boolean
  // eslint-disable-next-line unused-imports/no-unused-vars
  setState: (data: boolean) => void
}

export const useLoggedInState = create<LoggedInState>((set) => ({
  data: false,
  setState: (data) => set({ data }),
}))
