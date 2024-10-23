import { cn } from "@/lib/utils"

export default function BackgroundGrid({
  children,
  className,
}: {
  children: React.ReactNode
  className?: string
}) {
  return (
    <div
      className={cn(
        "dark:bg-grid-white/[0.1] relative flex  w-full items-center justify-center",
        className,
      )}
    >
      {children}
      <div className="bg-background pointer-events-none absolute inset-0 flex items-center justify-center [mask-image:radial-gradient(ellipse_at_center,transparent_60%,black)]"></div>
    </div>
  )
}
