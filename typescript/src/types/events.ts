import { EventStatus, CategoryInfo, DateTime, UUID } from './common';

/**
 * Event response object
 */
export interface Event {
  id: UUID;
  title: string;
  slug: string;
  description: string | null;
  content: string | null;
  location: string | null;
  venue: string | null;
  event_date: DateTime;
  event_time: string;
  end_date: DateTime | null;
  end_time: string | null;
  image: string | null;
  image_url: string | null;
  featured_image: string | null;
  category: CategoryInfo | null;
  status: EventStatus;
  is_featured: boolean;
  max_participants: number | null;
  registration_count: number;
  registration_fee: number;
  contact_person: string | null;
  contact_email: string | null;
  contact_phone: string | null;
  visibility: string;
  tags: string[];
  created_at: DateTime;
  updated_at: DateTime;
}

/**
 * Event category response object
 */
export interface EventCategory {
  id: UUID;
  name: string;
  color: string;
  sortOrder: number;
}

/**
 * Create event request body
 */
export interface CreateEventBody {
  projectId?: UUID;
  title: string;
  slug?: string;
  description?: string;
  content?: string;
  location?: string;
  venue?: string;
  event_date: DateTime;
  event_time?: string;
  end_date?: DateTime;
  end_time?: string;
  image_id?: string | null;
  category?: string | null;
  status?: EventStatus;
  max_participants?: number | null;
  registration_fee?: number | null;
  contact_person?: string | null;
  contact_email?: string | null;
  contact_phone?: string | null;
  is_featured?: boolean;
  tags?: string[];
}

/**
 * Update event request body
 */
export interface UpdateEventBody {
  title?: string;
  slug?: string;
  description?: string;
  content?: string;
  location?: string;
  venue?: string;
  event_date?: DateTime;
  event_time?: string;
  end_date?: DateTime;
  end_time?: string;
  image_id?: string | null;
  category?: string | null;
  status?: EventStatus;
  max_participants?: number | null;
  registration_fee?: number | null;
  contact_person?: string | null;
  contact_email?: string | null;
  contact_phone?: string | null;
  is_featured?: boolean;
  tags?: string[];
}

/**
 * Create event category request body
 */
export interface CreateEventCategoryBody {
  name: string;
  color?: string;
  sortOrder?: number;
}

/**
 * Update event category request body
 */
export interface UpdateEventCategoryBody {
  name?: string;
  color?: string;
  sortOrder?: number;
}

/**
 * Event list query parameters
 */
export interface EventListParams {
  projectId?: UUID;
  search?: string;
  status?: EventStatus;
  category?: string;
  limit?: number;
  page?: number;
}

/**
 * Event statistics response
 */
export interface EventStats {
  total: number;
  upcoming: number;
  ongoing: number;
  completed: number;
  cancelled: number;
  totalRegistrations: number;
}
