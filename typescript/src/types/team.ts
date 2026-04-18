import { DateTime, UUID } from './common';

/**
 * Team member response object
 */
export interface TeamMember {
  id: UUID;
  name: string;
  designation: string | null;
  bio: string | null;
  about: string | null;
  avatar_url: string | null;
  avatar: string | null;
  email: string | null;
  phone: string | null;
  social_links: any | null;
  category: string | null;
  sort_order: number | null;
  active: boolean;
  created_at: DateTime;
  updated_at: DateTime;
}

/**
 * Create team member request body
 */
export interface CreateTeamMemberBody {
  name: string;
  designation?: string | null;
  bio?: string | null;
  about?: string | null;
  avatarUrl?: string | null;
  avatar_url?: string | null;
  email?: string | null;
  phone?: string | null;
  socialLinks?: any | null;
  social_links?: any | null;
  category?: string | null;
  sortOrder?: number | null;
  sort_order?: number | null;
  active?: boolean;
}

/**
 * Update team member request body
 */
export interface UpdateTeamMemberBody {
  name?: string;
  designation?: string | null;
  bio?: string | null;
  about?: string | null;
  avatarUrl?: string | null;
  avatar_url?: string | null;
  email?: string | null;
  phone?: string | null;
  socialLinks?: any | null;
  social_links?: any | null;
  category?: string | null;
  sortOrder?: number | null;
  sort_order?: number | null;
  active?: boolean;
}

/**
 * Team member list query parameters
 */
export interface TeamMemberListParams {
  category?: string;
  active?: boolean;
  search?: string;
  limit?: number;
  page?: number;
}

/**
 * Team member statistics response
 */
export interface TeamMemberStats {
  total: number;
  active: number;
  inactive: number;
}
