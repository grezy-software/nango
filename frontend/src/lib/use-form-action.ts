import { FieldValues, UseFormProps, useForm } from "react-hook-form"

export function useFormAction<
  TFieldValues extends FieldValues = FieldValues,
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  TContext = any,
  TTransformedValues extends FieldValues | undefined = undefined,
>(props?: UseFormProps<TFieldValues, TContext>) {
  const form = useForm<TFieldValues, TContext, TTransformedValues>(props)

  // eslint-disable-next-line unused-imports/no-unused-vars
  const submitAction = (onAction: (formData: TFieldValues) => void) => {
    if (form.formState.isValid) {
      return { action: () => onAction(form.getValues()) }
    }
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    return { onSubmit: form.handleSubmit(onAction as any) }
  }

  return {
    ...form,
    submitAction,
  }
}
