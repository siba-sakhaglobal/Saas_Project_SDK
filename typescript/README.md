# Sakha MicroSite CMS - TypeScript SDK

Production-grade TypeScript SDK for Sakha MicroSite CMS API with full type safety and comprehensive API coverage.

## Features

- **Full TypeScript Support**: Strict type checking, branded types (UUID, DateTime, Money)
- **ESM and CommonJS**: Dual build targets for maximum compatibility
- **Zero External Dependencies**: Uses native `fetch` API (no axios or other HTTP libraries)
- **Comprehensive API Coverage**: All 17 modules with CRUD operations and statistics
- **Dual Authentication**: API key+secret for admins, JWT tokens for end-users
- **Immutable Data Patterns**: Safe, functional API design
- **Timeout Support**: Configurable request timeouts
- **Error Handling**: Structured error responses with proper type safety

## Installation

```bash
npm install @sakha/cms-sdk
```

## Quick Start

### Admin/Tenant Operations (API Key Authentication)

```typescript
import SakhaCMS from '@sakha/cms-sdk';

const cms = new SakhaCMS({
  baseUrl: 'https://api.sakha.example.com',
  apiKey: 'your-api-key',
  apiSecret: 'your-api-secret',
});

// Set project ID for project-scoped operations
cms.setProjectId('project-uuid-here');

// List blog posts
const { posts, pagination } = await cms.blog.listPosts({
  projectId: 'project-uuid',
  limit: 10,
  page: 1,
});

// Create a blog post
const newPost = await cms.blog.createPost({
  projectId: 'project-uuid',
  title: 'My First Post',
  slug: 'my-first-post',
  content: 'Post content here',
  authorId: 'author-uuid',
  status: 'draft',
});

// Update a blog post
const updated = await cms.blog.updatePost('post-id', {
  status: 'published',
  title: 'Updated Title',
});

// Delete a blog post
await cms.blog.deletePost('post-id');

// Get statistics
const stats = await cms.blog.getStats();
```

### End-User Operations (JWT Token)

```typescript
import SakhaCMS from '@sakha/cms-sdk';

// Register new user
const cms = new SakhaCMS({
  baseUrl: 'https://api.sakha.example.com',
});

const { token, user } = await cms.users.register({
  email: 'user@example.com',
  password: 'secure-password',
  name: 'John Doe',
});

// Login existing user
const loginResult = await cms.users.login({
  email: 'user@example.com',
  password: 'secure-password',
});

// Use token for authenticated requests
const cmsAuth = new SakhaCMS({
  baseUrl: 'https://api.sakha.example.com',
  token: loginResult.token,
});

// Get user profile
const profile = await cmsAuth.users.getProfile();

// Update profile
await cmsAuth.users.updateProfile({
  name: 'Updated Name',
  phone: '+1234567890',
});
```

## Modules

The SDK provides the following modules:

### Content Management
- `cms.blog` - Blog posts and categories
- `cms.events` - Events and event categories
- `cms.donations` - Donation campaigns
- `cms.team` - Team members

### E-Commerce
- `cms.products` - Products with categories, tags, variants
- `cms.services` - Services with duration and pricing
- `cms.orders` - Customer orders
- `cms.shipments` - Order shipments and tracking
- `cms.vendors` - Vendor management

### Transactions
- `cms.invoices` - Invoice management
- `cms.transactions` - Payment transactions
- `cms.appointments` - Service appointments

### System
- `cms.banners` - Marketing banners
- `cms.media` - File management (S3 integration)
- `cms.analytics` - Website analytics
- `cms.users` - End-user authentication and profiles
- `cms.userGroups` - User group management

## API Documentation

### Blog Module

```typescript
// List posts with filters
const { posts, pagination } = await cms.blog.listPosts({
  projectId: 'uuid',
  search: 'keyword',
  status: 'published',
  category: 'tech',
  limit: 20,
  page: 1,
});

// Get single post
const post = await cms.blog.getPost('post-id');

// Create post
const newPost = await cms.blog.createPost({
  projectId: 'uuid',
  title: 'Title',
  slug: 'slug',
  content: 'Content',
  authorId: 'author-uuid',
  category: 'tech',
  status: 'draft',
  tags: ['tag1', 'tag2'],
  viewCount: 0,
  commentCount: 0,
  shareCount: 0,
});

// Update post
const updated = await cms.blog.updatePost('post-id', {
  title: 'Updated Title',
  status: 'published',
});

// Delete post
await cms.blog.deletePost('post-id');

// Get statistics
const stats = await cms.blog.getStats();
```

### Products Module

```typescript
// List products
const { products, pagination } = await cms.products.listProducts({
  search: 'search term',
  category: 'category-uuid',
  status: 'active',
  featured: true,
  limit: 20,
  page: 1,
});

// Create product
const product = await cms.products.createProduct({
  name: 'Product Name',
  slug: 'product-slug',
  priceCents: 9999, // $99.99
  currency: 'USD',
  status: 'draft',
  featured: false,
  stockQuantity: 100,
  trackInventory: true,
});

// Product categories
const categories = await cms.products.listCategories();
await cms.products.createCategory({
  name: 'Category',
  slug: 'category',
});

// Product variants
const variants = await cms.products.listVariants('product-id');
await cms.products.createVariant('product-id', {
  title: 'Variant Title',
  sku: 'SKU-123',
});

// Product images
const images = await cms.products.listImages('product-id');
await cms.products.createImage('product-id', {
  url: 'https://example.com/image.jpg',
  isPrimary: true,
});
```

### Orders and Transactions

```typescript
// Orders
const { orders, pagination } = await cms.orders.listOrders({
  status: 'confirmed',
  limit: 20,
});
const order = await cms.orders.getOrder('order-id');
const orderStats = await cms.orders.getStats();

// Invoices
const { invoices, pagination } = await cms.invoices.listInvoices({
  status: 'paid',
});
const invoiceStats = await cms.invoices.getStats();

// Transactions
const { transactions, pagination } = await cms.transactions.listTransactions({
  status: 'completed',
  paymentMethod: 'card',
});
const transStats = await cms.transactions.getStats();

// Shipments
const { shipments, pagination } = await cms.shipments.listShipments({
  status: 'delivered',
  carrier: 'UPS',
});
const shipmentStats = await cms.shipments.getStats();
```

### Media Management

```typescript
// List media files
const { files, pagination } = await cms.media.listFiles({
  type: 'image',
  search: 'keyword',
  limit: 50,
});

// Upload file to S3
const { uploadUrl, key } = await cms.media.presignUpload({
  filename: 'my-image.jpg',
  contentType: 'image/jpeg',
  expiresInSec: 900, // 15 minutes
});

// Upload using fetch
const response = await fetch(uploadUrl, {
  method: 'PUT',
  body: fileBuffer,
  headers: {
    'Content-Type': 'image/jpeg',
  },
});

// Register file in database
const mediaFile = await cms.media.registerFile({
  fileName: 'my-image.jpg',
  fileType: 'image',
  mimeType: 'image/jpeg',
  sizeBytes: 102400,
  s3Key: key,
  url: 'https://cdn.example.com/my-image.jpg',
});

// Download file
const { downloadUrl } = await cms.media.presignDownload({
  key: mediaFile.s3Key,
  expiresInSec: 3600,
});

// Delete file
await cms.media.deleteFile('file-id');

// Bulk delete
await cms.media.bulkDelete({
  ids: ['id1', 'id2', 'id3'],
});

// Get media stats
const stats = await cms.media.getStats();
```

### Analytics

```typescript
// Get overview (visitors, pageviews, bounce rate)
const overview = await cms.analytics.getOverview({
  timeRange: '30d', // 7d, 30d, 90d, 1y
});

// Get traffic sources (Google, Facebook, Direct, etc.)
const traffic = await cms.analytics.getTraffic({
  timeRange: '30d',
});

// Get conversion events
const events = await cms.analytics.getEvents({
  timeRange: '30d',
});

// Get full dashboard
const dashboard = await cms.analytics.getDashboard({
  timeRange: '30d',
});
```

### User Groups

```typescript
// List groups
const groups = await cms.userGroups.listGroups();

// Create group
const group = await cms.userGroups.createGroup({
  name: 'Doctors',
  slug: 'doctors',
  color: '#FF0000',
});

// Get tree (compact view)
const tree = await cms.userGroups.getTree();

// Create subgroup
const subgroup = await cms.userGroups.createSubgroup('group-id', {
  name: 'Surgeons',
  slug: 'surgeons',
});

// Assign user to group
await cms.userGroups.assignUser({
  userId: 'user-id',
  groupId: 'group-id',
  subgroupId: 'subgroup-id',
});

// Bulk assign users
await cms.userGroups.bulkAssignUsers({
  userIds: ['id1', 'id2', 'id3'],
  groupId: 'group-id',
});
```

## Authentication

### API Key + Secret (Admin/Tenant)

Used for server-to-server authentication with admin/tenant privileges:

```typescript
const cms = new SakhaCMS({
  baseUrl: 'https://api.example.com',
  apiKey: 'sk_...',
  apiSecret: 'secret_...',
});
```

The SDK will automatically compute HMAC-SHA256 signatures for all requests.

### JWT Token (End-User)

Used for end-user authentication after login:

```typescript
const { token } = await cms.users.login({
  email: 'user@example.com',
  password: 'password',
});

const cms = new SakhaCMS({
  baseUrl: 'https://api.example.com',
  token: token,
});
```

## Project Scoping

Most endpoints require `X-Project-Id` header. Set it once and reuse:

```typescript
cms.setProjectId('project-uuid');

// All subsequent requests will include the header
const posts = await cms.blog.listPosts();
const events = await cms.events.listEvents();

// Clear when switching projects
cms.clearProjectId();
```

Or pass it per-request:

```typescript
const posts = await cms.blog.listPosts({
  projectId: 'different-project-uuid',
});
```

## Type Safety

All responses are fully typed:

```typescript
import type { BlogPost, Order, MediaFile } from '@sakha/cms-sdk';

// Types are automatically inferred
const posts: BlogPost[] = (await cms.blog.listPosts()).posts;
const order: Order = await cms.orders.getOrder('order-id');
const media: MediaFile = await cms.media.getFile('file-id');
```

## Error Handling

The SDK provides structured error handling:

```typescript
import { SakhaCMS, ApiError } from '@sakha/cms-sdk';

try {
  const post = await cms.blog.createPost({
    projectId: 'uuid',
    title: 'Title',
    slug: 'slug',
    content: 'Content',
  });
} catch (error) {
  if (error instanceof ApiError) {
    console.error('API Error:', error.status, error.message);
    console.error('Details:', error.details);
  } else {
    console.error('Unknown error:', error);
  }
}
```

## Configuration

```typescript
interface SakhaCMSConfig {
  // Required
  baseUrl: string;

  // Authentication (choose one)
  apiKey?: string;
  apiSecret?: string;
  token?: string;

  // Optional
  timeout?: number;        // Default: 30000ms
  headers?: Record<string, string>;
}
```

## Response Format

All successful API responses follow this format:

```typescript
interface ApiResponse<T> {
  success: boolean;
  data: T;
  error: string | null;
  metadata?: {
    total?: number;
    page?: number;
    limit?: number;
  };
}
```

Errors follow this format:

```typescript
interface ErrorResponse {
  success: false;
  data: null;
  error: string;
  details?: Record<string, string[]>;
}
```

## Building from Source

```bash
# Install dependencies
npm install

# Build ESM and CJS
npm run build

# Type check
npm run type-check

# Test
npm test
```

## Browser Usage

This SDK works in modern browsers with native `fetch` support:

```html
<script type="module">
  import SakhaCMS from '@sakha/cms-sdk';

  const cms = new SakhaCMS({
    baseUrl: 'https://api.sakha.example.com',
    token: 'user-jwt-token',
  });

  const profile = await cms.users.getProfile();
  console.log(profile);
</script>
```

## License

MIT

## Support

For issues, feature requests, or documentation updates, please contact the Sakha team.
