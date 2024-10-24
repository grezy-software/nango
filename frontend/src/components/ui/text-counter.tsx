import { useInView, useMotionValue, useSpring } from "framer-motion"
import { useEffect, useRef } from "react"

export default function TextCounter({
  value,
  direction = "up",
}: {
  value: number
  direction?: "up" | "down"
}) {
  const ref = useRef<HTMLSpanElement>(null)
  const motionValue = useMotionValue(direction === "down" ? value : 0)
  const springValue = useSpring(motionValue, {
    damping: 50,
    stiffness: 100,
  })
  const isInView = useInView(ref, { once: true, margin: "-100px" })

  useEffect(() => {
    if (isInView) {
      motionValue.set(direction === "down" ? 0 : value)
    }
  }, [motionValue, isInView, direction, value])

  useEffect(
    () =>
      springValue.on("change", (latest) => {
        if (ref.current) {
          ref.current.textContent = Intl.NumberFormat("en-US").format(
            Number(latest.toFixed(0)),
          )
        }
      }),
    [springValue],
  )

  return <span ref={ref} />
}