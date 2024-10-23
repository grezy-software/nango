import { MetadataRoute } from "next"

import {
  BACKGROUND_COLOR,
  ICON_PATH,
  ICON_TYPE,
  SITE_DESCRIPTION,
  SITE_NAME,
  SITE_SHORT_NAME,
  THEME_COLOR,
} from "@/config/nangoConf"

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: SITE_NAME,
    short_name: SITE_SHORT_NAME,
    description: SITE_DESCRIPTION,
    start_url: "/",
    display: "standalone",
    background_color: BACKGROUND_COLOR,
    theme_color: THEME_COLOR,
    icons: [
      {
        src: ICON_PATH,
        sizes: "1562x1562",
        type: ICON_TYPE,
      },
    ],
  }
}
