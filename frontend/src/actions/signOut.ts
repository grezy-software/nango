export default async function signOut() {
  localStorage.removeItem("access")
  localStorage.removeItem("refresh")
  return {
    success: true,
  }
}
