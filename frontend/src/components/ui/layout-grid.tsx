"use client"

import { motion } from "framer-motion"
import React, { useState } from "react"

import { cn } from "@/lib/utils"

type Card = {
  id: number
  title: string
  description: string
  price: number
  className: string
  thumbnail: string
}

const ExitImage = ({
  handleClick,
  handleOutsideClick,
  card,
  selected,
  lastSelected,
}: {
  handleClick: (card: Card) => void
  handleOutsideClick: () => void
  card: Card
  selected: Card | null
  lastSelected: Card | null
}) => {
  return (
    <div className={cn(card.className, "cursor-pointer")}>
      <motion.div
        onClick={() => {
          handleClick(card)
        }}
        onBlur={(e) => console.log(e)}
        className={cn(
          card.className,
          "relative overflow-hidden",
          selected?.id === card.id
            ? "absolute inset-0 z-50 m-auto flex h-1/2 w-full cursor-pointer flex-col flex-wrap items-center justify-center rounded-lg md:w-1/2"
            : lastSelected?.id === card.id
              ? "bg-background z-40 size-full rounded-xl"
              : "bg-background size-full rounded-xl",
        )}
        layoutId={`card-${card.id}`}
      >
        {selected?.id === card.id && <SelectedCard selected={selected} />}
        <ImageComponent card={card} />
      </motion.div>
    </div>
  )
}

export const LayoutGrid = ({ cards }: { cards: Card[] }) => {
  const [selected, setSelected] = useState<Card | null>(null)
  const [lastSelected, setLastSelected] = useState<Card | null>(null)

  const handleClick = (card: Card) => {
    setLastSelected(selected)
    setSelected(card)
  }

  const handleOutsideClick = () => {
    setLastSelected(selected)
    setSelected(null)
  }

  return (
    <div className="relative mx-auto grid size-full max-w-7xl  grid-cols-1 gap-4 md:grid-cols-3">
      {cards.map((card, i) => (
        <ExitImage
          key={i}
          handleClick={handleClick}
          handleOutsideClick={handleOutsideClick}
          card={card}
          selected={selected}
          lastSelected={lastSelected}
        />
      ))}
      <motion.div
        onClick={handleOutsideClick}
        className={cn(
          "absolute left-0 top-0 z-10 size-full opacity-0",
          selected?.id ? "pointer-events-auto" : "pointer-events-none",
        )}
        animate={{ opacity: selected?.id ? 0.3 : 0 }}
      />
    </div>
  )
}

const ImageComponent = ({ card }: { card: Card }) => {
  return (
    <motion.img
      layoutId={`image-${card.id}-image`}
      src={card.thumbnail}
      height="500"
      width="500"
      className={cn(
        "absolute inset-0 size-full object-cover object-top transition duration-200",
      )}
      alt="thumbnail"
    />
  )
}

const SelectedCard = ({ selected }: { selected: Card | null }) => {
  return (
    <div className="relative z-[60] flex size-full flex-col justify-end rounded-lg bg-transparent shadow-2xl">
      <motion.div
        initial={{
          opacity: 0,
        }}
        animate={{
          opacity: 0.6,
        }}
        className="absolute inset-0 z-10 size-full bg-black opacity-60"
      />
      <motion.div
        layoutId={`content-${selected?.id}`}
        initial={{
          opacity: 0,
          y: 100,
        }}
        animate={{
          opacity: 1,
          y: 0,
        }}
        exit={{
          opacity: 0,
          y: 100,
        }}
        transition={{
          duration: 0.3,
          ease: "easeInOut",
        }}
        className="relative z-[70] px-8 pb-4"
      >
        <p className="text-xl font-bold text-white md:text-4xl">
          {selected?.title}
        </p>
        <button
          className="group/button text-background relative inline-flex size-7 items-center justify-center overflow-hidden rounded-full font-medium transition-all duration-300 hover:w-32"
          onClick={async () => {}}
        >
          <p className="inline-flex whitespace-nowrap text-xs opacity-0 transition-all duration-200 group-hover/button:-translate-x-2.5 group-hover/button:opacity-100">
            Ajouter au panier
          </p>
          <div className="absolute right-1.5">
            <svg
              viewBox="0 0 15 15"
              xmlns="http://www.w3.org/2000/svg"
              className="fill-background size-4"
            >
              <path d="M8.14645 3.14645C8.34171 2.95118 8.65829 2.95118 8.85355 3.14645L12.8536 7.14645C13.0488 7.34171 13.0488 7.65829 12.8536 7.85355L8.85355 11.8536C8.65829 12.0488 8.34171 12.0488 8.14645 11.8536C7.95118 11.6583 7.95118 11.3417 8.14645 11.1464L11.2929 8H2.5C2.22386 8 2 7.77614 2 7.5C2 7.22386 2.22386 7 2.5 7H11.2929L8.14645 3.85355C7.95118 3.65829 7.95118 3.34171 8.14645 3.14645Z"></path>
            </svg>
          </div>
        </button>
        <p className="text-muted my-4 max-w-lg text-base font-normal">
          {selected?.description}
        </p>
        <p className="text-muted-foreground my-4 max-w-lg text-base">
          {selected?.price}€
        </p>
      </motion.div>
    </div>
  )
}
