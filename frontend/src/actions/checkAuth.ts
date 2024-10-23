import axiosInstance from "@/api/axios"

export default async function checkAuth() {
  try {
    const res = await axiosInstance.post("/api/token/verify/", {
      token: localStorage.getItem("access"),
    })

    if (res && res.status === 200) {
      return { success: true }
    }
    return {
      success: false,
    }
  } catch {
    return {
      success: false,
    }
  }
}
