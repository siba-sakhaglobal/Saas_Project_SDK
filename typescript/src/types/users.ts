import { DateTime, UUID } from './common';

/**
 * End-user response object (profile and basic info)
 */
export interface EndUser {
  id: UUID;
  email: string;
  name: string;
  phone: string | null;
  avatar: string | null;
  groupId: UUID | null;
  subgroupId: UUID | null;
  status: 'active' | 'inactive' | 'suspended';
  emailVerified: boolean;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * End-user registration request body
 */
export interface RegisterEndUserBody {
  email: string;
  password: string;
  name: string;
  phone?: string | null;
  groupId?: UUID | null;
  subgroupId?: UUID | null;
  metaJson?: any | null;
}

/**
 * End-user login request body
 */
export interface LoginEndUserBody {
  email: string;
  password: string;
}

/**
 * End-user login response body
 */
export interface LoginEndUserResponse {
  token: string;
  user: EndUser;
}

/**
 * Update end-user profile request body
 */
export interface UpdateEndUserProfileBody {
  name?: string;
  phone?: string | null;
  avatar?: string | null;
  groupId?: UUID | null;
  subgroupId?: UUID | null;
}

/**
 * Change password request body
 */
export interface ChangePasswordBody {
  currentPassword: string;
  newPassword: string;
}

/**
 * Request password reset body
 */
export interface RequestPasswordResetBody {
  email: string;
}

/**
 * Reset password request body
 */
export interface ResetPasswordBody {
  token: string;
  newPassword: string;
}

/**
 * End-user list query parameters
 */
export interface EndUserListParams {
  search?: string;
  status?: 'active' | 'inactive' | 'suspended';
  groupId?: UUID;
  subgroupId?: UUID;
  emailVerified?: boolean;
  limit?: number;
  page?: number;
}

/**
 * End-user statistics response
 */
export interface EndUserStats {
  total: number;
  active: number;
  inactive: number;
  suspended: number;
  emailVerified: number;
  emailUnverified: number;
}
