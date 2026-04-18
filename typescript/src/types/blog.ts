import { PostStatus, Author, CategoryInfo, DateTime, UUID } from './common';

/**
 * Blog post response object
 */
export interface BlogPost {
  id: UUID;
  title: string;
  slug: string;
  excerpt: string | null;
  content: string | null;
  featured_image: string | null;
  status: PostStatus;
  is_featured: boolean;
  author: Author;
  category: CategoryInfo | null;
  category_name: string | null;
  tags: string[];
  view_count: number;
  comment_count: number;
  share_count: number;
  published_at: DateTime | null;
  created_at: DateTime;
  updated_at: DateTime;
}

/**
 * Blog category response object
 */
export interface BlogCategory {
  id: UUID | null;
  name: string;
  slug: string;
  color: string;
  sortOrder: number;
  postCount?: number;
}

/**
 * Create blog post request body
 */
export interface CreatePostBody {
  projectId: UUID;
  title: string;
  slug?: string;
  excerpt?: string | null;
  content?: string | null;
  featured_image?: string | null;
  status?: PostStatus;
  tags?: string[] | null;
  is_featured?: boolean;
  published_at?: DateTime | null;
  author_name?: string | null;
}

/**
 * Update blog post request body
 */
export interface UpdatePostBody {
  title?: string;
  slug?: string;
  excerpt?: string | null;
  content?: string | null;
  featured_image?: string | null;
  status?: PostStatus;
  tags?: string[] | null;
  is_featured?: boolean;
  published_at?: DateTime | null;
  author_name?: string | null;
}

/**
 * Create blog category request body
 */
export interface CreateCategoryBody {
  name: string;
  slug?: string;
  color?: string;
  sortOrder?: number;
}

/**
 * Update blog category request body
 */
export interface UpdateCategoryBody {
  name?: string;
  slug?: string;
  color?: string;
  sortOrder?: number;
}

/**
 * Blog post list query parameters
 */
export interface BlogListParams {
  projectId: UUID;
  search?: string;
  status?: PostStatus;
  category?: string;
  author?: string;
  date?: string;
  tab?: string;
  limit?: number;
  page?: number;
}

/**
 * Blog statistics response
 */
export interface BlogStats {
  total: number;
  published: number;
  drafts: number;
  archived: number;
}

/**
 * Blog author info
 */
export interface BlogAuthor {
  id: number;
  name: string;
  role: string;
}
