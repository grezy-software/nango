import { Link } from "next-view-transitions"

import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export default function FreeTrial() {
  return (
    <div className="mt-auto md:fixed md:bottom-0 md:left-0 md:z-10 md:w-[220px] md:p-4 lg:w-[280px]">
      <Card>
        <CardHeader className="p-4">
          <CardTitle>Free Trial</CardTitle>
          <CardDescription>
            Until the official launch, you can use all of our features for free.
          </CardDescription>
        </CardHeader>
        <CardContent className="p-4 pt-0">
          <Link href="/pricing">
            <Button size="sm" className="w-full">
              View Pricing
            </Button>
          </Link>
        </CardContent>
      </Card>
    </div>
  )
}
