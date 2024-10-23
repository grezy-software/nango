import axiosInstance from "@/api/axios"

export default async function signIn({
  email,
  password,
}: {
  email: string
  password: string
}) {
  const res = await axiosInstance.post("/api/token/", {
    email,
    password,
  })

  if (res.status !== 200) {
    return {
      success: false,
    }
  }
  localStorage.setItem("access", res.data.access)
  localStorage.setItem("refresh", res.data.refresh)
  return {
    success: true,
  }
}
