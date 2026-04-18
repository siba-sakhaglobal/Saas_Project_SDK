import { HttpClient } from '../client';
import type {
  BlogPost,
  BlogCategory,
  CreatePostBody,
  UpdatePostBody,
  CreateCategoryBody,
  UpdateCategoryBody,
  BlogListParams,
  BlogStats,
} from '../types/blog';
import type { ApiResponse, PaginationMetadata } from '../types/common';

export class BlogModule {
  constructor(private client: HttpClient) {}

  /**
   * List blog posts with pagination and filters
   */
  async listPosts(params?: BlogListParams): Promise<{
    posts: BlogPost[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      posts: BlogPost[];
      pagination: PaginationMetadata;
    }>('/api/blog', { params });
    return response;
  }

  /**
   * Get a single blog post by ID
   */
  async getPost(id: string): Promise<BlogPost> {
    return this.client.get<BlogPost>(`/api/blog/${id}`);
  }

  /**
   * Create a new blog post
   */
  async createPost(body: CreatePostBody): Promise<BlogPost> {
    return this.client.post<BlogPost>('/api/blog', body);
  }

  /**
   * Update a blog post
   */
  async updatePost(id: string, body: UpdatePostBody): Promise<BlogPost> {
    return this.client.put<BlogPost>(`/api/blog/${id}`, body);
  }

  /**
   * Delete a blog post
   */
  async deletePost(id: string): Promise<void> {
    await this.client.delete(`/api/blog/${id}`);
  }

  /**
   * Get blog statistics
   */
  async getStats(): Promise<BlogStats> {
    return this.client.get<BlogStats>('/api/blog/stats');
  }

  /**
   * List blog categories
   */
  async listCategories(): Promise<BlogCategory[]> {
    return this.client.get<BlogCategory[]>('/api/blog/categories');
  }

  /**
   * Get a single blog category
   */
  async getCategory(id: string): Promise<BlogCategory> {
    return this.client.get<BlogCategory>(`/api/blog/categories/${id}`);
  }

  /**
   * Create a blog category
   */
  async createCategory(body: CreateCategoryBody): Promise<BlogCategory> {
    return this.client.post<BlogCategory>('/api/blog/categories', body);
  }

  /**
   * Update a blog category
   */
  async updateCategory(
    id: string,
    body: UpdateCategoryBody
  ): Promise<BlogCategory> {
    return this.client.put<BlogCategory>(`/api/blog/categories/${id}`, body);
  }

  /**
   * Delete a blog category
   */
  async deleteCategory(id: string): Promise<void> {
    await this.client.delete(`/api/blog/categories/${id}`);
  }
}
