import { HttpClient } from '../client';
import type {
  Event,
  EventCategory,
  CreateEventBody,
  UpdateEventBody,
  CreateEventCategoryBody,
  UpdateEventCategoryBody,
  EventListParams,
  EventStats,
} from '../types/events';
import type { PaginationMetadata } from '../types/common';

export class EventsModule {
  constructor(private client: HttpClient) {}

  /**
   * List events with pagination and filters
   */
  async listEvents(params?: EventListParams): Promise<{
    events: Event[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      events: Event[];
      pagination: PaginationMetadata;
    }>('/api/events', { params });
    return response;
  }

  /**
   * Get a single event by ID
   */
  async getEvent(id: string): Promise<Event> {
    return this.client.get<Event>(`/api/events/${id}`);
  }

  /**
   * Create a new event
   */
  async createEvent(body: CreateEventBody): Promise<Event> {
    return this.client.post<Event>('/api/events', body);
  }

  /**
   * Update an event
   */
  async updateEvent(id: string, body: UpdateEventBody): Promise<Event> {
    return this.client.put<Event>(`/api/events/${id}`, body);
  }

  /**
   * Delete an event
   */
  async deleteEvent(id: string): Promise<void> {
    await this.client.delete(`/api/events/${id}`);
  }

  /**
   * Get event statistics
   */
  async getStats(): Promise<EventStats> {
    return this.client.get<EventStats>('/api/events/stats');
  }

  /**
   * List event categories
   */
  async listCategories(): Promise<EventCategory[]> {
    return this.client.get<EventCategory[]>('/api/events/categories');
  }

  /**
   * Get a single event category
   */
  async getCategory(id: string): Promise<EventCategory> {
    return this.client.get<EventCategory>(`/api/events/categories/${id}`);
  }

  /**
   * Create an event category
   */
  async createCategory(body: CreateEventCategoryBody): Promise<EventCategory> {
    return this.client.post<EventCategory>('/api/events/categories', body);
  }

  /**
   * Update an event category
   */
  async updateCategory(
    id: string,
    body: UpdateEventCategoryBody
  ): Promise<EventCategory> {
    return this.client.put<EventCategory>(`/api/events/categories/${id}`, body);
  }

  /**
   * Delete an event category
   */
  async deleteCategory(id: string): Promise<void> {
    await this.client.delete(`/api/events/categories/${id}`);
  }
}
