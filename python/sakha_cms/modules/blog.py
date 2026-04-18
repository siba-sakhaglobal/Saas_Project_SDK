"""Blog module client."""

from typing import Any, Optional
from ..client import HttpClient
from ..models import (
    BlogPost,
    BlogCategory,
    BlogStats,
    CreateBlogPostBody,
    UpdateBlogPostBody,
    CreateBlogCategoryBody,
    UpdateBlogCategoryBody,
    PaginatedResponse,
    ListParams,
)


class BlogModule:
    """Blog module client."""

    def __init__(self, client: HttpClient) -> None:
        """Initialize blog module.

        Args:
            client: HTTP client instance
        """
        self.client = client

    # Blog Posts
    def get_posts(
        self,
        limit: int = 50,
        page: int = 1,
        search: Optional[str] = None,
    ) -> PaginatedResponse[BlogPost]:
        """Get all blog posts.

        Args:
            limit: Items per page
            page: Page number
            search: Search query

        Returns:
            Paginated blog posts
        """
        data = self.client.get(
            "/api/blog/posts",
            limit=limit,
            page=page,
            search=search,
        )
        return self._parse_paginated_response(data, BlogPost)

    async def get_posts_async(
        self,
        limit: int = 50,
        page: int = 1,
        search: Optional[str] = None,
    ) -> PaginatedResponse[BlogPost]:
        """Get all blog posts (async).

        Args:
            limit: Items per page
            page: Page number
            search: Search query

        Returns:
            Paginated blog posts
        """
        data = await self.client.get_async(
            "/api/blog/posts",
            limit=limit,
            page=page,
            search=search,
        )
        return self._parse_paginated_response(data, BlogPost)

    def get_post(self, post_id: str) -> BlogPost:
        """Get a blog post by ID.

        Args:
            post_id: Post ID

        Returns:
            Blog post
        """
        data = self.client.get(f"/api/blog/posts/{post_id}")
        return BlogPost(**data)

    async def get_post_async(self, post_id: str) -> BlogPost:
        """Get a blog post by ID (async).

        Args:
            post_id: Post ID

        Returns:
            Blog post
        """
        data = await self.client.get_async(f"/api/blog/posts/{post_id}")
        return BlogPost(**data)

    def create_post(self, body: CreateBlogPostBody) -> BlogPost:
        """Create a blog post.

        Args:
            body: Create post request

        Returns:
            Created blog post
        """
        data = self.client.post(
            "/api/blog/posts",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BlogPost(**data)

    async def create_post_async(self, body: CreateBlogPostBody) -> BlogPost:
        """Create a blog post (async).

        Args:
            body: Create post request

        Returns:
            Created blog post
        """
        data = await self.client.post_async(
            "/api/blog/posts",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BlogPost(**data)

    def update_post(self, post_id: str, body: UpdateBlogPostBody) -> BlogPost:
        """Update a blog post.

        Args:
            post_id: Post ID
            body: Update post request

        Returns:
            Updated blog post
        """
        data = self.client.put(
            f"/api/blog/posts/{post_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BlogPost(**data)

    async def update_post_async(self, post_id: str, body: UpdateBlogPostBody) -> BlogPost:
        """Update a blog post (async).

        Args:
            post_id: Post ID
            body: Update post request

        Returns:
            Updated blog post
        """
        data = await self.client.put_async(
            f"/api/blog/posts/{post_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BlogPost(**data)

    def delete_post(self, post_id: str) -> None:
        """Delete a blog post.

        Args:
            post_id: Post ID
        """
        self.client.delete(f"/api/blog/posts/{post_id}")

    async def delete_post_async(self, post_id: str) -> None:
        """Delete a blog post (async).

        Args:
            post_id: Post ID
        """
        await self.client.delete_async(f"/api/blog/posts/{post_id}")

    # Blog Categories
    def get_categories(
        self,
        limit: int = 50,
        page: int = 1,
    ) -> PaginatedResponse[BlogCategory]:
        """Get all blog categories.

        Args:
            limit: Items per page
            page: Page number

        Returns:
            Paginated blog categories
        """
        data = self.client.get(
            "/api/blog/categories",
            limit=limit,
            page=page,
        )
        return self._parse_paginated_response(data, BlogCategory)

    async def get_categories_async(
        self,
        limit: int = 50,
        page: int = 1,
    ) -> PaginatedResponse[BlogCategory]:
        """Get all blog categories (async).

        Args:
            limit: Items per page
            page: Page number

        Returns:
            Paginated blog categories
        """
        data = await self.client.get_async(
            "/api/blog/categories",
            limit=limit,
            page=page,
        )
        return self._parse_paginated_response(data, BlogCategory)

    def get_category(self, category_id: str) -> BlogCategory:
        """Get a blog category by ID.

        Args:
            category_id: Category ID

        Returns:
            Blog category
        """
        data = self.client.get(f"/api/blog/categories/{category_id}")
        return BlogCategory(**data)

    async def get_category_async(self, category_id: str) -> BlogCategory:
        """Get a blog category by ID (async).

        Args:
            category_id: Category ID

        Returns:
            Blog category
        """
        data = await self.client.get_async(f"/api/blog/categories/{category_id}")
        return BlogCategory(**data)

    def create_category(self, body: CreateBlogCategoryBody) -> BlogCategory:
        """Create a blog category.

        Args:
            body: Create category request

        Returns:
            Created blog category
        """
        data = self.client.post(
            "/api/blog/categories",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BlogCategory(**data)

    async def create_category_async(self, body: CreateBlogCategoryBody) -> BlogCategory:
        """Create a blog category (async).

        Args:
            body: Create category request

        Returns:
            Created blog category
        """
        data = await self.client.post_async(
            "/api/blog/categories",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BlogCategory(**data)

    def update_category(self, category_id: str, body: UpdateBlogCategoryBody) -> BlogCategory:
        """Update a blog category.

        Args:
            category_id: Category ID
            body: Update category request

        Returns:
            Updated blog category
        """
        data = self.client.put(
            f"/api/blog/categories/{category_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BlogCategory(**data)

    async def update_category_async(
        self, category_id: str, body: UpdateBlogCategoryBody
    ) -> BlogCategory:
        """Update a blog category (async).

        Args:
            category_id: Category ID
            body: Update category request

        Returns:
            Updated blog category
        """
        data = await self.client.put_async(
            f"/api/blog/categories/{category_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BlogCategory(**data)

    def delete_category(self, category_id: str) -> None:
        """Delete a blog category.

        Args:
            category_id: Category ID
        """
        self.client.delete(f"/api/blog/categories/{category_id}")

    async def delete_category_async(self, category_id: str) -> None:
        """Delete a blog category (async).

        Args:
            category_id: Category ID
        """
        await self.client.delete_async(f"/api/blog/categories/{category_id}")

    # Blog Stats
    def get_stats(self) -> BlogStats:
        """Get blog statistics.

        Returns:
            Blog statistics
        """
        data = self.client.get("/api/blog/stats")
        return BlogStats(**data)

    async def get_stats_async(self) -> BlogStats:
        """Get blog statistics (async).

        Returns:
            Blog statistics
        """
        data = await self.client.get_async("/api/blog/stats")
        return BlogStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
