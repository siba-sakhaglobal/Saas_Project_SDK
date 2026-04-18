# SaaS Project SDK

Multi-language SDK for the SaaS Project CMS API. Provides project-scoped access to all CMS modules — blog, events, donations, orders, invoices, products, media, analytics, and more.

> **IMPORTANT: Using Claude Code?** Clone the [SaaS Project Admin](https://github.com/siba-sakhaglobal/Saas_Project_Admin) repo instead — it includes a **Claude Code Skill file** that automatically teaches Claude about this entire platform. Just tell Claude what you want to build and it will set up the SDK, interview you about requirements, and build the frontend. See the [Admin repo README](https://github.com/siba-sakhaglobal/Saas_Project_Admin#build-your-own-website-with-claude-code) for example prompts.

## Get API Credentials

Before using the SDK, you need an API Key and Secret:

1. Visit **https://sakhaglobal.com** and request a project
2. You'll receive an API Key (`sk_live_...`) and Secret (`sec_...`)
3. The key is scoped to one project — all data access goes through it

## Available SDKs

| Language | Directory | Package Name | Status |
|----------|-----------|-------------|--------|
| **JavaScript** | [`/javascript`](./javascript) | `@sakha/cms-sdk-js` | Ready |
| **TypeScript** | [`/typescript`](./typescript) | `@sakha/cms-sdk` | Ready |
| **Python** | [`/python`](./python) | `sakha-cms` | Ready |
| **PHP** | [`/php`](./php) | `sakha/cms-sdk` | Ready |

## Quick Start

### JavaScript (Browser / Node.js)

```bash
npm install @sakha/cms-sdk-js
```

```javascript
import { SakhaCMS } from '@sakha/cms-sdk-js';

const cms = new SakhaCMS({
  baseUrl: 'https://your-cms-api.example.com',
  apiKey: 'sk_live_xxx',
  apiSecret: 'sec_yyy',
});

// List blog posts
const { data } = await cms.blog.list({ page: 1, limit: 10 });

// Create an order
const { data: order } = await cms.orders.create({
  customerName: 'John Doe',
  items: [{ name: 'Widget', quantity: 2, priceCents: 1500 }],
});
```

### TypeScript

```bash
npm install @sakha/cms-sdk
```

```typescript
import { SakhaCMS } from '@sakha/cms-sdk';

const cms = new SakhaCMS({
  baseUrl: 'https://your-cms-api.example.com',
  apiKey: 'sk_live_xxx',
  apiSecret: 'sec_yyy',
});

const { data } = await cms.blog.list({ page: 1, limit: 10, status: 'published' });
```

### Python

```bash
pip install sakha-cms
```

```python
from sakha_cms import SakhaCMS

cms = SakhaCMS(
    base_url="https://your-cms-api.example.com",
    api_key="sk_live_xxx",
    api_secret="sec_yyy",
)

# Sync
data = cms.blog.get_posts(limit=10)

# Async
data = await cms.blog.get_posts_async(limit=10)

cms.close()
```

### PHP

```bash
composer require sakha/cms-sdk
```

```php
use Sakha\CMS\SakhaCMS;

$cms = new SakhaCMS('sk_live_xxx', 'sec_yyy', 'https://your-cms-api.example.com');

$posts = $cms->blog()->listPosts(['page' => 1, 'limit' => 10]);
$stats = $cms->analytics()->overview(['timeRange' => '30d']);
```

## Authentication

The SDK supports two authentication modes:

### 1. API Key + Secret (Machine Auth)

For server-to-server or project-scoped access. The API key is created in the CMS admin panel and scoped to a specific project.

```
Authorization: Bearer sk_live_xxx:sec_yyy
```

### 2. JWT + API Key (End-User Auth)

For site visitors who register/login. The JWT identifies the user; the API key identifies the project.

```
Authorization: Bearer <end_user_jwt>
X-Api-Key: sk_live_xxx
```

## Available Modules

| Module | SDK Property | Description |
|--------|-------------|-------------|
| Blog | `cms.blog` | Posts, categories, authors, stats |
| Events | `cms.events` | Events, categories, stats |
| Donations | `cms.donations` | Campaigns, donations, stats |
| Products | `cms.products` | Products, categories, tags, attributes |
| Services | `cms.services` | Service catalog |
| Appointments | `cms.appointments` | Scheduling |
| Orders | `cms.orders` | Order management |
| Invoices | `cms.invoices` | Invoice management |
| Transactions | `cms.transactions` | Payment tracking |
| Shipments | `cms.shipments` | Delivery tracking |
| Vendors | `cms.vendors` | Vendor directory |
| Banners | `cms.banners` | Banner/slider management |
| Team | `cms.team` | Team member profiles |
| Media | `cms.media` | File uploads, S3 presigned URLs |
| Users | `cms.users` | End-user register/login/profile |
| Analytics | `cms.analytics` | Traffic, content, donation analytics |
| User Groups | `cms.userGroups` | User group hierarchy |

## Response Format

All SDK methods return `{ data, meta }`:

```javascript
const { data, meta } = await cms.blog.list({ page: 1, limit: 10 });
// data = { posts: [...] }
// meta = { total: 42, page: 1, limit: 10 }
```

## Error Handling

```javascript
import { SdkError } from '@sakha/cms-sdk-js';

try {
  await cms.blog.get('nonexistent-id');
} catch (err) {
  if (err instanceof SdkError) {
    console.log(err.status);   // 404
    console.log(err.message);  // "not found"
    console.log(err.details);  // { code: "not_found", ... }
  }
}
```

## License

MIT
