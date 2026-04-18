import { HttpClient } from '../client';
import type {
  TeamMember,
  CreateTeamMemberBody,
  UpdateTeamMemberBody,
  TeamMemberListParams,
  TeamMemberStats,
} from '../types/team';
import type { PaginationMetadata } from '../types/common';

export class TeamModule {
  constructor(private client: HttpClient) {}

  /**
   * List team members with pagination and filters
   */
  async listMembers(params?: TeamMemberListParams): Promise<{
    members: TeamMember[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      members: TeamMember[];
      pagination: PaginationMetadata;
    }>('/api/team', { params });
    return response;
  }

  /**
   * Get a single team member by ID
   */
  async getMember(id: string): Promise<TeamMember> {
    return this.client.get<TeamMember>(`/team/${id}`);
  }

  /**
   * Create a new team member
   */
  async createMember(body: CreateTeamMemberBody): Promise<TeamMember> {
    return this.client.post<TeamMember>('/api/team', body);
  }

  /**
   * Update a team member
   */
  async updateMember(id: string, body: UpdateTeamMemberBody): Promise<TeamMember> {
    return this.client.put<TeamMember>(`/team/${id}`, body);
  }

  /**
   * Delete a team member
   */
  async deleteMember(id: string): Promise<void> {
    await this.client.delete(`/team/${id}`);
  }

  /**
   * Get team member statistics
   */
  async getStats(): Promise<TeamMemberStats> {
    return this.client.get<TeamMemberStats>('/api/team/stats');
  }
}
