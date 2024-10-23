import axiosInstance from "@/api/axios"

export default async function getStripeCheckoutSession() {
  try {
    const res = await axiosInstance.get("/api/stripe/checkout_session/")
    return res.data.sessionUrl
  } catch {
    return {}
  }
}
