import { MetadataRoute } from "next"

import { BASE_URL } from "@/config/nangoConf"

export default function sitemap(): MetadataRoute.Sitemap {
  return [{ url: BASE_URL, lastModified: new Date(), priority: 1 }]
}
