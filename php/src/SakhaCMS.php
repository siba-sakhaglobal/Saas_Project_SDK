<?php

declare(strict_types=1);

namespace Sakha\CMS;

use Sakha\CMS\Modules\AnalyticsModule;
use Sakha\CMS\Modules\AppointmentsModule;
use Sakha\CMS\Modules\BannersModule;
use Sakha\CMS\Modules\BlogModule;
use Sakha\CMS\Modules\DonationsModule;
use Sakha\CMS\Modules\EndUsersModule;
use Sakha\CMS\Modules\EventsModule;
use Sakha\CMS\Modules\InvoicesModule;
use Sakha\CMS\Modules\MediaModule;
use Sakha\CMS\Modules\OrdersModule;
use Sakha\CMS\Modules\ProductsModule;
use Sakha\CMS\Modules\ServicesModule;
use Sakha\CMS\Modules\ShipmentsModule;
use Sakha\CMS\Modules\TeamModule;
use Sakha\CMS\Modules\TransactionsModule;
use Sakha\CMS\Modules\UserGroupsModule;
use Sakha\CMS\Modules\VendorsModule;

/**
 * Main Sakha CMS SDK client
 *
 * Initialize with:
 * ```php
 * $cms = new SakhaCMS('sk_live_xxx', 'sec_yyy', 'https://api.example.com');
 * $posts = $cms->blog()->listPosts();
 * ```
 */
class SakhaCMS
{
    private HttpClient $httpClient;

    private AnalyticsModule $analytics;
    private AppointmentsModule $appointments;
    private BannersModule $banners;
    private BlogModule $blog;
    private DonationsModule $donations;
    private EndUsersModule $endUsers;
    private EventsModule $events;
    private InvoicesModule $invoices;
    private MediaModule $media;
    private OrdersModule $orders;
    private ProductsModule $products;
    private ServicesModule $services;
    private ShipmentsModule $shipments;
    private TeamModule $team;
    private TransactionsModule $transactions;
    private UserGroupsModule $userGroups;
    private VendorsModule $vendors;

    /**
     * Initialize the Sakha CMS SDK client
     *
     * @param string $apiKey API key (e.g., sk_live_xxx)
     * @param string $apiSecret API secret (e.g., sec_yyy)
     * @param string $baseUrl Base URL of the CMS API (e.g., https://api.example.com)
     */
    public function __construct(
        string $apiKey,
        string $apiSecret,
        string $baseUrl,
    ) {
        $this->httpClient = new HttpClient($baseUrl, "{$apiKey}:{$apiSecret}");

        // Initialize all modules
        $this->analytics = new AnalyticsModule($this->httpClient);
        $this->appointments = new AppointmentsModule($this->httpClient);
        $this->banners = new BannersModule($this->httpClient);
        $this->blog = new BlogModule($this->httpClient);
        $this->donations = new DonationsModule($this->httpClient);
        $this->endUsers = new EndUsersModule($this->httpClient);
        $this->events = new EventsModule($this->httpClient);
        $this->invoices = new InvoicesModule($this->httpClient);
        $this->media = new MediaModule($this->httpClient);
        $this->orders = new OrdersModule($this->httpClient);
        $this->products = new ProductsModule($this->httpClient);
        $this->services = new ServicesModule($this->httpClient);
        $this->shipments = new ShipmentsModule($this->httpClient);
        $this->team = new TeamModule($this->httpClient);
        $this->transactions = new TransactionsModule($this->httpClient);
        $this->userGroups = new UserGroupsModule($this->httpClient);
        $this->vendors = new VendorsModule($this->httpClient);
    }

    /**
     * Set JWT token for end-user authenticated requests
     *
     * @param string $token JWT token from login/register endpoint
     */
    public function setUserToken(string $token): void
    {
        $this->httpClient->setJwtToken($token);
    }

    /**
     * Get current JWT token
     */
    public function getUserToken(): ?string
    {
        return $this->httpClient->getJwtToken();
    }

    /**
     * Clear JWT token (logout)
     */
    public function clearUserToken(): void
    {
        $this->httpClient->setJwtToken(null);
    }

    // Module accessors
    public function analytics(): AnalyticsModule
    {
        return $this->analytics;
    }

    public function appointments(): AppointmentsModule
    {
        return $this->appointments;
    }

    public function banners(): BannersModule
    {
        return $this->banners;
    }

    public function blog(): BlogModule
    {
        return $this->blog;
    }

    public function donations(): DonationsModule
    {
        return $this->donations;
    }

    public function endUsers(): EndUsersModule
    {
        return $this->endUsers;
    }

    public function events(): EventsModule
    {
        return $this->events;
    }

    public function invoices(): InvoicesModule
    {
        return $this->invoices;
    }

    public function media(): MediaModule
    {
        return $this->media;
    }

    public function orders(): OrdersModule
    {
        return $this->orders;
    }

    public function products(): ProductsModule
    {
        return $this->products;
    }

    public function services(): ServicesModule
    {
        return $this->services;
    }

    public function shipments(): ShipmentsModule
    {
        return $this->shipments;
    }

    public function team(): TeamModule
    {
        return $this->team;
    }

    public function transactions(): TransactionsModule
    {
        return $this->transactions;
    }

    public function userGroups(): UserGroupsModule
    {
        return $this->userGroups;
    }

    public function vendors(): VendorsModule
    {
        return $this->vendors;
    }

    /**
     * Get the underlying HTTP client
     */
    public function getHttpClient(): HttpClient
    {
        return $this->httpClient;
    }
}
