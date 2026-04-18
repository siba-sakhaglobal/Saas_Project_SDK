# Sakha CMS PHP SDK

A comprehensive PHP SDK for the Sakha MicroSite CMS API. Provides full access to all CMS modules with strong typing, PSR-4 autoloading, and comprehensive error handling.

## Features

- **22 API Modules**: Complete coverage of Blog, Events, Donations, Orders, Invoices, Transactions, Services, Appointments, Vendors, Banners, Shipments, Products, Team, Members, End-User Admin, User Groups, Auth, Media, Settings, End Users, Analytics, and Tenant Designations
- **Strong Typing**: PHP 8.1+ with full type hints
- **Error Handling**: Custom exception hierarchy (SakhaCMSException, NotFoundException, ValidationException, AuthException)
- **Pagination Support**: Built-in pagination handling with metadata
- **Authentication**: Support for API key+secret and end-user JWT tokens
- **Guzzle HTTP Client**: Reliable, battle-tested HTTP library

## Installation

```bash
composer require sakha/cms-sdk
```

## Quick Start

```php
require 'vendor/autoload.php';

use Sakha\CMS\SakhaCMS;

// Initialize with API credentials
$cms = new SakhaCMS(
    'sk_live_xxx',      // API Key
    'sec_yyy',          // API Secret
    'https://api.example.com'
);

// Blog posts
$posts = $cms->blog()->listPosts(page: 1, limit: 20);
$post = $cms->blog()->getPost('post-id');
$newPost = $cms->blog()->createPost(
    title: 'My First Post',
    content: '<p>Content here</p>',
    status: 'published'
);

// Events
$events = $cms->events()->listEvents();
$event = $cms->events()->getEvent('event-id');

// Products with variants
$products = $cms->products()->listProducts();
$product = $cms->products()->getProduct('product-id');
$variants = $cms->products()->listVariants('product-id');

// Orders and Transactions
$orders = $cms->orders()->listOrders();
$transactions = $cms->transactions()->listTransactions();
```

## End-User Authentication

For end-user (customer) operations:

```php
// Register new end user
$result = $cms->endUsers()->register(
    email: 'user@example.com',
    password: 'secure_password_123',
    fullName: 'John Doe'
);

// Store the access token
$cms->setUserToken($result['accessToken']);

// Now use end-user APIs
$profile = $cms->endUsers()->getProfile();

// Logout
$cms->endUsers()->logout();
$cms->clearUserToken();
```

## Staff Authentication

For staff/admin operations:

```php
// Login staff member
$result = $cms->auth()->login('staff@example.com', 'password');

// Get profile
$profile = $cms->auth()->profile();

// Change password
$cms->auth()->changePassword('old_password', 'new_password');

// Logout
$cms->auth()->logout();
```

## API Modules

### Content Management
- **Blog**: Posts and categories
- **Events**: Event management and categories
- **Donations**: Campaigns and donations

### E-Commerce
- **Products**: Full inventory with variants, attributes, images
- **Orders**: Order management
- **Invoices**: Invoice generation and tracking
- **Transactions**: Payment transaction tracking
- **Shipments**: Shipping and delivery tracking

### Services
- **Services**: Service offerings and pricing
- **Appointments**: Appointment scheduling
- **Vendors**: Vendor management with commission tracking

### Marketing
- **Banners**: Promotional banners with placements
- **Analytics**: Traffic, donations, content, and events analytics

### User Management
- **Team**: Organization team members (board, staff, volunteers, advisors)
- **Members**: Project staff members with roles
- **End User Admin**: Manage end users (customers)
- **User Groups**: Hierarchical user groups for end users
- **Tenant Designations**: Staff titles with module-level permissions

### Integration
- **Auth**: Staff authentication
- **Media**: File uploads and S3 integration
- **Settings**: Project configuration, providers, integrations

## Pagination

All list endpoints return paginated results:

```php
$response = $cms->blog()->listPosts(page: 2, limit: 50);

// $response is a PaginatedResponse
echo "Total items: " . $response->total;
echo "Current page: " . $response->page;
echo "Per page: " . $response->limit;
echo "Has more: " . ($response->hasMorePages() ? 'yes' : 'no');

// Access the items
foreach ($response->data as $item) {
    echo $item['title'];
}
```

## Error Handling

```php
use Sakha\CMS\Exceptions\SakhaCMSException;
use Sakha\CMS\Exceptions\NotFoundException;
use Sakha\CMS\Exceptions\ValidationException;
use Sakha\CMS\Exceptions\AuthException;

try {
    $post = $cms->blog()->getPost('invalid-id');
} catch (NotFoundException $e) {
    echo "Post not found: " . $e->getMessage();
    echo "Status code: " . $e->getStatusCode();
} catch (ValidationException $e) {
    echo "Validation error: " . $e->getMessage();
} catch (AuthException $e) {
    echo "Authentication error: " . $e->getMessage();
} catch (SakhaCMSException $e) {
    echo "API error: " . $e->getMessage();
}
```

## Money Handling

All monetary values are stored in cents (integers) in requests and responses:

```php
// Create product with price of $29.99
$product = $cms->products()->createProduct(
    name: 'Widget',
    description: 'A great widget',
    priceCents: 2999  // $29.99
);

// Price comes back in dollars in response
echo $product['price'];  // 29.99
```

## Response Format

All API responses follow a standard envelope:

```php
{
    "success": true,
    "data": { ... },
    "error": null,
    "meta": {
        "total": 100,
        "page": 1,
        "limit": 50
    }
}
```

The SDK automatically parses and returns the data:

```php
// Returns the data portion
$posts = $cms->blog()->listPosts();  // returns array of posts + pagination meta
```

## Configuration

### Custom HTTP Client

```php
use GuzzleHttp\Client;
use Sakha\CMS\HttpClient;

$customClient = new Client([
    'timeout' => 60,
    'max_redirects' => 5,
]);

$httpClient = new HttpClient(
    'https://api.example.com',
    base64_encode('key:secret'),
    $customClient
);
```

### Set JWT Token

```php
// For end-user operations
$cms->setUserToken('jwt_token_here');

// Get current token
$token = $cms->getUserToken();

// Clear token
$cms->clearUserToken();
```

## Development

Install dev dependencies:

```bash
composer install --dev
```

Run tests:

```bash
composer test
```

Run static analysis:

```bash
composer phpstan
```

Check coding standards:

```bash
composer phpcs
```

## API Documentation

Full API documentation available at: [https://api.example.com/docs](https://api.example.com/docs)

## License

MIT
