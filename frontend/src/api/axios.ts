import axios from "axios"

import { BASE_API_URL } from "@/lib/constants"

import signOut from "@/actions/signOut"

// Add the baseURL to the request
const axiosInstance = axios.create({
  baseURL: BASE_API_URL,
})

// Add the access token (if it exist) to the request
axiosInstance.interceptors.request.use((request) => {
  if (localStorage.getItem("access")) {
    request.headers.Authorization = `Bearer ${localStorage.getItem("access")}`
  }
  if (request.url && !request.url.endsWith("/")) {
    request.url += "/"
  }
  return request
})

// Ask for new tokens if the current access token expired and replay the request
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    const { config } = error
    if (
      error.response?.status === 401 &&
      !error.request.responseURL.endsWith("/api/token/") &&
      !config.retry
    ) {
      config.retry = true

      const refresh = localStorage.getItem("refresh")

      axios
        .post(`${BASE_API_URL}api/token/refresh/`, { refresh: refresh })
        .then((response) => {
          localStorage.setItem("access", response.data?.access)
          config.headers.Authorization = `Bearer ${response.data?.access}`
        })
        .catch(async (error) => {
          await signOut()
          window.location.href = "/login"
        })
    } else {
      return error.response
    }
  },
)

export default axiosInstance
