"use client"

import { motion, stagger, useAnimate } from "framer-motion"
import { useEffect } from "react"

import { cn } from "@/lib/utils"

export const TextGenerateEffect = ({
  words,
  className,
}: {
  words: string
  className?: string
}) => {
  const [scope, animate] = useAnimate()
  const wordsArray = words.split(" ")
  useEffect(() => {
    animate(
      "span",
      {
        opacity: 1,
      },
      {
        duration: 2,
        delay: stagger(0.05),
      },
    )
  }, [animate])

  const renderWords = () => {
    return (
      <motion.div ref={scope}>
        {wordsArray.map((word, idx) => {
          return (
            <motion.span
              key={word + idx}
              className={cn("text-white opacity-0", className)}
            >
              {word}{" "}
            </motion.span>
          )
        })}
      </motion.div>
    )
  }

  return <div className={className}>{renderWords()}</div>
}
