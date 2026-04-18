import { Currency, Money, DateTime, UUID } from './common';

/**
 * Product category response object
 */
export interface ProductCategory {
  id: UUID;
  name: string;
  slug: string;
  description: string | null;
  image: string | null;
  parentId: UUID | null;
  sortOrder: number;
  active: boolean;
  childrenCount: number;
  children?: ProductCategory[];
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Product tag response object
 */
export interface ProductTag {
  id: UUID;
  name: string;
  slug: string;
  color: string | null;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Product attribute response object
 */
export interface ProductAttribute {
  id: UUID;
  key: string;
  label: string;
  type: 'text' | 'select' | 'number' | 'color' | 'boolean' | 'textarea';
  description: string | null;
  required: boolean;
  filterable: boolean;
  searchable: boolean;
  displayOnCard: boolean;
  options: string[] | null;
  active: boolean;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Product variant response object
 */
export interface ProductVariant {
  id: UUID;
  productId: UUID;
  title: string;
  sku: string | null;
  price: Money | null;
  stockQuantity: number | null;
  image: string | null;
  options: any | null;
  active: boolean;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Product image response object
 */
export interface ProductImage {
  id: UUID;
  productId: UUID;
  url: string;
  altText: string | null;
  isPrimary: boolean;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Product response object
 */
export interface Product {
  id: UUID;
  name: string;
  slug: string;
  sku: string | null;
  description: string | null;
  shortDescription: string | null;
  price: Money;
  compareAtPrice: Money | null;
  costPrice: Money | null;
  currency: Currency;
  status: 'draft' | 'active' | 'inactive' | 'archived';
  featured: boolean;
  imageUrl: string | null;
  trackInventory: boolean;
  stockQuantity: number;
  lowStockThreshold: number;
  allowBackorder: boolean;
  weight: number | null;
  length: number | null;
  width: number | null;
  height: number | null;
  seoTitle: string | null;
  seoDescription: string | null;
  seoKeywords: string | null;
  categories: Array<{ id: UUID }>;
  tags: Array<{ id: UUID }>;
  attributes: any[];
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Create product category request body
 */
export interface CreateProductCategoryBody {
  name: string;
  slug: string;
  description?: string | null;
  image?: string | null;
  parentId?: UUID | null;
  sortOrder?: number;
  active?: boolean;
}

/**
 * Update product category request body
 */
export interface UpdateProductCategoryBody {
  name?: string;
  slug?: string;
  description?: string | null;
  image?: string | null;
  parentId?: UUID | null;
  sortOrder?: number;
  active?: boolean;
}

/**
 * Create product request body
 */
export interface CreateProductBody {
  name: string;
  slug: string;
  sku?: string | null;
  description?: string | null;
  shortDescription?: string | null;
  priceCents: number;
  compareAtPriceCents?: number | null;
  costPriceCents?: number | null;
  currency?: Currency;
  status?: 'draft' | 'active' | 'inactive' | 'archived';
  featured?: boolean;
  trackInventory?: boolean;
  stockQuantity?: number;
  lowStockThreshold?: number;
  allowBackorder?: boolean;
  weight?: number | null;
  length?: number | null;
  width?: number | null;
  height?: number | null;
  seoTitle?: string | null;
  seoDescription?: string | null;
  seoKeywords?: string | null;
  categoryIds?: UUID[] | null;
  tagIds?: UUID[] | null;
  attributes?: any[] | null;
}

/**
 * Update product request body
 */
export interface UpdateProductBody {
  name?: string;
  slug?: string;
  sku?: string | null;
  description?: string | null;
  shortDescription?: string | null;
  priceCents?: number;
  compareAtPriceCents?: number | null;
  costPriceCents?: number | null;
  currency?: Currency;
  status?: 'draft' | 'active' | 'inactive' | 'archived';
  featured?: boolean;
  trackInventory?: boolean;
  stockQuantity?: number;
  lowStockThreshold?: number;
  allowBackorder?: boolean;
  weight?: number | null;
  length?: number | null;
  width?: number | null;
  height?: number | null;
  seoTitle?: string | null;
  seoDescription?: string | null;
  seoKeywords?: string | null;
  categoryIds?: UUID[] | null;
  tagIds?: UUID[] | null;
  attributes?: any[] | null;
}

/**
 * Create product tag request body
 */
export interface CreateProductTagBody {
  name: string;
  slug: string;
  color?: string | null;
}

/**
 * Create product attribute request body
 */
export interface CreateProductAttributeBody {
  key: string;
  label: string;
  type: 'text' | 'select' | 'number' | 'color' | 'boolean' | 'textarea';
  description?: string | null;
  required?: boolean;
  filterable?: boolean;
  searchable?: boolean;
  displayOnCard?: boolean;
  options?: string[] | null;
  active?: boolean;
}

/**
 * Create product image request body
 */
export interface CreateProductImageBody {
  url: string;
  altText?: string | null;
  isPrimary?: boolean;
}

/**
 * Create product variant request body
 */
export interface CreateProductVariantBody {
  title: string;
  sku?: string | null;
  priceCents?: number | null;
  stockQuantity?: number | null;
  image?: string | null;
  options?: any | null;
  active?: boolean;
}

/**
 * Product list query parameters
 */
export interface ProductListParams {
  search?: string;
  category?: UUID;
  status?: 'draft' | 'active' | 'inactive' | 'archived';
  featured?: boolean;
  limit?: number;
  page?: number;
}

/**
 * Product statistics response
 */
export interface ProductStats {
  total: number;
  active: number;
  draft: number;
  inactive: number;
  archived: number;
  featured: number;
}
