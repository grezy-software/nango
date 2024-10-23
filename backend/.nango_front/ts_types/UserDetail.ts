
export type UserDetail = {
  id: number;
  last_login: Date;
  is_superuser: boolean;
  username: string;
  first_name: string;
  last_name: string;
  is_staff: boolean;
  is_active: boolean;
  email: string;
  created_at: Date;
  groups: number[];
  };