import { AppointmentStatus, DateTime, UUID } from './common';

/**
 * Appointment response object
 */
export interface Appointment {
  id: UUID;
  serviceId: UUID;
  serviceName: string | null;
  customerName: string;
  customerEmail: string;
  customerPhone: string | null;
  scheduledAt: DateTime;
  endAt: DateTime | null;
  durationMins: number | null;
  status: AppointmentStatus;
  notes: string | null;
  location: string | null;
  assignedTo: string | null;
  metaJson: any | null;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Create appointment request body
 */
export interface CreateAppointmentBody {
  projectId: UUID;
  serviceId: UUID;
  customerName: string;
  customerEmail: string;
  customerPhone?: string | null;
  scheduledAt: DateTime;
  endAt?: DateTime | null;
  durationMins?: number | null;
  status?: AppointmentStatus;
  notes?: string | null;
  location?: string | null;
  assignedTo?: string | null;
  metaJson?: any | null;
}

/**
 * Update appointment request body
 */
export interface UpdateAppointmentBody {
  serviceId?: UUID;
  customerName?: string;
  customerEmail?: string;
  customerPhone?: string | null;
  scheduledAt?: DateTime;
  endAt?: DateTime | null;
  durationMins?: number | null;
  status?: AppointmentStatus;
  notes?: string | null;
  location?: string | null;
  assignedTo?: string | null;
  metaJson?: any | null;
}

/**
 * Appointment list query parameters
 */
export interface AppointmentListParams {
  projectId?: UUID;
  search?: string;
  status?: AppointmentStatus;
  serviceId?: UUID;
  from?: DateTime;
  to?: DateTime;
  limit?: number;
  page?: number;
}

/**
 * Appointment statistics response
 */
export interface AppointmentStats {
  total: number;
  scheduled: number;
  confirmed: number;
  completed: number;
  cancelled: number;
}
