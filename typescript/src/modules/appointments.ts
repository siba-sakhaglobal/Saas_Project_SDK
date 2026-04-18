import { HttpClient } from '../client';
import type {
  Appointment,
  CreateAppointmentBody,
  UpdateAppointmentBody,
  AppointmentListParams,
  AppointmentStats,
} from '../types/appointments';
import type { PaginationMetadata } from '../types/common';

export class AppointmentsModule {
  constructor(private client: HttpClient) {}

  /**
   * List appointments with pagination and filters
   */
  async listAppointments(params?: AppointmentListParams): Promise<{
    appointments: Appointment[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      appointments: Appointment[];
      pagination: PaginationMetadata;
    }>('/api/project-appointments', { params });
    return response;
  }

  /**
   * Get a single appointment by ID
   */
  async getAppointment(id: string): Promise<Appointment> {
    return this.client.get<Appointment>(`/appointments/${id}`);
  }

  /**
   * Create a new appointment
   */
  async createAppointment(body: CreateAppointmentBody): Promise<Appointment> {
    return this.client.post<Appointment>('/api/project-appointments', body);
  }

  /**
   * Update an appointment
   */
  async updateAppointment(
    id: string,
    body: UpdateAppointmentBody
  ): Promise<Appointment> {
    return this.client.put<Appointment>(`/appointments/${id}`, body);
  }

  /**
   * Delete an appointment
   */
  async deleteAppointment(id: string): Promise<void> {
    await this.client.delete(`/appointments/${id}`);
  }

  /**
   * Get appointment statistics
   */
  async getStats(): Promise<AppointmentStats> {
    return this.client.get<AppointmentStats>('/api/project-appointments/stats');
  }
}
