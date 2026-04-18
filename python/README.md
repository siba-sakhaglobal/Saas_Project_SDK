# Sakha MicroSite CMS Python SDK

Official Python SDK for Sakha MicroSite CMS backend.

## Installation

```bash
pip install sakha-cms
```

## Quick Start

```python
from sakha_cms import SakhaCMS

# Initialize client
cms = SakhaCMS(
    api_key="sk_live_xxx",
    api_secret="sec_yyy",
    base_url="https://api.example.com"
)

# Use sync methods
posts = cms.blog.list(project_id="project-uuid", limit=10)

# Or use async
import asyncio

async def main():
    posts = await cms.blog.list_async(project_id="project-uuid", limit=10)

asyncio.run(main())
```

## Authentication

The SDK supports two authentication modes:

### API Key + Secret (for backend services)
```python
cms = SakhaCMS(
    api_key="sk_live_xxx",
    api_secret="sec_yyy",
    base_url="https://api.example.com"
)
```

### End-user JWT (for user operations)
```python
cms = SakhaCMS(
    api_key="sk_live_xxx",  # API key
    jwt_token="eyJ...",     # End-user JWT
    base_url="https://api.example.com"
)
```

## Modules

- `cms.blog` - Blog posts and categories
- `cms.events` - Event management
- `cms.donations` - Donation campaigns and donations
- `cms.products` - Product management
- `cms.services` - Service management
- `cms.appointments` - Appointment scheduling
- `cms.orders` - Order management
- `cms.invoices` - Invoice management
- `cms.transactions` - Transaction tracking
- `cms.shipments` - Shipment tracking
- `cms.vendors` - Vendor management
- `cms.banners` - Banner management
- `cms.team` - Team member management
- `cms.users` - End-user management
- `cms.analytics` - Analytics and reporting
- `cms.media` - Media file management
- `cms.user_groups` - User group management

## Error Handling

```python
from sakha_cms import SakhaCMSError, NotFoundError, ValidationError, AuthError

try:
    post = cms.blog.get(id="post-id")
except NotFoundError:
    print("Post not found")
except ValidationError as e:
    print(f"Validation error: {e.details}")
except AuthError:
    print("Authentication failed")
except SakhaCMSError as e:
    print(f"SDK error: {e}")
```

## License

MIT
