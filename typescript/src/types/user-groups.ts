import { DateTime, UUID } from './common';

/**
 * User subgroup response object
 */
export interface UserSubgroup {
  id: UUID;
  groupId: UUID;
  name: string;
  slug: string;
  description: string | null;
  sortOrder: number;
  active: boolean;
  userCount?: number;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * User group response object
 */
export interface UserGroup {
  id: UUID;
  name: string;
  slug: string;
  description: string | null;
  color: string;
  sortOrder: number;
  active: boolean;
  userCount: number;
  subgroups: UserSubgroup[];
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * User group tree response (compact)
 */
export interface UserGroupTree {
  id: UUID;
  name: string;
  slug: string;
  color: string;
  userCount: number;
  subgroups: Array<{
    id: UUID;
    name: string;
    slug: string;
  }>;
}

/**
 * Create user group request body
 */
export interface CreateUserGroupBody {
  name: string;
  slug?: string;
  description?: string | null;
  color?: string;
  sortOrder?: number;
  active?: boolean;
}

/**
 * Update user group request body
 */
export interface UpdateUserGroupBody {
  name?: string;
  slug?: string;
  description?: string | null;
  color?: string;
  sortOrder?: number;
  active?: boolean;
}

/**
 * Create user subgroup request body
 */
export interface CreateUserSubgroupBody {
  name: string;
  slug?: string;
  description?: string | null;
  sortOrder?: number;
  active?: boolean;
}

/**
 * Update user subgroup request body
 */
export interface UpdateUserSubgroupBody {
  name?: string;
  slug?: string;
  description?: string | null;
  sortOrder?: number;
  active?: boolean;
}

/**
 * Assign user to group request body
 */
export interface AssignUserToGroupBody {
  userId: UUID;
  groupId?: UUID | null;
  subgroupId?: UUID | null;
}

/**
 * Bulk assign users request body
 */
export interface BulkAssignUsersBody {
  userIds: UUID[];
  groupId?: UUID | null;
  subgroupId?: UUID | null;
}

/**
 * User group list query parameters
 */
export interface UserGroupListParams {
  active?: boolean;
}

/**
 * User group statistics response
 */
export interface UserGroupStats {
  total: number;
  active: number;
  inactive: number;
  totalUsers: number;
}
