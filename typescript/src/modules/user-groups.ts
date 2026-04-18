import { HttpClient } from '../client';
import type {
  UserGroup,
  UserGroupTree,
  UserSubgroup,
  CreateUserGroupBody,
  UpdateUserGroupBody,
  CreateUserSubgroupBody,
  UpdateUserSubgroupBody,
  AssignUserToGroupBody,
  BulkAssignUsersBody,
  UserGroupListParams,
  UserGroupStats,
} from '../types/user-groups';

export class UserGroupsModule {
  constructor(private client: HttpClient) {}

  /**
   * List all user groups with subgroups
   */
  async listGroups(params?: UserGroupListParams): Promise<UserGroup[]> {
    return this.client.get<UserGroup[]>('/api/user-groups', { params });
  }

  /**
   * Get a single user group with subgroups
   */
  async getGroup(id: string): Promise<UserGroup> {
    return this.client.get<UserGroup>(`/user-groups/${id}`);
  }

  /**
   * Create a new user group
   */
  async createGroup(body: CreateUserGroupBody): Promise<UserGroup> {
    return this.client.post<UserGroup>('/api/user-groups', body);
  }

  /**
   * Update a user group
   */
  async updateGroup(id: string, body: UpdateUserGroupBody): Promise<UserGroup> {
    return this.client.put<UserGroup>(`/user-groups/${id}`, body);
  }

  /**
   * Delete a user group (cascades subgroups)
   */
  async deleteGroup(id: string): Promise<void> {
    await this.client.delete(`/user-groups/${id}`);
  }

  /**
   * Get full group tree (compact view)
   */
  async getTree(): Promise<UserGroupTree[]> {
    return this.client.get<UserGroupTree[]>('/api/user-groups/tree');
  }

  // Subgroup operations

  /**
   * Create a subgroup under a group
   */
  async createSubgroup(
    groupId: string,
    body: CreateUserSubgroupBody
  ): Promise<UserSubgroup> {
    return this.client.post<UserSubgroup>(
      `/user-groups/${groupId}/subgroups`,
      body
    );
  }

  /**
   * Update a subgroup
   */
  async updateSubgroup(id: string, body: UpdateUserSubgroupBody): Promise<UserSubgroup> {
    return this.client.put<UserSubgroup>(`/user-groups/subgroups/${id}`, body);
  }

  /**
   * Delete a subgroup
   */
  async deleteSubgroup(id: string): Promise<void> {
    await this.client.delete(`/user-groups/subgroups/${id}`);
  }

  // User assignment operations

  /**
   * Assign a user to group/subgroup
   */
  async assignUser(body: AssignUserToGroupBody): Promise<void> {
    await this.client.post('/api/user-groups/assign', body);
  }

  /**
   * Bulk assign multiple users to group/subgroup
   */
  async bulkAssignUsers(body: BulkAssignUsersBody): Promise<void> {
    await this.client.post('/api/user-groups/bulk-assign', body);
  }

  /**
   * Seed default "Users" group for project
   */
  async seedDefaultGroup(): Promise<UserGroup> {
    return this.client.post<UserGroup>('/api/user-groups/seed-default', {});
  }

  /**
   * Get user groups statistics
   */
  async getStats(): Promise<UserGroupStats> {
    return this.client.get<UserGroupStats>('/api/user-groups/stats');
  }
}
