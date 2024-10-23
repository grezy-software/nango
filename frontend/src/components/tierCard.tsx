"use client"

import { CheckIcon } from "lucide-react"
import { AppRouterInstance } from "next/dist/shared/lib/app-router-context.shared-runtime"
import { useRouter } from "next/navigation"

import { cn } from "@/lib/utils"

import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

import { Badge } from "./ui/badge"

export type TierCardComponentProps = {
  className?: string
  cta: string
  description: React.ReactNode
  additionalInfo?: React.ReactNode
  features: string[]
  mostPopular?: boolean
  badge?: string
  name: string
  price: string
  priceSuffix?: string
  onClick?: (router: AppRouterInstance) => void
}

export default function TierCardComponent({
  className,
  cta,
  description,
  additionalInfo,
  features,
  mostPopular = false,
  badge,
  name,
  price,
  priceSuffix,
  onClick,
}: TierCardComponentProps) {
  const router = useRouter()
  return (
    <Card
      className={cn(
        "w-3/4",
        mostPopular && "ring-primary dark:bg-border/50 ring-2",
        className,
      )}
    >
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle
            className={cn(
              "text-lg font-semibold",
              mostPopular && "text-primary",
            )}
          >
            {name}
          </CardTitle>

          {mostPopular && badge && <Badge>{badge}</Badge>}
        </div>

        <CardDescription>{description}</CardDescription>
      </CardHeader>

      <CardContent className="flex flex-col justify-between">
        <p className={"flex items-baseline gap-x-1"}>
          <span className="text-4xl font-bold tracking-tight">{price}</span>

          {priceSuffix && (
            <span className="text-muted-foreground text-sm font-semibold">
              {priceSuffix}
            </span>
          )}
        </p>
        {additionalInfo && (
          <div className="text-muted-foreground text-sm">{additionalInfo}</div>
        )}
        <ul className="space-y-3 pt-6">
          {features.map((feature) => (
            <li
              key={feature}
              className="text-muted-foreground flex items-center gap-x-3 text-sm"
            >
              <CheckIcon
                aria-hidden="true"
                className="text-primary dark:text-foreground size-5 flex-none"
              />

              {feature}
            </li>
          ))}
        </ul>
      </CardContent>
      <CardFooter className="flex">
        <Button
          className="w-full"
          onClick={() => {
            if (onClick) {
              onClick(router)
            }
          }}
        >
          {cta}
        </Button>
      </CardFooter>
    </Card>
  )
}
