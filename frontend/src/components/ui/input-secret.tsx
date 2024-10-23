import { Eye, EyeOff } from "lucide-react"
import { Dispatch, SetStateAction } from "react"

import { cn } from "@/lib/utils"

import { Button } from "./button"
import { FormControl } from "./form"
import { Input } from "./input"

export default function InputSecret({
  field,
  visible,
  setVisible,
  error = false,
  className = "",
}: {
  field: object & { value: string }
  visible: boolean
  setVisible: Dispatch<SetStateAction<boolean>>
  error?: boolean
  className?: string
}) {
  return (
    <div className={cn("flex flex-row space-x-2", className)}>
      <FormControl>
        <Input
          className={error ? (field.value ? "" : "border border-red-500") : ""}
          type={visible ? "text" : "password"}
          {...field}
        />
      </FormControl>
      <Button type="button" onClick={() => setVisible(!visible)}>
        {visible ? <Eye className="size-4" /> : <EyeOff className="size-4" />}
      </Button>
    </div>
  )
}
