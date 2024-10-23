"use client"

import {
  Bell,
  ChevronRight,
  ChevronsUpDown,
  LogOut,
  LucideProps,
  Plus,
  Sparkles,
} from "lucide-react"
import { Link } from "next-view-transitions"
import * as React from "react"
import {
  ForwardRefExoticComponent,
  RefAttributes,
  useEffect,
  useState,
} from "react"

import { BASE_LOGGED_IN_URL } from "@/lib/constants"
import { useBreadcrumbState } from "@/lib/stores/breadcrumb"
import {
  SideBarHeadOptionWithReactIcon,
  useSideBarState,
} from "@/lib/stores/sidebarHead"
import { useUserState } from "@/lib/stores/user"

import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Separator } from "@/components/ui/separator"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarInset,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
  SidebarRail,
  SidebarTrigger,
  useSidebar,
} from "@/components/ui/sidebar"

type SideBarSettings = {
  header: {
    name: string
    options: SideBarHeadOptionWithReactIcon[]
    addOption?: {
      text: string
    }
  }
  sections: {
    title: string
    subSections: {
      title: string
      url: string
      defaultOpen: boolean
      icon?: ForwardRefExoticComponent<
        Omit<LucideProps, "ref"> & RefAttributes<SVGSVGElement>
      >
      subSubSections?: {
        icon?: ForwardRefExoticComponent<
          Omit<LucideProps, "ref"> & RefAttributes<SVGSVGElement>
        >
        url: string
        title: string
      }[]
    }[]
  }[]
}

export default function AppSideBar() {
  const [sideBarSettings, setSideBarSettings] = useState<SideBarSettings>()
  const user = useUserState()
  const userState = user.getState()
  const breadcrumb = useBreadcrumbState()
  const sidebarHead = useSideBarState()
  const sidebarHeadState = sidebarHead.getState()
  const sidebar = useSidebar()
  useEffect(() => {
    setSideBarSettings({
      header: {
        name: "Test",
        options: [
          {
            title: "Test",
            subtitle: "sub",
            iconName: "Bell",
            icon: Bell,
          },
        ],
      },
      sections: [
        {
          title: "Example",
          subSections: [
            {
              title: "Subsection1",
              url: BASE_LOGGED_IN_URL + "/1",
              defaultOpen: true,
              icon: Bell,
              subSubSections: [
                {
                  title: "SubSubSection1",
                  url: BASE_LOGGED_IN_URL,
                },
                {
                  title: "SubSubSection2",
                  url: BASE_LOGGED_IN_URL,
                  icon: Bell,
                },
              ],
            },
            {
              title: "Subsection2",
              url: BASE_LOGGED_IN_URL,
              defaultOpen: false,
            },
          ],
        },
      ],
    })
    sidebarHead.setState({
      title: "Test",
      subtitle: "sub",
      icon: "Bell",
    })
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])
  useEffect(() => {
    breadcrumb.setState([{ name: "Test", url: "/" }])
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])
  console.log(sidebar)
  return (
    <>
      {sideBarSettings && (
        <>
          <Sidebar collapsible="icon">
            {sidebarHeadState && (
              <SidebarHeader>
                <SidebarMenu>
                  <SidebarMenuItem>
                    <DropdownMenu>
                      <DropdownMenuTrigger asChild>
                        <SidebarMenuButton
                          size="lg"
                          className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
                        >
                          <div className="bg-sidebar-primary text-sidebar-primary-foreground flex aspect-square size-8 items-center justify-center rounded-lg">
                            <sidebarHeadState.icon className="size-4" />
                          </div>
                          <div className="grid flex-1 text-left text-sm leading-tight">
                            <span className="truncate font-semibold">
                              {sidebarHeadState.title}
                            </span>
                            <span className="truncate text-xs">
                              {sidebarHeadState.subtitle}
                            </span>
                          </div>
                          <ChevronsUpDown className="ml-auto" />
                        </SidebarMenuButton>
                      </DropdownMenuTrigger>
                      <DropdownMenuContent
                        className="w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg"
                        align="start"
                        side="bottom"
                        sideOffset={4}
                      >
                        <DropdownMenuLabel className="text-muted-foreground text-xs">
                          {sideBarSettings.header.name}
                        </DropdownMenuLabel>
                        {sideBarSettings.header.options.map((option, index) => (
                          <DropdownMenuItem
                            key={index}
                            onClick={() =>
                              sidebarHead.setState({
                                ...option,
                                icon: option.iconName,
                              })
                            }
                            className="gap-2 p-2"
                          >
                            <div className="flex size-6 items-center justify-center rounded-sm border">
                              <option.icon className="size-4 shrink-0" />
                            </div>
                            {option.title}
                          </DropdownMenuItem>
                        ))}
                        {sideBarSettings.header.addOption && (
                          <>
                            <DropdownMenuSeparator />
                            <DropdownMenuItem className="gap-2 p-2">
                              <div className="bg-background flex size-6 items-center justify-center rounded-md border">
                                <Plus className="size-4" />
                              </div>
                              <div className="text-muted-foreground font-medium">
                                {sideBarSettings.header.addOption.text}
                              </div>
                            </DropdownMenuItem>
                          </>
                        )}
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </SidebarMenuItem>
                </SidebarMenu>
              </SidebarHeader>
            )}
            <SidebarContent>
              {sideBarSettings.sections.map((section, index) => (
                <SidebarGroup key={index}>
                  <SidebarGroupLabel>{section.title}</SidebarGroupLabel>
                  <SidebarMenu>
                    {section.subSections.map((subsection, index) => {
                      return (
                        <div key={index}>
                          {subsection.subSubSections &&
                          subsection.subSubSections?.length > 0 ? (
                            <Collapsible
                              key={index}
                              asChild
                              defaultOpen={subsection.defaultOpen}
                              className="group/collapsible"
                            >
                              <SidebarMenuItem>
                                <CollapsibleTrigger asChild>
                                  <SidebarMenuButton
                                    onClick={() => sidebar.setOpen(true)}
                                    tooltip={subsection.title}
                                  >
                                    {subsection.icon && (
                                      <subsection.icon className="size-4" />
                                    )}
                                    <span>{subsection.title}</span>
                                    <ChevronRight className="ml-auto transition-transform duration-200 group-data-[state=open]/collapsible:rotate-90" />
                                  </SidebarMenuButton>
                                </CollapsibleTrigger>
                                <CollapsibleContent>
                                  <SidebarMenuSub>
                                    {subsection.subSubSections?.map(
                                      (subSubsection, index) => (
                                        <SidebarMenuSubItem key={index}>
                                          <SidebarMenuSubButton asChild>
                                            <Link href={subSubsection.url}>
                                              {subSubsection.icon && (
                                                <subSubsection.icon className="size-4" />
                                              )}
                                              <span>{subSubsection.title}</span>
                                            </Link>
                                          </SidebarMenuSubButton>
                                        </SidebarMenuSubItem>
                                      ),
                                    )}
                                  </SidebarMenuSub>
                                </CollapsibleContent>
                              </SidebarMenuItem>
                            </Collapsible>
                          ) : (
                            <SidebarMenuItem key={index}>
                              <Link href={subsection.url}>
                                <SidebarMenuButton tooltip={subsection.title}>
                                  {subsection.icon && (
                                    <subsection.icon className="size-4" />
                                  )}
                                  <span>{subsection.title}</span>
                                </SidebarMenuButton>
                              </Link>
                            </SidebarMenuItem>
                          )}
                        </div>
                      )
                    })}
                  </SidebarMenu>
                </SidebarGroup>
              ))}
            </SidebarContent>
            {userState && (
              <SidebarFooter>
                <SidebarMenu>
                  <SidebarMenuItem>
                    <DropdownMenu>
                      <DropdownMenuTrigger asChild>
                        <SidebarMenuButton
                          size="lg"
                          className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
                        >
                          <Avatar className="size-8 rounded-lg">
                            <AvatarImage
                              src={userState.avatar}
                              alt={userState.name}
                            />
                            <AvatarFallback className="rounded-lg">
                              {userState.name[0].toUpperCase()}
                            </AvatarFallback>
                          </Avatar>
                          <div className="grid flex-1 text-left text-sm leading-tight">
                            <span className="truncate font-semibold">
                              {userState.name}
                            </span>
                            <span className="truncate text-xs">
                              {userState.email}
                            </span>
                          </div>
                          <ChevronsUpDown className="ml-auto size-4" />
                        </SidebarMenuButton>
                      </DropdownMenuTrigger>
                      <DropdownMenuContent
                        className="w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg"
                        side="bottom"
                        align="end"
                        sideOffset={4}
                      >
                        <DropdownMenuLabel className="p-0 font-normal">
                          <div className="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
                            <Avatar className="size-8 rounded-lg">
                              <AvatarImage
                                src={userState.avatar}
                                alt={userState.name}
                              />
                              <AvatarFallback className="rounded-lg">
                                {userState.name[0].toUpperCase()}
                              </AvatarFallback>
                            </Avatar>
                            <div className="grid flex-1 text-left text-sm leading-tight">
                              <span className="truncate font-semibold">
                                {userState.name}
                              </span>
                              <span className="truncate text-xs">
                                {userState.email}
                              </span>
                            </div>
                          </div>
                        </DropdownMenuLabel>
                        <DropdownMenuSeparator />
                        <DropdownMenuGroup>
                          <DropdownMenuItem>
                            <Sparkles className="mr-2 size-4" />
                            Upgrade to Pro
                          </DropdownMenuItem>
                        </DropdownMenuGroup>
                        <DropdownMenuItem>
                          <LogOut className="mr-2 size-4" />
                          Log out
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </SidebarMenuItem>
                </SidebarMenu>
              </SidebarFooter>
            )}
            <SidebarRail />
          </Sidebar>
          <SidebarInset>
            <header className="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-[[data-collapsible=icon]]/sidebar-wrapper:h-12">
              <div className="flex items-center gap-2 px-4">
                <SidebarTrigger className="size-4" />
                <Separator orientation="vertical" className="mr-2 h-4" />
                <Breadcrumb>
                  <BreadcrumbList>
                    {breadcrumb.data.map((elem, index) => (
                      <div key={index}>
                        <BreadcrumbItem className="hidden md:block">
                          {index !== breadcrumb.data.length - 1 ? (
                            <BreadcrumbLink href={elem.url}>
                              {elem.name}
                            </BreadcrumbLink>
                          ) : (
                            <BreadcrumbPage>{elem.name}</BreadcrumbPage>
                          )}
                        </BreadcrumbItem>
                        {index !== breadcrumb.data.length - 1 && (
                          <BreadcrumbSeparator className="hidden md:block" />
                        )}
                      </div>
                    ))}
                  </BreadcrumbList>
                </Breadcrumb>
              </div>
            </header>
          </SidebarInset>
        </>
      )}
    </>
  )
}
