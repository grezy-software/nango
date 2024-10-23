export type ServerActionResponse<zod_T, prisma_T> = {
  success: boolean
  errors?: z.typeToFlattenedError<zod_T> | string
  data?: prisma_T
}
