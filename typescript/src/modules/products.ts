import { HttpClient } from '../client';
import type {
  Product,
  ProductCategory,
  ProductTag,
  ProductAttribute,
  ProductVariant,
  ProductImage,
  CreateProductBody,
  UpdateProductBody,
  CreateProductCategoryBody,
  UpdateProductCategoryBody,
  CreateProductTagBody,
  CreateProductAttributeBody,
  CreateProductImageBody,
  CreateProductVariantBody,
  ProductListParams,
  ProductStats,
} from '../types/products';
import type { PaginationMetadata } from '../types/common';

export class ProductsModule {
  constructor(private client: HttpClient) {}

  /**
   * List products with pagination and filters
   */
  async listProducts(params?: ProductListParams): Promise<{
    products: Product[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      products: Product[];
      pagination: PaginationMetadata;
    }>('/api/products', { params });
    return response;
  }

  /**
   * Get a single product by ID
   */
  async getProduct(id: string): Promise<Product> {
    return this.client.get<Product>(`/products/${id}`);
  }

  /**
   * Create a new product
   */
  async createProduct(body: CreateProductBody): Promise<Product> {
    return this.client.post<Product>('/api/products', body);
  }

  /**
   * Update a product
   */
  async updateProduct(id: string, body: UpdateProductBody): Promise<Product> {
    return this.client.put<Product>(`/products/${id}`, body);
  }

  /**
   * Delete a product
   */
  async deleteProduct(id: string): Promise<void> {
    await this.client.delete(`/products/${id}`);
  }

  /**
   * Get product statistics
   */
  async getStats(): Promise<ProductStats> {
    return this.client.get<ProductStats>('/api/products/stats');
  }

  // Category operations

  /**
   * List product categories
   */
  async listCategories(): Promise<ProductCategory[]> {
    return this.client.get<ProductCategory[]>('/api/products/categories');
  }

  /**
   * Get a single category
   */
  async getCategory(id: string): Promise<ProductCategory> {
    return this.client.get<ProductCategory>(`/products/categories/${id}`);
  }

  /**
   * Create a product category
   */
  async createCategory(body: CreateProductCategoryBody): Promise<ProductCategory> {
    return this.client.post<ProductCategory>('/api/products/categories', body);
  }

  /**
   * Update a product category
   */
  async updateCategory(
    id: string,
    body: UpdateProductCategoryBody
  ): Promise<ProductCategory> {
    return this.client.put<ProductCategory>(`/products/categories/${id}`, body);
  }

  /**
   * Delete a product category
   */
  async deleteCategory(id: string): Promise<void> {
    await this.client.delete(`/products/categories/${id}`);
  }

  // Tag operations

  /**
   * List product tags
   */
  async listTags(): Promise<ProductTag[]> {
    return this.client.get<ProductTag[]>('/api/products/tags');
  }

  /**
   * Get a single tag
   */
  async getTag(id: string): Promise<ProductTag> {
    return this.client.get<ProductTag>(`/products/tags/${id}`);
  }

  /**
   * Create a product tag
   */
  async createTag(body: CreateProductTagBody): Promise<ProductTag> {
    return this.client.post<ProductTag>('/api/products/tags', body);
  }

  /**
   * Delete a product tag
   */
  async deleteTag(id: string): Promise<void> {
    await this.client.delete(`/products/tags/${id}`);
  }

  // Attribute operations

  /**
   * List product attributes
   */
  async listAttributes(): Promise<ProductAttribute[]> {
    return this.client.get<ProductAttribute[]>('/api/products/attributes');
  }

  /**
   * Get a single attribute
   */
  async getAttribute(id: string): Promise<ProductAttribute> {
    return this.client.get<ProductAttribute>(`/products/attributes/${id}`);
  }

  /**
   * Create a product attribute
   */
  async createAttribute(body: CreateProductAttributeBody): Promise<ProductAttribute> {
    return this.client.post<ProductAttribute>('/api/products/attributes', body);
  }

  /**
   * Delete a product attribute
   */
  async deleteAttribute(id: string): Promise<void> {
    await this.client.delete(`/products/attributes/${id}`);
  }

  // Image operations

  /**
   * List product images
   */
  async listImages(productId: string): Promise<ProductImage[]> {
    return this.client.get<ProductImage[]>(`/products/${productId}/images`);
  }

  /**
   * Create a product image
   */
  async createImage(productId: string, body: CreateProductImageBody): Promise<ProductImage> {
    return this.client.post<ProductImage>(`/products/${productId}/images`, body);
  }

  /**
   * Delete a product image
   */
  async deleteImage(productId: string, imageId: string): Promise<void> {
    await this.client.delete(`/products/${productId}/images/${imageId}`);
  }

  // Variant operations

  /**
   * List product variants
   */
  async listVariants(productId: string): Promise<ProductVariant[]> {
    return this.client.get<ProductVariant[]>(`/products/${productId}/variants`);
  }

  /**
   * Get a single variant
   */
  async getVariant(productId: string, variantId: string): Promise<ProductVariant> {
    return this.client.get<ProductVariant>(`/products/${productId}/variants/${variantId}`);
  }

  /**
   * Create a product variant
   */
  async createVariant(
    productId: string,
    body: CreateProductVariantBody
  ): Promise<ProductVariant> {
    return this.client.post<ProductVariant>(`/products/${productId}/variants`, body);
  }

  /**
   * Delete a product variant
   */
  async deleteVariant(productId: string, variantId: string): Promise<void> {
    await this.client.delete(`/products/${productId}/variants/${variantId}`);
  }
}
