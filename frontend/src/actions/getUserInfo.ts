import axiosInstance from "@/api/axios"
import { UserDetail } from "@/api/nango_front/ts_types/UserDetail"

export default async function getUserInfo(): Promise<UserDetail> {
  const res = await axiosInstance.get("/api/user/")
  return res.data
}
